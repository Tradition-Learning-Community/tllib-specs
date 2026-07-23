from __future__ import annotations

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/practice"
REP = ROOT / "reports/domain-progress/practice"
BASELINE = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
SOURCE = "maths/13-practice.md"


def load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8-sig"))


def dump(name: str, data) -> None:
    REG.mkdir(parents=True, exist_ok=True)
    (REG / name).write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )


def report(name: str, title: str, facts: list[str], reservations: list[str]) -> None:
    REP.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", "", f"Baseline: `{BASELINE}`", "", "## Findings", ""]
    lines += [f"- {item}" for item in facts]
    lines += ["", "## Reservations", ""] + [f"- {item}" for item in reservations]
    lines += ["", "No final contract, IR, optimization, or implementation is produced.", ""]
    (REP / name).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    base = "registry/scientific-objects/practice"
    objects = load(f"{base}/scientific-objects.candidate.yaml")["objects"]
    relations = load(f"{base}/scientific-relations.candidate.yaml")["relations"]
    unresolved = load(f"{base}/unresolved-terms.yaml")["unresolved_terms"]
    duplicates = load(f"{base}/duplicate-candidates.yaml")["duplicate_candidates"]
    feature_catalogue = load("registry/features/revised/feature-candidates.yaml")["features"]
    features = [
        item for item in feature_catalogue
        if item["candidate_feature_id"].startswith("TLC-FC-13-PRACTICE-")
    ]
    feature_ids = [item["candidate_feature_id"] for item in features]
    object_ids = {item["provisional_object_id"] for item in objects}
    relation_ids = {item["provisional_relation_id"] for item in relations}
    feature_object_ids = {
        object_id
        for feature in features
        for object_id in feature["scientific_basis"]["scientific_object_ids"]
    }
    feature_relation_ids = {
        relation_id
        for feature in features
        for relation_id in feature["scientific_basis"]["scientific_relation_ids"]
    }

    source_inventory = {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "status": "prepared_with_reservations",
        "counts": {
            "objects": len(objects),
            "relations": len(relations),
            "unresolved": len(unresolved),
            "duplicate_candidates": len(duplicates),
            "revised_features": len(features),
        },
        "canonical_inputs": [
            SOURCE,
            f"{base}/scientific-objects.candidate.yaml",
            f"{base}/scientific-relations.candidate.yaml",
            f"{base}/unresolved-terms.yaml",
            f"{base}/duplicate-candidates.yaml",
            "registry/features/revised/feature-candidates.yaml",
        ],
    }
    dump("source-inventory.yaml", source_inventory)
    report(
        "source-inventory-report.md",
        "Practice source inventory",
        [
            f"{len(objects)} objects, {len(relations)} relations, {len(unresolved)} unresolved records, "
            f"{len(duplicates)} duplicate candidates, and {len(features)} revised features are canonical inputs."
        ],
        ["Candidate extraction status is preserved and is not scientific approval."],
    )

    scientific_rows = []
    for item in objects:
        object_id = item["provisional_object_id"]
        scientific_rows.append({
            **item,
            "source_file": SOURCE,
            "explicit_definition": item.get("object_type") == "Definition",
            "symbols": item.get("symbols_mentioned", []),
            "dependencies": item.get("explicit_dependencies", []),
            "status": item.get("validation_status", "candidate"),
            "ambiguity": item.get("issues", []) or "none_recorded",
            "unresolved_ids": [
                record["unresolved_id"]
                for record in unresolved
                if object_id in record.get("affected_object_ids", [])
            ],
            "non_invention_note": "Canonical extraction copied without semantic completion.",
        })
    dump("scientific-inventory.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "objects": scientific_rows,
        "duplicate_candidates": duplicates,
        "summary": {"objects": len(scientific_rows), "covered": len(scientific_rows), "missing": 0},
        "status": "complete_with_reservations",
    })
    report(
        "scientific-inventory-report.md",
        "Practice scientific inventory",
        ["Every canonical extracted object is preserved with source trace and unresolved links."],
        ["No object identity or type is changed."],
    )

    relation_rows = [{
        **item,
        "direction": "source_to_target",
        "explicit_or_inferred": item.get("evidence_type", "not_yet_determinable"),
        "confidence": "candidate",
        "status": item.get("validation_status", "candidate"),
        "unresolved_ids": [],
        "blocking_status": "not_yet_determinable",
        "notes": "Textual proximity is not converted into a formal dependency.",
    } for item in relations]
    dump("relation-inventory.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "relations": relation_rows,
        "summary": {"relations": len(relation_rows), "covered": len(relation_rows), "missing": 0},
        "status": "complete_with_reservations",
    })
    report(
        "relation-inventory-report.md",
        "Practice relation inventory",
        ["All canonical candidate relations are represented directionally."],
        ["No candidate relation is promoted to a software dependency."],
    )

    unresolved_rows = []
    for item in unresolved:
        affected = set(item.get("affected_object_ids", []))
        mapped_features = [
            feature["candidate_feature_id"]
            for feature in features
            if affected & set(feature["scientific_basis"]["scientific_object_ids"])
        ]
        unresolved_rows.append({
            **item,
            "features": mapped_features,
            "domain_global": not bool(mapped_features),
            "contract_blocking": True,
            "ir_blocking": True,
            "code_generation_blocking": True,
            "human_decision_required": True,
            "status": "unresolved",
        })
    dump("unresolved-status.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "unresolved": unresolved_rows,
        "summary": {
            "source_total": len(unresolved_rows),
            "covered": len(unresolved_rows),
            "missing": 0,
            "mapped_to_features": sum(bool(item["features"]) for item in unresolved_rows),
        },
        "status": "complete_with_reservations",
    })
    report(
        "unresolved-report.md",
        "Practice unresolved analysis",
        [f"All {len(unresolved_rows)} canonical unresolved records are preserved."],
        ["No unresolved record is closed or interpreted."],
    )

    patterns = [
        {
            "pattern_id": "PRACTICE-PATTERN-CANDIDATE-001",
            "source_reference": f"{SOURCE}:76-81",
            "source_term": "patterns tacites",
            "formal_structure": "not_specified",
            "status": "unresolved",
        },
        {
            "pattern_id": "PRACTICE-PATTERN-CANDIDATE-002",
            "source_reference": f"{SOURCE}:179-185",
            "source_term": "patterns reconnus et intégrés",
            "formal_structure": "not_specified",
            "status": "unresolved",
        },
    ]
    dump("pattern-analysis.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "patterns": patterns,
        "formal_patterns": 0,
        "candidate_mentions": len(patterns),
        "status": "complete_with_reservations",
    })
    report(
        "pattern-analysis-report.md",
        "Practice pattern analysis",
        ["Two explicit textual pattern mentions are inventoried."],
        ["Neither mention defines a formal pattern type, structure, algorithm, or matcher."],
    )

    boundaries = []
    for concept, lines in {
        "capacity": "11-22,31",
        "competency": "11-22,31",
        "lived_experience": "62-65",
        "value": "112-113,164-169",
        "virtue": "112-113,164-169",
        "principle": "112-113,164-169",
    }.items():
        boundaries.append({
            "pair": f"practice_vs_{concept}",
            "classification": "explicit_relation_without_identity",
            "source_reference": f"{SOURCE}:{lines}",
            "status": "requires_external_reconciliation",
            "notes": "Relation does not authorize conceptual equivalence.",
        })
    dump("concept-boundaries.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "boundaries": boundaries,
        "status": "complete_with_reservations",
    })
    report(
        "concept-boundaries-report.md",
        "Practice concept boundaries",
        ["Practice remains distinct from capacity, competency, lived experience, value, virtue, and principle."],
        ["Explicit relations do not establish equivalence or shared type."],
    )

    class_map = {
        "constraint_evaluation": "constraint_contract",
        "evolution_dynamics": "computational_contract",
        "transformation": "structural_contract",
        "metric_evaluation": "validation_contract",
        "scientific_operator": "structural_contract",
        "relation_evaluation": "relational_contract",
    }
    feature_rows, classifications = [], []
    for feature in features:
        feature_id = feature["candidate_feature_id"]
        basis = feature["scientific_basis"]
        affected_unresolved = sorted({
            record["unresolved_id"]
            for record in unresolved
            if set(record.get("affected_object_ids", [])) & set(basis["scientific_object_ids"])
        })
        feature_rows.append({
            "feature_id": feature_id,
            "canonical_name": feature["name"],
            "source_objects": basis["scientific_object_ids"],
            "source_relations": basis["scientific_relation_ids"],
            "source_unresolved": affected_unresolved,
            "purpose": feature["plain_language_purpose"],
            "candidate_inputs": feature["construction_question"]["candidate_inputs"],
            "candidate_outputs": feature["construction_question"]["candidate_outputs"],
            "preconditions": feature["behavior"]["preconditions"],
            "postconditions": feature["behavior"]["postconditions"],
            "constraints": feature["behavior"]["constraints"],
            "dependencies": feature["dependencies"],
            "readiness": feature["readiness"],
            "review_classification": feature["review_application"]["classification"],
            "future_reconciliation_required": True,
            "status": "inventoried",
        })
        classifications.append({
            "feature_id": feature_id,
            "classification": class_map.get(feature["category"], "not_yet_determinable"),
            "source_category": feature["category"],
            "review_classification": feature["review_application"]["classification"],
            "execution_ready": False,
            "status": "candidate",
        })
    gaps = sorted(object_ids - feature_object_ids)
    dump("functional-coverage.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "features": feature_rows,
        "catalogue_gap_candidates": [{
            "object_id": object_id,
            "status": "candidate",
            "reason": "The revised catalogue does not cite this extracted object.",
        } for object_id in gaps],
        "summary": {
            "catalogue_features": len(features),
            "inventoried_features": len(feature_rows),
            "missing_features": 0,
            "orphan_features": 0,
            "catalogue_objects": len(feature_object_ids),
            "catalogue_relations": len(feature_relation_ids),
            "catalogue_gap_candidates": len(gaps),
        },
        "status": "complete_with_reservations",
    })
    dump("feature-classification.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "features": classifications,
        "summary": {"classified": len(classifications)},
        "status": "complete_with_reservations",
    })
    report(
        "functional-coverage-report.md",
        "Practice functional coverage",
        [
            f"All {len(features)} revised features are inventoried.",
            f"{len(gaps)} extracted objects outside revised feature citations remain catalogue-gap candidates.",
        ],
        ["Gap candidates are not converted into new canonical features."],
    )
    report(
        "feature-classification-report.md",
        "Practice feature classification",
        ["Every revised feature has a conservative preparation classification."],
        ["Computational source material does not imply implementation readiness."],
    )

    external_spec = {
        "master": ("canonical", [5, 18, 30, 38, 70, 131]),
        "disciple": ("canonical", [48, 77, 85, 196]),
        "community": ("canonical_complete_to_ir_with_reservations", [30, 40, 93, 134, 194]),
        "message": ("not_reconciled", [112, 113]),
        "principle": ("not_reconciled", [5, 26, 112, 113, 164, 169]),
        "values": ("not_reconciled", [5, 63, 112, 113, 164, 169]),
        "virtues": ("not_reconciled", [112, 113, 164, 169, 219, 225]),
        "capacities": ("external_non_reconciled", [5, 11, 17, 31, 98, 101, 102, 113, 219, 224]),
        "competencies": ("external_non_reconciled", [5, 11, 20, 31, 98, 101, 102, 103, 113, 219, 223]),
        "lived_experience": ("external_non_reconciled", [62, 65]),
        "relations": ("canonical_source_only", [246]),
    }
    external = [{
        "domain": domain,
        "authority_status": authority_status,
        "dependency_status": "explicit_textual_dependency_requires_reconciliation",
        "confirmed_feature_edges": [],
        "source_references": [f"{SOURCE}:{line}" for line in lines],
        "contract_required": False,
        "ir_required": False,
        "blocking_full_contract_generation": True,
        "future_reconciliation_required": True,
    } for domain, (authority_status, lines) in external_spec.items()]
    dump("external-domain-dependencies.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "dependencies": external,
        "status": "complete_with_reservations",
    })
    report(
        "external-domain-dependencies-report.md",
        "Practice external dependencies",
        ["Explicit source references to eleven adjacent domains are recorded."],
        [
            "Capacities, Competencies, and Lived Experience are external non-reconciled dependencies.",
            "Unmerged branches and PRs are not used as scientific authority.",
        ],
    )

    internal = {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "nodes": feature_ids,
        "confirmed_edges": [],
        "inferred_edges": [],
        "unresolved_edges": [],
        "root_features": feature_ids,
        "leaf_features": feature_ids,
        "cycles": [],
        "candidate_order": feature_ids,
        "order_semantics": "stable catalogue listing only; no dependency order asserted",
        "status": "complete_with_reservations",
    }
    dump("internal-dependencies.yaml", internal)
    dump("dependency-matrix.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "feature_ids": feature_ids,
        "matrix": [[0 for _ in feature_ids] for _ in feature_ids],
        "meaning": "0 means no canonical functional dependency edge is established",
        "status": "complete_with_reservations",
    })
    report(
        "internal-dependencies-report.md",
        "Practice internal dependencies",
        ["No canonical functional edge or cycle is asserted among the ten revised features."],
        ["Catalogue listing order is not a production dependency."],
    )
    report(
        "dependency-matrix-report.md",
        "Practice dependency matrix",
        ["The ten-by-ten matrix records no established canonical internal edge."],
        ["Zero means unestablished, not scientifically disproven."],
    )

    contract_plans, ir_plans = [], []
    for feature, classification in zip(feature_rows, classifications):
        feature_id = feature["feature_id"]
        suffix = feature_id.rsplit("-", 1)[-1]
        blockers = feature["source_unresolved"] + feature["readiness"].get("blocking_object_ids", []) + feature["readiness"].get("blocking_relation_ids", [])
        contract_plans.append({
            "feature_id": feature_id,
            "future_contract_id": f"TLC-MC-13-PRACTICE-{suffix}",
            "classification": classification["classification"],
            "source_basis": feature["source_objects"] + feature["source_relations"],
            "candidate_inputs": feature["candidate_inputs"],
            "candidate_outputs": feature["candidate_outputs"],
            "preconditions": feature["preconditions"],
            "postconditions": feature["postconditions"],
            "constraints": feature["constraints"],
            "unresolved_propagation": feature["source_unresolved"],
            "blockers": blockers,
            "readiness": "partial_plan_only",
            "explicit_exclusions": ["no invented type", "no invented unit", "no invented threshold", "no invented temporal semantics"],
        })
        ir_plans.append({
            "feature_id": feature_id,
            "future_ir_id": f"TLC-IR-13-PRACTICE-{suffix}",
            "future_contract_id": f"TLC-MC-13-PRACTICE-{suffix}",
            "source_basis": feature["source_objects"] + feature["source_relations"],
            "candidate_operation_kind": "not_yet_determinable",
            "candidate_operands": [],
            "candidate_result": "not_yet_determinable",
            "candidate_types": [],
            "candidate_shapes": [],
            "candidate_dimensions": [],
            "candidate_state_effects": [],
            "unresolved_propagation": feature["source_unresolved"],
            "blockers": blockers,
            "execution_readiness": False,
            "explicit_exclusions": ["no opcode", "no memory model", "no numerical method", "no optimization"],
        })
    dump("contract-production-plan.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "plans": contract_plans,
        "summary": {"planned_contracts": len(contract_plans)},
        "status": "complete_with_reservations",
    })
    dump("ir-production-plan.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "plans": ir_plans,
        "summary": {"planned_irs": len(ir_plans)},
        "status": "complete_with_reservations",
    })
    report(
        "contract-production-plan-report.md",
        "Practice contract production plan",
        [f"All {len(contract_plans)} revised features have non-final contract plans."],
        ["Plans preserve blockers and do not constitute contracts."],
    )
    report(
        "ir-production-plan-report.md",
        "Practice IR production plan",
        [f"All {len(ir_plans)} revised features have non-final IR plans."],
        ["Operations, types, dimensions, shapes, and state effects remain undetermined."],
    )

    readiness_rows = [{
        "feature_id": feature["feature_id"],
        "ready_for_contract_plan": True,
        "ready_for_partial_contract": feature["review_classification"] == "retained_with_reservations",
        "ready_for_full_contract": False,
        "ready_for_ir": False,
        "ready_for_implementation": False,
        "ready_for_code_generation": False,
        "blockers": feature["source_unresolved"],
    } for feature in feature_rows]
    dump("production-readiness.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "features": readiness_rows,
        "ready_for_contract_generation_now": True,
        "ready_for_full_contract_generation": False,
        "ready_for_ir_generation": False,
        "ready_for_implementation_planning": False,
        "ready_for_code_generation": False,
        "status": "complete_with_reservations",
    })
    report(
        "production-readiness-report.md",
        "Practice production readiness",
        ["Preparation and contract planning are complete; retained features may enter later partial-contract work."],
        ["Full contracts, IR, implementation, optimization, and code generation are not ready."],
    )

    dump("historical-artifact-assessment.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "artifacts_found": [],
        "modified": [],
        "promoted": [],
        "status": "complete",
    })
    report(
        "historical-artifact-assessment.md",
        "Practice historical artifact assessment",
        ["No canonical Practice contract, IR, optimization, implementation, or dedicated test artifact was found."],
        ["Non-merged work is excluded from scientific authority."],
    )

    decisions = [
        {
            "decision_id": "PRACTICE-DECISION-001",
            "question": "How are Practice, Capacity, Competency, and Lived Experience typed and separated canonically?",
            "authority": "human_scientific_review",
            "status": "unresolved",
        },
        {
            "decision_id": "PRACTICE-DECISION-002",
            "question": "What formal semantics, if any, do the two textual pattern mentions carry?",
            "authority": "human_scientific_review",
            "status": "unresolved",
        },
        {
            "decision_id": "PRACTICE-DECISION-003",
            "question": "Which source thresholds, temporal parameters, spaces, units, and stochastic terms are contractually normative?",
            "authority": "human_scientific_review",
            "status": "unresolved",
        },
    ]
    dump("decision-required.yaml", {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "decisions": decisions,
        "status": "unresolved",
    })
    report(
        "decision-required-report.md",
        "Practice decisions required",
        [f"{len(decisions)} grouped human decisions are recorded."],
        ["They summarize blockers and do not replace the 60 canonical unresolved records."],
    )

    manifest = {
        "domain": "practice",
        "source": SOURCE,
        "baseline_commit": BASELINE,
        "authority": "origin/main",
        "preparation_status": "preparation_complete_with_reservations",
        "coverage": {
            "objects": len(objects),
            "relations": len(relations),
            "unresolved": len(unresolved),
            "duplicate_candidates": len(duplicates),
            "features": len(features),
            "contract_plans": len(contract_plans),
            "ir_plans": len(ir_plans),
        },
        "non_invention": {
            "contracts_created": 0,
            "irs_created": 0,
            "optimizations_created": 0,
            "implementations_created": 0,
        },
        "ready_for_contract_generation_now": True,
        "ready_for_full_contract_generation": False,
        "ready_for_ir_generation": False,
        "ready_for_implementation_planning": False,
        "ready_for_code_generation": False,
        "next_required_gate": "human scientific review and canonical reconciliation of external domains",
        "final_decision": "preparation_complete_with_reservations",
    }
    dump("preparation-manifest.yaml", manifest)
    report(
        "domain-preparation-report.md",
        "Practice domain preparation",
        [
            f"Preparation covers {len(objects)} objects, {len(relations)} relations, {len(unresolved)} unresolved records, "
            f"{len(features)} features, {len(contract_plans)} contract plans, and {len(ir_plans)} IR plans."
        ],
        [
            "Capacities, Competencies, and Lived Experience remain external non-reconciled dependencies.",
            "Preparation is not scientific validation or implementation authorization.",
        ],
    )


if __name__ == "__main__":
    main()
