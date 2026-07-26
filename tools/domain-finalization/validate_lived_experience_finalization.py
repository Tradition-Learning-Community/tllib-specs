#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
EXPECTED = [
    "TLC-FC-14-LIVED-EXPERIENCE-001", "TLC-FC-14-LIVED-EXPERIENCE-002",
    "TLC-FC-14-LIVED-EXPERIENCE-004", "TLC-FC-14-LIVED-EXPERIENCE-005",
    "TLC-FC-14-LIVED-EXPERIENCE-006", "TLC-FC-14-LIVED-EXPERIENCE-007",
    "TLC-FC-14-LIVED-EXPERIENCE-008", "TLC-FC-14-LIVED-EXPERIENCE-009",
    "TLC-FC-14-LIVED-EXPERIENCE-010", "TLC-FC-14-LIVED-EXPERIENCE-011",
    "TLC-FC-14-LIVED-EXPERIENCE-012", "TLC-FC-14-LIVED-EXPERIENCE-013",
]
FLAGS = {
    "source_ir_preserved": True, "source_contract_preserved": True,
    "replaces_source_ir": False, "scientific_source_modified": False,
    "experience_invented": False, "event_invented": False,
    "state_invented": False, "chronology_invented": False,
    "interpretation_invented": False, "causality_invented": False,
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(path: str) -> dict[str, Any]:
    target = ROOT / path
    if not target.is_file():
        fail(f"missing file: {path}")
    try:
        data = yaml.safe_load(target.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"YAML parse failure in {path}: {exc}")
    if not isinstance(data, dict):
        fail(f"expected mapping in {path}")
    return data


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        fail(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


matrix = load("registry/global-reconciliation/domain-feature-matrix.yaml")
rows = [row for row in matrix.get("rows", []) if row.get("domain") == "lived-experience"]
population = [row.get("feature_id") for row in rows]
if population != EXPECTED or len(population) != 12:
    fail(f"authoritative population mismatch: {population}")
row_by_id = {row["feature_id"]: row for row in rows}

manifest = load("registry/domain-finalization/lived-experience/manifest.yaml")
if manifest.get("feature_count") != 12 or manifest.get("features") != EXPECTED:
    fail("manifest population mismatch")
status = load("registry/domain-finalization/lived-experience/feature-status.yaml")
if [item.get("feature_id") for item in status.get("features", [])] != EXPECTED:
    fail("feature-status population mismatch")
if any(item.get("rejected") for item in status.get("features", [])):
    fail("a feature was rejected")
module = load("registry/domain-finalization/lived-experience/module-specification.yaml")
if module.get("feature_count") != 12:
    fail("module feature count mismatch")
tasks = load("registry/domain-finalization/lived-experience/implementation-tasks.yaml")
if len(tasks.get("feature_tasks", [])) != 12:
    fail("implementation task count mismatch")
decisions = load("registry/domain-finalization/lived-experience/decision-required.yaml")
if decisions.get("package_blockers") or decisions.get("real_remaining_blocker_count_for_structural_package") != 0:
    fail("unexpected structural package blocker")
load("registry/domain-finalization/lived-experience/patterns.yaml")

for feature_id in EXPECTED:
    row = row_by_id[feature_id]
    contract = load(row["contract_ref"])
    source_ir = load(row["ir_registry_ref"])
    load(row["test_plan_ref"])
    object_ids = [obj["object_id"] for obj in contract.get("covered_objects", [])]
    ir_path = f"registry/optimized-ir/lived-experience/{feature_id}/ir.yaml"
    algorithm_path = f"registry/algorithms/lived-experience/{feature_id}/algorithm.yaml"
    oracle_path = f"registry/oracles/lived-experience/{feature_id}/oracle.yaml"
    final_ir = load(ir_path)
    algorithm = load(algorithm_path)
    oracle = load(oracle_path)
    for label, artifact in [("IR", final_ir), ("algorithm", algorithm), ("oracle", oracle)]:
        if artifact.get("feature_id") != feature_id:
            fail(f"{feature_id}: {label} feature mismatch")
        if artifact.get("status") != "selected_for_lived_experience_implementation_specification":
            fail(f"{feature_id}: {label} status mismatch")
    if final_ir.get("source_contract_ref") != row["contract_ref"]:
        fail(f"{feature_id}: contract traceability mismatch")
    if final_ir.get("source_ir_ref") != row["ir_registry_ref"]:
        fail(f"{feature_id}: IR traceability mismatch")
    if final_ir.get("source_test_plan_ref") != row["test_plan_ref"]:
        fail(f"{feature_id}: test-plan traceability mismatch")
    if final_ir.get("source_ir_raw_status") != row.get("selection_status"):
        fail(f"{feature_id}: raw selection status not preserved")
    if final_ir.get("source_ir_kind") != source_ir.get("ir_kind"):
        fail(f"{feature_id}: source IR kind not preserved")
    if final_ir.get("identity", {}).get("ordered_object_ids") != object_ids:
        fail(f"{feature_id}: identity/object order mismatch")
    if final_ir.get("experience", {}).get("ordered_object_ids") != object_ids:
        fail(f"{feature_id}: experience reference mismatch")
    if final_ir.get("order", {}).get("covered_object_order") != object_ids:
        fail(f"{feature_id}: covered-object order mismatch")
    if final_ir.get("order", {}).get("temporal_order"):
        fail(f"{feature_id}: temporal order invented")
    source_relations = list(contract.get("covered_relations", []) or []) + list(contract.get("contextual_relations", []) or [])
    if final_ir.get("relations_explicitly_defined", []) != source_relations:
        fail(f"{feature_id}: relation mismatch")
    for field in ["actors_explicitly_defined", "events_explicitly_defined", "states_explicitly_defined", "transitions_explicitly_defined", "observations_explicitly_defined", "perceptions_explicitly_defined", "interpretations_explicitly_defined", "results_explicitly_defined", "effects_explicitly_defined"]:
        if final_ir.get(field):
            fail(f"{feature_id}: undeclared semantic content in {field}")
    if not set(source_ir.get("propagated_unresolved", []) or []).issubset(set(final_ir.get("unresolved_propagated", []) or [])):
        fail(f"{feature_id}: source unresolved removed")
    if not set(source_ir.get("propagated_reservations", []) or []).issubset(set(final_ir.get("reservations", []) or [])):
        fail(f"{feature_id}: source reservation removed")
    for key, expected in FLAGS.items():
        if final_ir.get(key) is not expected:
            fail(f"{feature_id}: flag {key} mismatch")
    if final_ir.get("algorithm_ref") != algorithm_path or final_ir.get("oracle_ref") != oracle_path:
        fail(f"{feature_id}: IR links mismatch")
    if algorithm.get("finalized_ir_ref") != ir_path:
        fail(f"{feature_id}: algorithm link mismatch")
    if oracle.get("finalized_ir_ref") != ir_path or oracle.get("algorithm_ref") != algorithm_path:
        fail(f"{feature_id}: oracle links mismatch")
    if final_ir.get("implementation_aptitude", {}).get("production_readiness_asserted") is not False:
        fail(f"{feature_id}: production readiness asserted")

for folder, filename in [("registry/optimized-ir/lived-experience", "ir.yaml"), ("registry/algorithms/lived-experience", "algorithm.yaml"), ("registry/oracles/lived-experience", "oracle.yaml")]:
    actual = sorted(str(path.relative_to(ROOT)) for path in (ROOT / folder).glob(f"*/{filename}"))
    if len(actual) != 12:
        fail(f"{folder}: expected 12 artifacts, found {len(actual)}")

changed = set(filter(None, git("diff", "--name-only", f"{BASE}...HEAD").splitlines()))
allowed_prefixes = (
    "registry/domain-finalization/lived-experience/",
    "registry/optimized-ir/lived-experience/",
    "registry/algorithms/lived-experience/",
    "registry/oracles/lived-experience/",
    "reports/domain-finalization/lived-experience/",
)
allowed_exact = {"tools/domain-finalization/validate_lived_experience_finalization.py"}
if os.environ.get("ALLOW_TEMP_WORKFLOW") == "1":
    allowed_exact.add(".github/workflows/lived-experience-finalization-bootstrap.yml")
illegal = sorted(path for path in changed if path not in allowed_exact and not path.startswith(allowed_prefixes))
if illegal:
    fail(f"paths outside scope: {illegal}")
if any(path.startswith("maths/") for path in changed):
    fail("maths/ modification detected")
if any(path.startswith("registry/global-reconciliation/") for path in changed):
    fail("global registry modification detected")
if any(path.endswith((".cpp", ".cc", ".cxx", ".hpp", ".hxx", ".pyi")) for path in changed):
    fail("C++ or binding artifact detected")
if any("reference_implementation" in path or "reference-implementation" in path or "bindings/python" in path for path in changed):
    fail("reference implementation or Python binding detected")
if any("__pycache__" in path or path.endswith(".status") or path.endswith(".log") for path in changed):
    fail("temporary artifact detected")

constraints = manifest.get("constraints", {})
expected_constraints = {
    "source_contracts_preserved": True, "source_irs_preserved": True,
    "maths_preserved": True, "other_domains_modified": False,
    "global_registry_regenerated": False, "cpp_produced": False,
    "python_bindings_produced": False, "reference_implementation_produced": False,
    "features_rejected": 0,
}
for key, expected in expected_constraints.items():
    if constraints.get(key) != expected:
        fail(f"manifest constraint mismatch: {key}")

subprocess.run(["git", "diff", "--check", f"{BASE}...HEAD"], cwd=ROOT, check=True)
print("Lived Experience finalization validation passed")
print("features=12 finalized_ir=12 algorithms=12 oracles=12")
print(f"changed_paths={len(changed)}")
