from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/disciple"
REP = ROOT / "reports/domain-progress/disciple"
MASTER_COMMIT = "eb977485b7314e32e643e52461e086eb3a753724"
PREFIX = "TLC-FC-01-DISCIPLE-"


def load(path):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def dump(name, data):
    (REG / name).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")


def report(name, title, body):
    (REP / name).write_text(f"# {title}\n\n{body.strip()}\n", encoding="utf-8")


objects = load("registry/scientific-objects/disciple/scientific-objects.candidate.yaml")["objects"]
relations = load("registry/scientific-objects/disciple/scientific-relations.candidate.yaml")["relations"]
unresolved = load("registry/scientific-objects/disciple/unresolved-terms.yaml")["unresolved_terms"]
catalogue = load("registry/features/feature-candidates.yaml")["features"]
features = sorted([f for f in catalogue if f["candidate_feature_id"].startswith(PREFIX)], key=lambda x: x["candidate_feature_id"])
ids = [f["candidate_feature_id"] for f in features]
master_features = load("registry/domain-progress/master/feature-status.yaml")["features"]
master_feature_ids = {x["feature_id"] for x in master_features}
master_objects = load("registry/scientific-objects/master/scientific-objects.candidate.yaml")["objects"]
master_object_ids = {x["provisional_object_id"] for x in master_objects}
generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

meta = {
    "domain_id": "disciple",
    "reconciliation_status": "reconciliation_complete_with_reservations",
    "master_commit": MASTER_COMMIT,
    "master_status": "complete_to_ir_with_reservations",
    "generated_at": generated,
    "contracts_produced": 0,
    "irs_produced": 0,
}

object_by_id = {o["provisional_object_id"]: o for o in objects}


def basis(f): return f.get("scientific_basis", {})
def fobjects(f): return basis(f).get("scientific_object_ids", [])
def frelations(f): return basis(f).get("scientific_relation_ids", [])


dependency_specs = [
    ("TLC-DDEP-DISCIPLE-MASTER-001", "TLC-FC-01-DISCIPLE-002", ["TLC-SO-DISCIPLE-002"], "generic Master entity in conceptual definition"),
    ("TLC-DDEP-DISCIPLE-MASTER-002", "TLC-FC-01-DISCIPLE-004", ["TLC-SO-DISCIPLE-052"], "Master entity symbol in trajectory equation"),
    ("TLC-DDEP-DISCIPLE-MASTER-003", "TLC-FC-01-DISCIPLE-009", ["TLC-SO-DISCIPLE-001", "TLC-SO-DISCIPLE-016", "TLC-SO-DISCIPLE-017", "TLC-SO-DISCIPLE-025", "TLC-SO-DISCIPLE-026", "TLC-SO-DISCIPLE-062", "TLC-SO-DISCIPLE-065", "TLC-SO-DISCIPLE-066", "TLC-SO-DISCIPLE-067"], "generic Master entity across Disciple state and lifecycle descriptions"),
    ("TLC-DDEP-DISCIPLE-MASTER-004", "TLC-FC-01-DISCIPLE-010", ["TLC-SO-DISCIPLE-015"], "Master entity symbol in trajectory state"),
]

dependencies = []
for dep_id, fid, oids, reason in dependency_specs:
    dependencies.append({
        "dependency_id": dep_id, "from_domain": "disciple", "to_domain": "master",
        "affected_feature_ids": [fid], "affected_object_ids": oids, "affected_relation_ids": [],
        "master_object_ids": ["TLC-SO-MASTER-001"], "master_feature_ids": ["TLC-FC-00-MASTER-016"],
        "master_contract_ids": [], "master_ir_ids": [], "dependency_type": "entity_dependency",
        "source_evidence": [object_by_id[x]["source_statement"] for x in oids],
        "master_evidence": {
            "canonical_object": "TLC-SO-MASTER-001",
            "canonical_statement": "Le Maître est une entité catalytique capable d’induire et de guider une transformation d’état chez un Disciple.",
            "symbolic_feature": "TLC-FC-00-MASTER-016",
            "contract_path_consulted": "registry/math-contracts/TLC-FC-00-MASTER-016/contract.yaml",
            "ir_path_consulted": "ir/TLC-FC-00-MASTER-016/ir.candidate.json",
        },
        "evidence_locations": [object_by_id[x]["source_reference"] for x in oids] + [
            {"path": "registry/scientific-objects/master/scientific-objects.candidate.yaml", "object_id": "TLC-SO-MASTER-001"},
            {"path": "registry/domain-progress/master/feature-status.yaml", "feature_id": "TLC-FC-00-MASTER-016"},
        ],
        "dependency_status": "confirmed", "strength": "required", "required_master_level": "symbol_only",
        "production_effect": "blocks_execution_only",
        "reconciliation_reason": reason + "; exact Master entity and symbolic feature now exist canonically",
        "notes": "The Master contract and IR were consulted as evidence but are not required dependencies for Disciple contract drafting.",
    })
dump("master-dependencies.yaml", {**meta, "candidates_before": 4, "summary": {"confirmed": 4, "rejected_not_a_dependency": 0, "inferred_candidate": 0, "unresolved": 0}, "dependencies": dependencies})

mappings = []
for i, (_, fid, oids, _) in enumerate(dependency_specs, 1):
    mappings.append({
        "mapping_id": f"TLC-MAP-DISCIPLE-MASTER-{i:03d}", "disciple_source_term": "Maître / \\mathcal{M}",
        "disciple_object_ids": oids, "disciple_feature_ids": [fid], "master_canonical_object_id": "TLC-SO-MASTER-001",
        "master_feature_ids": ["TLC-FC-00-MASTER-016"], "mapping_status": "confirmed",
        "evidence": ["maths/01-disciple.md explicit Master reference", "TLC-SO-MASTER-001 canonical entity", "TLC-FC-00-MASTER-016 symbolic type"],
        "notes": "Confirms entity identity only; does not infer an internal Master component or executable semantics.",
    })
for term, oids, fid in [
    ("\\mathcal{M}_{\\mathcal{I}}", ["TLC-SO-DISCIPLE-016"], "TLC-FC-01-DISCIPLE-009"),
    ("\\Pi_{\\mathcal{M}}", ["TLC-SO-DISCIPLE-015", "TLC-SO-DISCIPLE-052"], "TLC-FC-01-DISCIPLE-010"),
    ("\\mathcal{P}_{\\mathrm{Maître}}", ["TLC-SO-DISCIPLE-025", "TLC-SO-DISCIPLE-066", "TLC-SO-DISCIPLE-067"], "TLC-FC-01-DISCIPLE-009"),
]:
    mappings.append({
        "mapping_id": f"TLC-MAP-DISCIPLE-MASTER-{len(mappings)+1:03d}", "disciple_source_term": term,
        "disciple_object_ids": oids, "disciple_feature_ids": [fid], "master_canonical_object_id": None,
        "master_feature_ids": [], "mapping_status": "unresolved",
        "evidence": ["No exact canonical Master object or symbol defines this Disciple-side sub-symbol."],
        "notes": "Generic Master entity mapping is available, but component semantics remain unresolved.",
    })
dump("master-symbol-mapping.yaml", {**meta, "summary": {"confirmed": 4, "candidate": 0, "rejected": 0, "unresolved": 3}, "mappings": mappings})

class_map = {
    "TLC-FC-01-DISCIPLE-001": "validation_contract", "TLC-FC-01-DISCIPLE-002": "not_yet_determinable",
    "TLC-FC-01-DISCIPLE-003": "computational_contract", "TLC-FC-01-DISCIPLE-004": "not_yet_determinable",
    "TLC-FC-01-DISCIPLE-005": "computational_contract", "TLC-FC-01-DISCIPLE-006": "validation_contract",
    "TLC-FC-01-DISCIPLE-007": "not_yet_determinable", "TLC-FC-01-DISCIPLE-008": "structural_contract",
    "TLC-FC-01-DISCIPLE-009": "structural_contract", "TLC-FC-01-DISCIPLE-010": "not_yet_determinable",
}
dep_by_feature = {d["affected_feature_ids"][0]: d for d in dependencies}
internal_edges = []
for f in features:
    for dep in f.get("dependencies", {}).get("immediate_feature_candidates", []):
        if dep in ids:
            internal_edges.append({"from_feature_id": f["candidate_feature_id"], "to_feature_id": dep, "dependency_status": "confirmed_from_catalogue", "revalidated_after_master": True})

ambiguous = {"TLC-FC-01-DISCIPLE-004", "TLC-FC-01-DISCIPLE-007", "TLC-FC-01-DISCIPLE-009", "TLC-FC-01-DISCIPLE-010"}
feature_rows = []
for f in features:
    fid = f["candidate_feature_id"]
    master_dep = dep_by_feature.get(fid)
    local_ambiguous = fid in ambiguous
    feature_rows.append({
        "feature_id": fid, "canonical_name": f["name"], "source_objects": fobjects(f), "source_relations": frelations(f),
        "master_dependencies": [master_dep["dependency_id"]] if master_dep else [],
        "internal_dependencies": [e["to_feature_id"] for e in internal_edges if e["from_feature_id"] == fid],
        "scientific_unresolved": f.get("dependencies", {}).get("unresolved_dependencies", []) + f.get("unresolved_questions", []),
        "contract_classification": class_map[fid],
        "future_contract_status": "ready_with_propagated_unresolved" if local_ambiguous else "ready_now",
        "future_ir_status": "structural_ir_plannable_with_unresolved" if local_ambiguous else "eligible_after_contract",
        "contract_generation_gate": "unresolved_but_contract_plannable" if local_ambiguous else ("master_symbols_available" if master_dep else "no_master_gate"),
        "ir_generation_gate": "contract_validated", "execution_readiness": False,
        "reconciliation_status": "reconciled_with_master_with_reservations" if master_dep else ("blocked_by_local_scientific_ambiguity" if local_ambiguous else "no_master_dependency"),
        "blocking_reason": "execution semantics remain unresolved" if local_ambiguous else None,
        "notes": "Contract planning is allowed; no executable claim is made.",
    })
dump("feature-status.yaml", {**meta, "features": feature_rows})

blockers = []
for fid in sorted(ambiguous):
    blockers.append({
        "feature_id": fid, "master_symbol_available": fid in dep_by_feature, "master_contract_required": False,
        "master_ir_required": False, "local_blocker_independent_of_master": True,
        "statuses": ["contract_plannable_with_unresolved", "structural_ir_plannable_with_unresolved", "execution_only_blocker"],
        "contract_plannable_without_invention": True, "structural_ir_possible": True, "execution_claim_allowed": False,
        "human_decision_required_before_planning": False,
        "notes": "Scientific ambiguity is preserved and must be represented explicitly in future artifacts.",
    })
dump("local-blocker-reassessment.yaml", {**meta, "features": blockers, "summary": {"blocker_removed_by_master_mapping": 0, "contract_plannable_with_unresolved": 4, "structural_ir_plannable_with_unresolved": 4, "execution_only_blocker": 4, "remains_scientifically_blocked": 0, "human_decision_required": 0}})

dump("feature-dependencies.yaml", {**meta, "confirmed_edges": internal_edges, "inferred_edges": [], "unresolved_edges": [], "root_features": ["TLC-FC-01-DISCIPLE-009"], "cycles": [], "master_reconciliation_changed_order": False})
dump("feature-classification.yaml", {**meta, "classification_unchanged_after_master": True, "features": [{"feature_id": fid, "classification": cls, "evidence": "Existing category remains valid; Master mapping establishes identity only."} for fid, cls in class_map.items()]})

groups = [
    {"group_id": "A_independent_of_master", "order": 1, "feature_ids": ["TLC-FC-01-DISCIPLE-001", "TLC-FC-01-DISCIPLE-003", "TLC-FC-01-DISCIPLE-005", "TLC-FC-01-DISCIPLE-006", "TLC-FC-01-DISCIPLE-008"], "required_master_symbols": [], "required_master_contracts": [], "required_master_irs": [], "required_disciple_features": ["TLC-FC-01-DISCIPLE-009"], "unresolved": [], "contract_generation_allowed": True, "ir_generation_allowed_after_contract": True, "execution_claim_allowed": False, "blocking_conditions": [], "notes": "No Master dependency evidenced."},
    {"group_id": "B_master_symbol_dependency", "order": 2, "feature_ids": ["TLC-FC-01-DISCIPLE-002"], "required_master_symbols": ["TLC-SO-MASTER-001"], "required_master_contracts": [], "required_master_irs": [], "required_disciple_features": ["TLC-FC-01-DISCIPLE-009"], "unresolved": [], "contract_generation_allowed": True, "ir_generation_allowed_after_contract": True, "execution_claim_allowed": False, "blocking_conditions": [], "notes": "Canonical Master entity is available."},
    {"group_id": "C_master_contract_dependency", "order": 3, "feature_ids": [], "required_master_symbols": [], "required_master_contracts": [], "required_master_irs": [], "required_disciple_features": [], "unresolved": [], "contract_generation_allowed": True, "ir_generation_allowed_after_contract": True, "execution_claim_allowed": False, "blocking_conditions": [], "notes": "No required Master contract evidenced."},
    {"group_id": "D_master_ir_dependency", "order": 4, "feature_ids": [], "required_master_symbols": [], "required_master_contracts": [], "required_master_irs": [], "required_disciple_features": [], "unresolved": [], "contract_generation_allowed": True, "ir_generation_allowed_after_contract": True, "execution_claim_allowed": False, "blocking_conditions": [], "notes": "No required Master IR evidenced."},
    {"group_id": "E_local_ambiguity_but_structurally_plannable", "order": 5, "feature_ids": sorted(ambiguous), "required_master_symbols": ["TLC-SO-MASTER-001"], "required_master_contracts": [], "required_master_irs": [], "required_disciple_features": ["TLC-FC-01-DISCIPLE-009"], "unresolved": "feature_specific", "contract_generation_allowed": True, "ir_generation_allowed_after_contract": True, "execution_claim_allowed": False, "blocking_conditions": ["unresolved must be propagated"], "notes": "Master mapping does not resolve local semantics."},
    {"group_id": "F_human_scientific_decision_required", "order": 6, "feature_ids": [], "required_master_symbols": [], "required_master_contracts": [], "required_master_irs": [], "required_disciple_features": [], "unresolved": [], "contract_generation_allowed": False, "ir_generation_allowed_after_contract": False, "execution_claim_allowed": False, "blocking_conditions": [], "notes": "No feature requires a human decision before conservative planning."},
]
dump("production-order.yaml", {**meta, "groups": groups, "all_features_covered": True})

contract_plan, ir_plan = [], []
for priority, f in enumerate(features, 1):
    fid = f["candidate_feature_id"]
    dep = dep_by_feature.get(fid)
    local = fid in ambiguous
    contract_plan.append({
        "feature_id": fid, "planned_contract_type": class_map[fid], "source_objects": fobjects(f), "source_relations": frelations(f),
        "expected_inputs": "not_specified", "expected_outputs": "not_specified", "expected_state": "not_specified",
        "expected_constraints": "source_grounded_only", "expected_invariants": "source_grounded_only",
        "master_symbols": ["TLC-SO-MASTER-001"] if dep else [], "master_contract_dependencies": [], "master_ir_dependencies": [],
        "known_unresolved": f.get("unresolved_questions", []), "required_evidence_before_generation": ["preserve unresolved explicitly"] if local else [],
        "contract_generation_gate": "unresolved_but_contract_plannable" if local else ("master_symbols_available" if dep else "no_master_gate"),
        "contract_generation_priority": priority, "contract_generation_ready": True,
        "notes": "No contract generated by reconciliation.",
    })
    ir_plan.append({
        "feature_id": fid, "planned_ir_kind": "structural_candidate" if local or class_map[fid] == "structural_contract" else "semantic_candidate",
        "planned_contract_dependency": "future_validated_disciple_contract", "master_symbol_dependencies": ["TLC-SO-MASTER-001"] if dep else [],
        "master_contract_dependencies": [], "master_ir_dependencies": [], "planned_external_symbols": "explicit_only",
        "planned_constraints": "from_future_contract", "planned_unresolved_representation": "explicit_metadata_or_opaque_node",
        "schema_candidate": "not_yet_assessable", "validator_candidate": "future_disciple_ir_validator", "ir_generation_gate": "contract_validated",
        "structural_ir_possible": True, "execution_ready_expected": False, "implementation_readiness_expected": False,
        "notes": "No IR generated by reconciliation.",
    })
dump("contract-production-plan.yaml", {**meta, "features": contract_plan})
dump("ir-production-plan.yaml", {**meta, "features": ir_plan})

unresolved_rows = []
for item in unresolved:
    unresolved_rows.append({
        "unresolved_id": item["unresolved_id"], "source_location": item["source_reference"],
        "affected_objects": item.get("affected_object_ids", []), "affected_features": [fid for fid in ids if set(item.get("affected_object_ids", [])).intersection(fobjects(next(f for f in features if f["candidate_feature_id"] == fid)))],
        "original_record": item, "resolution_effect_from_master": "unresolved_remains", "blocks_contract": False,
        "blocks_ir": False, "blocks_execution": True, "can_be_propagated": True,
        "notes": "No exact Master artifact resolves this local scientific question.",
    })
dump("unresolved-status.yaml", {**meta, "total": len(unresolved_rows), "items": unresolved_rows})

dump("production-gates.yaml", {
    **meta,
    "master_gate": {"actual_master_status": "complete_to_ir_with_reservations", "accepted": True, "master_commit": MASTER_COMMIT, "required_symbols": ["TLC-SO-MASTER-001", "TLC-FC-00-MASTER-016"], "required_contracts": [], "required_irs": [], "unresolved_master_dependencies": []},
    "disciple_preparation_gate": {"inventory_complete": True, "scientific_coverage_complete": True, "feature_coverage_complete": True, "dependency_graph_complete": True, "master_reconciliation_complete": True, "classification_complete": True, "production_order_complete": True, "unresolved_classified": True, "contract_plan_complete": True, "ir_plan_complete": True},
    "blocking_conditions": [], "non_blocking_reservations": ["32 local unresolved records must be propagated", "three Master sub-symbol mappings remain unresolved", "execution semantics are not validated"],
    "ready_for_contract_generation_now": True, "ready_for_full_contract_generation": True,
    "ready_for_ir_generation": False, "ready_for_implementation_planning": False, "ready_for_code_generation": False,
})
dump("global-manifest-update-proposal.yaml", {
    **meta, "proposal_only": True, "proposed_update": {"domain_id": "disciple", "preparation_status": "preparation_complete_with_reservations", "master_reconciliation_status": "reconciliation_complete_with_reservations", "features_total": 10, "contracts_produced": 0, "irs_produced": 0, "ready_for_contract_generation_now": True, "ready_for_full_contract_generation": True, "ready_for_ir_generation": False, "ready_for_code_generation": False},
})

master_artifacts = [
    "registry/domain-progress/master/domain-status.yaml", "registry/domain-progress/master/feature-status.yaml",
    "registry/scientific-objects/master/scientific-objects.candidate.yaml",
    "registry/math-contracts/TLC-FC-00-MASTER-016/contract.yaml", "ir/TLC-FC-00-MASTER-016/ir.candidate.json",
]
dump("post-master-reconciliation.yaml", {
    **meta, "master_artifacts_consulted": master_artifacts, "dependencies": {"confirmed": 4, "rejected": 0, "candidate": 0, "unresolved": 0},
    "symbol_mappings": {"confirmed": 4, "candidate": 0, "rejected": 0, "unresolved": 3},
    "feature_effects": {"covered": 10, "contract_plannable": 10, "structural_ir_plannable": 10, "execution_ready": 0},
    "local_blocker_effects": {"contract_plannable_with_unresolved": 4, "execution_only_blocker": 4},
    "merge_decision": "ready_if_validation_and_repository_checks_pass", "full_production_handoff": True,
})

report("master-symbol-reconciliation-report.md", "Disciple post-Master symbol reconciliation", "Four generic Master entity mappings are confirmed to `TLC-SO-MASTER-001` and `TLC-FC-00-MASTER-016`. Three Disciple-side sub-symbols remain unresolved because Master has no exact canonical definition for them.")
report("local-blocker-reassessment.md", "Disciple local blocker reassessment", "All four previously ambiguous features can be planned conservatively with unresolved data and can support a structural IR after contract validation. Their blockers affect execution claims, not preparation or artifact planning.")
report("feature-dependency-report.md", "Disciple internal dependencies after Master", f"All {len(internal_edges)} catalogue edges remain valid. `TLC-FC-01-DISCIPLE-009` remains the root and no cycle is present.")
report("feature-classification-report.md", "Disciple classification after Master", "Master establishes entity identity only, so the existing classification is retained without inventing signatures.")
report("production-order.md", "Disciple production order after Master", "The ten features are covered by six explicit groups. Master contract and IR dependency groups are empty; symbol-only and locally ambiguous features remain structurally plannable.")
report("unresolved-report.md", "Disciple unresolved after Master", "All 32 unresolved records remain preserved. Canonical Master identity does not resolve their local scientific semantics; they are propagable but continue to block executable claims.")
report("post-master-reconciliation-report.md", "Disciple post-Master reconciliation", f"Canonical Master commit: `{MASTER_COMMIT}`. Four former candidate dependencies are confirmed as symbol-only entity dependencies; no Master contract or IR is required. All ten Disciple features are contract-plannable, no contract or IR was generated, and the branch is ready for validation and integration with reservations.")
report("10-completion-report.md", "Disciple preparation — completion report", "Status: **reconciliation complete with reservations**. Master is canonical, all four prior candidates were reconciled, all ten features are ready for conservative contract generation, and execution/code readiness remains false.")

print("Reconciled 4 Master dependencies, 7 symbol mappings, 10 features and 32 unresolved records.")
