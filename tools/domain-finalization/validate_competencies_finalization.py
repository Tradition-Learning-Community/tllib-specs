from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError as exc:
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
DOMAIN = "competencies"
EXPECTED_COUNT = 13
FINAL_STATUS = "selected_for_competencies_implementation_specification"
RAW_IR_STATUS = "canonical_declarative_ir_with_reservations"
FEATURE_PREFIX = "TLC-FC-12-COMPETENCIES-"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_yaml(relative: str | Path) -> dict[str, Any]:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing file: {relative}")
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validator must aggregate diagnostics
        fail(f"invalid YAML {relative}: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(f"expected YAML mapping: {relative}")
        return {}
    return data


def require_keys(data: dict[str, Any], keys: list[str], label: str) -> None:
    for key in keys:
        if key not in data:
            fail(f"{label}: missing key {key}")


def input_record(data: dict[str, Any], name: str) -> dict[str, Any]:
    for item in data.get("inputs", []):
        if isinstance(item, dict) and item.get("name") == name:
            return item
    return {}


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode != 0:
        fail(f"git {' '.join(args)} failed: {result.stderr.strip()}")
        return []
    return [line for line in result.stdout.splitlines() if line]


def assert_false_mapping(mapping: Any, label: str) -> None:
    if not isinstance(mapping, dict):
        fail(f"{label}: expected mapping")
        return
    for key, value in mapping.items():
        if value is not False:
            fail(f"{label}.{key}: expected false, got {value!r}")


baseline = load_yaml("registry/global-reconciliation/current-baseline.yaml")
domain_matrix = load_yaml("registry/global-reconciliation/domain-feature-matrix.yaml")
manifest = load_yaml("registry/domain-finalization/competencies/manifest.yaml")
feature_status = load_yaml("registry/domain-finalization/competencies/feature-status.yaml")
patterns = load_yaml("registry/domain-finalization/competencies/patterns.yaml")
module_spec = load_yaml("registry/domain-finalization/competencies/module-specification.yaml")
tasks = load_yaml("registry/domain-finalization/competencies/implementation-tasks.yaml")
decisions = load_yaml("registry/domain-finalization/competencies/decision-required.yaml")

baseline_domain = next(
    (item for item in baseline.get("domains", []) if item.get("domain_id") == DOMAIN),
    None,
)
if baseline_domain is None:
    fail("baseline: competencies domain not found")
    baseline_domain = {}
for key in (
    "feature_count",
    "contracts_present",
    "ir_registry_entries_present",
    "ir_artifacts_present",
    "test_plans_present",
    "ir_layer_complete_features",
):
    if baseline_domain.get(key) != EXPECTED_COUNT:
        fail(f"baseline competencies {key}: expected 13, got {baseline_domain.get(key)!r}")
if baseline_domain.get("selection_statuses", {}).get(RAW_IR_STATUS) != EXPECTED_COUNT:
    fail("baseline: raw canonical declarative IR count is not 13")
if baseline_domain.get("normalized_selection_gate_passed_features") != 0:
    fail("baseline: normalized selection gate must remain unpassed")

matrix_rows = [row for row in domain_matrix.get("rows", []) if row.get("domain") == DOMAIN]
expected_features = [row.get("feature_id") for row in matrix_rows]
if len(expected_features) != EXPECTED_COUNT or len(set(expected_features)) != EXPECTED_COUNT:
    fail(f"domain matrix: expected 13 unique Competencies features, got {len(expected_features)}/{len(set(expected_features))}")
if any(not isinstance(fid, str) or not fid.startswith(FEATURE_PREFIX) for fid in expected_features):
    fail("domain matrix: invalid Competencies feature identifier")
for row in matrix_rows:
    fid = row.get("feature_id")
    for key in ("contract_present", "ir_registry_present", "ir_artifact_present", "test_plan_present", "ir_layer_complete"):
        if row.get(key) is not True:
            fail(f"domain matrix {fid}: {key} is not true")
    if row.get("selection_status") != RAW_IR_STATUS:
        fail(f"domain matrix {fid}: raw selection status changed")
    if row.get("normalized_selection_gate_passed") is not False:
        fail(f"domain matrix {fid}: normalized selection gate unexpectedly passed")
    if row.get("implementation_ready_asserted") is not False:
        fail(f"domain matrix {fid}: implementation readiness unexpectedly asserted")

manifest_features = manifest.get("population", {}).get("feature_ids", [])
status_features = [item.get("feature_id") for item in feature_status.get("features", [])]
operation_features = [item.get("feature_id") for item in module_spec.get("public_operations", [])]
task_features = [item.get("feature_id") for item in tasks.get("feature_tasks", [])]
for label, values in (
    ("manifest", manifest_features),
    ("feature-status", status_features),
    ("module public operations", operation_features),
    ("implementation tasks", task_features),
):
    if values != expected_features:
        fail(f"{label}: feature population or order differs from authoritative matrix")
if manifest.get("population", {}).get("expected_count") != EXPECTED_COUNT:
    fail("manifest: expected_count is not 13")
if manifest.get("raw_ir_status", {}).get("value") != RAW_IR_STATUS:
    fail("manifest: raw IR status not preserved")
if module_spec.get("feature_count") != EXPECTED_COUNT:
    fail("module specification: feature_count is not 13")
if feature_status.get("summary", {}).get("rejected_features") != 0:
    fail("feature-status: a feature is rejected")
if decisions.get("closure_blocked") is not False:
    fail("decision-required: structural closure is unexpectedly blocked")
if patterns.get("scientific_equivalence_claimed") is not False:
    fail("patterns: scientific equivalence was claimed")

status_by_feature = {item.get("feature_id"): item for item in feature_status.get("features", [])}
mandatory_final_ir_keys = [
    "feature_id",
    "status",
    "source_contract",
    "source_ir",
    "source_test_plan",
    "nature",
    "competency_or_reference",
    "identity",
    "scope",
    "context",
    "inputs",
    "outputs",
    "types",
    "opaque_values",
    "preconditions",
    "prerequisites_explicit",
    "application_conditions",
    "manifestations_explicit",
    "relations_explicit",
    "operations",
    "execution_order",
    "control_flow",
    "scientific_behaviors",
    "effects",
    "postconditions",
    "invariants",
    "errors",
    "determinism",
    "dependencies",
    "unresolved_propagated",
    "reservations",
    "transformations_applied",
    "preservation_obligations",
    "links",
    "actual_implementation_readiness",
]
mandatory_behaviors = ["mobilization", "exercise", "acquisition", "development", "mastery", "evaluation", "comparison"]

for row in matrix_rows:
    fid = row["feature_id"]
    source_contract_path = row["contract_ref"]
    source_ir_path = row["ir_artifact_ref"]
    source_test_path = row["test_plan_ref"]
    final_ir_path = f"registry/optimized-ir/competencies/{fid}/ir.yaml"
    algorithm_path = f"registry/algorithms/competencies/{fid}/algorithm.yaml"
    oracle_path = f"registry/oracles/competencies/{fid}/oracle.yaml"

    contract = load_yaml(source_contract_path)
    source_ir = load_yaml(source_ir_path)
    source_test = load_yaml(source_test_path)
    final_ir = load_yaml(final_ir_path)
    algorithm = load_yaml(algorithm_path)
    oracle = load_yaml(oracle_path)
    status_record = status_by_feature.get(fid, {})

    if contract.get("feature_id") != fid:
        fail(f"{fid}: source contract feature id mismatch")
    if source_ir.get("feature_id") != fid or source_ir.get("ir_kind") != RAW_IR_STATUS:
        fail(f"{fid}: source IR identity or raw status mismatch")
    if source_test.get("feature_id") != fid:
        fail(f"{fid}: source test plan feature id mismatch")
    if source_ir.get("contract_id") != contract.get("contract_id"):
        fail(f"{fid}: source IR contract id mismatch")
    if source_test.get("contract_id") != contract.get("contract_id") or source_test.get("ir_id") != source_ir.get("ir_id"):
        fail(f"{fid}: source test plan traceability mismatch")

    source_contract_objects = input_record(contract, "object_payloads").get("required_keys", [])
    source_ir_objects = input_record(source_ir, "object_payloads").get("required_keys", [])
    final_objects = final_ir.get("competency_or_reference", {}).get("ordered_object_ids", [])
    final_input_objects = input_record(final_ir, "object_payloads").get("required_keys", [])
    status_objects = status_record.get("object_ids", [])
    if not (source_contract_objects == source_ir_objects == final_objects == final_input_objects == status_objects):
        fail(f"{fid}: source/final object identity or order mismatch")

    require_keys(final_ir, mandatory_final_ir_keys, f"{fid} finalized IR")
    if final_ir.get("feature_id") != fid or final_ir.get("status") != FINAL_STATUS:
        fail(f"{fid}: finalized IR id or status mismatch")
    if final_ir.get("nature") != "declarative":
        fail(f"{fid}: declarative nature not preserved")
    if final_ir.get("source_contract", {}).get("path") != source_contract_path:
        fail(f"{fid}: finalized IR source contract path mismatch")
    if final_ir.get("source_ir", {}).get("path") != source_ir_path or final_ir.get("source_ir", {}).get("raw_status") != RAW_IR_STATUS:
        fail(f"{fid}: finalized IR source IR path or raw status mismatch")
    if final_ir.get("source_test_plan") != source_test_path:
        fail(f"{fid}: finalized IR source test plan mismatch")
    for flag, expected in (
        ("source_ir_preserved", True),
        ("source_contract_preserved", True),
        ("replaces_source_ir", False),
        ("scientific_source_modified", False),
        ("competency_invented", False),
        ("measurement_invented", False),
        ("ordering_invented", False),
    ):
        if final_ir.get(flag) is not expected:
            fail(f"{fid}: preservation flag {flag} expected {expected}")
    if final_ir.get("unresolved_propagated") != source_ir.get("propagated_unresolved", []):
        fail(f"{fid}: source unresolved not propagated exactly")
    if not final_ir.get("reservations"):
        fail(f"{fid}: reservations missing")
    for behavior in mandatory_behaviors:
        record = final_ir.get("scientific_behaviors", {}).get(behavior)
        if not isinstance(record, dict) or record.get("executable") is not False:
            fail(f"{fid}: scientific behavior {behavior} is missing or executable")
    if final_ir.get("effects") != []:
        fail(f"{fid}: side effects were introduced")
    readiness = final_ir.get("actual_implementation_readiness", {})
    if readiness.get("structural_descriptor") != "ready" or readiness.get("blocker_for_structural_layer") is not False:
        fail(f"{fid}: structural implementation readiness mismatch")
    if "not_" not in str(readiness.get("scientific_execution")) and "blocked" not in str(readiness.get("scientific_execution")):
        fail(f"{fid}: scientific execution is not explicitly unavailable")
    if final_ir.get("links", {}).get("algorithm") != algorithm_path or final_ir.get("links", {}).get("oracle") != oracle_path:
        fail(f"{fid}: finalized IR links mismatch")

    require_keys(algorithm, ["feature_id", "algorithm_id", "finalized_ir", "signature", "inputs", "outputs", "validations", "preconditions", "prerequisites", "conditions_of_application", "ordered_steps", "branches", "competency_construction", "identity_validation", "scope_validation", "context_validation", "relation_processing", "mobilization", "exercise", "acquisition", "development", "mastery", "evaluation", "comparison", "effects", "errors", "postconditions", "invariants", "determinism", "edge_cases", "dependencies", "unresolved_preserved", "pseudocode"], f"{fid} algorithm")
    if algorithm.get("feature_id") != fid or algorithm.get("finalized_ir") != final_ir_path:
        fail(f"{fid}: algorithm traceability mismatch")
    if algorithm.get("effects") != []:
        fail(f"{fid}: algorithm effects introduced")
    if not isinstance(algorithm.get("pseudocode"), str) or "construct_immutable_descriptor" not in algorithm.get("pseudocode", ""):
        fail(f"{fid}: directly implementable structural pseudocode missing")

    require_keys(oracle, ["feature_id", "oracle_id", "source_test_plan", "finalized_ir", "algorithm", "oracle_kind", "fixture_policy", "acceptance_tests", "blocked_tests", "acceptance_invariants", "dependency_tests", "no_invention"], f"{fid} oracle")
    if oracle.get("feature_id") != fid or oracle.get("source_test_plan") != source_test_path or oracle.get("finalized_ir") != final_ir_path or oracle.get("algorithm") != algorithm_path:
        fail(f"{fid}: oracle traceability mismatch")
    if not oracle.get("acceptance_tests"):
        fail(f"{fid}: oracle has no acceptance tests")
    assert_false_mapping(oracle.get("no_invention"), f"{fid} oracle no_invention")

    source_dependency = contract.get("capacities_dependency")
    if status_record.get("capacities_dependency") != source_dependency:
        fail(f"{fid}: dependency status changed")
    external_dependencies = final_ir.get("dependencies", {}).get("external", [])
    if source_dependency == "external_unreconciled":
        if not any(dep.get("domain") == "capacities" and dep.get("status") == "external_unreconciled" and dep.get("runtime_required") is False for dep in external_dependencies):
            fail(f"{fid}: external Capacities dependency not preserved as non-runtime")
    elif external_dependencies:
        fail(f"{fid}: an external execution/scientific dependency was added")

    if fid == "TLC-FC-12-COMPETENCIES-016":
        relation = final_ir.get("relations_explicit", {})
        if relation.get("relation_object_declared") is not True or relation.get("endpoints_declared_by_selected_contract") is not False or relation.get("endpoint_inference") != "forbidden":
            fail("feature 016: relation endpoint preservation mismatch")
        if contract.get("covered_relations") != []:
            fail("feature 016: source covered_relations unexpectedly non-empty")

allowed_prefixes = (
    "registry/domain-finalization/competencies/",
    "registry/optimized-ir/competencies/",
    "registry/algorithms/competencies/",
    "registry/oracles/competencies/",
    "reports/domain-finalization/competencies/",
)
allowed_exact = {"tools/domain-finalization/validate_competencies_finalization.py"}
if os.environ.get("COMPETENCIES_ALLOW_TEMPORARY_VALIDATION_FILES") == "1":
    allowed_exact.update({
        ".github/workflows/validate-competencies-finalization.yml",
        ".github/competencies-finalization.trigger",
    })
changed_paths = git_lines("diff", "--name-only", f"{BASE_SHA}..HEAD")
if not changed_paths:
    fail("git diff: no finalization artifacts detected")
for changed in changed_paths:
    if not (changed.startswith(allowed_prefixes) or changed in allowed_exact):
        fail(f"out-of-scope changed path: {changed}")
    if changed.startswith("maths/"):
        fail(f"scientific source modified: {changed}")
    if changed.startswith("registry/global-reconciliation/"):
        fail(f"global registry modified: {changed}")
    if changed.startswith(("registry/math-contracts/", "registry/ir/", "registry/test-plans/")):
        fail(f"source contract, IR or test plan modified: {changed}")
    if changed.endswith((".cpp", ".cc", ".cxx", ".hpp", ".hh", ".h")):
        fail(f"C++ artifact produced: {changed}")
    if changed.endswith(".py") and changed != "tools/domain-finalization/validate_competencies_finalization.py":
        fail(f"unexpected Python implementation or binding produced: {changed}")
    if any(token in changed for token in ("__pycache__", ".status", ".log", ".cache")):
        fail(f"temporary diagnostic artifact tracked: {changed}")

# git diff --check is part of the requested validation contract.
diff_check = subprocess.run(
    ["git", "diff", "--check", f"{BASE_SHA}..HEAD"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if diff_check.returncode != 0:
    fail(f"git diff --check failed:\n{diff_check.stdout}{diff_check.stderr}")

if ERRORS:
    print("COMPETENCIES FINALIZATION VALIDATION FAILED")
    for error in ERRORS:
        print(f"- {error}")
    raise SystemExit(1)

print("COMPETENCIES FINALIZATION VALIDATION PASSED")
print(f"base_sha={BASE_SHA}")
print(f"features={len(expected_features)}")
print("contracts=13 source_irs=13 source_test_plans=13")
print("finalized_irs=13 algorithms=13 oracles=13")
print("source_contracts_modified=false source_irs_modified=false maths_modified=false")
print("other_domains_modified=false global_registry_modified=false")
print("cpp=false python_bindings=false reference_implementation=false")
print("features_rejected=0")
