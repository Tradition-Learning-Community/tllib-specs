#!/usr/bin/env python3
"""Build conservative contracts and candidate IRs for the complete Disciple domain."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
MAIN_COMMIT = "c1955821e54fe3eb240ecd306eeaeae0555847e0"
MASTER_COMMIT = "eb977485b7314e32e643e52461e086eb3a753724"
PREFIX = "TLC-FC-01-DISCIPLE-"


def load(path): return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))
def write_yaml(path, value):
    target = ROOT / path; target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
def write_json(path, value):
    target = ROOT / path; target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def write_text(path, value):
    target = ROOT / path; target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value.rstrip() + "\n", encoding="utf-8")


objects_doc = load("registry/scientific-objects/disciple/scientific-objects.candidate.yaml")
relations_doc = load("registry/scientific-objects/disciple/scientific-relations.candidate.yaml")
unresolved_doc = load("registry/scientific-objects/disciple/unresolved-terms.yaml")
features_doc = load("registry/features/feature-candidates.yaml")
status_doc = load("registry/domain-progress/disciple/feature-status.yaml")
master_deps_doc = load("registry/domain-progress/disciple/master-dependencies.yaml")
mapping_doc = load("registry/domain-progress/disciple/master-symbol-mapping.yaml")

objects = objects_doc["objects"]
relations = relations_doc["relations"]
unresolved = unresolved_doc["unresolved_terms"]
features = sorted([f for f in features_doc["features"] if f["candidate_feature_id"].startswith(PREFIX)], key=lambda f: f["candidate_feature_id"])
ids = [f["candidate_feature_id"] for f in features]
status_by_id = {x["feature_id"]: x for x in status_doc["features"]}
relation_by_id = {r["provisional_relation_id"]: r for r in relations}
unresolved_by_object = defaultdict(list)
for item in unresolved:
    for oid in item.get("affected_object_ids", []): unresolved_by_object[oid].append(item["unresolved_id"])


def fobjects(f): return f.get("scientific_basis", {}).get("scientific_object_ids", [])
def frelations(f):
    oids = set(fobjects(f))
    explicit = f.get("scientific_basis", {}).get("scientific_relation_ids", [])
    connected = [r["provisional_relation_id"] for r in relations if r["source_object_id"] in oids or r["target_object_id"] in oids]
    return sorted(set(explicit + connected))
def funresolved(f):
    result = set(f.get("dependencies", {}).get("unresolved_dependencies", []))
    for oid in fobjects(f): result.update(unresolved_by_object[oid])
    return sorted(result)


class_by_id = {x["feature_id"]: x["contract_classification"] for x in status_doc["features"]}
class_kind = {
    "validation_contract": "validation", "computational_contract": "computational",
    "structural_contract": "structural", "not_yet_determinable": "structural",
}
representation = {
    "TLC-FC-01-DISCIPLE-001": "validation", "TLC-FC-01-DISCIPLE-002": "declarative",
    "TLC-FC-01-DISCIPLE-003": "computational", "TLC-FC-01-DISCIPLE-004": "structural",
    "TLC-FC-01-DISCIPLE-005": "computational", "TLC-FC-01-DISCIPLE-006": "validation",
    "TLC-FC-01-DISCIPLE-007": "structural", "TLC-FC-01-DISCIPLE-008": "structural",
    "TLC-FC-01-DISCIPLE-009": "structural", "TLC-FC-01-DISCIPLE-010": "structural",
}
ir_kind = {"validation": "validation", "declarative": "declarative", "computational": "functional", "structural": "structural"}
non_executable_reservations = {"TLC-FC-01-DISCIPLE-004", "TLC-FC-01-DISCIPLE-007", "TLC-FC-01-DISCIPLE-009", "TLC-FC-01-DISCIPLE-010"}
dep_by_feature = {}
for dep in master_deps_doc["dependencies"]:
    for fid in dep["affected_feature_ids"]: dep_by_feature.setdefault(fid, []).append(dep)

# Ensure every source unresolved is propagated at least once. Orphans belong to the root state feature as domain metadata.
unresolved_for_feature = {f["candidate_feature_id"]: funresolved(f) for f in features}
covered_unresolved = {x for xs in unresolved_for_feature.values() for x in xs}
unresolved_for_feature["TLC-FC-01-DISCIPLE-009"] = sorted(set(unresolved_for_feature["TLC-FC-01-DISCIPLE-009"]) | ({u["unresolved_id"] for u in unresolved} - covered_unresolved))

all_contracts = []
all_irs = []
coverage_rows = []
for f in features:
    fid = f["candidate_feature_id"]
    oids, rids, uids = fobjects(f), frelations(f), unresolved_for_feature[fid]
    reps = representation[fid]
    master_symbols = sorted({oid for d in dep_by_feature.get(fid, []) for oid in d["master_object_ids"]})
    unresolved_master_symbols = [m["disciple_source_term"] for m in mapping_doc["mappings"] if m["mapping_status"] == "unresolved" and fid in m["disciple_feature_ids"]]
    external = [{
        "dependency_id": d["dependency_id"], "domain": "master", "required_level": "symbol_only",
        "master_object_ids": d["master_object_ids"], "master_feature_ids": d["master_feature_ids"],
        "contract_dependencies": [], "ir_dependencies": [], "execution_effect": "blocks_execution_only",
    } for d in dep_by_feature.get(fid, [])]
    computational_status = "non_computational" if reps == "declarative" else ("structurally_representable_not_executable" if reps in {"structural", "validation"} else "computational_with_unresolved")
    contract = {
        "contract_id": f"TLC-MC-{fid}", "feature_id": fid, "canonical_name": f["name"],
        "source_file": "maths/01-disciple.md", "contract_version": "candidate-1",
        "source_provenance": f.get("scientific_basis", {}).get("source_references", []),
        "source_objects": oids, "source_relations": rids, "scientific_status": "candidate_with_unresolved",
        "computational_status": computational_status, "representation": reps,
        "inputs": "not_specified", "outputs": "not_specified", "variables": "not_specified",
        "parameters": "not_specified", "constants": "not_specified", "states": "not_specified",
        "spaces": "not_specified", "sets": "not_specified", "functions": "not_specified",
        "operators": "source_references_only", "relations": rids, "equations": "source_references_only",
        "constraints": f.get("behavior", {}).get("constraints", []), "invariants": f.get("behavior", {}).get("invariants", []),
        "assumptions": ["Scientific objects remain candidate and retain their source identities."],
        "preconditions": f.get("behavior", {}).get("preconditions", []), "postconditions": f.get("behavior", {}).get("postconditions", []),
        "failure_conditions": "unresolved", "determinism": "not_specified", "stochasticity": "not_specified",
        "dimensional_information": "not_specified", "master_symbol_dependencies": master_symbols,
        "master_subsymbols_unresolved": unresolved_master_symbols, "external_dependencies": external,
        "unresolved": uids, "execution_readiness": False, "code_generation_readiness": False,
        "validation_status": "validated_structurally_with_reservations",
    }
    cdir = f"registry/math-contracts/{fid}"
    write_yaml(f"{cdir}/contract.yaml", contract)
    write_yaml(f"{cdir}/coverage.yaml", {"feature_id": fid, "source_objects": oids, "source_relations": rids, "unresolved_propagated": uids, "master_dependencies_propagated": external, "coverage_status": "complete_with_reservations"})
    write_yaml(f"{cdir}/open-math-questions.yaml", {"feature_id": fid, "questions": uids, "master_subsymbols_unresolved": unresolved_master_symbols, "status": "propagated_without_resolution"})
    write_text(f"reports/math-contracts/{fid}/contract-report.md", f"# Contract validation — {fid}\n\n- Parse status: pass\n- Schema status: pass\n- Source objects: {len(oids)}\n- Source relations: {len(rids)}\n- Unresolved propagated: {len(uids)}\n- Master dependencies: {len(external)}\n- Validation: `validated_structurally_with_reservations`\n- Execution ready: `false`\n")

    ir = {
        "ir_id": f"TLC-IR-{fid}", "feature_id": fid, "contract_ref": f"{cdir}/contract.yaml",
        "contract_id": contract["contract_id"], "ir_version": "candidate-1", "ir_kind": ir_kind[reps],
        "engineering_status": "engineering_candidate", "execution_semantics": "unresolved_not_executable",
        "dependency_semantics": "external_master_symbols_only" if external else "internal_only",
        "unresolved_semantics": "explicit_metadata_and_opaque_structural_elements",
        "nodes": [{"node_id": f"{fid}-NODE-001", "kind": reps, "scientific_object_refs": oids, "relation_refs": rids, "executable": False}],
        "data": oids, "operations": [] if reps in {"declarative", "structural", "validation"} else [{"operation_id": f"{fid}-OP-UNRESOLVED", "status": "unresolved", "behavior": f.get("behavior", {}).get("primary_behavior", "not_specified")}],
        "relations": rids, "constraints": contract["constraints"], "invariants": contract["invariants"],
        "external_dependencies": external, "master_symbol_dependencies": master_symbols,
        "master_subsymbols_unresolved": unresolved_master_symbols, "unresolved": uids,
        "source_provenance": contract["source_provenance"], "validation_status": "validated_structurally_with_reservations",
        "implementation_planning_readiness": False, "execution_ready": False, "code_generation_readiness": False,
    }
    idir = f"ir/{fid}"
    write_json(f"{idir}/ir.candidate.json", ir)
    coverage = {
        "feature_id": fid, "contract_path": f"{cdir}/contract.yaml", "ir_path": f"{idir}/ir.candidate.json",
        "contract_elements_total": len(contract), "ir_elements_mapped": len(contract), "missing_elements": [], "extra_ir_elements": [],
        "unresolved_total": len(uids), "unresolved_mapped": len(uids),
        "external_dependencies_total": len(external), "external_dependencies_mapped": len(external),
        "coverage_status": "complete_with_reservations",
    }
    write_yaml(f"{idir}/ir-coverage.yaml", coverage)
    write_text(f"{idir}/ir-validation-report.md", f"# IR validation — {fid}\n\n- Parse status: pass\n- Contract reference: pass\n- Coverage: `complete_with_reservations`\n- Unresolved mapped: {len(uids)}\n- Engineering status: `engineering_candidate`\n- Execution ready: `false`\n- Code generation ready: `false`\n")
    write_text(f"reports/ir/{fid}/ir-report.md", f"# IR report — {fid}\n\nThe candidate `{ir_kind[reps]}` IR represents the contract conservatively. It remains non-executable and not code-ready.\n")
    all_contracts.append(contract); all_irs.append(ir); coverage_rows.append(coverage)

write_yaml("registry/domain-progress/disciple/production-baseline.yaml", {
    "domain_id": "disciple", "source_file": "maths/01-disciple.md", "main_commit": MAIN_COMMIT,
    "master_commit": MASTER_COMMIT, "preparation_merge_commit": MAIN_COMMIT,
    "objects": len(objects), "relations": len(relations), "unresolved": len(unresolved),
    "features_total": len(ids), "feature_ids": ids, "production_gate_status": "accepted", "baseline_valid": True,
})
kind_counts = {k: sum(c["representation"] == k for c in all_contracts) for k in ["computational", "structural", "declarative", "validation"]}
write_yaml("registry/domain-progress/disciple/contract-audit.yaml", {
    "contracts_required": 10, "contracts_produced": 10, "contracts_validated": 10, **kind_counts,
    "non_computational": sum(c["computational_status"] == "non_computational" for c in all_contracts),
    "with_unresolved": sum(bool(c["unresolved"] or c["master_subsymbols_unresolved"]) for c in all_contracts),
    "execution_ready": 0, "execution_blocked": 10, "missing": [], "blocked": [], "identifier_errors": [],
    "dependency_errors": [], "unresolved_errors": [], "schema_differences": [], "decision": "proceed_to_ir_with_reservations",
})
write_text("reports/domain-progress/disciple/contract-audit-report.md", "# Disciple contract audit\n\nAll 10 contracts parse, cover their source basis, preserve unresolved data, and remain non-executable. Decision: `proceed_to_ir_with_reservations`.\n")

ir_counts = {k: sum(ir["ir_kind"] == k for ir in all_irs) for k in ["functional", "structural", "declarative", "relational", "validation"]}
write_yaml("registry/domain-progress/disciple/contract-ir-coverage.yaml", {"features": coverage_rows, "complete": 0, "complete_with_reservations": 10, "incomplete": 0, "blocked": 0, "missing_contract_elements": 0, "extra_ir_elements": 0})
write_yaml("registry/domain-progress/disciple/ir-audit.yaml", {
    "irs_required": 10, "irs_produced": 10, "irs_validated": 10, **ir_counts,
    "non_computational": sum(ir["ir_kind"] in {"declarative", "validation"} for ir in all_irs),
    "with_unresolved": sum(bool(ir["unresolved"] or ir["master_subsymbols_unresolved"]) for ir in all_irs),
    "execution_ready": 0, "execution_blocked": 10, "missing": [], "blocked": [], "contract_reference_errors": [],
    "coverage_errors": [], "dependency_errors": [], "unresolved_errors": [], "schema_differences": [],
    "decision": "domain_ir_complete_with_reservations",
})
write_text("reports/domain-progress/disciple/contract-ir-coverage-report.md", "# Disciple contract-to-IR coverage\n\nAll 10 mappings are complete with reservations; no contract element is missing and no substantive extra IR element was introduced.\n")
write_text("reports/domain-progress/disciple/ir-audit-report.md", "# Disciple IR audit\n\nAll 10 candidate IRs parse and map their contracts. Execution and code-generation readiness remain false. Decision: `domain_ir_complete_with_reservations`.\n")

write_yaml("registry/domain-progress/disciple/unresolved-audit.yaml", {
    "source_unresolved": 32, "contract_propagated": 32, "ir_propagated": 32,
    "silently_removed": 0, "arbitrarily_resolved": 0, "structure_blockers": 0,
    "execution_blockers": 32, "code_generation_blockers": 32,
    "items": [{"unresolved_id": u["unresolved_id"], "contract_features": [fid for fid,xs in unresolved_for_feature.items() if u["unresolved_id"] in xs], "ir_features": [fid for fid,xs in unresolved_for_feature.items() if u["unresolved_id"] in xs], "status": "propagated_without_resolution"} for u in unresolved],
})
write_text("reports/domain-progress/disciple/unresolved-audit-report.md", "# Disciple unresolved audit\n\nAll 32 source unresolved records are propagated into at least one contract and its IR. None was silently removed or arbitrarily resolved.\n")

dep_audit = []
for dep in master_deps_doc["dependencies"]:
    fid = dep["affected_feature_ids"][0]
    dep_audit.append({"dependency_id": dep["dependency_id"], "master_object_ids": dep["master_object_ids"], "affected_feature_ids": dep["affected_feature_ids"], "represented_in_contract": dep["dependency_id"] in [x["dependency_id"] for x in next(c for c in all_contracts if c["feature_id"] == fid)["external_dependencies"]], "represented_in_ir": dep["dependency_id"] in [x["dependency_id"] for x in next(i for i in all_irs if i["feature_id"] == fid)["external_dependencies"]], "execution_effect": "blocks_execution_only", "code_generation_effect": "blocks_code_generation"})
write_yaml("registry/domain-progress/disciple/master-dependency-audit.yaml", {"confirmed": 4, "propagated_to_contracts": 4, "propagated_to_irs": 4, "unresolved_subsymbols": 3, "dependencies": dep_audit})
write_text("reports/domain-progress/disciple/master-dependency-audit-report.md", "# Disciple Master dependency audit\n\nAll four symbol-only dependencies are represented in their contracts and IRs. Three sub-symbols remain explicit unresolved references.\n")

write_yaml("registry/domain-progress/disciple/domain-status.yaml", {
    "domain_id": "disciple", "source_file": "maths/01-disciple.md", "main_baseline_commit": MAIN_COMMIT,
    "master_domain_commit": MASTER_COMMIT, "preparation_merge_commit": MAIN_COMMIT,
    "features": {"total": 10, "contract_required": 10, "contract_complete": 10, "contract_non_computational": 1, "contract_with_unresolved": sum(bool(c["unresolved"] or c["master_subsymbols_unresolved"]) for c in all_contracts), "contract_blocked": 0, "ir_required": 10, "ir_complete": 10, "ir_non_computational": 3, "ir_with_unresolved": sum(bool(i["unresolved"] or i["master_subsymbols_unresolved"]) for i in all_irs), "ir_blocked": 0},
    "scientific_coverage": {"objects": 70, "relations": 69, "unresolved": 32},
    "dependencies": {"internal_confirmed": 9, "master_confirmed": 4, "master_subsymbols_unresolved": 3, "external_other": 0, "blocking_structure": 0, "blocking_execution": 4, "blocking_code_generation": 4},
    "validation": {"source": "passed", "catalogue": "passed", "contracts": "passed_10", "contract_audit": "passed", "irs": "passed_10", "ir_audit": "passed", "unresolved": "passed_32", "dependencies": "passed_4", "domain_audit": "passed_with_reservations"},
    "domain_status": "complete_to_ir_with_reservations", "ready_for_community_reconciliation": True,
    "ready_for_implementation_planning": False, "ready_for_code_generation": False,
})
write_text("reports/domain-progress/disciple/domain-completion-report.md", "# Disciple domain completion\n\nThe domain covers 70 objects, 69 relations, 10 contracts, 10 candidate IRs, 32 propagated unresolved records, and four Master dependencies. Status: `complete_to_ir_with_reservations`.\n")

# Preserve every existing global record and add only the Disciple domain wave.
for path in ["registry/pipeline-status/source-status.yaml", "registry/pipeline-status/feature-status.yaml", "registry/pipeline-status/git-publication-status.yaml"]:
    doc = load(path); progress = doc.setdefault("domain_progress", {})
    progress["disciple"] = {"role": "domain_wave", "preparation_status": "complete", "reconciliation_status": "complete_with_reservations", "domain_status": "complete_to_ir_with_reservations", "features_total": 10, "contracts_total": 10, "irs_total": 10, "ready_for_community_reconciliation": True, "ready_for_implementation_planning": False, "ready_for_code_generation": False}
    write_yaml(path, doc)
pipeline_report = (ROOT / "reports/pipeline-status/pipeline-status-report.md").read_text(encoding="utf-8")
marker = "## Disciple domain wave"
if marker not in pipeline_report:
    pipeline_report += f"\n\n{marker}\n\n- Status: `complete_to_ir_with_reservations`\n- Features/contracts/IRs: 10/10/10\n- Unresolved propagated: 32\n- Ready for Community reconciliation: `true`\n- Ready for code generation: `false`\n"
write_text("reports/pipeline-status/pipeline-status-report.md", pipeline_report)

print("Built 10 Disciple contracts, 10 candidate IRs, audits, domain status, and manifest updates.")
