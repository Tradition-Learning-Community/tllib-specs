#!/usr/bin/env python3
"""Build preparation-only artifacts for the 15-relations domain."""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry" / "domain-progress" / "relations"
REP = ROOT / "reports" / "domain-progress" / "relations"
BASE_COMMIT = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
SOURCE = "maths/15-relations.md"
DOMAIN = "relations"
STATUS = "preparation_complete_with_reservations"


def load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=110),
        encoding="utf-8",
    )


def report(path: str, title: str, body: str) -> None:
    target = REP / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f"# {title}\n\n{body.rstrip()}\n", encoding="utf-8")


objects_doc = load("registry/scientific-objects/relations/scientific-objects.candidate.yaml")
relations_doc = load("registry/scientific-objects/relations/scientific-relations.candidate.yaml")
unresolved_doc = load("registry/scientific-objects/relations/unresolved-terms.yaml")
duplicates_doc = load("registry/scientific-objects/relations/duplicate-candidates.yaml")
catalogue_doc = load("registry/features/revised/feature-candidates.yaml")

objects = objects_doc["objects"]
relations = relations_doc["relations"]
unresolved = unresolved_doc["unresolved_terms"]
duplicates = duplicates_doc["duplicate_candidates"]
features = sorted(
    (
        item
        for item in catalogue_doc["features"]
        if item["candidate_feature_id"].startswith("TLC-FC-15-RELATIONS-")
    ),
    key=lambda item: item["candidate_feature_id"],
)
feature_ids = [item["candidate_feature_id"] for item in features]
object_ids = {item["provisional_object_id"] for item in objects}
relation_ids = {item["provisional_relation_id"] for item in relations}
unresolved_ids = {item["unresolved_id"] for item in unresolved}
source_lines = (ROOT / SOURCE).read_text(encoding="utf-8").splitlines()
generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

common = {
    "domain_id": DOMAIN,
    "status": STATUS,
    "authority": "origin/main",
    "working_base_commit": BASE_COMMIT,
    "generated_at": generated_at,
    "scope": "preparation_only_no_contract_or_ir",
}

mapped_object_features: dict[str, list[str]] = {object_id: [] for object_id in object_ids}
for feature in features:
    for object_id in feature["scientific_basis"].get("scientific_object_ids", []):
        mapped_object_features[object_id].append(feature["candidate_feature_id"])

source_inventory = {
    **common,
    "source_file": SOURCE,
    "source_commit_recorded_by_extraction": objects_doc["artifact"]["source_commit"],
    "source_blob_sha_recorded_by_extraction": objects_doc["artifact"]["source_blob_sha"],
    "source_lines": len(source_lines),
    "objects_count": len(objects),
    "relations_count": len(relations),
    "unresolved_count": len(unresolved),
    "duplicate_candidates_count": len(duplicates),
    "features_total": len(features),
    "feature_ids": feature_ids,
    "existing_contracts_for_domain": 0,
    "existing_irs_for_domain": 0,
    "input_artifacts": [
        "registry/scientific-objects/relations/scientific-objects.candidate.yaml",
        "registry/scientific-objects/relations/scientific-relations.candidate.yaml",
        "registry/scientific-objects/relations/unresolved-terms.yaml",
        "registry/scientific-objects/relations/duplicate-candidates.yaml",
        "registry/features/revised/feature-candidates.yaml",
    ],
    "validators": [
        "tools/scientific-audit/audit_scientific_extractions.py",
        "tools/functional-decomposition-revision/validate_revision.py",
        "scripts/validate_relations_preparation.py",
    ],
    "inventory_status": "complete_with_reservations",
}
dump(REG / "source-inventory.yaml", source_inventory)

scientific_audit = {
    **common,
    "objects": {
        "total": len(objects),
        "by_type": dict(sorted(Counter(item["object_type"] for item in objects).items())),
        "ids_unique": len(object_ids) == len(objects),
    },
    "relations": {
        "total": len(relations),
        "by_extraction_type": dict(
            sorted(Counter(item["relation_type"] for item in relations).items())
        ),
        "ids_unique": len(relation_ids) == len(relations),
        "directions_preserved": True,
        "scientific_semantics_inferred_from_extraction_edges": False,
        "note": (
            "refers_to and depends_on are preserved as extraction relations only; "
            "they are not silently promoted to social, mathematical, graph, interaction, "
            "dependency, or operator semantics."
        ),
    },
    "unresolved": {
        "total": len(unresolved),
        "ids_unique": len(unresolved_ids) == len(unresolved),
        "status_preserved": all(item["status"] == "unresolved" for item in unresolved),
    },
    "duplicate_candidates": {
        "total": len(duplicates),
        "automatic_merges": 0,
        "status": "unresolved",
    },
    "traceability": {
        "source_file": SOURCE,
        "all_object_ranges_valid": all(
            1 <= item["source_reference"]["start_line"]
            <= item["source_reference"]["end_line"]
            <= len(source_lines)
            for item in objects
        ),
        "all_relation_ranges_valid": all(
            1 <= item["source_reference"]["start_line"]
            <= item["source_reference"]["end_line"]
            <= len(source_lines)
            for item in relations
        ),
    },
    "audit_status": "complete_with_reservations",
}
dump(REG / "scientific-audit.yaml", scientific_audit)

patterns = {
    **common,
    "patterns": [
        {
            "pattern_id": "TLC-PAT-RELATIONS-001",
            "name": "five_named_master_dimension_relations",
            "source_ranges": ["9-71", "73-111", "116-155", "159-187", "199-228"],
            "occurrences": 5,
            "interpretation": "source_explicit_structural_repetition",
            "semantic_equivalence": "unresolved",
            "automatic_generalization_allowed": False,
        },
        {
            "pattern_id": "TLC-PAT-RELATIONS-002",
            "name": "tuple_formalizations",
            "source_ranges": ["54-66", "99-109", "143-153", "183-185", "224-226"],
            "occurrences": 5,
            "interpretation": "source_explicit_tuple_shape_only",
            "tuple_types_and_component_types": "unresolved",
            "automatic_generalization_allowed": False,
        },
        {
            "pattern_id": "TLC-PAT-RELATIONS-003",
            "name": "theorem_or_optimum_claims",
            "source_ranges": ["68-71", "111", "155", "187", "228"],
            "occurrences": 5,
            "interpretation": "claims_preserved_verbatim_for_future_contract_review",
            "proof_status": "not_established_by_domain_preparation",
            "automatic_generalization_allowed": False,
        },
        {
            "pattern_id": "TLC-PAT-RELATIONS-004",
            "name": "community_regulatory_roles",
            "source_ranges": ["47-52", "93-97", "136-140", "177-180", "220-222"],
            "occurrences": 5,
            "interpretation": "qualitative_source_pattern",
            "relation_direction_cardinality_temporality": "unresolved",
            "automatic_generalization_allowed": False,
        },
        {
            "pattern_id": "TLC-PAT-RELATIONS-005",
            "name": "synthesis_interdependencies",
            "source_ranges": ["244-257"],
            "occurrences": 3,
            "interpretation": "explicit_prose_dependencies_requiring_later_reconciliation",
            "automatic_generalization_allowed": False,
        },
    ],
    "shared_ambiguities": [
        "relation_kind",
        "endpoint_identity",
        "direction_beyond_written_orientation",
        "cardinality",
        "symmetry",
        "transitivity",
        "temporality",
        "tuple_component_types",
        "equation_domains_and_oracles",
    ],
    "pattern_analysis_status": "complete_with_reservations",
}
dump(REG / "pattern-analysis.yaml", patterns)

classification_by_category = {
    "transformation": "computational_contract",
    "invariant_check": "validation_contract",
    "scientific_operator": "computational_contract",
    "relation_evaluation": "relational_contract",
}
feature_rows = []
classification_rows = []
readiness_rows = []
coverage_rows = []
for feature in features:
    feature_id = feature["candidate_feature_id"]
    source_objects = feature["scientific_basis"].get("scientific_object_ids", [])
    source_relations = feature["scientific_basis"].get("scientific_relation_ids", [])
    readiness = feature["readiness"]
    catalogue_status = feature["review_application"]["classification"]
    feature_rows.append(
        {
            "feature_id": feature_id,
            "canonical_name": feature["name"],
            "category": feature["category"],
            "catalogue_status": catalogue_status,
            "source_objects": source_objects,
            "source_relations": source_relations,
            "source_references": feature["scientific_basis"]["source_references"],
            "contract_plan_present": True,
            "ir_plan_present": True,
            "status": "candidate",
        }
    )
    classification_rows.append(
        {
            "feature_id": feature_id,
            "contract_classification": classification_by_category[feature["category"]],
            "basis": "origin/main revised catalogue category and review application",
            "invented_signature": False,
            "relation_semantics_fixed": False,
        }
    )
    blocking = (
        readiness["status"] != "retained_with_reservations"
        or bool(readiness.get("blocking_object_ids"))
        or bool(readiness.get("blocking_relation_ids"))
        or bool(readiness.get("blocking_decision_ids"))
        or bool(readiness.get("blocking_terms"))
    )
    readiness_rows.append(
        {
            "feature_id": feature_id,
            "catalogue_readiness": readiness["status"],
            "blocking_object_ids": readiness.get("blocking_object_ids", []),
            "blocking_relation_ids": readiness.get("blocking_relation_ids", []),
            "blocking_decision_ids": readiness.get("blocking_decision_ids", []),
            "blocking_terms": readiness.get("blocking_terms", []),
            "ready_for_contract_generation_now": not blocking,
            "ready_for_full_contract_generation": False,
            "ready_for_ir_generation": False,
            "ready_for_implementation_planning": False,
            "ready_for_code_generation": False,
        }
    )

for object_id in sorted(object_ids):
    mapped = mapped_object_features[object_id]
    coverage_rows.append(
        {
            "object_id": object_id,
            "feature_ids": mapped,
            "coverage_status": (
                "mapped_to_active_revised_feature"
                if mapped
                else "not_promoted_by_revised_catalogue"
            ),
            "note": (
                "No new feature invented; future review may promote this object."
                if not mapped
                else "Covered by origin/main revised feature catalogue."
            ),
        }
    )

feature_inventory = {
    **common,
    "features_total": len(features),
    "features": feature_rows,
    "orphan_features": [],
    "object_coverage": {
        "objects_total": len(objects),
        "mapped_to_active_features": sum(bool(value) for value in mapped_object_features.values()),
        "not_promoted_by_revised_catalogue": sum(
            not value for value in mapped_object_features.values()
        ),
        "rows": coverage_rows,
    },
}
dump(REG / "feature-inventory.yaml", feature_inventory)
dump(
    REG / "feature-classification.yaml",
    {**common, "features": classification_rows, "coverage": len(classification_rows)},
)
dump(
    REG / "feature-readiness.yaml",
    {
        **common,
        "features": readiness_rows,
        "ready_for_contract_generation_now_count": sum(
            item["ready_for_contract_generation_now"] for item in readiness_rows
        ),
        "ready_for_full_contract_generation_count": 0,
        "ready_for_ir_generation_count": 0,
    },
)

external_dependencies = [
    {
        "dependency_id": "TLC-DEP-RELATIONS-MASTER-001",
        "target_domain": "00-master",
        "source_evidence": {"source_path": SOURCE, "start_line": 1, "end_line": 257},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-DISCIPLE-001",
        "target_domain": "01-disciple",
        "source_evidence": {"source_path": SOURCE, "start_line": 18, "end_line": 228},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-COMMUNITY-001",
        "target_domain": "02-community",
        "source_evidence": {"source_path": SOURCE, "start_line": 47, "end_line": 222},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-MESSAGE-001",
        "target_domain": "06-message",
        "source_evidence": {"source_path": SOURCE, "start_line": 9, "end_line": 71},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-PRINCIPLE-001",
        "target_domain": "08-principle",
        "source_evidence": {"source_path": SOURCE, "start_line": 118, "end_line": 118},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-VALUES-001",
        "target_domain": "09-values",
        "source_evidence": {"source_path": SOURCE, "start_line": 116, "end_line": 155},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-VIRTUES-001",
        "target_domain": "10-virtues",
        "source_evidence": {"source_path": SOURCE, "start_line": 73, "end_line": 111},
        "reconciliation_status": "canonical_source_available_reconciliation_pending",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-CAPACITIES-001",
        "target_domain": "11-capacities",
        "source_evidence": {"source_path": SOURCE, "start_line": 159, "end_line": 187},
        "reconciliation_status": "external_unreconciled_not_merged",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-COMPETENCIES-001",
        "target_domain": "12-competencies",
        "source_evidence": {"source_path": SOURCE, "start_line": 199, "end_line": 228},
        "reconciliation_status": "external_unreconciled_not_merged",
        "imported_semantics": False,
    },
    {
        "dependency_id": "TLC-DEP-RELATIONS-PRACTICE-001",
        "target_domain": "13-practice",
        "source_evidence": {"source_path": SOURCE, "start_line": 118, "end_line": 118},
        "reconciliation_status": "external_unreconciled_not_merged",
        "imported_semantics": False,
    },
]

feature_dependencies = {
    **common,
    "intra_domain": {
        "edges": [],
        "status": "none_authorized_by_origin_main_catalogue",
        "note": "No ordering or dependency between the five candidate features is invented.",
    },
    "extraction_dependency_edges": [
        {
            "relation_id": item["provisional_relation_id"],
            "source_object_id": item["source_object_id"],
            "target_object_id": item["target_object_id"],
            "direction_preserved": True,
            "semantic_scope": "extraction_dependency_only",
            "status": item["validation_status"],
        }
        for item in relations
        if item["relation_type"] == "depends_on"
    ],
    "external_domains": external_dependencies,
    "non_merged_domains": ["11-capacities", "12-competencies", "13-practice"],
    "no_dependency_detected": ["14-lived-experience"],
    "dependency_graph_status": "complete_with_unreconciled_external_dependencies",
}
dump(REG / "feature-dependencies.yaml", feature_dependencies)

contract_plans = []
ir_plans = []
for feature, classification, readiness in zip(
    features, classification_rows, readiness_rows, strict=True
):
    feature_id = feature["candidate_feature_id"]
    contract_plans.append(
        {
            "feature_id": feature_id,
            "planned_contract_kind": classification["contract_classification"],
            "source_objects": feature["scientific_basis"]["scientific_object_ids"],
            "source_relations": feature["scientific_basis"].get(
                "scientific_relation_ids", []
            ),
            "preserve_unresolved": True,
            "preserve_duplicate_candidates": True,
            "external_dependency_policy": "reference_only_until_reconciled",
            "signature": "not_specified",
            "types": "not_specified",
            "direction": "not_specified_unless_source_explicit",
            "cardinality": "not_specified",
            "symmetry": "not_specified",
            "transitivity": "not_specified",
            "temporality": "not_specified",
            "oracle": "not_identified",
            "generation_gate": (
                "scientific_decision_required"
                if not readiness["ready_for_contract_generation_now"]
                else "candidate_contract_may_be_generated_with_reservations"
            ),
            "ready_for_contract_generation_now": readiness[
                "ready_for_contract_generation_now"
            ],
            "ready_for_full_contract_generation": False,
        }
    )
    ir_plans.append(
        {
            "feature_id": feature_id,
            "planned_ir_kind": {
                "computational_contract": "candidate_functional_or_semantic_ir",
                "validation_contract": "candidate_validation_or_semantic_ir",
                "relational_contract": "candidate_relational_or_semantic_ir",
            }[classification["contract_classification"]],
            "planned_contract_dependency": "validated_future_contract_required",
            "planned_nodes": "not_specified",
            "planned_edges": "not_specified",
            "planned_relation_semantics": "unresolved",
            "planned_unresolved_representation": "explicit_unresolved_nodes_or_metadata",
            "external_dependency_policy": "reference_only_until_reconciled",
            "ir_generation_gate": "validated_future_contract_required",
            "ready_for_ir_generation": False,
            "ready_for_implementation_planning": False,
            "ready_for_code_generation": False,
        }
    )

dump(
    REG / "contract-production-plan.yaml",
    {
        **common,
        "plans": contract_plans,
        "plans_total": len(contract_plans),
        "ready_now": sum(
            item["ready_for_contract_generation_now"] for item in contract_plans
        ),
        "ready_for_full_contract_generation": False,
    },
)
dump(
    REG / "ir-production-plan.yaml",
    {
        **common,
        "plans": ir_plans,
        "plans_total": len(ir_plans),
        "ready_for_ir_generation": False,
    },
)

domain_status = {
    **common,
    "source": SOURCE,
    "objects": len(objects),
    "relations": len(relations),
    "unresolved": len(unresolved),
    "duplicate_candidates": len(duplicates),
    "features": len(features),
    "contract_plans": len(contract_plans),
    "ir_plans": len(ir_plans),
    "contracts_generated": 0,
    "irs_generated": 0,
    "cpp_generated": False,
    "python_bindings_generated": False,
    "files_outside_relations_preparation_scope": 0,
    "external_unreconciled_dependencies": [
        "11-capacities",
        "12-competencies",
        "13-practice",
    ],
    "ready_for_contract_generation_now": [
        item["feature_id"]
        for item in readiness_rows
        if item["ready_for_contract_generation_now"]
    ],
    "ready_for_full_contract_generation": False,
    "ready_for_ir_generation": False,
    "ready_for_implementation_planning": False,
    "ready_for_code_generation": False,
    "domain_status": STATUS,
}
dump(REG / "domain-status.yaml", domain_status)

report(
    "preparation-report.md",
    "Relations domain preparation",
    f"""## Authority and scope

This preparation is derived only from `origin/main` at `{BASE_COMMIT}`. The scientific source is
`{SOURCE}`. No unmerged branch or pull request supplies scientific authority. No contract, IR, C++,
binding, or reference implementation is produced.

## Audit

- Objects: **{len(objects)}** ({dict(sorted(Counter(item['object_type'] for item in objects).items()))})
- Extraction relations: **{len(relations)}** (`refers_to`: 93; `depends_on`: 6)
- Unresolved: **{len(unresolved)}**, all preserved
- Duplicate candidates: **{len(duplicates)}**, none merged
- Revised candidate features: **{len(features)}**

The extraction relation types are metadata from the extraction stage. This preparation does not
equate them with a scientific relation, social relation, graph edge, interaction, operator, or
implementation dependency.

## Coverage and plans

The five active revised features each have source objects, a classification, readiness record,
contract plan, and IR plan. Seventeen objects are mapped to active revised features. The remaining
83 are recorded as `not_promoted_by_revised_catalogue`; no feature is invented for them and no
object is silently discarded.

## Dependencies and reservations

Dependencies on `11-capacities`, `12-competencies`, and `13-practice` are external and
unreconciled because their preparation work is not merged. No dependency is asserted for
`14-lived-experience`. Relation type, endpoint identity, direction beyond written orientation,
cardinality, symmetry, transitivity, temporality, component types, equation domains, and oracles
remain unresolved.

## Readiness

Only `TLC-FC-15-RELATIONS-004` and `TLC-FC-15-RELATIONS-007` may proceed to candidate contract
generation now, with reservations and source-grounded oracle work still required. Full-domain
contract generation, IR generation, implementation planning, and code generation are not ready.
""",
)

decision = {
    **common,
    "work_item_id": "TLC-PREP-15-RELATIONS",
    "stage": "domain_preparation",
    "artifacts_produced": [
        f"registry/domain-progress/relations/{name}"
        for name in [
            "source-inventory.yaml",
            "scientific-audit.yaml",
            "pattern-analysis.yaml",
            "feature-inventory.yaml",
            "feature-classification.yaml",
            "feature-dependencies.yaml",
            "feature-readiness.yaml",
            "contract-production-plan.yaml",
            "ir-production-plan.yaml",
            "domain-status.yaml",
        ]
    ]
    + [
        "reports/domain-progress/relations/preparation-report.md",
        "reports/domain-progress/relations/decision-required.yaml",
        "scripts/build_relations_preparation.py",
        "scripts/validate_relations_preparation.py",
    ],
    "blocking_issues": [
        "TLC-FC-15-RELATIONS-002 requires scientific decision TLC-HR-0054",
        "TLC-FC-15-RELATIONS-003 requires scientific decision TLC-HR-0074",
        "TLC-FC-15-RELATIONS-008 requires scientific decision TLC-HR-0074",
        "61 source unresolved items remain open",
        "12 duplicate candidates remain unmerged",
    ],
    "external_unreconciled_dependencies": [
        "11-capacities",
        "12-competencies",
        "13-practice",
    ],
    "questions_for_human": [
        "Resolve the 61 extraction uncertainties without bulk classification.",
        "Review the 12 duplicate candidates without automatic merging.",
        "Resolve TLC-HR-0054 and TLC-HR-0074 before blocked feature contracts.",
        "Reconcile Capacities, Competencies, and Practice only after their work is merged.",
    ],
    "recommended_decision": "approved_with_reservations",
    "allowed_decisions": ["approved", "approved_with_reservations", "revise", "rejected"],
    "verdict": "preparation_complete_with_reservations",
    "ready_for_contract_generation_now": [
        "TLC-FC-15-RELATIONS-004",
        "TLC-FC-15-RELATIONS-007",
    ],
    "ready_for_full_contract_generation": False,
    "ready_for_ir_generation": False,
    "ready_for_implementation_planning": False,
    "ready_for_code_generation": False,
}
dump(REP / "decision-required.yaml", decision)

print(
    json.dumps(
        {
            "objects": len(objects),
            "relations": len(relations),
            "unresolved": len(unresolved),
            "duplicates": len(duplicates),
            "features": len(features),
            "contract_plans": len(contract_plans),
            "ir_plans": len(ir_plans),
        },
        sort_keys=True,
    )
)
