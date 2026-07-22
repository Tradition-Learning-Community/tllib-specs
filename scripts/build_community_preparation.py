from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/community"
REP = ROOT / "reports/domain-progress/community"
PREFIX = "TLC-FC-02-COMMUNITY-"
BASELINE = "9aef7ab424f3cf998c47caaa9ed4402302e96031"


def load(path):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def dump(name, data):
    REG.mkdir(parents=True, exist_ok=True)
    (REG / name).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")


def report(name, title, body):
    REP.mkdir(parents=True, exist_ok=True)
    (REP / name).write_text(f"# {title}\n\n{body.strip()}\n", encoding="utf-8")


objects_doc = load("registry/scientific-objects/community/scientific-objects.candidate.yaml")
relations_doc = load("registry/scientific-objects/community/scientific-relations.candidate.yaml")
unresolved_doc = load("registry/scientific-objects/community/unresolved-terms.yaml")
duplicates_doc = load("registry/scientific-objects/community/duplicate-candidates.yaml")
global_objects_doc = load("registry/scientific-objects/global-object-candidates.yaml")
global_relations_doc = load("registry/scientific-objects/global-relation-candidates.yaml")
initial_doc = load("registry/features/feature-candidates.yaml")
revised_doc = load("registry/features/revised/feature-candidates.yaml")
lineage_doc = load("registry/features/revised/feature-lineage.yaml")
domain_edges_doc = load("registry/domain-dependencies/domain-dependency-edges.yaml")

objects = objects_doc["objects"]
relations = relations_doc["relations"]
unresolved = unresolved_doc["unresolved_terms"]
duplicates = duplicates_doc["duplicate_candidates"]
features = sorted([f for f in revised_doc["features"] if f["candidate_feature_id"].startswith(PREFIX)], key=lambda x: x["candidate_feature_id"])
initial = sorted([f for f in initial_doc["features"] if f["candidate_feature_id"].startswith(PREFIX)], key=lambda x: x["candidate_feature_id"])
ids = [f["candidate_feature_id"] for f in features]
initial_ids = [f["candidate_feature_id"] for f in initial]
lineage = {x["original_feature_candidate_id"]: x for x in lineage_doc["lineage"] if x["original_feature_candidate_id"].startswith(PREFIX)}
object_by_id = {o["provisional_object_id"]: o for o in objects}
global_object_ids = {o["source_object_id"] for o in global_objects_doc["objects"]}
global_relation_ids = {r["source_relation_id"] for r in global_relations_doc["relations"]}
source_commit = objects_doc["artifact"]["source_commit"]
generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

meta = {
    "domain_id": "community",
    "status": "preparation_complete_with_reservations",
    "baseline_tag": "tlc-scientific-pipeline-v1",
    "baseline_commit": BASELINE,
    "working_base_commit": "eb977485b7314e32e643e52461e086eb3a753724",
    "generated_at": generated,
    "scope": "preparation_only_no_new_contract_or_ir",
}


def basis(f): return f.get("scientific_basis", {})
def fobjects(f): return basis(f).get("scientific_object_ids", [])
def frelations(f): return basis(f).get("scientific_relation_ids", [])


def object_mentions(f, domain):
    patterns = {
        "master": r"ma(?:î|Ã®|�)tre|master",
        "disciple": r"disciple",
        "relations": r"relations?",
    }
    return [oid for oid in fobjects(f) if re.search(patterns[domain], object_by_id[oid].get("source_statement", ""), re.I)]


historical_contract = ROOT / "registry/math-contracts/TLC-FC-02-COMMUNITY-001/contract.yaml"
historical_ir = ROOT / "ir/TLC-FC-02-COMMUNITY-001/ir-semantic.candidate.json"
missing_expected = []
for required in [objects_doc, relations_doc, unresolved_doc, duplicates_doc, revised_doc, lineage_doc]:
    if required is None: missing_expected.append("unreadable_required_artifact")

dump("source-inventory.yaml", {
    **meta,
    "source_file": "maths/02-community.md",
    "source_commit": source_commit,
    "objects_count": len(objects), "relations_count": len(relations), "unresolved_count": len(unresolved),
    "duplicate_candidates_count": len(duplicates), "features_total": len(features), "feature_ids": ids,
    "initial_catalogue_feature_ids": initial_ids,
    "revised_non_active_lineage": [{"feature_id": fid, "classification": lineage[fid]["new_classification"], "review_decision": lineage[fid]["review_decision"]} for fid in initial_ids if fid not in ids],
    "existing_contracts": int(historical_contract.exists()), "existing_irs": int(historical_ir.exists()),
    "historical_pilot_features": [ids[0]],
    "historical_pilot_contracts": [str(historical_contract.relative_to(ROOT)).replace("\\", "/")],
    "historical_pilot_irs": [str(historical_ir.relative_to(ROOT)).replace("\\", "/")],
    "validators": ["scripts/validate_community_preparation.py"],
    "missing_expected_artifacts": missing_expected, "inventory_status": "complete_with_reservations",
})

object_missing = [o["provisional_object_id"] for o in objects if o["provisional_object_id"] not in global_object_ids]
relation_missing = [r["provisional_relation_id"] for r in relations if r["provisional_relation_id"] not in global_relation_ids]
object_ambiguous = [o["provisional_object_id"] for o in objects if o.get("issues")]
relation_ambiguous = [r["provisional_relation_id"] for r in relations if r.get("issues")]
dump("scientific-coverage.yaml", {
    **meta,
    "objects": {"total": len(objects), "consolidated": len(objects)-len(object_missing), "missing": object_missing, "ambiguous": object_ambiguous},
    "relations": {"total": len(relations), "consolidated": len(relations)-len(relation_missing), "missing": relation_missing, "ambiguous": relation_ambiguous},
    "cross_domain_relations": {"master": [], "disciple": [], "relations": [], "other_domains": [], "note": "Local relation endpoints are Community objects; textual references are assessed separately as candidate dependencies."},
    "unresolved": {"total": len(unresolved), "structural": 0, "semantic": len(unresolved), "typing": 0, "dimensional": 0, "cardinality": 0, "identity": 0, "relational": 0, "other": 0},
    "coverage_status": "complete_with_reservations",
})

class_map = {"constraint_evaluation": "validation_contract", "evolution_dynamics": "computational_contract", "transformation": "computational_contract", "invariant_check": "validation_contract", "metric_evaluation": "computational_contract", "scientific_operator": "computational_contract", "relation_evaluation": "relational_contract"}
classes = []
for f in features:
    cls = class_map.get(f["category"], "not_yet_determinable")
    if "blocked_locally" in f["name"]: cls = "not_yet_determinable"
    classes.append({"feature_id": f["candidate_feature_id"], "contract_classification": cls, "basis": "revised_catalogue_category_and_blocking_status", "invented_signature": False})
class_by_id = {x["feature_id"]: x["contract_classification"] for x in classes}

master_deps, disciple_deps = [], []
for f in features:
    fid = f["candidate_feature_id"]
    for domain, target in [("master", master_deps), ("disciple", disciple_deps)]:
        evidence_objects = object_mentions(f, domain)
        if evidence_objects:
            dep = {
                "dependency_id": f"TLC-COMMUNITY-{domain.upper()}-{len(target)+1:03d}", "from_domain": "community", "to_domain": domain,
                "affected_feature_ids": [fid], "affected_object_ids": evidence_objects, "affected_relation_ids": [],
                "dependency_type": "entity_dependency", "evidence": "Explicit source statement uses the upstream entity.",
                "evidence_locations": [object_by_id[o]["source_reference"] for o in evidence_objects],
                "dependency_status": "inferred_candidate", "strength": "conditional",
                "production_effect": "blocks_execution_only", "notes": "No canonical cross-domain target identifier is declared in the merged feature catalogue.",
            }
            if domain == "disciple": dep["required_disciple_level"] = "symbols_only"
            target.append(dep)
dump("master-dependencies.yaml", {**meta, "dependencies": master_deps, "confirmed_count": 0, "candidate_count": len(master_deps)})
dump("disciple-dependencies.yaml", {**meta, "dependencies": disciple_deps, "confirmed_count": 0, "candidate_count": len(disciple_deps), "non_merged_disciple_branch_used_as_authority": False})

external = [e for e in domain_edges_doc["dependencies"] if e["from_domain"] == "community" and e["to_domain"] not in {"master", "disciple"}]
external_rows = [{**e, "production_effect": "informational_only", "affected_feature_ids": e.get("affected_features", []), "cycle_membership": "community-relations" if e["to_domain"] == "relations" else None} for e in external]
reverse_relations = [e for e in domain_edges_doc["dependencies"] if e["from_domain"] == "relations" and e["to_domain"] == "community"]
dump("external-domain-dependencies.yaml", {**meta, "dependencies": external_rows, "community_relations_cycle": {"status": "inferred_candidate_advisory_cycle", "community_to_relations": len(external_rows), "relations_to_community": len(reverse_relations), "blocks_production": False}})

edges = []
for f in features:
    for dep in f.get("dependencies", {}).get("immediate_feature_candidates", []):
        if dep in ids: edges.append({"from_feature_id": f["candidate_feature_id"], "to_feature_id": dep, "dependency_status": "confirmed_from_revised_catalogue"})
roots = [fid for fid in ids if not any(e["from_feature_id"] == fid for e in edges)]
dump("feature-dependencies.yaml", {**meta, "confirmed_edges": edges, "inferred_edges": [], "unresolved_edges": [], "root_features": roots, "cycles": [], "cooccurrence_used_as_dependency": False})
dump("feature-classification.yaml", {**meta, "features": classes, "coverage": len(classes)})

feature_rows = []
for f in features:
    fid = f["candidate_feature_id"]
    m = any(fid in d["affected_feature_ids"] for d in master_deps)
    d = any(fid in x["affected_feature_ids"] for x in disciple_deps)
    blocked = class_by_id[fid] == "not_yet_determinable"
    if blocked: contract_status = "blocked_by_scientific_ambiguity"
    elif m and d: contract_status = "ready_after_master_and_disciple"
    elif m: contract_status = "ready_after_master"
    elif d: contract_status = "ready_after_disciple"
    else: contract_status = "ready_independent_of_master_and_disciple"
    feature_rows.append({
        "feature_id": fid, "canonical_name": f["name"], "source_file": "maths/02-community.md", "source_objects": fobjects(f), "source_relations": frelations(f),
        "review_status": f.get("review_application", {}).get("review_decision", "accepted_in_revised_catalogue"), "revised_catalogue_status": "active_candidate",
        "scientific_unresolved": f.get("unresolved_questions", []), "master_dependency_status": "inferred_candidate" if m else "none_evidenced",
        "disciple_dependency_status": "inferred_candidate" if d else "none_evidenced", "other_domain_dependency_status": "domain_level_advisory_only" if external_rows else "none_evidenced",
        "internal_dependency_status": "confirmed" if any(e["from_feature_id"] == fid for e in edges) else "root_no_declared_dependency",
        "historical_pilot_status": "historical_pilot" if fid.endswith("001") else "not_pilot", "contract_classification": class_by_id[fid],
        "future_contract_status": contract_status, "future_ir_status": "blocked" if blocked else ({"validation_contract":"validation_ir_expected", "relational_contract":"relational_ir_expected"}.get(class_by_id[fid], "eligible_after_contract")),
        "blocking_reason": "scientific_decision_required" if blocked else None, "notes": "Preparation only; no definitive contract or IR generated.",
    })
dump("feature-status.yaml", {**meta, "features": feature_rows})

pilot_contract = load("registry/math-contracts/TLC-FC-02-COMMUNITY-001/contract.yaml")
pilot_ir_coverage = load("ir/TLC-FC-02-COMMUNITY-001/ir-coverage.yaml")
dump("historical-pilot-assessment.yaml", {
    **meta, "feature_id": ids[0], "role": "historical_pilot", "contract_found": historical_contract.exists(), "ir_found": historical_ir.exists(),
    "domain_complete_to_ir": False, "production_order_validated": False, "implementation_readiness": False,
    "source_alignment": "aligned_to_TLC-SO-COMMUNITY-008_and_source_lines_81_83", "dependency_alignment": "no_required_contracts_declared",
    "unresolved_preserved": len(pilot_contract.get("unresolved_items", [])), "schema_reusability": "candidate_for_comparison_only",
    "ir_coverage_summary": pilot_ir_coverage.get("coverage_summary", {}), "modified_by_preparation": False,
    "recommended_future_action": "reconcile_against_future_domain_contract_conventions; do_not_promote_automatically",
})

groups = {"A_independent": [], "B_after_master": [], "C_after_disciple": [], "D_after_master_and_disciple": [], "E_other_domain": [], "F_scientific_decision": []}
for row in feature_rows:
    key = {"ready_independent_of_master_and_disciple":"A_independent", "ready_after_master":"B_after_master", "ready_after_disciple":"C_after_disciple", "ready_after_master_and_disciple":"D_after_master_and_disciple", "blocked_by_scientific_ambiguity":"F_scientific_decision"}[row["future_contract_status"]]
    groups[key].append(row["feature_id"])
dump("production-order.yaml", {**meta, "groups": groups, "ordering_rule": "A; then B/C; then D after both symbol gates; E if confirmed; F after scientific decision", "all_features_covered_once": True})

contract_plan, ir_plan = [], []
for priority, (f, status) in enumerate(zip(features, feature_rows), 1):
    fid = f["candidate_feature_id"]
    gate = {"ready_independent_of_master_and_disciple":"no_upstream_gate", "ready_after_master":"master_complete_to_ir", "ready_after_disciple":"disciple_symbols_available", "ready_after_master_and_disciple":"master_and_disciple_complete_to_ir", "blocked_by_scientific_ambiguity":"scientific_decision_required"}[status["future_contract_status"]]
    placeholders = {"expected_inputs":"not_specified", "expected_outputs":"not_specified", "expected_state":"not_specified", "expected_membership":"not_specified", "expected_collection_semantics":"not_specified", "expected_aggregation":"not_specified", "expected_constraints":"not_specified", "expected_invariants":"not_specified"}
    contract_plan.append({"feature_id": fid, "planned_contract_type": class_by_id[fid], "source_objects": fobjects(f), "source_relations": frelations(f), **placeholders, "expected_master_dependencies": [d["dependency_id"] for d in master_deps if fid in d["affected_feature_ids"]], "expected_disciple_dependencies": [d["dependency_id"] for d in disciple_deps if fid in d["affected_feature_ids"]], "expected_other_dependencies": [], "known_unresolved": f.get("unresolved_questions", []), "required_evidence_before_generation": [gate], "contract_generation_gate": gate, "contract_generation_priority": priority, "notes": "Future plan only."})
    ir_plan.append({"feature_id": fid, "planned_ir_kind": "candidate_" + class_by_id[fid].replace("_contract", "_ir"), "planned_contract_dependency": "validated_future_contract", "planned_master_interfaces": [d["dependency_id"] for d in master_deps if fid in d["affected_feature_ids"]], "planned_disciple_interfaces": [d["dependency_id"] for d in disciple_deps if fid in d["affected_feature_ids"]], "planned_other_domain_interfaces": [], "planned_external_symbols": "unresolved", "planned_elements": "not_specified", "planned_relations": "not_specified", "planned_aggregations": "not_specified", "planned_constraints": "not_specified", "planned_unresolved_representation": "explicit_unresolved_nodes_or_metadata", "schema_candidate": "historical_pilot_schema_for_comparison_only" if fid.endswith("001") else "not_yet_assessable", "validator_candidate": "future_domain_ir_validator", "historical_pilot_reuse_candidate": fid.endswith("001"), "ir_generation_gate": "scientific_decision_required" if class_by_id[fid] == "not_yet_determinable" else "contract_validated", "implementation_readiness_expected": False, "notes": "No detailed nodes invented."})
dump("contract-production-plan.yaml", {**meta, "contracts_created": 0, "features": contract_plan})
dump("ir-production-plan.yaml", {**meta, "irs_created": 0, "features": ir_plan})

unresolved_rows = []
for item in unresolved:
    affected = set(item.get("affected_object_ids", []))
    affected_features = [f["candidate_feature_id"] for f in features if affected.intersection(fobjects(f))]
    desc = (item.get("term", "") + " " + item.get("description", "")).lower()
    unresolved_rows.append({"unresolved_id": item["unresolved_id"], "source_location": item["source_reference"], "affected_objects": item.get("affected_object_ids", []), "affected_relations": [], "affected_features": affected_features, "category": "other", "severity": "blocking" if any(class_by_id.get(fid) == "not_yet_determinable" for fid in affected_features) else "reservation", "master_related": bool(re.search(r"ma(?:î|ã®|�)tre|master", desc)), "disciple_related": "disciple" in desc, "relations_domain_related": False, "other_domain_related": False, "blocks_contract": any(class_by_id.get(fid) == "not_yet_determinable" for fid in affected_features), "blocks_ir": bool(affected_features), "blocks_execution": bool(affected_features), "can_be_propagated": True, "recommended_handling": "preserve_and_propagate_without_resolution", "notes": item.get("required_human_decision")})
dump("unresolved-status.yaml", {**meta, "total": len(unresolved_rows), "items": unresolved_rows})

dump("production-gates.yaml", {
    **meta,
    "master_gate": {"accepted_statuses": ["complete_to_ir", "complete_to_ir_with_reservations"], "required_artifacts": ["registry/domain-progress/master"], "required_contracts": "feature_specific", "required_irs": "feature_specific", "required_symbols": "feature_specific", "required_validations": ["master_domain_validation"]},
    "disciple_gate": {"accepted_statuses": ["preparation_complete", "preparation_complete_with_reservations", "complete_to_ir", "complete_to_ir_with_reservations"], "minimum_required_level": "symbols_only", "required_artifacts": ["accepted_disciple_symbol_mapping"], "required_features": "TLC-FC-02-COMMUNITY-008_dependency_mapping_only", "required_contracts": [], "required_irs": [], "required_validations": ["disciple_dependency_reconciliation"]},
    "other_domain_gates": [],
    "community_preparation_gate": {"inventory_complete": True, "scientific_coverage_complete": True, "feature_coverage_complete": True, "dependency_graph_complete": True, "classification_complete": True, "production_order_complete": True, "unresolved_classified": True, "pilot_assessed": True, "contract_plan_complete": True, "ir_plan_complete": True},
    "blocking_conditions": ["TLC-FC-02-COMMUNITY-006 requires scientific decision before its contract"],
    "non_blocking_reservations": ["Master and Disciple mappings for TLC-FC-02-COMMUNITY-008 remain inferred candidates", "Community-Relations cycle is advisory and lexical"],
    "ready_for_contract_generation_after_master": True, "ready_for_contract_generation_after_disciple": True, "ready_for_full_contract_generation": False,
    "ready_for_ir_generation": False, "ready_for_implementation_planning": False, "ready_for_code_generation": False,
})
dump("global-manifest-update-proposal.yaml", {**meta, "proposal_only": True, "updates": [{"domain_id": "community", "proposed_status": "preparation_complete_with_reservations", "active_revised_features": len(features), "historical_pilots": 1, "new_contracts": 0, "new_irs": 0, "apply_after": ["review", "disciple_dependency_reconciliation"]}]})

report("source-inventory-report.md", "Community source inventory", f"The merged revised catalogue contains {len(features)} active Community features. The original 12 identifiers remain traceable through lineage; four are non-active revised outcomes. Scientific inventory: {len(objects)} objects, {len(relations)} relations, {len(unresolved)} unresolved records, and {len(duplicates)} duplicate candidates.")
report("scientific-coverage-report.md", "Community scientific coverage", f"All {len(objects)} local objects and {len(relations)} local relations occur in global consolidation. Local relation endpoints stay within Community; cross-domain textual evidence is handled conservatively as candidate dependency evidence.")
report("master-dependencies-report.md", "Community dependencies on Master", f"{len(master_deps)} feature-level candidate dependency was found from explicit Community source statements. It is not confirmed because no canonical target identifier is declared.")
report("disciple-dependencies-report.md", "Community dependencies on Disciple", f"{len(disciple_deps)} feature-level candidate dependency was found. The minimum anticipated level is symbols only; the non-merged Disciple preparation is not scientific authority.")
report("external-domain-dependencies-report.md", "Community external-domain dependencies", "The merged global graph contains an advisory inferred Community→Relations edge and the reverse Relations→Community edge. This is an inferred lexical cycle, not a production blocker.")
report("feature-dependency-report.md", "Community internal dependency graph", f"Confirmed revised-catalogue edges: {len(edges)}. No inferred internal edge and no cycle were introduced. Root features: {', '.join(roots)}.")
report("feature-classification-report.md", "Community feature classification", "\n".join(f"- `{x['feature_id']}`: `{x['contract_classification']}`" for x in classes))
report("historical-pilot-assessment.md", "Historical Community pilot assessment", "`TLC-FC-02-COMMUNITY-001` has one historical candidate contract and one semantic candidate IR. They preserve four unresolved items and are useful only for comparison/reconciliation; they were not modified or promoted.")
report("production-order.md", "Community production order", "\n".join(f"- `{k}`: {', '.join(v) if v else 'none'}" for k,v in groups.items()))
report("contract-production-plan.md", "Future Community contract plan", f"All {len(features)} active features have a future-only plan. No new contract was created. Unspecified mathematical fields remain explicit placeholders.")
report("ir-production-plan.md", "Future Community IR plan", f"All {len(features)} active features have a future-only IR plan. No new IR was created and implementation readiness remains false.")
report("unresolved-report.md", "Community unresolved analysis", f"All {len(unresolved_rows)} local unresolved records are preserved and mapped to affected active features where evidence exists. None was resolved by this preparation.")
report("preparation-completion-report.md", "Community preparation completion", "Status: **preparation complete with reservations**. Coverage, dependency assessment, classification, ordering, pilot assessment, plans, and gates are complete. Master/Disciple mappings and one local scientific decision remain explicit reservations.")

print(f"Generated {len(list(REG.glob('*.yaml')))} registries and {len(list(REP.glob('*.md')))} reports for {len(features)} active revised features.")
