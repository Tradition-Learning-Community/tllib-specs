#!/usr/bin/env python3
"""Audit déterministe des extractions scientifiques TLC."""

from __future__ import annotations

import collections
import re
import subprocess
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MATHS = ROOT / "maths"
REGISTRY = ROOT / "registry" / "scientific-objects"
EXTRACTION_REPORTS = ROOT / "reports" / "scientific-extraction"
CONSOLIDATION = ROOT / "reports" / "scientific-consolidation"

FILES = {
    "objects": "scientific-objects.candidate.yaml",
    "relations": "scientific-relations.candidate.yaml",
    "unresolved_terms": "unresolved-terms.yaml",
    "duplicate_candidates": "duplicate-candidates.yaml",
}


class LiteralDumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


LiteralDumper.add_representer(str, _str_presenter)


def dump_yaml(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(data, Dumper=LiteralDumper, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
        newline="\n",
    )


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def slug_for(source: Path) -> str:
    return re.sub(r"^\d+-", "", source.stem)


def norm(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value)).casefold()
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\W+", " ", text).strip()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8").strip()


def headings(path: Path) -> list[dict]:
    result = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            result.append({"level": len(match.group(1)), "title": match.group(2).strip(), "line": line_no})
    return result


def nested_statuses(value: object, path="") -> list[dict]:
    found = []
    if isinstance(value, dict):
        for key, item in value.items():
            here = f"{path}.{key}" if path else key
            if key in {"status", "validation_status"}:
                found.append({"path": here, "value": item})
            found.extend(nested_statuses(item, here))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(nested_statuses(item, f"{path}[{index}]"))
    return found


def main() -> None:
    sources = sorted(MATHS.glob("*.md"))
    source_by_slug = {slug_for(source): source for source in sources}
    package_dirs = {p.name: p for p in REGISTRY.iterdir() if p.is_dir()}
    report_dirs = {p.name: p for p in EXTRACTION_REPORTS.iterdir() if p.is_dir()}
    all_slugs = sorted(set(source_by_slug) | set(package_dirs) | set(report_dirs))

    parsed: dict[str, dict] = {}
    completeness = []
    structural_issues = []
    schema_shapes: dict[str, dict[str, set[str]]] = collections.defaultdict(dict)
    global_ids: dict[str, list[str]] = collections.defaultdict(list)

    for slug in all_slugs:
        source = source_by_slug.get(slug)
        package = package_dirs.get(slug, REGISTRY / slug)
        report_dir = report_dirs.get(slug, EXTRACTION_REPORTS / slug)
        expected = {kind: package / filename for kind, filename in FILES.items()}
        expected.update({
            "report": report_dir / "scientific-extraction-report.md",
            "decision": report_dir / "decision_required.yaml",
        })
        anomalies = []
        if source is None:
            anomalies.append("package_without_source")
        if slug not in package_dirs:
            anomalies.append("source_without_registry_package")
        if slug not in report_dirs:
            anomalies.append("source_without_report_package")
        data_for_slug = {}
        for kind, path in expected.items():
            if not path.is_file():
                anomalies.append(f"missing:{rel(path)}")
                continue
            if path.stat().st_size == 0:
                anomalies.append(f"empty:{rel(path)}")
            if path.suffix == ".yaml":
                try:
                    data = load_yaml(path)
                    data_for_slug[kind] = data
                except Exception as exc:  # audit must report every parser failure
                    anomalies.append(f"unreadable_yaml:{rel(path)}:{type(exc).__name__}")
                    continue
                if not isinstance(data, dict):
                    structural_issues.append({"file": rel(path), "issue": "top_level_not_mapping"})
                    continue
                schema_shapes[kind][slug] = set(data)
                artifact = data.get("artifact", data if kind == "decision" else {})
                declared_slug = artifact.get("source_slug") if isinstance(artifact, dict) else None
                if declared_slug and declared_slug != slug:
                    structural_issues.append({"file": rel(path), "issue": "source_slug_mismatch", "observed": declared_slug, "expected": slug})
                declared_path = artifact.get("source_path") if isinstance(artifact, dict) else None
                if declared_path and not (ROOT / declared_path).exists():
                    structural_issues.append({"file": rel(path), "issue": "nonexistent_source_path", "value": declared_path})
                for status in nested_statuses(data):
                    if status["value"] == "approved":
                        structural_issues.append({"file": rel(path), "issue": "approved_status_requires_justification", **status})
                list_key = kind if kind in FILES else None
                entries = data.get(list_key, []) if list_key else []
                if list_key and not isinstance(entries, list):
                    structural_issues.append({"file": rel(path), "issue": f"{list_key}_not_list"})
                    entries = []
                ids = []
                for entry in entries:
                    if not isinstance(entry, dict):
                        continue
                    identifier = next((entry.get(k) for k in ("provisional_object_id", "provisional_relation_id", "unresolved_id", "duplicate_candidate_id") if entry.get(k)), None)
                    if identifier:
                        ids.append(identifier)
                        global_ids[identifier].append(rel(path))
                repeated = sorted(i for i, count in collections.Counter(ids).items() if count > 1)
                for identifier in repeated:
                    structural_issues.append({"file": rel(path), "issue": "duplicate_identifier_in_file", "identifier": identifier})
        parsed[slug] = data_for_slug
        present = {kind: expected[kind].is_file() and expected[kind].stat().st_size > 0 for kind in expected}
        completeness.append({
            "source": rel(source) if source else None,
            "package_slug": slug,
            "artifacts": present,
            "package_complete": bool(source) and all(present.values()),
            "anomalies": anomalies,
        })

    for identifier, paths in sorted(global_ids.items()):
        if len(paths) > 1:
            structural_issues.append({"issue": "global_duplicate_identifier", "identifier": identifier, "files": paths})

    # Schema differences are reported, never normalized.
    schema_divergences = []
    for kind, shapes in sorted(schema_shapes.items()):
        union = set().union(*shapes.values()) if shapes else set()
        intersection = set.intersection(*shapes.values()) if shapes else set()
        for slug, keys in sorted(shapes.items()):
            missing, extra = sorted(union - keys), sorted(keys - intersection)
            if missing or extra:
                schema_divergences.append({"artifact_kind": kind, "package_slug": slug, "missing_fields": missing, "additional_fields": extra})

    objects = []
    relations = []
    unresolved = []
    local_duplicates = []
    for slug in sorted(parsed):
        source = rel(source_by_slug[slug]) if slug in source_by_slug else None
        package_ref = f"registry/scientific-objects/{slug}"
        for obj in (parsed[slug].get("objects") or {}).get("objects", []):
            objects.append({"candidate_index_id": f"TLC-GO-{len(objects)+1:05d}", "source_object_id": obj.get("provisional_object_id"), "canonical_name": obj.get("canonical_name"), "object_type": obj.get("object_type"), "source": source, "source_package": package_ref, "source_reference": obj.get("source_reference"), "status": "candidate"})
        for relation in (parsed[slug].get("relations") or {}).get("relations", []):
            relations.append({"candidate_relation_index_id": f"TLC-GR-{len(relations)+1:05d}", "source_relation_id": relation.get("provisional_relation_id"), "source_object_id": relation.get("source_object_id"), "relation_type": relation.get("relation_type"), "target_object_id": relation.get("target_object_id"), "evidence": relation.get("evidence_statement"), "source": source, "source_package": package_ref, "status": "candidate"})
        for term in (parsed[slug].get("unresolved_terms") or {}).get("unresolved_terms", []):
            unresolved.append({"source_unresolved_id": term.get("unresolved_id"), "term": term.get("term"), "category": term.get("category"), "description": term.get("description"), "source": source, "affected_object_ids": term.get("affected_object_ids", []), "status": "candidate"})
        for duplicate in (parsed[slug].get("duplicate_candidates") or {}).get("duplicate_candidates", []):
            local_duplicates.append({"source": source, "source_package": package_ref, **duplicate})

    object_by_id = {o["source_object_id"]: o for o in objects if o["source_object_id"]}
    by_name: dict[str, list[dict]] = collections.defaultdict(list)
    for obj in objects:
        if obj["canonical_name"]:
            by_name[norm(obj["canonical_name"])].append(obj)

    cross_duplicates = []
    for same_name in sorted(by_name.values(), key=lambda group: norm(group[0]["canonical_name"])):
        sources_in_group = sorted({o["source"] for o in same_name})
        if len(sources_in_group) < 2:
            continue
        types = sorted({o["object_type"] for o in same_name})
        recommendation = "merge_candidate" if len(types) == 1 else "requires_scientific_review"
        cross_duplicates.append({
            "candidate_id": f"TLC-XD-{len(cross_duplicates)+1:04d}",
            "objects": [o["source_object_id"] for o in same_name],
            "sources": sources_in_group,
            "match_type": "same_normalized_name_across_sources",
            "evidence": f"Nom canonique normalisé commun: {norm(same_name[0]['canonical_name'])}",
            "observed_differences": {"object_types": types},
            "merge_risk": "high" if len(types) > 1 else "medium",
            "recommendation": recommendation,
            "status": "candidate",
        })

    # Resolve only exact normalized term/name matches, as candidates with citations.
    consolidated_terms = []
    for index, term in enumerate(unresolved, 1):
        matches = [o for o in by_name.get(norm(term["term"]), []) if o["source"] != term["source"]]
        if matches:
            resolution_class = "probably_resolved_by_another_source"
            candidate_resolution = [{"object_id": o["source_object_id"], "source": o["source"]} for o in matches]
        else:
            resolution_class = "unresolved_in_corpus"
            candidate_resolution = []
        consolidated_terms.append({"global_unresolved_id": f"TLC-GU-{index:05d}", **term, "resolution_class": resolution_class, "candidate_resolutions": candidate_resolution, "requires_human_decision": True, "status": "candidate"})

    relation_issues = []
    for relation in relations:
        missing = [identifier for identifier in (relation["source_object_id"], relation["target_object_id"]) if identifier and identifier not in object_by_id]
        if missing:
            relation_issues.append({"relation_id": relation["source_relation_id"], "missing_object_ids": missing, "source": relation["source"]})

    object_ids_with_relation = {identifier for relation in relations for identifier in (relation["source_object_id"], relation["target_object_id"]) if identifier}
    isolated_objects = [o["source_object_id"] for o in objects if o["source_object_id"] not in object_ids_with_relation]

    coverage_issues = []
    for slug, source in sorted(source_by_slug.items()):
        source_lines = source.read_text(encoding="utf-8").splitlines()
        source_headings = headings(source)
        registry_objects = (parsed.get(slug, {}).get("objects") or {}).get("objects", [])
        referenced_sections = {
            norm(value)
            for obj in registry_objects
            for value in (
                (obj.get("source_reference") or {}).get("section"),
                (obj.get("source_reference") or {}).get("subsection"),
            )
            if value
        }
        for heading in source_headings:
            if norm(heading["title"]) not in referenced_sections:
                coverage_issues.append({"source": rel(source), "issue_type": "heading_without_object_section_reference", "section": heading["title"], "line": heading["line"], "review": "targeted"})
        for obj in registry_objects:
            ref = obj.get("source_reference") or {}
            start, end = ref.get("start_line"), ref.get("end_line")
            if not isinstance(start, int) or not isinstance(end, int) or start < 1 or end < start or end > len(source_lines):
                coverage_issues.append({"source": rel(source), "issue_type": "invalid_line_range", "object_id": obj.get("provisional_object_id"), "start_line": start, "end_line": end, "source_line_count": len(source_lines), "review": "targeted"})
        report_path = EXTRACTION_REPORTS / slug / "scientific-extraction-report.md"
        if report_path.exists():
            report_text = report_path.read_text(encoding="utf-8")
            claimed_objects = re.search(r"Objets\s*:\s*\*\*(\d+)\*\*", report_text)
            claimed_relations = re.search(r"Relations\s*:\s*\*\*(\d+)\*\*", report_text)
            for label, match, actual in (("objects", claimed_objects, len(registry_objects)), ("relations", claimed_relations, len((parsed.get(slug, {}).get("relations") or {}).get("relations", [])))):
                if match and int(match.group(1)) != actual:
                    coverage_issues.append({"source": rel(source), "issue_type": "report_count_mismatch", "registry": label, "reported": int(match.group(1)), "actual": actual, "review": "targeted"})

    blocking = []
    incomplete = [item for item in completeness if not item["package_complete"]]
    if incomplete:
        blocking.append({"issue_id": "TLC-CONS-BLOCK-001", "summary": "Paquets incomplets", "affected": [i["package_slug"] for i in incomplete]})
    if relation_issues:
        blocking.append({"issue_id": "TLC-CONS-BLOCK-002", "summary": "Relations vers des objets inexistants", "affected": relation_issues})
    approved_issues = [i for i in structural_issues if i.get("issue") == "approved_status_requires_justification"]
    if approved_issues:
        blocking.append({"issue_id": "TLC-CONS-BLOCK-003", "summary": "Statuts approved à justifier", "affected": approved_issues})

    review_queue = []
    for issue in blocking:
        review_queue.append({"decision_id": f"TLC-HR-{len(review_queue)+1:04d}", "category": "critical_blocker", "affected": issue["affected"], "question": issue["summary"], "options": [{"value": "revise", "consequence": "Corriger puis réauditer."}, {"value": "accept_with_reservations", "consequence": "Conserver le risque documenté; étape suivante bloquée."}], "non_normative_recommendation": "revise", "priority": "critical", "status": "pending"})
    for duplicate in cross_duplicates:
        review_queue.append({"decision_id": f"TLC-HR-{len(review_queue)+1:04d}", "category": "merge_or_separate", "affected": duplicate["objects"], "question": f"Faut-il rapprocher les objets de {duplicate['candidate_id']} ?", "options": [{"value": "merge", "consequence": "Créer ultérieurement un objet unifié après validation scientifique."}, {"value": "alias", "consequence": "Conserver les objets et enregistrer une équivalence de nom."}, {"value": "keep_separate", "consequence": "Conserver des identités distinctes."}], "non_normative_recommendation": duplicate["recommendation"], "priority": "high" if duplicate["merge_risk"] == "high" else "medium", "status": "pending"})
    if coverage_issues:
        review_queue.append({"decision_id": f"TLC-HR-{len(review_queue)+1:04d}", "category": "traceability", "affected": sorted({i["source"] for i in coverage_issues}), "question": "Les trous de couverture probables doivent-ils donner lieu à une extraction ciblée ?", "options": [{"value": "targeted_revision", "consequence": "Réviser uniquement les sections signalées."}, {"value": "accept_documented", "consequence": "Conserver les trous comme limites connues."}], "non_normative_recommendation": "targeted_revision", "priority": "high", "status": "pending"})
    unresolved_without_match = [t for t in consolidated_terms if not t["candidate_resolutions"]]
    if unresolved_without_match:
        review_queue.append({"decision_id": f"TLC-HR-{len(review_queue)+1:04d}", "category": "non_blocking_warning", "affected": [t["global_unresolved_id"] for t in unresolved_without_match], "question": "Comment traiter les termes restant non résolus dans le corpus ?", "options": [{"value": "scientific_review", "consequence": "Décision scientifique terme par terme."}, {"value": "retain_unresolved", "consequence": "Maintenir explicitement les termes non résolus."}], "non_normative_recommendation": "scientific_review", "priority": "medium", "status": "pending"})

    dump_yaml(CONSOLIDATION / "package-completeness.yaml", {"work_item_id": "TLC-SCIENTIFIC-CONSOLIDATION", "status": "candidate", "packages": completeness})
    dump_yaml(CONSOLIDATION / "schema-divergences.yaml", {"status": "candidate", "divergences": schema_divergences, "structural_issues": structural_issues, "mechanical_correction_candidates": []})
    dump_yaml(CONSOLIDATION / "source-coverage-issues.yaml", {"status": "candidate", "issues": coverage_issues})
    dump_yaml(REGISTRY / "global-object-candidates.yaml", {"artifact": {"artifact_type": "global_object_candidate_index", "status": "candidate"}, "objects": objects})
    dump_yaml(REGISTRY / "global-relation-candidates.yaml", {"artifact": {"artifact_type": "global_relation_candidate_index", "status": "candidate"}, "relations": relations, "relation_endpoint_issues": relation_issues, "objects_without_relations": isolated_objects})
    dump_yaml(REGISTRY / "cross-source-duplicate-candidates.yaml", {"artifact": {"artifact_type": "cross_source_duplicate_candidates", "status": "candidate"}, "cross_source_candidates": cross_duplicates, "local_candidates_preserved": local_duplicates})
    dump_yaml(REGISTRY / "global-unresolved-terms.yaml", {"artifact": {"artifact_type": "global_unresolved_terms", "status": "candidate"}, "unresolved_terms": consolidated_terms})
    dump_yaml(CONSOLIDATION / "human-review-queue.yaml", {"work_item_id": "TLC-SCIENTIFIC-CONSOLIDATION", "status": "candidate", "decisions": review_queue})

    sources_list = "\n".join(f"- `{rel(source)}`" for source in sources)
    table_rows = []
    for item in completeness:
        flags = item["artifacts"]
        yes = lambda value: "oui" if value else "non"
        table_rows.append(f"| {item['source'] or '—'} | {item['package_slug']} | {yes(flags['objects'])} | {yes(flags['relations'])} | {yes(flags['unresolved_terms'])} | {yes(flags['duplicate_candidates'])} | {yes(flags['report'])} | {yes(flags['decision'])} | {yes(item['package_complete'])} | {'; '.join(item['anomalies']) or 'aucune'} |")
    git_status = git("status", "--short", "--branch")
    last_commit = git("log", "-1", "--format=%H %s")
    audit_md = f"""# Audit du dépôt — consolidation scientifique

## État Git observé

- Branche de travail : `audit/scientific-extraction-consolidation`
- État avant création des sorties : dépôt propre, branche de départ `main` en avance de 2 commits sur `origin/main`.
- Dernier commit observé : `{last_commit}`
- État au moment de la génération : `{git_status}`

## Sources détectées

{sources_list}

## Paquets détectés

{', '.join(f'`{slug}`' for slug in sorted(package_dirs))}

## Complétude

| Source | Slug | Objets | Relations | Non résolus | Doublons | Rapport | Décision | Complet | Anomalies |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
{chr(10).join(table_rows)}

## Anomalies structurelles

- Problèmes structurels : {len(structural_issues)}.
- Divergences de schéma de premier niveau : {len(schema_divergences)}.
- Relations vers des objets absents : {len(relation_issues)}.
- Détails structurés : `schema-divergences.yaml` et `source-coverage-issues.yaml`.

## Conclusion

Paquets complets : {len(completeness)-len(incomplete)}/{len(completeness)}. La consolidation reste candidate et doit passer par la file de revue humaine.
"""
    (CONSOLIDATION / "repository-audit.md").write_text(audit_md, encoding="utf-8", newline="\n")

    resolved_count = sum(bool(t["candidate_resolutions"]) for t in consolidated_terms)
    report_md = f"""# Rapport de consolidation scientifique

## Synthèse globale

- Sources auditées : {len(sources)}
- Objets indexés : {len(objects)}
- Relations indexées : {len(relations)}
- Candidats de rapprochement transversaux : {len(cross_duplicates)}
- Termes non résolus consolidés : {len(consolidated_terms)}
- Termes probablement résolus transversalement : {resolved_count}
- Objets sans relation : {len(isolated_objects)}
- Relations vers des objets inexistants : {len(relation_issues)}

## Problèmes bloquants

{chr(10).join(f"- {issue['issue_id']} — {issue['summary']}" for issue in blocking) or '- Aucun blocage mécanique détecté.'}

## Préparation de l'étape suivante

Le corpus est prêt pour la revue humaine : **{'non' if not review_queue else 'oui'}**. Il n'est pas prêt pour le découpage en fonctionnalités tant que les décisions `pending` n'ont pas été examinées. Aucune fusion, correction scientifique, IR ou fonctionnalité logicielle n'a été produite.
"""
    (CONSOLIDATION / "consolidation-report.md").write_text(report_md, encoding="utf-8", newline="\n")

    artifacts = [
        "reports/scientific-consolidation/repository-audit.md",
        "reports/scientific-consolidation/package-completeness.yaml",
        "reports/scientific-consolidation/schema-divergences.yaml",
        "reports/scientific-consolidation/source-coverage-issues.yaml",
        "registry/scientific-objects/global-object-candidates.yaml",
        "registry/scientific-objects/global-relation-candidates.yaml",
        "registry/scientific-objects/cross-source-duplicate-candidates.yaml",
        "registry/scientific-objects/global-unresolved-terms.yaml",
        "reports/scientific-consolidation/human-review-queue.yaml",
        "reports/scientific-consolidation/consolidation-report.md",
        "reports/scientific-consolidation/decision_required.yaml",
    ]
    decision = {
        "work_item_id": "TLC-SCIENTIFIC-CONSOLIDATION",
        "stage": "scientific_extraction_consolidation",
        "status": "candidate",
        "artifacts_produced": artifacts,
        "blocking_issues": blocking,
        "non_blocking_issues": [{"issue": "coverage_review_required", "count": len(coverage_issues)}, {"issue": "unresolved_terms_without_cross_source_match", "count": len(unresolved_without_match)}],
        "questions_for_human": [d["decision_id"] for d in review_queue],
        "readiness": {"ready_for_human_review": True, "ready_for_feature_decomposition": False},
        "recommended_decision": {"value": "revise", "justification": "Examiner les blocages, rapprochements candidats, lacunes de traçabilité et termes non résolus avant toute étape logicielle."},
        "allowed_decisions": ["approved", "approved_with_reservations", "revise", "rejected"],
    }
    dump_yaml(CONSOLIDATION / "decision_required.yaml", decision)

    print(f"sources={len(sources)} packages={len(completeness)} objects={len(objects)} relations={len(relations)}")
    print(f"cross_source_duplicates={len(cross_duplicates)} unresolved_terms={len(consolidated_terms)} coverage_issues={len(coverage_issues)}")
    print(f"blocking_issues={len(blocking)} human_decisions={len(review_queue)}")


if __name__ == "__main__":
    main()
