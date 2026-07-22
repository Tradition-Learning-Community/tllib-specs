#!/usr/bin/env python3
"""Build the traceable, non-functional input package for decomposition."""
from __future__ import annotations

import subprocess
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "registry" / "scientific-objects"
AUTO = ROOT / "reports" / "scientific-auto-review"
OUT = ROOT / "reports" / "functional-decomposition-input"
SNAPSHOT = ROOT / "registry" / "functional-decomposition" / "decomposition-input-snapshot.yaml"


def load(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def dump(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        yaml.safe_dump(data, stream, allow_unicode=True, sort_keys=False, width=120)


def main() -> None:
    objects = load(REGISTRY / "global-object-candidates.yaml")["objects"]
    relations = load(REGISTRY / "global-relation-candidates.yaml")["relations"]
    terms = load(REGISTRY / "global-unresolved-terms.yaml")["unresolved_terms"]
    decisions = load(AUTO / "decision-classification.yaml")["decisions"]
    source_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.strip()

    blocked_by_decision = defaultdict(list)
    separated_by_decision = defaultdict(list)
    decision_summary = []
    for decision in decisions:
        decision_summary.append({
            "source_decision_id": decision["source_decision_id"],
            "risk_level": decision["risk_level"],
            "selected_option": decision.get("selected_option"),
            "affected_items": decision.get("affected_items", []),
            "source": "reports/scientific-auto-review/decision-classification.yaml",
        })
        target = blocked_by_decision if decision["risk_level"] == "HUMAN_REQUIRED" else separated_by_decision
        if decision.get("selected_option") == "keep_separate" or decision["risk_level"] == "HUMAN_REQUIRED":
            for object_id in decision.get("affected_items", []):
                if object_id.startswith("TLC-SO-"):
                    target[object_id].append(decision["source_decision_id"])

    blocking_terms = []
    non_blocking_terms = []
    term_blockers = defaultdict(list)
    for term in terms:
        entry = {
            "term_id": term["global_unresolved_id"],
            "term": term["term"],
            "category": term["category"],
            "affected_object_ids": term.get("affected_object_ids", []),
            "source": term["source"],
            "source_decision_id": "TLC-HR-0147",
            "status": "candidate",
        }
        # Only explicit semantic/mathematical defects block contract interpretation.
        # A classification uncertainty does not by itself prevent local use.
        if term["category"] == "classification_uncertainty":
            entry["impact"] = "non_blocking_for_decomposition"
            entry["justification"] = "Le terme nomme déjà un objet; seule sa classification scientifique reste incertaine."
            non_blocking_terms.append(entry)
        else:
            entry["impact"] = "blocks_contract_for_affected_objects"
            entry["justification"] = "La catégorie explicite empêche une interprétation contractuelle stable sans résolution."
            blocking_terms.append(entry)
            for object_id in term.get("affected_object_ids", []):
                term_blockers[object_id].append(term["global_unresolved_id"])

    object_rows = []
    for obj in objects:
        object_id = obj["source_object_id"]
        decisions_for_object = sorted(set(blocked_by_decision[object_id]))
        terms_for_object = sorted(set(term_blockers[object_id]))
        separated = sorted(set(separated_by_decision[object_id]))
        if decisions_for_object or terms_for_object:
            status = "blocked_locally"
        elif separated:
            status = "provisionally_separated"
        else:
            status = "admissible"
        row = {
            "object_id": object_id,
            "status": status,
            "object_type": obj.get("object_type"),
            "canonical_name": obj.get("canonical_name"),
            "source": obj.get("source"),
            "source_reference": obj.get("source_reference"),
            "source_commit": obj.get("source_reference", {}).get("source_commit"),
            "decisions": decisions_for_object or separated,
            "blocking_terms": terms_for_object,
            "restrictions": (
                ["Do not use for contract derivation until cited blockers are resolved."] if status == "blocked_locally"
                else ["Preserve identity; do not merge with similarly named objects."] if status == "provisionally_separated"
                else ["Candidate scientific status only; no approval implied."]
            ),
        }
        object_rows.append(row)

    object_status = {row["object_id"]: row["status"] for row in object_rows}
    relation_rows = []
    for rel in relations:
        endpoints = [rel["source_object_id"], rel["target_object_id"]]
        blocked_endpoints = [item for item in endpoints if object_status.get(item) == "blocked_locally"]
        relation_rows.append({
            "relation_id": rel["source_relation_id"],
            "status": "blocked_locally" if blocked_endpoints else "admissible",
            "relation_type": rel["relation_type"],
            "source_object_id": rel["source_object_id"],
            "target_object_id": rel["target_object_id"],
            "source": rel["source"],
            "evidence": rel.get("evidence"),
            "blocked_by_objects": blocked_endpoints,
            "restriction": "No endpoint substitution or identity inference is permitted.",
        })

    blockers = []
    for row in object_rows:
        if row["status"] == "blocked_locally":
            blockers.append({
                "object_id": row["object_id"],
                "decision_ids": row["decisions"],
                "term_ids": row["blocking_terms"],
                "sources": sorted(set(filter(None, [row["source"]]))),
                "scope": "local_to_object_and_incident_relations",
            })

    by_source = defaultdict(lambda: {"objects": [], "relations": [], "source_commits": set()})
    for row in object_rows:
        by_source[row["source"]]["objects"].append(row["object_id"])
        if row["source_commit"]:
            by_source[row["source"]]["source_commits"].add(row["source_commit"])
    for row in relation_rows:
        by_source[row["source"]]["relations"].append(row["relation_id"])
    source_rows = [{
        "source": source,
        "source_commits": sorted(data["source_commits"]),
        "object_ids": sorted(data["objects"]),
        "relation_ids": sorted(data["relations"]),
    } for source, data in sorted(by_source.items())]

    object_counts = Counter(row["status"] for row in object_rows)
    relation_counts = Counter(row["status"] for row in relation_rows)
    restrictions = [
        "Do not propose final features in this input-preparation stage.",
        "Do not merge, alias, or substitute scientific objects.",
        "Do not derive an IR, API, contract, or implementation from blocked objects.",
        "Treat all artifacts as candidate, never approved.",
        "Keep blockers local to cited objects and incident relations.",
        "Carry unresolved terms forward without reconstructing definitions.",
    ]
    snapshot = {
        "snapshot_id": "TLC-FUNCTIONAL-DECOMPOSITION-INPUT-SNAPSHOT-V1",
        "status": "candidate",
        "source_commit": source_commit,
        "source_artifacts": [
            "registry/scientific-objects/global-object-candidates.yaml",
            "registry/scientific-objects/global-relation-candidates.yaml",
            "registry/scientific-objects/global-unresolved-terms.yaml",
            "reports/scientific-auto-review/decision-classification.yaml",
            "reports/scientific-auto-review/human-exceptions.yaml",
        ],
        "summary": {
            "total_objects": len(object_rows), **{f"objects_{key}": value for key, value in object_counts.items()},
            "total_relations": len(relation_rows), **{f"relations_{key}": value for key, value in relation_counts.items()},
            "terms_blocking_contract": len(blocking_terms),
            "terms_non_blocking": len(non_blocking_terms),
            "decisions_concerned": len(decision_summary),
        },
        "admissible_objects": [row for row in object_rows if row["status"] == "admissible"],
        "provisionally_separated_objects": [row for row in object_rows if row["status"] == "provisionally_separated"],
        "blocked_objects": [row for row in object_rows if row["status"] == "blocked_locally"],
        "admissible_relations": [row for row in relation_rows if row["status"] == "admissible"],
        "blocked_relations": [row for row in relation_rows if row["status"] == "blocked_locally"],
        "contract_blocking_terms": blocking_terms,
        "non_blocking_terms": non_blocking_terms,
        "decisions_concerned": decision_summary,
        "source_references": source_rows,
        "restrictions_for_next_chat": restrictions,
    }
    dump(SNAPSHOT, snapshot)
    dump(OUT / "object-status.yaml", {"status": "candidate", "source_commit": source_commit, "count": len(object_rows), "objects": object_rows})
    dump(OUT / "relation-status.yaml", {"status": "candidate", "source_commit": source_commit, "count": len(relation_rows), "relations": relation_rows})
    dump(OUT / "blockers.yaml", {"status": "candidate", "count": len(blockers), "blockers": blockers})
    dump(OUT / "unresolved-impact.yaml", {"status": "candidate", "blocking_count": len(blocking_terms), "non_blocking_count": len(non_blocking_terms), "contract_blocking_terms": blocking_terms, "non_blocking_terms": non_blocking_terms})
    dump(OUT / "source-map.yaml", {"status": "candidate", "source_commit": source_commit, "sources": source_rows})
    dump(OUT / "decision_required.yaml", {
        "status": "candidate", "ready_for_unblocked_local_decomposition": True,
        "ready_for_global_unrestricted_decomposition": False,
        "human_required_decisions": sorted({d for values in blocked_by_decision.values() for d in values}),
        "contract_blocking_terms": [term["term_id"] for term in blocking_terms],
        "instruction": "Do not request decisions globally; consult only when a blocked object is needed.",
    })
    readme = f"""# Paquet d'entrée du découpage fonctionnel TLC

Ce paquet est un instantané **candidate** du corpus au commit `{source_commit}`. Il ne contient aucune fonctionnalité, IR, API, contrat ou décision scientifique nouvelle.

## Portée

- {len(object_rows)} objets classés exactement une fois : {object_counts['admissible']} admissibles, {object_counts['provisionally_separated']} provisoirement séparés, {object_counts['blocked_locally']} bloqués localement.
- {len(relation_rows)} relations : {relation_counts['admissible']} admissibles et {relation_counts['blocked_locally']} bloquées localement.
- {len(blocking_terms)} termes bloquent l'interprétation contractuelle de leurs seuls objets affectés; {len(non_blocking_terms)} incertitudes de classification restent non bloquantes.

Le fichier canonique d'échange est `registry/functional-decomposition/decomposition-input-snapshot.yaml`. Le chat suivant doit respecter `restrictions_for_next_chat` et ne jamais transformer un statut candidate en approved.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
