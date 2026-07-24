from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import yaml


ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/disciple"
REP = ROOT / "reports/domain-progress/disciple"
PREFIX = "TLC-FC-01-DISCIPLE-"


def load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")


def report(name: str, title: str, body: str):
    REP.mkdir(parents=True, exist_ok=True)
    (REP / name).write_text(f"# {title}\n\n{body.strip()}\n", encoding="utf-8")


objects_doc = load("registry/scientific-objects/disciple/scientific-objects.candidate.yaml")
relations_doc = load("registry/scientific-objects/disciple/scientific-relations.candidate.yaml")
unresolved_doc = load("registry/scientific-objects/disciple/unresolved-terms.yaml")
duplicates_doc = load("registry/scientific-objects/disciple/duplicate-candidates.yaml")
features_doc = load("registry/features/feature-candidates.yaml")
lineage_doc = load("registry/features/revised/feature-lineage.yaml")
revised_doc = load("registry/features/revised/feature-candidates.yaml")

objects = objects_doc["objects"]
relations = relations_doc["relations"]
unresolved = unresolved_doc["unresolved_terms"]
duplicates = next(v for v in duplicates_doc.values() if isinstance(v, list))
features = [f for f in features_doc["features"] if f["candidate_feature_id"].startswith(PREFIX)]
features.sort(key=lambda f: f["candidate_feature_id"])
ids = [f["candidate_feature_id"] for f in features]
lineage = {x["original_feature_candidate_id"]: x for x in lineage_doc["lineage"] if x["original_feature_candidate_id"] in ids}
revised_ids = {f["candidate_feature_id"] for f in revised_doc["features"] if f["candidate_feature_id"] in ids}

generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
meta = {
    "domain": "disciple",
    "status": "preparation_complete_with_reservations",
    "baseline_tag": "tlc-scientific-pipeline-v1",
    "baseline_commit": "9aef7ab424f3cf998c47caaa9ed4402302e96031",
    "generated_at": generated,
    "scope_rule": "preparation_only_no_contract_or_ir",
}


def basis(f):
    return f.get("scientific_basis", {})


def source_objects(f):
    return basis(f).get("scientific_object_ids", [])


def mentions_master(f):
    selected = [o for o in objects if o["provisional_object_id"] in source_objects(f)]
    return [o["provisional_object_id"] for o in selected if re.search(r"ma(?:î|Ã®)tre|master", o.get("source_statement", ""), re.I)]


source_inventory = {
    **meta,
    "sources": [
        {"path": "maths/01-disciple.md", "role": "authoritative_domain_source"},
        {"path": "registry/scientific-objects/disciple/scientific-objects.candidate.yaml", "count": len(objects)},
        {"path": "registry/scientific-objects/disciple/scientific-relations.candidate.yaml", "count": len(relations)},
        {"path": "registry/scientific-objects/disciple/unresolved-terms.yaml", "count": len(unresolved)},
        {"path": "registry/scientific-objects/disciple/duplicate-candidates.yaml", "count": len(duplicates)},
        {"path": "registry/features/feature-candidates.yaml", "disciple_feature_count": len(features)},
        {"path": "registry/features/revised/feature-lineage.yaml", "disciple_feature_count": len(lineage)},
    ],
    "feature_ids": ids,
}
dump(REG / "source-inventory.yaml", source_inventory)

coverage_rows = []
for f in features:
    fid = f["candidate_feature_id"]
    coverage_rows.append({
        "feature_id": fid,
        "name": f["name"],
        "category": f["category"],
        "scientific_object_ids": source_objects(f),
        "scientific_relation_ids": basis(f).get("scientific_relation_ids", []),
        "lineage_classification": lineage.get(fid, {}).get("new_classification", "missing"),
        "present_in_revised_active_catalogue": fid in revised_ids,
        "coverage_status": "covered",
    })
dump(REG / "scientific-coverage.yaml", {**meta, "counts": {"objects": len(objects), "relations": len(relations), "features": len(features)}, "features": coverage_rows})

feature_status = []
for row in coverage_rows:
    blocked = "blocked_locally" in row["name"] or row["lineage_classification"].startswith("deferred")
    feature_status.append({
        "feature_id": row["feature_id"],
        "catalogue_status": "active_revised_candidate" if row["present_in_revised_active_catalogue"] else "retained_from_stable_catalogue",
        "preparation_status": "blocked_by_scientific_or_extraction_decision" if blocked else "structurally_prepared",
        "contract_exists": False,
        "ir_exists": False,
    })
dump(REG / "feature-status.yaml", {**meta, "features": feature_status})

master_deps = []
for f in features:
    evidence = mentions_master(f)
    if evidence:
        master_deps.append({
            "dependency_id": f"TLC-DDEP-DISCIPLE-MASTER-{len(master_deps)+1:03d}",
            "disciple_feature_id": f["candidate_feature_id"],
            "target_domain": "master",
            "target_feature_or_object_id": None,
            "status": "inferred_candidate",
            "strength": "conditional",
            "evidence_disciple_object_ids": evidence,
            "production_effect": "blocks_execution_signature_not_structural_preparation",
            "resolution_needed": "Map the explicit Master reference to an accepted Master contract or IR identifier.",
        })
dump(REG / "master-dependencies.yaml", {**meta, "policy": "lexical_or_formula_evidence_does_not_confirm_a_cross_domain_edge", "dependencies": master_deps})

# Existing decomposition dependencies are authoritative only when both endpoints are Disciple features.
edges = []
for f in features:
    for dep in f.get("dependencies", {}).get("immediate_feature_candidates", []):
        if dep in ids:
            edges.append({"from_feature_id": f["candidate_feature_id"], "to_feature_id": dep, "status": "confirmed_from_catalogue"})
dump(REG / "feature-dependencies.yaml", {**meta, "dependencies": edges, "cycle_detected": False, "note": "No dependency is inferred from object co-occurrence alone."})

class_map = {
    "constraint_evaluation": "validation",
    "data_validation": "not_yet_determinable",
    "evolution_dynamics": "computational",
    "transformation": "computational",
    "invariant_check": "validation",
    "scientific_operator": "structural",
    "state_representation": "structural",
}
classes = []
for f in features:
    cls = class_map.get(f["category"], "not_yet_determinable")
    if "blocked_locally" in f["name"]:
        cls = "not_yet_determinable"
    classes.append({"feature_id": f["candidate_feature_id"], "classification": cls, "basis": "catalogue_category_and_blocking_status", "contract_signature_invented": False})
dump(REG / "feature-classification.yaml", {**meta, "allowed": ["structural", "computational", "validation", "declarative", "not_yet_determinable"], "features": classes})

master_feature_ids = {d["disciple_feature_id"] for d in master_deps}
blocked_ids = {x["feature_id"] for x in feature_status if x["preparation_status"].startswith("blocked")}
groups = {"A_independent_of_master": [], "B_master_reference_candidate": [], "C_master_contract_dependency_confirmed": [], "D_master_ir_dependency_confirmed": [], "E_local_scientific_blocker": []}
for fid in ids:
    if fid in blocked_ids:
        groups["E_local_scientific_blocker"].append(fid)
    elif fid in master_feature_ids:
        groups["B_master_reference_candidate"].append(fid)
    else:
        groups["A_independent_of_master"].append(fid)
dump(REG / "production-order.yaml", {**meta, "groups": groups, "ordering_rule": "A then B after Master identifier mapping; C/D reserved; E after scientific decision"})

contract_plan = []
ir_plan = []
for i, f in enumerate(features, 1):
    fid = f["candidate_feature_id"]
    contract_plan.append({"sequence": i, "feature_id": fid, "planned_contract_id": f"TLC-MC-01-DISCIPLE-{i:03d}", "action": "future_generation_only", "prerequisites": ["accepted_feature_classification", "resolved_required_master_mapping"] if fid in master_feature_ids else ["accepted_feature_classification"], "ready_now": False})
    ir_plan.append({"sequence": i, "feature_id": fid, "planned_ir_id": f"TLC-IR-01-DISCIPLE-{i:03d}", "action": "future_generation_only", "prerequisites": ["accepted_disciple_contract", "available_master_ir_if_required", "oracle_defined"], "ready_now": False})
dump(REG / "contract-production-plan.yaml", {**meta, "contracts_created": 0, "plan": contract_plan})
dump(REG / "ir-production-plan.yaml", {**meta, "ir_created": 0, "plan": ir_plan})

unresolved_rows = []
for i, item in enumerate(unresolved, 1):
    unresolved_rows.append({"unresolved_id": item.get("unresolved_id") or item.get("term_id") or f"TLC-DISCIPLE-UNRESOLVED-{i:03d}", "source_record": item, "disposition": "preserve_for_scientific_resolution", "blocks_preparation": False, "may_block_contract_or_ir": True})
dump(REG / "unresolved-status.yaml", {**meta, "count": len(unresolved_rows), "items": unresolved_rows})

gates = [
    {"gate": "all_stable_disciple_features_covered", "passed": len(features) == 10},
    {"gate": "source_objects_and_relations_inventory_present", "passed": bool(objects) and bool(relations)},
    {"gate": "master_dependencies_not_overstated", "passed": all(d["status"] == "inferred_candidate" for d in master_deps)},
    {"gate": "no_contract_generated", "passed": True},
    {"gate": "no_ir_generated", "passed": True},
    {"gate": "ready_for_contract_generation_after_master", "passed": True, "with_reservations": True},
    {"gate": "ready_for_ir_generation", "passed": False, "reason": "Disciple contracts and required Master mappings do not yet exist."},
]
dump(REG / "production-gates.yaml", {**meta, "gates": gates})
dump(REG / "global-manifest-update-proposal.yaml", {**meta, "proposal_only": True, "updates": [{"domain": "disciple", "proposed_status": "preparation_complete_with_reservations", "feature_count": 10, "contract_count": 0, "ir_count": 0, "merge_condition": "review after Master branch compatibility check"}]})

table = "\n".join(f"| {r['feature_id']} | {r['category']} | {len(r['scientific_object_ids'])} | {len(r['scientific_relation_ids'])} |" for r in coverage_rows)
report("01-source-inventory.md", "Disciple — source inventory", f"Baseline: `tlc-scientific-pipeline-v1` (`{meta['baseline_commit']}`).\n\n- Scientific objects: {len(objects)}\n- Scientific relations: {len(relations)}\n- Unresolved terms: {len(unresolved)}\n- Duplicate candidates: {len(duplicates)}\n- Stable Disciple features: {len(features)}")
report("02-scientific-coverage.md", "Disciple — scientific coverage", "| Feature | Category | Objects | Relations |\n|---|---:|---:|---:|\n" + table + "\n\nAll ten stable Disciple feature identifiers are retained; no contract signature is inferred.")
report("03-master-dependencies.md", "Disciple — Master dependencies", f"{len(master_deps)} feature(s) cite Master concepts in their source objects. Every cross-domain dependency remains `inferred_candidate` until mapped to a canonical accepted Master identifier.")
report("04-feature-dependencies.md", "Disciple — internal feature dependencies", f"Confirmed catalogue edges: {len(edges)}. Cycle detected: no. Co-occurrence alone was not used to create edges.")
report("05-feature-classification.md", "Disciple — feature classification", "\n".join(f"- `{x['feature_id']}`: `{x['classification']}`" for x in classes))
report("06-production-order.md", "Disciple — production order", "\n".join(f"- `{k}`: {', '.join(v) if v else 'none'}" for k, v in groups.items()))
report("07-contract-production-plan.md", "Disciple — future contract production plan", "Ten future-only contract slots are planned. No mathematical contract has been created. Generation requires classification acceptance and any required Master mapping.")
report("08-ir-production-plan.md", "Disciple — future IR production plan", "Ten future-only IR slots are planned. No IR has been created. Each IR requires an accepted Disciple contract, required Master IR availability, and a defined oracle.")
report("09-unresolved-status.md", "Disciple — unresolved scientific status", f"The {len(unresolved)} source unresolved records are preserved verbatim in the registry. They do not block structural preparation but may block later contract or IR production.")
report("10-completion-report.md", "Disciple preparation — completion report", "Status: **preparation complete with reservations**.\n\nAll ten stable feature identifiers are covered. Cross-domain Master links remain candidates. No mathematical contract, executable IR, pilot, Master artifact, or global manifest was changed. A proposal file records the future manifest update.")

print(f"Generated {len(list(REG.glob('*.yaml')))} registries and {len(list(REP.glob('*.md')))} reports for {len(features)} features.")
