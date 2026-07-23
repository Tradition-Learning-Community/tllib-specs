from __future__ import annotations

from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/values"
REP = ROOT / "reports/domain-progress/values"
BASELINE = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
SOURCE = "maths/09-values.md"


def load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8-sig"))


def dump(name: str, data) -> None:
    REG.mkdir(parents=True, exist_ok=True)
    (REG / name).write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def report(name: str, title: str, facts: list[str], reservations: list[str]) -> None:
    REP.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", "", f"Baseline: `{BASELINE}`", "", "## Findings", ""]
    lines += [f"- {x}" for x in facts]
    lines += ["", "## Reservations", ""] + [f"- {x}" for x in reservations]
    lines += ["", "No scientific approval, final contract, final IR, or implementation is produced.", ""]
    (REP / name).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    obj_doc = load("registry/scientific-objects/values/scientific-objects.candidate.yaml")
    rel_doc = load("registry/scientific-objects/values/scientific-relations.candidate.yaml")
    unr_doc = load("registry/scientific-objects/values/unresolved-terms.yaml")
    dup_doc = load("registry/scientific-objects/values/duplicate-candidates.yaml")
    feat_doc = load("registry/features/revised/feature-candidates.yaml")
    objects = obj_doc["objects"]
    relations = rel_doc["relations"]
    unresolved = unr_doc["unresolved_terms"]
    duplicates = dup_doc["duplicate_candidates"]
    features = [x for x in feat_doc["features"] if x["candidate_feature_id"].startswith("TLC-FC-09-VALUES-")]
    feature_ids = [x["candidate_feature_id"] for x in features]
    object_ids = {x["provisional_object_id"] for x in objects}
    relation_ids = {x["provisional_relation_id"] for x in relations}
    unresolved_ids = {x["unresolved_id"] for x in unresolved}
    feature_object_ids = {oid for f in features for oid in f["scientific_basis"]["scientific_object_ids"]}
    feature_relation_ids = {rid for f in features for rid in f["scientific_basis"]["scientific_relation_ids"]}

    general = {
        "domain_id": "values", "canonical_name": "Values", "source_file": SOURCE,
        "baseline_commit": BASELINE, "authority": "origin/main", "status": "complete_with_reservations",
        "counts": {"objects": len(objects), "relations": len(relations), "unresolved": len(unresolved),
                   "duplicate_candidates": len(duplicates), "catalogue_features": len(features)},
        "non_invention": {"definitions_added": 0, "hierarchies_added": 0, "scales_added": 0,
                           "utility_functions_added": 0, "contracts_created": 0, "irs_created": 0},
    }
    dump("source-inventory.yaml", general)
    report("source-inventory-report.md", "Values source inventory",
           [f"{len(objects)} canonical candidate objects, {len(relations)} relations, {len(unresolved)} unresolved terms, and {len(features)} revised catalogue features are inventoried.",
            f"{len(duplicates)} duplicate candidate is preserved without merging."],
           ["Extraction artifacts remain candidates and are not scientifically promoted."])

    scientific_objects = []
    for item in objects:
        scientific_objects.append({
            **item,
            "source_file": SOURCE,
            "explicit_definition": item.get("object_type") == "Definition",
            "dependencies": item.get("explicit_dependencies", []),
            "symbols": item.get("symbols_mentioned", []),
            "status": item.get("validation_status", "candidate"),
            "ambiguity": item.get("issues", []) or "none_recorded",
            "unresolved_ids": [u["unresolved_id"] for u in unresolved if item["provisional_object_id"] in u.get("affected_object_ids", [])],
            "non_invention_note": "Canonical extraction preserved; absent properties are not inferred.",
        })
    dump("scientific-inventory.yaml", {"domain_id": "values", "baseline_commit": BASELINE,
        "objects": scientific_objects, "duplicate_candidates": duplicates,
        "summary": {"objects": len(objects), "covered": len(scientific_objects), "missing": 0}, "status": "complete_with_reservations"})
    report("scientific-inventory-report.md", "Values scientific inventory",
           ["Every canonical extracted object is represented with its source trace and unresolved links."],
           ["Object types are copied from the candidate extraction, not independently validated."])

    relation_inventory = []
    for item in relations:
        relation_inventory.append({**item, "direction": "source_to_target", "explicit_or_inferred": item.get("evidence_type", "not_yet_determinable"),
            "confidence": "candidate", "status": item.get("validation_status", "candidate"), "unresolved_ids": [],
            "blocking_status": "not_yet_determinable", "notes": "No formal relation is inferred from textual proximity."})
    dump("relation-inventory.yaml", {"domain_id": "values", "baseline_commit": BASELINE,
        "relations": relation_inventory, "summary": {"relations": len(relations), "covered": len(relation_inventory), "missing": 0},
        "status": "complete_with_reservations"})
    report("relation-inventory-report.md", "Values relation inventory",
           ["All canonical candidate relations are preserved directionally and traceably."],
           ["Candidate relations are not promoted to scientific or software dependencies."])

    value_properties = ["carrier", "domain", "scope", "context", "source", "target", "individual_or_collective",
        "descriptive_or_normative", "qualitative_or_quantitative", "ordinal_or_cardinal", "unit", "scale", "bound", "order",
        "comparability", "composition", "temporal_dependency", "cultural_dependency", "action_or_practice_relation",
        "satisfaction_condition", "mechanical_validation"]
    semantics = {
        "domain_id": "values", "baseline_commit": BASELINE, "source_basis": f"{SOURCE}:5-26",
        "explicit_nature": ["orientation_axiologique", "criteria_of_desirable", "quality", "multidimensional_structure", "dynamic_attractor"],
        "formal_representation": {"kind": "10-tuple", "source_location": f"{SOURCE}:11-26",
            "components": ["P", "H", "W", "O", "I", "T", "C", "E", "A", "M"]},
        "property_assessment": {p: "not_yet_determinable_unless_explicit_per_object" for p in value_properties},
        "explicit_computational_material": ["weights", "partial_orders", "metrics", "differential_equations", "optimization_expressions"],
        "semantic_limit": "Source formulas are recorded but not converted into executable semantics.",
        "status": "complete_with_reservations",
    }
    dump("value-semantics.yaml", semantics)
    report("value-semantics-report.md", "Value semantics",
           ["The source explicitly defines Value as a ten-component multidimensional object and supplies mathematical expressions."],
           ["No ordinary-language utility, preference, reward, or metric semantics are substituted for TL Value."])

    structure = {
        "domain_id": "values", "baseline_commit": BASELINE,
        "explicit": {"value_tuple": True, "categories": ["ethical", "cultural", "professional_or_functional", "hybrid_or_contextual"],
            "dynamic_hierarchy": True, "partial_order": True, "compatibility_tension_matrix": True,
            "context_dependency": True, "collective_dependency": True, "temporal_dependency": True},
        "not_authorized_as_global_fact": {"finite_closed_list": "not_yet_determinable", "total_order": "not_explicit",
            "universal_priority": "not_explicit", "global_comparability": "not_explicit", "single_numeric_scale": "not_explicit",
            "aggregation_rule": "not_yet_determinable"},
        "source_references": [f"{SOURCE}:11-26", f"{SOURCE}:57-69", f"{SOURCE}:211-254"],
        "status": "complete_with_reservations",
    }
    dump("value-structure.yaml", structure)
    report("value-structure-report.md", "Values structure",
           ["Tuple components, four named forms, contextual hierarchy, partial order, and coherence matrix are explicit."],
           ["No global hierarchy, total order, universal priority, or new score is inferred."])

    pairs = ["Principle", "Virtue", "Capacity", "Competency", "Goal", "Objective", "Preference", "Utility", "Reward",
        "Metric", "Measure", "Norm", "Rule", "Constraint", "Invariant", "State", "Property", "Quality", "Message", "Practice", "Lived Experience"]
    explicit_distinct = {"Principle": "explicit_non_equivalence", "Virtue": "provisional_distinction", "Quality": "candidate_relation", "Practice": "candidate_relation"}
    sep = [{"pair": f"Value vs {p}", "classification": explicit_distinct.get(p, "unresolved"),
            "source_reference": f"{SOURCE}:5-7" if p == "Principle" else SOURCE,
            "notes": "No ordinary philosophical definition is used."} for p in pairs]
    dump("concept-separation.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "pairs": sep,
        "summary": {"pairs": len(sep), "unresolved": sum(x["classification"] == "unresolved" for x in sep)}, "status": "complete_with_reservations"})
    report("concept-separation-report.md", "Values concept separation",
           ["Twenty-one required conceptual pairs are explicitly classified."],
           ["Most distinctions remain unresolved where the source provides no explicit equivalence or non-equivalence."])

    class_map = {"constraint_evaluation": "constraint_contract", "evolution_dynamics": "computational_contract",
        "transformation": "structural_contract", "invariant_check": "validation_contract", "metric_evaluation": "value_validation_contract",
        "scientific_operator": "structural_contract", "relation_evaluation": "value_relation_contract"}
    feature_rows = []
    classifications = []
    for f in features:
        fid = f["candidate_feature_id"]
        uids = sorted({u["unresolved_id"] for u in unresolved if set(u.get("affected_object_ids", [])) & set(f["scientific_basis"]["scientific_object_ids"])})
        feature_rows.append({"feature_id": fid, "canonical_name": f["name"], "source_objects": f["scientific_basis"]["scientific_object_ids"],
            "source_relations": f["scientific_basis"]["scientific_relation_ids"], "source_unresolved": uids,
            "purpose": f["plain_language_purpose"], "scientific_scope": f["scope"],
            "candidate_inputs": f["construction_question"]["candidate_inputs"], "candidate_outputs": f["construction_question"]["candidate_outputs"],
            "preconditions": f["behavior"]["preconditions"], "postconditions": f["behavior"]["postconditions"],
            "constraints": f["behavior"]["constraints"], "invariants": f["behavior"]["invariants"],
            "dependencies": f["dependencies"], "exclusions": f["scope"]["excluded"], "readiness": f["readiness"],
            "blockers": f["readiness"].get("blocking_object_ids", []) + f["readiness"].get("blocking_relation_ids", []),
            "future_reconciliation_required": True, "status": "inventoried"})
        classifications.append({"feature_id": fid, "classification": class_map.get(f["category"], "not_yet_determinable"),
            "source_category": f["category"], "review_classification": f["review_application"]["classification"],
            "computational_semantics_claimed": f["category"] == "evolution_dynamics",
            "status": "candidate", "notes": "Classification does not override canonical scientific review."})
    gaps = sorted(object_ids - feature_object_ids)
    dump("functional-coverage.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "features": feature_rows,
        "catalogue_gap_candidates": [{"object_id": x, "status": "candidate", "reason": "Canonical revised catalogue does not cite this extracted object."} for x in gaps],
        "summary": {"catalogue_features": len(features), "inventoried_features": len(feature_rows), "missing_features": 0,
            "orphan_features": 0, "catalogue_objects": len(feature_object_ids), "catalogue_relations": len(feature_relation_ids),
            "catalogue_gap_candidates": len(gaps)}, "status": "complete_with_reservations"})
    dump("feature-classification.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "features": classifications,
        "summary": {"classified": len(classifications)}, "status": "complete_with_reservations"})
    report("functional-coverage-report.md", "Values functional coverage",
           [f"All {len(features)} revised catalogue features are inventoried and classified.", f"{len(gaps)} extracted objects not cited by the revised catalogue remain catalogue-gap candidates."],
           ["Gap candidates are not silently converted into canonical features."])
    report("feature-classification-report.md", "Values feature classification",
           ["Every revised feature receives one conservative preparation classification."],
           ["Computational classification records explicit source dynamics only and does not claim execution readiness."])

    domain_refs = {
        "master": [5, 7, 41, 76, 103, 125, 237], "disciple": [34, 85, 90, 126, 148, 191, 243],
        "community": [5, 7, 43, 92, 103, 161, 182, 189, 238, 258], "huit_dimensions": [], "invariants": [17, 30, 223],
        "dynamics": [18, 25, 134, 160, 183], "theorems": [235], "message": [], "principle": [5, 7, 17, 120, 223, 258],
        "virtues": [], "capacities": [], "competencies": [], "practice": [7, 34, 42, 63, 89, 161, 194, 258],
        "lived_experience": [42, 80, 92], "relations": [23, 262],
    }
    external = []
    for domain, lines in domain_refs.items():
        external.append({"domain": domain, "confirmed": 1 if lines else 0, "inferred_candidate": 0, "rejected": 0,
            "unresolved": 1 if lines else 0, "symbol_only": 1 if lines else 0, "contract_required": 0, "ir_required": 0,
            "proof_premise": 0, "blocking_contract_generation": False, "blocking_ir_generation": bool(lines),
            "blocking_execution_only": False, "blocking_code_generation": bool(lines), "canonical_in_main": domain in {"master", "disciple", "community"},
            "future_reconciliation_required": bool(lines), "source_references": [f"{SOURCE}:{n}" for n in lines],
            "status": "confirmed_textual_reference" if lines else "no_explicit_reference_found"})
    dump("external-domain-dependencies.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "domains": external,
        "status": "complete_with_reservations"})
    report("external-domain-dependencies-report.md", "Values external dependencies",
           ["Required adjacent domains are assessed independently from explicit source references."],
           ["Textual references are not promoted to contract or IR requirements.", "Non-merged parallel branches are not used as authority."])

    graph = {"domain_id": "values", "baseline_commit": BASELINE, "nodes": feature_ids, "confirmed_edges": [], "inferred_edges": [],
        "unresolved_edges": [], "root_features": feature_ids, "leaf_features": feature_ids, "cycles": [], "cycle_classifications": [],
        "production_groups": {"A_retained_with_reservations": [f["candidate_feature_id"] for f in features if f["review_application"]["classification"] == "retained_with_reservations"],
            "B_scientific_decision_required": [f["candidate_feature_id"] for f in features if f["review_application"]["classification"] != "retained_with_reservations"]},
        "candidate_production_order": feature_ids, "order_basis": "catalogue identifiers only; no dependency order asserted",
        "status": "complete_with_reservations"}
    dump("internal-dependencies.yaml", graph)
    report("internal-dependencies-report.md", "Values internal dependencies",
           ["No canonical functional dependency edge is asserted among the fourteen revised features."],
           ["Catalogue order is recorded only as a stable listing, not as scientific production precedence."])

    unresolved_rows = []
    for u in unresolved:
        affected_features = [f["candidate_feature_id"] for f in features if set(u.get("affected_object_ids", [])) & set(f["scientific_basis"]["scientific_object_ids"])]
        unresolved_rows.append({**u, "source": u.get("source_reference"), "objects": u.get("affected_object_ids", []),
            "relations": [], "features": affected_features, "domain_global": not bool(affected_features), "cross_domain": False,
            "contract_blocking": True, "ir_blocking": True, "execution_only_blocking": False, "proof_blocking": False,
            "code_generation_blocking": True, "human_decision_required": True, "future_source_required": True,
            "reconciliation_domain": "values", "not_yet_assessable": False, "status": "unresolved"})
    dump("unresolved-status.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "unresolved": unresolved_rows,
        "summary": {"source_total": len(unresolved), "covered": len(unresolved_rows), "missing": 0,
            "mapped_to_features": sum(bool(x["features"]) for x in unresolved_rows), "domain_global": sum(x["domain_global"] for x in unresolved_rows)},
        "status": "complete_with_reservations"})
    report("unresolved-report.md", "Values unresolved analysis",
           [f"All {len(unresolved)} canonical unresolved terms are preserved."],
           ["No unresolved item is adjudicated during preparation."])

    historical_paths = ["registry/math-contracts/TLC-FC-09-VALUES-018", "reports/math-contracts/TLC-FC-09-VALUES-018",
        "ir/TLC-FC-09-VALUES-018", "reports/ir/TLC-FC-09-VALUES-018", "tools/math-contracts/TLC-FC-09-VALUES-018",
        "tools/ir/TLC-FC-09-VALUES-018"]
    artifacts = [{"path": p, "feature_id": "TLC-FC-09-VALUES-018", "source_alignment": "requires_comparison",
        "catalogue_alignment": "feature_present", "unresolved_preserved": "requires_audit", "schema_compatibility": "candidate",
        "scientific_compatibility": "not_validated_here", "classification": "comparison_only", "risks": ["pilot_scope_only"],
        "future_reuse_decision": "human_review_required", "modified": False, "promoted": False} for p in historical_paths if (ROOT / p).exists()]
    dump("historical-artifact-assessment.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "artifacts": artifacts,
        "summary": {"artifacts_found": len(artifacts), "modified": 0, "promoted": 0}, "status": "complete_with_reservations"})
    report("historical-artifact-assessment.md", "Values historical artifact assessment",
           [f"{len(artifacts)} existing pilot directories for feature 018 are recorded for comparison only."],
           ["No pilot artifact is modified, promoted, or generalized."])

    contract_plans, ir_plans = [], []
    for f, c in zip(feature_rows, classifications):
        fid = f["feature_id"]
        suffix = fid.rsplit("-", 1)[-1]
        contract_plans.append({"feature_id": fid, "future_contract_id": f"TLC-MC-09-VALUES-{suffix}",
            "contract_category": c["classification"], "source_basis": f["source_objects"] + f["source_relations"], "purpose": f["purpose"],
            "candidate_inputs": f["candidate_inputs"], "candidate_outputs": f["candidate_outputs"], "preconditions": f["preconditions"],
            "postconditions": f["postconditions"], "constraints": f["constraints"], "invariants": f["invariants"],
            "validation_rules": [], "failure_cases": [], "unresolved_propagation": f["source_unresolved"], "dependencies": f["dependencies"],
            "readiness": "partial_plan_only", "blockers": f["blockers"] + f["source_unresolved"], "required_upstream_reconciliation": True,
            "explicit_non_invention_exclusions": ["no invented type", "no invented scale", "no invented ordering", "no invented utility"]})
        ir_plans.append({"feature_id": fid, "future_ir_id": f"TLC-IR-09-VALUES-{suffix}", "future_contract_id": f"TLC-MC-09-VALUES-{suffix}",
            "source_basis": f["source_objects"] + f["source_relations"], "candidate_operation_kind": "not_yet_determinable",
            "candidate_operands": [], "candidate_result": "not_yet_determinable", "candidate_types": [], "candidate_shapes": [],
            "candidate_dimensions": [], "candidate_state_effects": [], "validation_operations": [],
            "unresolved_propagation": f["source_unresolved"], "execution_readiness": False,
            "blockers": f["blockers"] + f["source_unresolved"], "required_upstream_reconciliation": True,
            "explicit_non_invention_exclusions": ["no opcode", "no numeric type", "no memory layout", "no score", "no aggregation"]})
    dump("contract-production-plan.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "plans": contract_plans,
        "summary": {"planned_contracts": len(contract_plans)}, "status": "complete_with_reservations"})
    dump("ir-production-plan.yaml", {"domain_id": "values", "baseline_commit": BASELINE, "plans": ir_plans,
        "summary": {"planned_irs": len(ir_plans)}, "status": "complete_with_reservations"})
    report("contract-production-plan-report.md", "Values contract production plan",
           [f"A non-final contract plan exists for each of the {len(features)} revised features."], ["Plans preserve blockers and unresolved items."])
    report("ir-production-plan-report.md", "Values IR production plan",
           [f"A non-final IR plan exists for each of the {len(features)} revised features."], ["All operation kinds and executable details remain undetermined."])

    readiness = {"domain_id": "values", "baseline_commit": BASELINE, "independent_features": [], "ready_after_master": [],
        "ready_after_disciple": [], "ready_after_community": [], "ready_after_huit_dimensions": [], "ready_after_invariants": [],
        "ready_after_dynamics": [], "ready_after_theorems": [], "ready_after_message": [], "ready_after_principle": [],
        "ready_after_virtues": [], "ready_after_capacities": [], "ready_after_competencies": [], "ready_after_practice": [],
        "ready_after_lived_experience": [], "ready_after_relations": [], "ready_after_multiple_domains": feature_ids,
        "blocked_by_missing_value_definition": [], "blocked_by_missing_scale": [], "blocked_by_missing_ordering": [],
        "blocked_by_missing_comparison_semantics": [], "blocked_by_scientific_ambiguity": feature_ids,
        "blocked_by_missing_source": [], "blocked_by_missing_proof": [], "not_yet_assessable": [],
        "ready_for_contract_plan": True, "ready_for_partial_contract": True, "ready_for_complete_contract": False,
        "ready_for_ir": False, "ready_for_mechanical_validation": False, "ready_for_implementation": False,
        "ready_for_code_generation": False, "status": "complete_with_reservations"}
    dump("production-readiness.yaml", readiness)
    report("production-readiness-report.md", "Values production readiness",
           ["Contract and IR planning coverage is complete."], ["Complete contracts, IR, implementation, and code generation remain blocked."])

    manifest = {**general, "coverage": {"objects": len(objects), "relations": len(relations), "unresolved": len(unresolved),
        "features": len(features), "contract_plans": len(contract_plans), "ir_plans": len(ir_plans)},
        "preparation_status": "preparation_complete_with_reservations", "ready_for_contract_generation_now": True,
        "ready_for_full_contract_generation": False, "ready_for_ir_generation": False,
        "ready_for_implementation_planning": False, "ready_for_code_generation": False,
        "next_required_gate": "scientific review of unresolved semantics and canonical upstream reconciliation",
        "final_decision": "values_preparation_complete_locally", "next_task": "reconcile_values_after_required_upstream_domains"}
    dump("preparation-manifest.yaml", manifest)
    report("domain-preparation-report.md", "Values domain preparation",
           [f"Preparation covers {len(objects)} objects, {len(relations)} relations, {len(unresolved)} unresolved terms, and {len(features)} features.",
            "Contract and IR plans are complete at preparation level."],
           ["Preparation is not scientific validation.", "No final contract, IR, implementation, or code is produced."])


if __name__ == "__main__":
    main()
