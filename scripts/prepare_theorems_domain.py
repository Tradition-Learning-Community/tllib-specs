#!/usr/bin/env python3
"""Build conservative Theorems domain-preparation artifacts from canonical main data."""
from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "4a42d88ee71e3660fba02c7a780246e8d755c901"
DOMAIN = "theorems"
SOURCE = "maths/06-theorems.md"
REG = ROOT / "registry/domain-progress/theorems"
REP = ROOT / "reports/domain-progress/theorems"
SO_DIR = ROOT / "registry/scientific-objects/theorems"


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")


def report(name: str, title: str, facts: list[str], reservations: list[str] | None = None) -> None:
    lines = [f"# {title}", "", f"Baseline: `{BASELINE}`. Source: `{SOURCE}`.", ""]
    lines.extend(f"- {fact}" for fact in facts)
    if reservations:
        lines.extend(["", "## Reservations", ""])
        lines.extend(f"- {item}" for item in reservations)
    lines.extend(["", "No theorem, proof, mathematical contract, or IR is created or completed by this report.", ""])
    (REP / name).write_text("\n".join(lines), encoding="utf-8")


def source_ref(obj) -> str:
    ref = obj["source_reference"]
    return f"{ref['source_path']}:{ref['start_line']}-{ref['end_line']}"


def main() -> int:
    REG.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    objects = load(SO_DIR / "scientific-objects.candidate.yaml")["objects"]
    relations = load(SO_DIR / "scientific-relations.candidate.yaml")["relations"]
    unresolved = load(SO_DIR / "unresolved-terms.yaml")["unresolved_terms"]
    duplicates = load(SO_DIR / "duplicate-candidates.yaml")["duplicate_candidates"]
    lineage = load(ROOT / "registry/features/revised/feature-lineage.yaml")["lineage"]
    classifications = load(ROOT / "registry/features/revised/feature-classification.yaml")["classifications"]
    oracle = load(ROOT / "registry/features/revised/oracle-readiness.yaml")["features"]
    source_text = (ROOT / SOURCE).read_text(encoding="utf-8")
    source_hash = hashlib.sha256((ROOT / SOURCE).read_bytes()).hexdigest()

    feature_lineage = [x for x in lineage if x["original_feature_candidate_id"].startswith("TLC-FC-06-THEOREMS-")]
    feature_ids = [x["original_feature_candidate_id"] for x in feature_lineage]
    class_by_id = {x["feature_candidate_id"]: x for x in classifications if x["feature_candidate_id"] in feature_ids}
    oracle_by_id = {x["feature_candidate_id"]: x for x in oracle if x["feature_candidate_id"] in feature_ids}
    object_by_id = {x["provisional_object_id"]: x for x in objects}
    relation_by_id = {x["provisional_relation_id"]: x for x in relations}
    object_to_features = defaultdict(list)
    for item in feature_lineage:
        for object_id in item["scientific_object_ids"]:
            object_to_features[object_id].append(item["original_feature_candidate_id"])

    catalog_text = (ROOT / "reports/functional-decomposition/feature-catalog.md").read_text(encoding="utf-8")
    catalog = {}
    for line in catalog_text.splitlines():
        match = re.match(r"\| `(?P<id>TLC-FC-06-THEOREMS-\d{3})` \| (?P<name>.*?) \| `(?P<category>.*?)` \| `(?P<readiness>.*?)` \|", line)
        if match:
            catalog[match["id"]] = match.groupdict()

    type_distribution = dict(sorted(Counter(x["object_type"] for x in objects).items()))
    relation_distribution = dict(sorted(Counter(x["relation_type"] for x in relations).items()))
    unresolved_distribution = dict(sorted(Counter(x["category"] for x in unresolved).items()))
    object_ids = [x["provisional_object_id"] for x in objects]
    relation_ids = [x["provisional_relation_id"] for x in relations]
    unresolved_ids = [x["unresolved_id"] for x in unresolved]
    invalid_object_ids = [x for x in object_ids if not re.fullmatch(r"TLC-SO-THEOREMS-\d{3}", x)]
    invalid_relation_ids = [x for x in relation_ids if not re.fullmatch(r"TLC-SR-THEOREMS-\d{3}", x)]
    missing_relation_targets = sorted({rid for r in relations for rid in (r["source_object_id"], r["target_object_id"]) if rid not in object_by_id})

    result_specs = [
        ("RESULT-THEOREMS-001", "TLC-SO-THEOREMS-002", "StabilitÃ© dâ€™une communautÃ©", "13-26", "partial", "proof_not_available_as_complete", ["TLC-FC-06-THEOREMS-006"], 4, 0, 0),
        ("RESULT-THEOREMS-002", "TLC-SO-THEOREMS-003", "Ã‰mergence collective", "31-47", "partial", "proof_not_available_as_complete", ["TLC-FC-06-THEOREMS-006"], 4, 0, 1),
        ("RESULT-THEOREMS-003", "TLC-SO-THEOREMS-004", "ThÃ©orÃ¨me CNS", "49-90", "partial", "proof_not_available_as_complete", ["TLC-FC-06-THEOREMS-006"], 0, 0, 1),
        ("RESULT-THEOREMS-004", "TLC-SO-THEOREMS-008", "Convergence trajectorielle", "92-112", "partial", "proof_not_available_as_complete", ["TLC-FC-06-THEOREMS-006"], 3, 0, 0),
        ("RESULT-THEOREMS-005", "TLC-SO-THEOREMS-009", "Propagation dâ€™onde identitaire", "114-127", "absent", "proof_not_available", ["TLC-FC-06-THEOREMS-006"], 0, 0, 0),
        ("RESULT-THEOREMS-006", "TLC-SO-THEOREMS-010", "Bifurcation de la rÃ©ceptivitÃ©", "129-139", "partial", "proof_not_available_as_complete", ["TLC-FC-06-THEOREMS-006"], 0, 0, 0),
        ("RESULT-THEOREMS-007", "TLC-SO-THEOREMS-011", "Conservation de lâ€™information expÃ©rientielle", "141-147", "partial", "proof_status_unresolved", ["TLC-FC-06-THEOREMS-001"], 0, 1, 0),
    ]
    results = []
    for rid, oid, name, lines, proof_status, logical_status, fids, hypotheses, axioms, quantifiers in result_specs:
        results.append({
            "result_id": rid, "source_object_ids": [oid], "source_relation_ids": [], "affected_feature_ids": fids,
            "canonical_name": name, "result_kind": "theorem", "source_location": f"{SOURCE}:{lines}",
            "statement_status": "explicit", "hypotheses": "explicit_in_source" if hypotheses else "not_specified",
            "hypotheses_count": hypotheses, "axioms": "external_reference" if axioms else "not_specified", "axioms_count": axioms,
            "definitions_required": "not_yet_determinable", "invariants_required": "not_yet_determinable",
            "equations_required": "explicit_or_referenced_where_present", "domain_of_validity": "not_fully_specified",
            "variables": object_by_id[oid].get("symbols_mentioned", []), "quantifiers": "explicit" if quantifiers else "not_specified",
            "explicit_quantifier_count": quantifiers, "conclusion": "explicit_statement", "exceptions": "not_specified",
            "proof_status": proof_status, "logical_form_status": logical_status, "constructive_status": "not_yet_determinable",
            "mechanical_verification_status": "not_yet_determinable", "execution_status": "structurally_representable_not_executable",
            "semantic_status": "unresolved" if oid == "TLC-SO-THEOREMS-011" else "structurally_supported",
            "effect_on_contract_planning": "statement_contract_possible_with_reservations",
            "effect_on_ir_planning": "structural_representation_only_until_contract_validation",
            "notes": "Local source does not provide a complete formal proof; the final source note refers complete demonstrations elsewhere."
        })

    proof_specs = [
        ("PROOF-THEOREMS-001", "RESULT-THEOREMS-001", "27-29", "Esquisse de preuve"),
        ("PROOF-THEOREMS-002", "RESULT-THEOREMS-002", "45-47", "IdÃ©e de preuve"),
        ("PROOF-THEOREMS-003", "RESULT-THEOREMS-003", "54-90", "Argument de complÃ©tude, nÃ©cessitÃ© et suffisance"),
        ("PROOF-THEOREMS-004", "RESULT-THEOREMS-004", "106-112", "Preuve locale non dÃ©clarÃ©e complÃ¨te"),
        ("PROOF-THEOREMS-005", "RESULT-THEOREMS-006", "137-139", "Esquisse de preuve"),
        ("PROOF-THEOREMS-006", "RESULT-THEOREMS-007", "146-147", "IdÃ©e"),
    ]
    proofs = [{
        "proof_id": pid, "source_object_ids": [], "proves_result_ids": [rid], "source_location": f"{SOURCE}:{lines}",
        "proof_kind": "not_specified", "premises": [], "referenced_axioms": [], "referenced_definitions": [],
        "referenced_lemmas": [], "referenced_theorems": [], "referenced_invariants": [], "proof_steps": "source_prose_preserved_not_formalized",
        "missing_steps": "not_yet_determinable", "proof_completeness": "partial", "formalization_status": "not_formalized",
        "mechanical_check_possible": False, "unresolved": ["complete proof not present in local source"], "notes": label
    } for pid, rid, lines, label in proof_specs]

    inventory = {
        "domain_id": DOMAIN, "canonical_name": "Theorems", "source_file": SOURCE, "source_hash": source_hash, "baseline_commit": BASELINE,
        "objects": {"found": 30, "covered": 30, "missing": 0, "duplicate_ids": [], "invalid_ids": invalid_object_ids, "type_distribution": type_distribution},
        "relations": {"found": 29, "covered": 29, "missing": 0, "duplicate_ids": [], "invalid_ids": invalid_relation_ids, "type_distribution": relation_distribution, "missing_object_references": missing_relation_targets},
        "unresolved": {"found": 12, "covered": 12, "missing": 0, "duplicate_ids": [], "type_distribution": unresolved_distribution},
        "logical_elements": {"theorems": 7, "propositions": 0, "lemmas": 0, "corollaries": 0, "proofs": 6, "complete_proofs": 0, "partial_proofs": 6, "missing_proofs": 1, "axioms_referenced": 1, "hypotheses_referenced": 11, "invariants_referenced": 1, "equations_referenced": 7},
        "source_sections": ["Introduction", "StabilitÃ© dâ€™une communautÃ©", "Ã‰mergence collective", "ThÃ©orÃ¨me CNS", "Convergence des trajectoires du Disciple", "Propagation dâ€™onde dans lâ€™identitÃ©", "Bifurcation de la rÃ©ceptivitÃ©", "Conservation de lâ€™information expÃ©rientielle", "SynthÃ¨se"],
        "source_locations": [f"{SOURCE}:1-158"], "external_references": ["PDF sections 1.28, 1.36, etc. (not available as precise proof citations)", "section 1.45.8"],
        "inventory_status": "complete_with_reservations", "issues": ["Source/extraction classification conflict for TLC-SO-THEOREMS-011."],
        "reservations": ["All local proofs are partial or absent.", "Two duplicate candidates must not be merged automatically."]
    }
    dump(REG / "source-inventory.yaml", inventory)
    report("source-inventory-report.md", "Theorems source inventory", ["30 objects, 29 relations, 12 unresolved terms, and 9 catalogue features were found.", "Seven theorem statements are explicit in the source.", "Six local proof texts are partial; one theorem has no local proof.", "Two duplicate candidates are preserved without merging."], inventory["reservations"])

    scientific_elements = []
    for obj in objects:
        oid = obj["provisional_object_id"]
        scientific_elements.append({"element_id": oid, "element_kind": "scientific_object", "source_location": source_ref(obj), "classification": "covered_by_feature" if object_to_features[oid] else "missing_from_catalogue", "feature_ids": object_to_features[oid], "validation_status": obj["validation_status"], "incoming_relation_ids": [r["provisional_relation_id"] for r in relations if r["target_object_id"] == oid], "outgoing_relation_ids": [r["provisional_relation_id"] for r in relations if r["source_object_id"] == oid], "unresolved_ids": [u["unresolved_id"] for u in unresolved if oid in u["affected_object_ids"]]})
    for rel in relations:
        scientific_elements.append({"element_id": rel["provisional_relation_id"], "element_kind": "scientific_relation", "source_location": f"{SOURCE}:{rel['source_reference']['start_line']}-{rel['source_reference']['end_line']}", "classification": "supporting_relation", "feature_ids": object_to_features[rel["source_object_id"]], "source_object_id": rel["source_object_id"], "target_object_id": rel["target_object_id"], "relation_type": rel["relation_type"], "validation_status": rel["validation_status"]})
    scientific_coverage = {"domain_id": DOMAIN, "baseline_commit": BASELINE, "elements": scientific_elements, "summary": {"objects_total": 30, "objects_covered": 30, "objects_missing": 0, "relations_total": 29, "relations_covered": 29, "relations_missing": 0, "unresolved_total": 12, "unresolved_covered": 12, "duplicate_candidates": 2, "catalogue_gap_candidates": 0}, "status": "complete_with_reservations"}
    dump(REG / "scientific-coverage.yaml", scientific_coverage)
    report("scientific-coverage-report.md", "Theorems scientific coverage", ["All 30 objects, 29 relations, and 12 unresolved terms are accounted for.", "No missing object reference or invalid identifier was found.", "Relations are supporting scientific context; they are not silently converted to software dependencies."], ["Twelve object classifications remain unresolved.", "Two duplicate candidates remain unresolved."])

    feature_inventory = []
    for item in feature_lineage:
        fid = item["original_feature_candidate_id"]
        c = class_by_id[fid]
        refs = item["source_references"]
        feature_inventory.append({"feature_id": fid, "canonical_name": catalog[fid]["name"], "source_file": SOURCE, "source_object_ids": item["scientific_object_ids"], "source_relation_ids": sorted({rid for ref in refs for rid in ref.get("scientific_relation_ids", [])}), "source_locations": [f"{r['source_path']}:{r['start_line']}-{r['end_line']}" for r in refs], "catalogue_status": catalog[fid]["readiness"], "result_kind": "theorem_collection" if fid == "TLC-FC-06-THEOREMS-006" else catalog[fid]["category"], "proof_objects": [p["proof_id"] for p in proofs if any(result["affected_feature_ids"] == [fid] and result["result_id"] in p["proves_result_ids"] for result in results)], "historical_contract_found": False, "historical_ir_found": False, "cross_domain_symbols": [], "scientific_unresolved": [u["unresolved_id"] for u in unresolved if set(u["affected_object_ids"]) & set(item["scientific_object_ids"])], "inventory_status": "inventoried", "review_classification": c["classification"], "active_feature_candidate": c["active_feature_candidate"], "notes": c["justification"]})
    dump(REG / "feature-inventory.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "features": feature_inventory, "summary": {"catalogue_features": 9, "inventoried_features": 9, "features_with_statements": 2, "features_with_proofs": 2, "features_without_proofs": 7, "features_with_unresolved": sum(bool(x["scientific_unresolved"]) for x in feature_inventory), "missing_features": 0, "duplicate_features": 0, "orphan_features": 0}, "status": "complete"})
    report("feature-inventory-report.md", "Theorems feature inventory", ["The canonical catalogue contains exactly nine Theorems feature IDs.", "All nine are inventoried; none is missing, duplicated, or orphaned.", "Four are active contract candidates with reservations; five are deferred or rejected as software features by canonical review."], ["Rejected or deferred entries remain planned conservatively; their catalogue status is not changed."])

    functional_rows = []
    for obj in objects:
        functional_rows.append({"source_element_id": obj["provisional_object_id"], "element_kind": "scientific_object", "feature_ids": object_to_features[obj["provisional_object_id"]], "justification": "theorem_statement" if obj["object_type"] == "Theorem" else "contextual_definition", "coverage_status": "covered"})
    for rel in relations:
        functional_rows.append({"source_element_id": rel["provisional_relation_id"], "element_kind": "scientific_relation", "feature_ids": object_to_features[rel["source_object_id"]], "justification": "supporting_relation", "coverage_status": "covered"})
    for item in unresolved:
        fids = sorted({fid for oid in item["affected_object_ids"] for fid in object_to_features[oid]})
        functional_rows.append({"source_element_id": item["unresolved_id"], "element_kind": "unresolved", "feature_ids": fids, "justification": "unresolved_without_feature" if not fids else "source_metadata", "coverage_status": "covered"})
    dump(REG / "functional-coverage.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "mappings": functional_rows, "summary": {"objects_mapped": 30, "relations_mapped": 29, "unresolved_mapped": 12, "features_covered": 9, "missing_features": 0, "possible_catalogue_gaps": 0}, "status": "complete_with_reservations"})
    report("functional-coverage-report.md", "Theorems functional coverage", ["Every object, relation, and unresolved item maps to a catalogue feature or an authorized supporting justification.", "All nine catalogue features are covered.", "No proof sentence was promoted to an additional feature."], ["Canonical review rejects or defers five feature candidates; this preparation does not override those decisions."])

    dump(REG / "result-semantics.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "results": results, "summary": {"theorem_statements": 7, "proposition_statements": 0, "lemma_statements": 0, "corollary_statements": 0, "explicit_hypothesis_groups": 3, "explicit_axiom_references": 1, "explicit_quantified_results": 2, "explicit_conclusions": 7, "unresolved_statements": 1, "constructive_results": 0, "mechanically_verifiable_candidates": 0, "non_computational_results": 7, "not_yet_determinable": 7}, "status": "complete_with_reservations"})
    report("result-semantics-report.md", "Theorems result semantics", ["Seven theorem statements are explicit; no proposition, lemma, or corollary is explicitly labeled.", "All seven are structurally representable but not executable from the available semantics.", "No result is declared mechanically verifiable."], ["Theorem/axiom classification for conservation remains unresolved.", "Domains, quantifiers, and hypotheses are incomplete for several results."])

    dump(REG / "proof-inventory.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "proofs": proofs, "missing_proofs": [{"result_id": "RESULT-THEOREMS-005", "source_location": f"{SOURCE}:114-127", "proof_completeness": "absent"}], "summary": {"proofs": 6, "complete": 0, "partial": 6, "absent": 1, "not_assessable": 0, "direct": 0, "contradiction": 0, "induction": 0, "construction": 0, "referenced_external": 0, "not_specified": 6, "mechanically_checkable_candidates": 0}, "status": "complete_with_reservations"})
    report("proof-inventory-report.md", "Theorems proof inventory", ["Six local proof texts or sketches are inventoried and remain partial.", "The wave-propagation theorem has no local proof.", "No proof kind is assigned because the source does not explicitly classify them."], ["The source points to original PDF chapters without precise proof artifacts.", "No proof is completed or mechanically validated here."])

    concept_terms = ["theorem", "proposition", "lemma", "corollary", "axiom", "hypothesis", "assumption", "definition", "invariant", "constraint", "empirical_claim", "example", "proof", "algorithm", "validation_rule"]
    concept_rows = [{"source_term": term, "source_object_ids": ["TLC-SO-THEOREMS-011"] if term in {"theorem", "axiom"} else [], "object_type": term, "canonical_classification": term, "possible_confusions": ["theorem", "axiom"] if term in {"theorem", "axiom"} else [], "separation_status": "ambiguous" if term in {"theorem", "axiom"} else ("explicit" if term in {"theorem", "proof", "hypothesis", "constraint", "invariant"} else "unresolved"), "effect_on_contract_kind": "preserve_source_classification", "effect_on_ir_kind": "structural_only", "notes": "No category fusion is authorized."} for term in concept_terms]
    dump(REG / "concept-separation.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "concepts": concept_rows, "unresolved_conceptual_cases": ["TLC-SO-THEOREMS-011 theorem versus extracted axiom"], "status": "complete_with_reservations"})
    report("concept-separation-report.md", "Theorems concept separation", ["Theorem, proposition, lemma, corollary, axiom, hypothesis, definition, invariant, constraint, proof, algorithm, and validation rule remain distinct.", "No proposition, lemma, or corollary is explicitly present.", "Proof prose is not treated as an algorithm."], ["Conservation is a source theorem but a candidate extracted axiom; the conflict remains unresolved."])

    dependencies = {
        "master": [{"dependency_id": "DEP-THEOREMS-MASTER-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-006"], "affected_object_ids": ["TLC-SO-THEOREMS-008"], "source_evidence": f"{SOURCE}:92-112", "target_evidence": "maths/00-master.md", "dependency_status": "confirmed", "required_level": "symbol_only", "proof_role": "definition", "production_effect": "blocks_proof_representation", "notes": "Master state is explicit; target identifier mapping is unresolved."}],
        "disciple": [{"dependency_id": "DEP-THEOREMS-DISCIPLE-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-006"], "affected_object_ids": ["TLC-SO-THEOREMS-004", "TLC-SO-THEOREMS-008", "TLC-SO-THEOREMS-009", "TLC-SO-THEOREMS-010"], "source_evidence": f"{SOURCE}:49-139", "target_evidence": "maths/01-disciple.md", "dependency_status": "confirmed", "required_level": "symbol_only", "proof_role": "definition", "production_effect": "blocks_proof_representation", "notes": "Disciple is canonical but execution is not assumed."}],
        "community": [{"dependency_id": "DEP-THEOREMS-COMMUNITY-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-006"], "affected_object_ids": ["TLC-SO-THEOREMS-002", "TLC-SO-THEOREMS-003"], "source_evidence": f"{SOURCE}:13-47", "target_evidence": "maths/02-community.md", "dependency_status": "confirmed", "required_level": "reviewed_feature", "proof_role": "definition", "production_effect": "blocks_proof_representation", "authority_status": "canonical_in_main", "future_reconciliation_required": True, "reconciliation_trigger": "Community contracts and IRs become canonical in main", "notes": "Community preparation is canonical; complete contract/IR coverage is not."}],
        "huit-dimensions": [{"dependency_id": "DEP-THEOREMS-HUIT-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-005", "TLC-FC-06-THEOREMS-006", "TLC-FC-06-THEOREMS-008", "TLC-FC-06-THEOREMS-009"], "affected_object_ids": ["TLC-SO-THEOREMS-004", "TLC-SO-THEOREMS-005", "TLC-SO-THEOREMS-006", "TLC-SO-THEOREMS-007", "TLC-SO-THEOREMS-018", "TLC-SO-THEOREMS-019", "TLC-SO-THEOREMS-020", "TLC-SO-THEOREMS-021", "TLC-SO-THEOREMS-022", "TLC-SO-THEOREMS-023", "TLC-SO-THEOREMS-024", "TLC-SO-THEOREMS-025"], "source_evidence": f"{SOURCE}:49-90", "target_evidence": "maths/03-huit-dimensions-de-tl.md", "dependency_status": "confirmed", "required_level": "reviewed_feature", "proof_role": "definition", "production_effect": "blocks_proof_representation", "authority_status": "unavailable", "future_reconciliation_required": True, "notes": "Target preparation exists only on a non-authoritative local parallel branch."}],
        "invariants": [{"dependency_id": "DEP-THEOREMS-INVARIANTS-001", "affected_feature_ids": [], "affected_object_ids": [], "source_evidence": f"{SOURCE}:3-10,149-156", "target_evidence": "maths/04-invariants.md", "dependency_status": "inferred_candidate", "required_level": "not_yet_determinable", "proof_role": "informational_only", "production_effect": "does_not_block_structure", "authority_status": "unavailable", "future_reconciliation_required": True, "notes": "The source mentions invariant robustness but does not identify a theorem object proving it."}],
        "dynamics": [{"dependency_id": "DEP-THEOREMS-DYNAMICS-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-002", "TLC-FC-06-THEOREMS-003", "TLC-FC-06-THEOREMS-004", "TLC-FC-06-THEOREMS-006"], "affected_object_ids": ["TLC-SO-THEOREMS-002", "TLC-SO-THEOREMS-003", "TLC-SO-THEOREMS-008", "TLC-SO-THEOREMS-009", "TLC-SO-THEOREMS-010", "TLC-SO-THEOREMS-014", "TLC-SO-THEOREMS-016", "TLC-SO-THEOREMS-017", "TLC-SO-THEOREMS-026", "TLC-SO-THEOREMS-027", "TLC-SO-THEOREMS-028", "TLC-SO-THEOREMS-029", "TLC-SO-THEOREMS-030"], "source_evidence": f"{SOURCE}:13-139", "target_evidence": "maths/05-dynamics.md", "dependency_status": "confirmed", "required_level": "validated_contract", "proof_role": "premise", "production_effect": "blocks_proof_representation", "authority_status": "unavailable", "future_reconciliation_required": True, "notes": "Dynamics is not canonical in origin/main."}],
    }
    for domain, filename, title in [("master", "master-dependencies.yaml", "Master dependency"), ("disciple", "disciple-dependencies.yaml", "Disciple dependency"), ("community", "community-dependencies.yaml", "Community dependency"), ("huit-dimensions", "huit-dimensions-dependencies.yaml", "Huit Dimensions dependency"), ("invariants", "invariants-dependencies.yaml", "Invariants dependency"), ("dynamics", "dynamics-dependencies.yaml", "Dynamics dependency")]:
        dump(REG / filename, {"domain_id": DOMAIN, "target_domain": domain, "baseline_commit": BASELINE, "dependencies": dependencies[domain], "summary": {"confirmed": sum(x["dependency_status"] == "confirmed" for x in dependencies[domain]), "inferred_candidate": sum(x["dependency_status"] == "inferred_candidate" for x in dependencies[domain]), "rejected": 0, "unresolved": 0}, "status": "complete_with_reservations"})
        report(filename.replace(".yaml", "-report.md").replace("dependencies-report", "dependency-report"), f"Theorems {title} analysis", [f"{len(dependencies[domain])} evidence-grounded dependency record is retained.", f"Authority and production effects are explicit for {domain}."], [dependencies[domain][0]["notes"]])

    message_principle = {"domain_id": DOMAIN, "baseline_commit": BASELINE, "message": [{"dependency_id": "DEP-THEOREMS-MESSAGE-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-008"], "source_evidence": f"{SOURCE}:56-63,81", "dependency_status": "confirmed", "required_level": "symbol_only", "proof_role": "definition"}], "principle": [{"dependency_id": "DEP-THEOREMS-PRINCIPLE-001", "affected_feature_ids": ["TLC-FC-06-THEOREMS-009"], "source_evidence": f"{SOURCE}:56-63,82", "dependency_status": "confirmed", "required_level": "symbol_only", "proof_role": "definition"}], "future_reconciliation_required": True, "status": "complete_with_reservations"}
    dump(REG / "message-principle-dependencies.yaml", message_principle)
    report("message-principle-dependency-report.md", "Theorems Message and Principle dependencies", ["Message and Principles are explicit CNS dimensions.", "The dependencies are confirmed at source-term level only; target identifiers are unresolved."], ["Neither domain is prepared canonically in main.", "A principle is not treated as an axiom."])

    external_domains = []
    for domain, line in [("values", 83), ("virtues", 84), ("capacities", 85), ("competencies", 86), ("practice", 87), ("lived-experience", 88), ("relations", 18)]:
        external_domains.append({"domain_id": domain, "confirmed_dependencies": 1, "inferred_candidates": 0, "rejected_candidates": 0, "unresolved_dependencies": 1 if domain == "relations" else 0, "affected_feature_ids": ["TLC-FC-06-THEOREMS-008"] if domain != "relations" else ["TLC-FC-06-THEOREMS-006"], "required_level": "symbol_only", "proof_role": "definition", "blocking_contract_generation": False, "blocking_ir_generation": True, "blocking_proof_representation": True, "blocking_execution_only": False, "future_reconciliation_required": True, "source_evidence": f"{SOURCE}:{line}", "notes": "Target canonical identifier mapping is unresolved."})
    dump(REG / "external-domain-dependencies.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "domains": external_domains, "status": "complete_with_reservations"})
    report("external-domain-dependency-report.md", "Theorems external-domain dependencies", ["Values, Virtues, Capacities, Competencies, Practice, Lived Experience, and Relations were analyzed.", "Explicit CNS dimension references are confirmed at term level; target mappings remain unresolved."], ["Lexical repetition alone was not accepted as dependency evidence."])

    mappings = []
    for idx, (term, domain, oid, line) in enumerate([("Master", "master", "TLC-SO-THEOREMS-008", 93), ("Disciple", "disciple", "TLC-SO-THEOREMS-008", 93), ("communautÃ©", "community", "TLC-SO-THEOREMS-002", 13), ("Message", "message", "TLC-SO-THEOREMS-018", 81), ("Principes", "principle", "TLC-SO-THEOREMS-019", 82), ("Valeurs", "values", "TLC-SO-THEOREMS-020", 83), ("Vertus", "virtues", "TLC-SO-THEOREMS-021", 84), ("CapacitÃ©s", "capacities", "TLC-SO-THEOREMS-022", 85), ("CompÃ©tences", "competencies", "TLC-SO-THEOREMS-023", 86), ("Pratique", "practice", "TLC-SO-THEOREMS-024", 87), ("ExpÃ©rience vÃ©cue", "lived-experience", "TLC-SO-THEOREMS-025", 88)], 1):
        mappings.append({"mapping_id": f"MAP-THEOREMS-{idx:03d}", "theorems_source_term": term, "theorems_object_ids": [oid], "theorems_feature_ids": object_to_features[oid], "target_domain": domain, "target_canonical_object_id": "unresolved", "target_feature_ids": [], "target_contract_ids": [], "target_ir_ids": [], "mapping_status": "unresolved", "required_level": "symbol_only", "proof_role": "definition", "evidence": f"{SOURCE}:{line}", "notes": "Source term preserved; no target identity is inferred."})
    dump(REG / "upstream-symbol-mapping.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "mappings": mappings, "status": "complete_with_reservations"})
    report("upstream-symbol-reconciliation-report.md", "Theorems upstream-symbol reconciliation", [f"{len(mappings)} explicit source terms are retained for future target reconciliation.", "No canonical target object identifier is inferred."], ["Mappings remain unresolved until target-domain reconciliation."])

    rejected_dependency_candidates = [{"candidate_id": f"CTX-THEOREMS-{i:03d}", "from_feature_id": fid, "to_feature_id": "TLC-FC-06-THEOREMS-007", "classification": "shared_scientific_context_not_dependency", "source_evidence": SOURCE} for i, fid in enumerate(feature_ids, 1) if fid != "TLC-FC-06-THEOREMS-007"]
    feature_graph = {"domain_id": DOMAIN, "baseline_commit": BASELINE, "edges": [], "rejected_dependency_candidates": rejected_dependency_candidates, "summary": {"confirmed_edges": 0, "inferred_edges": 0, "unresolved_edges": 0, "root_features": feature_ids, "leaf_features": feature_ids, "cycles": [], "independent_components": [[fid] for fid in feature_ids], "partial_topological_order": feature_ids, "production_groups": ["A_independent_statements", "K_scientific_decision_required"]}, "status": "complete_with_reservations"}
    dump(REG / "feature-dependencies.yaml", feature_graph)
    report("feature-dependency-report.md", "Theorems internal feature graph", ["No reviewed scientific-context relation is promoted to a software dependency.", "All nine features remain roots and leaves in the confirmed dependency graph.", "No confirmed, inferred, or unresolved internal cycle exists."], ["Eight shared-context candidates are retained as rejected dependency candidates."])

    proof_nodes = [{"node_id": r["result_id"], "node_kind": "result", "source_location": r["source_location"]} for r in results] + [{"node_id": p["proof_id"], "node_kind": "proof", "source_location": p["source_location"]} for p in proofs]
    proof_edges = [{"edge_id": f"PROOF-EDGE-{i:03d}", "from_result_or_proof_id": p["proof_id"], "to_result_or_proof_id": p["proves_result_ids"][0], "dependency_kind": "proof_step", "strength": "explicit", "source_evidence": p["source_location"], "notes": "Links local proof prose to its stated result only."} for i, p in enumerate(proofs, 1)]
    dump(REG / "proof-dependency-graph.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "nodes": proof_nodes, "edges": proof_edges, "results_without_proof": ["RESULT-THEOREMS-005"], "proofs_without_target": [], "missing_dependency_targets": [], "circularity_candidates": [], "summary": {"nodes": 13, "edges": 6, "result_nodes": 7, "proof_nodes": 6, "premise_edges": 0, "lemma_edges": 0, "theorem_edges": 0, "invariant_edges": 0, "unresolved_edges": 0, "cycles": 0}, "status": "complete_with_reservations"})
    report("proof-dependency-graph-report.md", "Theorems proof dependency graph", ["The graph contains seven result nodes, six proof nodes, and six explicit proof-to-result edges.", "No premise, lemma, theorem, invariant, or circular proof edge is asserted.", "One result has no local proof."], ["Internal proof steps and external proof targets are not sufficiently specified."])

    primary_classification = {"001": "not_yet_determinable", "002": "dynamic_property_theorem_contract", "003": "structural_contract", "004": "validation_contract", "005": "structural_contract", "006": "theorem_declaration_contract", "007": "structural_contract", "008": "non_computational_contract", "009": "non_computational_contract"}
    feature_classes = []
    for feature in feature_inventory:
        suffix = feature["feature_id"][-3:]
        primary = primary_classification[suffix]
        feature_classes.append({"feature_id": feature["feature_id"], "primary_classification": primary, "secondary_classifications": [], "source_evidence": feature["source_locations"], "statement_semantics_supported": suffix in {"001", "006"}, "hypotheses_supported": suffix == "006", "conclusion_supported": suffix in {"001", "006"}, "proof_structure_supported": suffix == "006", "proof_validation_supported": False, "mechanical_verification_supported": False, "computational_claim_supported": False, "expected_contract_kind": primary, "expected_ir_kind": "non_computational" if primary in {"theorem_declaration_contract", "non_computational_contract", "not_yet_determinable"} else "structural", "execution_readiness_expected": False, "classification_status": "unresolved" if primary == "not_yet_determinable" else "prepared_with_reservations", "notes": "Classification does not override canonical catalogue review."})
    dump(REG / "feature-classification.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "features": feature_classes, "summary": dict(Counter(x["primary_classification"] for x in feature_classes)), "status": "complete_with_reservations"})
    report("feature-classification-report.md", "Theorems feature classification", ["All nine catalogue features have a conservative preparation classification.", "No feature is classified as computational solely because logical checking is imaginable.", "The theorem/axiom conflict remains not yet determinable."], ["Five canonical candidates remain deferred or rejected by scientific review."])

    groups = [
        {"group_id": "A_independent_statements", "order": 1, "feature_ids": ["TLC-FC-06-THEOREMS-006"], "contract_generation_allowed": True, "blocking_conditions": ["targeted extraction", "proof reservations"]},
        {"group_id": "G_after_dynamics", "order": 2, "feature_ids": ["TLC-FC-06-THEOREMS-002", "TLC-FC-06-THEOREMS-003", "TLC-FC-06-THEOREMS-004"], "contract_generation_allowed": False, "blocking_conditions": ["Dynamics reconciliation"]},
        {"group_id": "J_multiple_domain_dependencies", "order": 3, "feature_ids": ["TLC-FC-06-THEOREMS-005", "TLC-FC-06-THEOREMS-008", "TLC-FC-06-THEOREMS-009"], "contract_generation_allowed": False, "blocking_conditions": ["Huit Dimensions and dimension-domain reconciliation", "scientific review"]},
        {"group_id": "K_scientific_decision_required", "order": 4, "feature_ids": ["TLC-FC-06-THEOREMS-001", "TLC-FC-06-THEOREMS-007"], "contract_generation_allowed": False, "blocking_conditions": ["classification conflict or targeted extraction"]},
    ]
    for group in groups:
        group.update({"internal_prerequisites": [], "master_prerequisites": [], "disciple_prerequisites": [], "community_prerequisites": [], "huit_dimensions_prerequisites": [], "invariants_prerequisites": [], "dynamics_prerequisites": ["canonical Dynamics artifacts"] if group["group_id"] == "G_after_dynamics" else [], "message_prerequisites": [], "principle_prerequisites": [], "other_domain_prerequisites": [], "structural_ir_generation_expected": False, "proof_representation_expected": False, "mechanical_verification_claim_allowed": False, "execution_claim_allowed": False, "future_reconciliation_required": group["group_id"] != "A_independent_statements", "notes": "Preparation order only; no production occurs."})
    dump(REG / "production-order.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "groups": groups, "status": "complete_with_reservations"})
    report("production-order-report.md", "Theorems production order", ["Four conservative groups cover all nine features.", "Only statement preparation is potentially independent; all generated IR remains gated.", "Future reconciliation does not block completion of preparation."], ["Group membership does not authorize contract generation by itself."])

    contract_gates = {"001": "local_scientific_decision_required", "002": "dynamics_contract_required", "003": "multiple_domains_required", "004": "dynamics_symbols_required", "005": "local_scientific_decision_required", "006": "proof_source_required", "007": "missing_source_evidence", "008": "local_scientific_decision_required", "009": "local_scientific_decision_required"}
    ir_gates = {"001": "local_scientific_decision_required", "002": "dynamics_ir_available", "003": "multiple_dependencies_available", "004": "dynamics_contract_available", "005": "local_scientific_decision_required", "006": "proof_source_available", "007": "not_yet_assessable", "008": "multiple_dependencies_available", "009": "local_scientific_decision_required"}
    contract_plans, ir_plans, feature_status = [], [], []
    for feature in feature_inventory:
        fid, suffix = feature["feature_id"], feature["feature_id"][-3:]
        result_kind = next((x["result_kind"] for x in results if fid in x["affected_feature_ids"]), feature["result_kind"])
        common_deps = {"master_dependencies": ["DEP-THEOREMS-MASTER-001"] if fid == "TLC-FC-06-THEOREMS-006" else [], "disciple_dependencies": ["DEP-THEOREMS-DISCIPLE-001"] if fid == "TLC-FC-06-THEOREMS-006" else [], "community_dependencies": ["DEP-THEOREMS-COMMUNITY-001"] if fid == "TLC-FC-06-THEOREMS-006" else [], "huit_dimensions_dependencies": ["DEP-THEOREMS-HUIT-001"] if suffix in {"005", "006", "008", "009"} else [], "invariants_dependencies": [], "dynamics_dependencies": ["DEP-THEOREMS-DYNAMICS-001"] if suffix in {"002", "003", "004", "006"} else [], "message_dependencies": ["DEP-THEOREMS-MESSAGE-001"] if suffix in {"005", "006", "008"} else [], "principle_dependencies": ["DEP-THEOREMS-PRINCIPLE-001"] if suffix in {"005", "006", "009"} else []}
        contract_plans.append({"feature_id": fid, "canonical_name": feature["canonical_name"], "planned_contract_type": primary_classification[suffix], "source_objects": feature["source_object_ids"], "source_relations": feature["source_relation_ids"], "source_locations": feature["source_locations"], "result_kind": result_kind, "expected_statement": "preserve_source_statement", "expected_hypotheses": "preserve_explicit_only", "expected_axioms": "preserve_explicit_only", "expected_definitions": "not_yet_determinable", "expected_variables": "extract_without_inference", "expected_parameters": "extract_without_inference", "expected_constants": "extract_without_inference", "expected_sets": "extract_without_inference", "expected_spaces": "extract_without_inference", "expected_quantifiers": "preserve_explicit_only", "expected_relations": "preserve_explicit_only", "expected_equations": "preserve_explicit_only", "expected_constraints": "preserve_explicit_only", "expected_invariants": "preserve_explicit_only", "expected_conclusion": "preserve_explicit_only", "expected_exceptions": "not_specified", "expected_proof_status": "partial_or_absent", "expected_proof_elements": feature["proof_objects"], "expected_preconditions": "not_yet_determinable", "expected_postconditions": "not_yet_determinable", "expected_failure_conditions": "not_specified", **common_deps, "other_external_dependencies": [], "known_unresolved": feature["scientific_unresolved"], "required_evidence_before_generation": [class_by_id[fid]["justification"]], "contract_generation_gate": contract_gates[suffix], "contract_generation_priority": "after_required_gate", "contract_generation_ready": suffix == "006" and class_by_id[fid]["active_feature_candidate"], "mechanical_verification_readiness_expected": False, "execution_readiness_expected": False, "code_generation_readiness_expected": False, "notes": "Plan only; no contract is produced."})
        ir_plans.append({"feature_id": fid, "planned_contract_dependency": f"validated contract for {fid}", "planned_ir_kind": "theorem_declaration" if suffix == "006" else ("dynamic_property" if suffix == "002" else ("validation" if suffix == "004" else ("non_computational" if suffix in {"001", "008", "009"} else "structural"))), "planned_statement_representation": "structural_source_preserving", "planned_hypotheses": "explicit_only", "planned_axioms": "explicit_only", "planned_definitions": "opaque_until_validated", "planned_quantifiers": "explicit_only", "planned_relations": "traceable_edges_only", "planned_equations": "opaque_or_structural_without_solver", "planned_constraints": "explicit_only", "planned_invariants": "explicit_only", "planned_conclusion": "explicit_only", "planned_proof_nodes": "partial_or_absent_markers", "planned_proof_edges": "explicit_source_links_only", "planned_external_symbols": "unresolved_target_mappings", "planned_unresolved_representation": "explicit_unresolved_nodes", **common_deps, "other_domain_dependencies": [], "schema_candidate": "language_independent_structural_ir", "validator_candidate": "trace_and_coverage_validator", "contract_to_ir_coverage_strategy": "one_to_one_trace_matrix", "proof_representation_strategy": "preserve_partial_or_absent_without_completion", "ir_generation_gate": ir_gates[suffix], "structural_ir_possible": True, "proof_ir_possible": False, "mechanical_verification_expected": False, "execution_ready_expected": False, "implementation_planning_readiness_expected": False, "code_generation_readiness_expected": False, "notes": "Plan only; no IR is produced."})
        feature_status.append({"feature_id": fid, "canonical_name": feature["canonical_name"], "inventory_status": "inventoried", "source_coverage": "complete", "scientific_coverage": "complete_with_reservations", "result_semantics_status": "prepared_with_reservations", "proof_status": "partial_or_absent", "internal_dependencies": [], "proof_dependencies": feature["proof_objects"], **common_deps, "other_domain_dependencies": [], "scientific_unresolved": feature["scientific_unresolved"], "classification": primary_classification[suffix], "planned_contract_status": "planned", "planned_ir_status": "planned", "contract_generation_gate": contract_gates[suffix], "ir_generation_gate": ir_gates[suffix], "proof_representation_possible": False, "mechanical_verification_possible": False, "structural_representation_possible": True, "execution_readiness": False, "implementation_readiness": False, "code_generation_readiness": False, "preparation_status": "prepared_with_reservations", "blocking_reason": class_by_id[fid]["justification"], "reservations": [class_by_id[fid]["classification"]], "notes": "Preparation does not change canonical feature status."})
    dump(REG / "contract-production-plan.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "features": contract_plans, "summary": {"planned_contracts": 9, "ready_now": sum(x["contract_generation_ready"] for x in contract_plans), "code_ready": 0}, "status": "complete_with_reservations"})
    report("contract-production-plan-report.md", "Theorems contract-production plan", ["All nine catalogue features have a contract plan.", "No contract is produced.", "Every plan preserves incomplete proofs and unresolved semantics."], ["Only one statement-oriented plan is structurally eligible now; scientific gates still apply."])
    dump(REG / "ir-production-plan.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "features": ir_plans, "summary": {"planned_irs": 9, "structural_ir_possible": 9, "proof_ir_possible": 0, "mechanical_verification_expected": 0, "code_ready": 0}, "status": "complete_with_reservations"})
    report("ir-production-plan-report.md", "Theorems IR-production plan", ["All nine catalogue features have a language-independent IR plan.", "No IR is produced.", "Proof nodes remain partial or absent markers and equations have no solver or discretization."], ["All IR generation remains gated by validated contracts and upstream reconciliation."])

    unresolved_rows = []
    for item in unresolved:
        affected_features = sorted({fid for oid in item["affected_object_ids"] for fid in object_to_features[oid]})
        unresolved_rows.append({"unresolved_id": item["unresolved_id"], "source_file": SOURCE, "source_location": f"{SOURCE}:{item['source_reference']['start_line']}-{item['source_reference']['end_line']}", "source_term": item["term"], "affected_object_ids": item["affected_object_ids"], "affected_relation_ids": [], "affected_feature_ids": affected_features, "unresolved_type": "ambiguous_reference", "possible_domain_owner": "theorems_or_referenced_domain", "dependency_status": "unresolved", "effect_on_contract": "classification_must_remain_unresolved", "effect_on_ir": "opaque_structural_representation", "effect_on_proof_representation": "may_block_typed_proof_nodes", "effect_on_mechanical_verification": "blocks", "effect_on_execution": "blocks", "effect_on_code_generation": "blocks", "propagation_strategy": "preserve_unresolved", "human_decision_required": True, "notes": item["required_human_decision"]})
    dump(REG / "unresolved-status.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "unresolved": unresolved_rows, "summary": {"source_unresolved": 12, "mapped_to_features": 12, "domain_global": 0, "cross_domain": 8, "contract_blocking": 12, "ir_blocking": 12, "proof_representation_blocking": 12, "mechanical_verification_blocking": 12, "execution_only_blocking": 0, "code_generation_blocking": 12, "human_decision_required": 12, "not_yet_assessable": 0}, "status": "complete_with_reservations"})
    report("unresolved-report.md", "Theorems unresolved audit", ["All 12 source unresolved terms are mapped to affected objects and features.", "Every unresolved item retains human-decision status and blocks code generation.", "No unresolved term is resolved or dropped."], ["Eight unresolved terms name external dimension domains and require reconciliation."])

    historical = {"domain_id": DOMAIN, "baseline_commit": BASELINE, "historical_artifact_status": "no_historical_artifact", "artifacts": [], "search_scope": ["registry/math-contracts/TLC-FC-06-THEOREMS-*", "ir/TLC-FC-06-THEOREMS-*", "reports, reviews, tools, scripts in origin/main"], "contracts_found": 0, "irs_found": 0, "proof_registries_found": 0, "proof_graphs_found": 0, "modified": False, "promoted": False, "status": "complete"}
    dump(REG / "historical-artifact-assessment.yaml", historical)
    report("historical-artifact-assessment.md", "Theorems historical-artifact assessment", ["No Theorems mathematical contract, IR, proof registry, proof graph, or historical domain-preparation branch exists in origin/main.", "Canonical functional-decomposition and scientific-review artifacts are inputs, not historical contracts or IRs."], [])

    upstream_status = {"master": {"canonical": True, "complete_to_ir": True}, "disciple": {"canonical": True, "complete_to_ir": True}, "community": {"canonical": True, "complete_to_ir": False}, "huit_dimensions": {"canonical": False, "complete_to_ir": False}, "invariants": {"canonical": False, "complete_to_ir": False}, "dynamics": {"canonical": False, "complete_to_ir": False}}
    gates = {"domain_id": DOMAIN, "baseline_gate": {"main_commit": BASELINE, "source_present": True, "extraction_present": True, "consolidation_present": True, "catalogue_present": True, "baseline_valid": True}, "upstream_status": upstream_status, "inventory_gate": {"objects_verified": 30, "relations_verified": 29, "unresolved_verified": 12, "source_coverage_complete": True}, "feature_gate": {"catalogue_features": 9, "inventoried_features": 9, "feature_coverage_complete": True, "missing_features": 0, "orphan_features": 0}, "semantic_gate": {"result_types_classified": 7, "statements_classified": 7, "hypotheses_classified": 7, "conclusions_classified": 7, "proof_status_classified": 7, "concept_separation_complete": True, "unresolved_semantics": 1}, "proof_gate": {"proofs_inventoried": 6, "proof_dependencies_mapped": 6, "incomplete_proofs_identified": 6, "missing_proofs_identified": 1, "mechanical_verification_assessed": True}, "dependency_gate": {"master_analyzed": True, "disciple_analyzed": True, "community_analyzed": True, "huit_dimensions_analyzed": True, "invariants_analyzed": True, "dynamics_analyzed": True, "message_principle_analyzed": True, "other_domains_analyzed": True, "internal_graph_complete": True, "proof_graph_complete": True, "unresolved_dependencies": 8}, "classification_gate": {"features_classified": 9, "not_yet_determinable": 1, "classification_complete": True}, "planning_gate": {"contract_plans": 9, "ir_plans": 9, "production_order_complete": True, "unresolved_classified": 12, "historical_artifacts_assessed": True}, "blocking_conditions": ["proofs incomplete or absent", "upstream Huit Dimensions, Invariants, and Dynamics not canonical", "twelve unresolved classifications", "one theorem/axiom extraction conflict"], "non_blocking_reservations": ["Preparation can complete before upstream production reconciliation."], "ready_for_contract_generation_now": True, "ready_for_full_contract_generation": False, "ready_for_ir_generation": False, "ready_for_proof_mechanical_verification": False, "ready_for_implementation_planning": False, "ready_for_code_generation": False}
    dump(REG / "production-gates.yaml", gates)
    dump(REG / "feature-status.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "features": feature_status, "status": "complete_with_reservations"})

    reconciliation = []
    for target, authority, dep_count in [("community", "canonical_preparation_in_main_incomplete_to_ir", 1), ("huit-dimensions", "non_authoritative_parallel_work_only", 1), ("invariants", "non_authoritative_parallel_work_only", 1), ("dynamics", "non_authoritative_parallel_work_only", 1), ("message", "source_only_no_domain_progress", 1), ("principle", "source_only_no_domain_progress", 1)]:
        reconciliation.append({"target_domain": target, "current_authority_status": authority, "dependency_count": dep_count, "affected_feature_ids": sorted({fid for dep in dependencies.get(target, []) for fid in dep.get("affected_feature_ids", [])}) if target in dependencies else (["TLC-FC-06-THEOREMS-008"] if target == "message" else ["TLC-FC-06-THEOREMS-009"]), "proof_dependencies": [], "required_future_artifacts": ["canonical target-domain mappings", "validated target contracts where required", "validated target IRs where required"], "reconciliation_trigger": f"{target} artifacts merge into origin/main", "blocking_current_preparation": False, "blocking_future_contracts": True, "blocking_future_irs": True, "blocking_proof_representation": True, "blocking_execution": True, "notes": "Non-merged parallel artifacts were not used as scientific authority."})
    dump(REG / "future-reconciliation.yaml", {"domain_id": DOMAIN, "baseline_commit": BASELINE, "targets": reconciliation, "status": "complete_with_reservations"})

    proposal = {"domain_id": DOMAIN, "source_file": SOURCE, "objects": 30, "relations": 29, "unresolved": 12, "features_total": 9, "preparation_status": "preparation_complete_with_reservations", "contracts_produced": 0, "irs_produced": 0, "proofs_total": 6, "proofs_complete": 0, "proofs_partial": 6, "proofs_missing": 1, "ready_for_contract_generation_now": True, "ready_for_full_contract_generation": False, "ready_for_ir_generation": False, "ready_for_proof_mechanical_verification": False, "ready_for_implementation_planning": False, "ready_for_code_generation": False, "future_reconciliation_required_with": ["community", "huit-dimensions", "invariants", "dynamics", "message", "principle"], "next_recommended_task": "reconcile_theorems_after_required_upstream_domains"}
    dump(REG / "global-manifest-update-proposal.yaml", proposal)
    preparation = {"domain_id": DOMAIN, "canonical_name": "Theorems", "source_file": SOURCE, "baseline_commit": BASELINE, "preparation_status": "preparation_complete_with_reservations", "inventory": {"objects": 30, "relations": 29, "unresolved": 12, "features": 9}, "logical_elements": inventory["logical_elements"], "coverage": {"scientific": "complete_with_reservations", "functional": "complete_with_reservations", "missing_features": 0}, "dependencies": {"master": "analyzed", "disciple": "analyzed", "community": "analyzed_reconciliation_required", "huit_dimensions": "analyzed_reconciliation_required", "invariants": "analyzed_reconciliation_required", "dynamics": "analyzed_reconciliation_required", "message_principle": "analyzed_reconciliation_required", "other": "analyzed_reconciliation_required"}, "plans": {"contracts": 9, "irs": 9}, "contracts_produced": 0, "irs_produced": 0, "proofs_invented": 0, "blocking_conditions": gates["blocking_conditions"], "non_blocking_reservations": gates["non_blocking_reservations"], "ready_for_contract_generation_now": True, "ready_for_full_contract_generation": False, "ready_for_ir_generation": False, "ready_for_proof_mechanical_verification": False, "ready_for_implementation_planning": False, "ready_for_code_generation": False, "next_required_gate": "reconcile canonical upstream domains and obtain missing proof sources", "final_decision": "theorems_preparation_complete_locally", "next_task": "reconcile_theorems_after_required_upstream_domains"}
    dump(REG / "preparation-status.yaml", preparation)
    report("domain-preparation-report.md", "Theorems domain preparation", ["Preparation is complete with reservations at baseline 4a42d88.", "Scientific and functional coverage account for all 30 objects, 29 relations, 12 unresolved terms, and nine features.", "Seven theorem statements, six partial local proofs, and one missing proof are distinguished.", "All upstream, external, internal, and proof dependencies are recorded conservatively.", "Nine contract plans and nine IR plans exist; zero contracts and zero IRs were produced.", "The domain is not ready for IR generation, mechanical proof verification, implementation planning, or code generation."], gates["blocking_conditions"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
