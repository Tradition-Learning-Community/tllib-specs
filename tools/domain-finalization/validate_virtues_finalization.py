#!/usr/bin/env python3
"""Validate the Virtues domain-finalization implementation package."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATUS = "selected_for_virtues_implementation_specification"
EXPECTED_IDS = [
    "TLC-FC-10-VIRTUES-001",
    "TLC-FC-10-VIRTUES-002",
    "TLC-FC-10-VIRTUES-005",
    "TLC-FC-10-VIRTUES-006",
    "TLC-FC-10-VIRTUES-007",
    "TLC-FC-10-VIRTUES-008",
    "TLC-FC-10-VIRTUES-009",
    "TLC-FC-10-VIRTUES-010",
    "TLC-FC-10-VIRTUES-011",
    "TLC-FC-10-VIRTUES-014",
]
EXPECTED_SET = set(EXPECTED_IDS)
FINAL_ROOT = ROOT / "registry/domain-finalization/virtues"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # validation must aggregate failures
        fail(f"cannot parse YAML {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(f"YAML root is not a mapping: {path.relative_to(ROOT)}")
        return {}
    return data


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")


def run_git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


# Required compact domain artifacts.
required_domain_files = [
    "manifest.yaml",
    "feature-status.yaml",
    "patterns.yaml",
    "module-specification.yaml",
    "implementation-tasks.yaml",
    "decision-required.yaml",
]
for name in required_domain_files:
    require_file(FINAL_ROOT / name)
require_file(ROOT / "reports/domain-finalization/virtues/finalization-report.md")

manifest = load_yaml(FINAL_ROOT / "manifest.yaml")
feature_status = load_yaml(FINAL_ROOT / "feature-status.yaml")
patterns = load_yaml(FINAL_ROOT / "patterns.yaml")
module = load_yaml(FINAL_ROOT / "module-specification.yaml")
tasks = load_yaml(FINAL_ROOT / "implementation-tasks.yaml")
decisions = load_yaml(FINAL_ROOT / "decision-required.yaml")

# Authoritative population from the current baseline and global matrices.
baseline = load_yaml(ROOT / "registry/global-reconciliation/current-baseline.yaml")
virtues_domains = [row for row in baseline.get("domains", []) if row.get("domain_id") == "virtues"]
if len(virtues_domains) != 1:
    fail(f"current baseline must contain exactly one virtues domain row, found {len(virtues_domains)}")
else:
    row = virtues_domains[0]
    for key in ("feature_count", "contracts_present", "ir_registry_entries_present", "ir_artifacts_present", "test_plans_present", "ir_layer_complete_features"):
        if row.get(key) != 10:
            fail(f"baseline virtues {key} must be 10, found {row.get(key)!r}")
    if row.get("ir_layer_complete") is not True:
        fail("baseline does not confirm a complete Virtues IR layer")

matrix = load_yaml(ROOT / "registry/global-reconciliation/domain-feature-matrix.yaml")
virtues_rows = [row for row in matrix if row.get("domain") == "virtues"] if isinstance(matrix, list) else [row for row in matrix.get("rows", []) if row.get("domain") == "virtues"]
matrix_ids = {row.get("feature_id") for row in virtues_rows}
if matrix_ids != EXPECTED_SET:
    fail(f"authoritative matrix population mismatch: {sorted(matrix_ids)}")
if len(virtues_rows) != 10:
    fail(f"authoritative matrix must contain 10 Virtues rows, found {len(virtues_rows)}")
for row in virtues_rows:
    for key in ("contract_present", "ir_registry_present", "ir_artifact_present", "test_plan_present", "ir_layer_complete"):
        if row.get(key) is not True:
            fail(f"{row.get('feature_id')} matrix field {key} is not true")

contract_matrix = load_yaml(ROOT / "registry/global-reconciliation/feature-contract-matrix.yaml")
contract_rows = [row for row in contract_matrix.get("rows", []) if row.get("domain") == "virtues"]
if {row.get("feature_id") for row in contract_rows} != EXPECTED_SET or len(contract_rows) != 10:
    fail("feature-contract matrix does not contain exactly the authoritative Virtues population")

ir_matrix = load_yaml(ROOT / "registry/global-reconciliation/feature-ir-matrix.yaml")
ir_rows = [row for row in ir_matrix.get("rows", []) if row.get("domain") == "virtues"]
if {row.get("feature_id") for row in ir_rows} != EXPECTED_SET or len(ir_rows) != 10:
    fail("feature-IR matrix does not contain exactly the authoritative Virtues population")

# Domain-wide population and preservation declarations.
if manifest.get("active_feature_count") != 10 or set(manifest.get("active_features", [])) != EXPECTED_SET:
    fail("manifest population is not the authoritative ten-feature set")
if manifest.get("status") != "ready_for_implementation_package":
    fail("manifest package status is not ready_for_implementation_package")
if manifest.get("selection_status") != STATUS:
    fail("manifest selection status is invalid")
for key, expected in {
    "source_ir_preserved": True,
    "source_contract_preserved": True,
    "scientific_source_modified": False,
    "feature_rejected": False,
    "global_registry_regenerated": False,
    "other_domain_artifacts_modified": False,
    "cpp_produced": False,
    "python_bindings_produced": False,
    "reference_implementation_produced": False,
}.items():
    if manifest.get(key) is not expected:
        fail(f"manifest preservation field {key} must be {expected}")
for key, value in manifest.get("non_invention", {}).items():
    if value is not False:
        fail(f"manifest non-invention field {key} must be false")

status_rows = feature_status.get("features", [])
if len(status_rows) != 10 or {row.get("feature_id") for row in status_rows} != EXPECTED_SET:
    fail("feature-status population mismatch")
if feature_status.get("no_feature_rejected") is not True:
    fail("feature-status must state that no feature was rejected")

module_ids = module.get("active_features", [])
public_ops = module.get("public_operations", [])
if len(module_ids) != 10 or set(module_ids) != EXPECTED_SET:
    fail("module population mismatch")
if len(public_ops) != 10 or {row.get("feature_id") for row in public_ops} != EXPECTED_SET:
    fail("module must expose exactly one public operation for each active feature")
if module.get("implementation_package_ready") is not True or module.get("status") != STATUS:
    fail("module is not marked ready with the selected status")
if module.get("comparisons", {}).get("public_operations") != []:
    fail("module invents or exposes a comparison operation")
if module.get("evaluation", {}).get("public_operations") != []:
    fail("module invents or exposes an evaluation operation")
if module.get("evolution", {}).get("public_operations") != []:
    fail("module invents or exposes an evolution operation")
for key, value in module.get("non_invention", {}).items():
    if value is not False:
        fail(f"module non-invention field {key} must be false")

feature_task_ids = {row.get("feature_id") for row in tasks.get("feature_tasks", [])}
if feature_task_ids != EXPECTED_SET or len(tasks.get("feature_tasks", [])) != 10:
    fail("implementation tasks do not cover exactly all active features")
if decisions.get("blocking") != [] or decisions.get("real_blockers_remaining") != []:
    fail("decision registry declares a blocking item")
if not patterns.get("shared_patterns"):
    fail("patterns registry is empty")

# Per-feature source and finalized artifact conformance.
for row in virtues_rows:
    feature_id = row["feature_id"]
    contract_path = ROOT / row["contract_ref"]
    source_ir_path = ROOT / row["ir_registry_ref"]
    test_plan_path = ROOT / row["test_plan_ref"]
    final_ir_path = ROOT / f"registry/optimized-ir/virtues/{feature_id}/ir.yaml"
    algorithm_path = ROOT / f"registry/algorithms/virtues/{feature_id}/algorithm.yaml"
    oracle_path = ROOT / f"registry/oracles/virtues/{feature_id}/oracle.yaml"
    for path in (contract_path, source_ir_path, test_plan_path, final_ir_path, algorithm_path, oracle_path):
        require_file(path)
    if not all(path.is_file() for path in (contract_path, source_ir_path, test_plan_path, final_ir_path, algorithm_path, oracle_path)):
        continue

    contract = load_yaml(contract_path)
    source_ir = load_yaml(source_ir_path)
    test_plan = load_yaml(test_plan_path)
    final_ir = load_yaml(final_ir_path)
    algorithm = load_yaml(algorithm_path)
    oracle = load_yaml(oracle_path)

    source_objects = contract.get("source_objects", [])
    source_unresolved = contract.get("unresolved_propagated", [])
    if contract.get("feature_id") != feature_id or source_ir.get("feature_id") != feature_id or test_plan.get("feature_id") != feature_id:
        fail(f"{feature_id}: source artifact feature-id mismatch")
    if source_ir.get("source_objects") != source_objects or test_plan.get("source_objects") != source_objects:
        fail(f"{feature_id}: source object mismatch among contract, IR, and test plan")
    if source_ir.get("unresolved_propagated", []) != source_unresolved:
        fail(f"{feature_id}: source contract and source IR unresolved mismatch")
    if source_ir.get("entrypoint") != test_plan.get("entrypoint"):
        fail(f"{feature_id}: source IR and source test-plan entrypoint mismatch")

    if final_ir.get("feature_id") != feature_id or final_ir.get("status") != STATUS:
        fail(f"{feature_id}: finalized IR identity or status mismatch")
    source = final_ir.get("source", {})
    if source.get("contract_ref") != row["contract_ref"]:
        fail(f"{feature_id}: finalized IR contract traceability mismatch")
    if source.get("source_ir_ref") != row["ir_registry_ref"]:
        fail(f"{feature_id}: finalized IR source-IR traceability mismatch")
    if source.get("test_plan_ref") != row["test_plan_ref"]:
        fail(f"{feature_id}: finalized IR source-test traceability mismatch")
    if source.get("source_objects") != source_objects:
        fail(f"{feature_id}: finalized IR source objects differ from contract")
    if source.get("source_ir_raw_status") != source_ir.get("status"):
        fail(f"{feature_id}: finalized IR raw source status mismatch")
    if final_ir.get("unresolved_propagated", []) != source_unresolved:
        fail(f"{feature_id}: finalized IR does not conserve source unresolved items exactly")
    for key, expected in {
        "source_ir_preserved": True,
        "source_contract_preserved": True,
        "replaces_source_ir": False,
        "scientific_source_modified": False,
        "virtue_invented": False,
        "measurement_invented": False,
        "ordering_invented": False,
    }.items():
        if final_ir.get(key) is not expected:
            fail(f"{feature_id}: finalized IR field {key} must be {expected}")
    if final_ir.get("comparisons") != []:
        fail(f"{feature_id}: finalized IR invents comparison behavior")
    if not final_ir.get("implementation_aptitude", {}).get("ready"):
        fail(f"{feature_id}: finalized IR is not apt for its bounded implementation")

    expected_algorithm_ref = f"registry/algorithms/virtues/{feature_id}/algorithm.yaml"
    expected_oracle_ref = f"registry/oracles/virtues/{feature_id}/oracle.yaml"
    expected_ir_ref = f"registry/optimized-ir/virtues/{feature_id}/ir.yaml"
    if final_ir.get("algorithm_ref") != expected_algorithm_ref or final_ir.get("oracle_ref") != expected_oracle_ref:
        fail(f"{feature_id}: finalized IR algorithm/oracle links are incoherent")
    if algorithm.get("feature_id") != feature_id or algorithm.get("status") != STATUS:
        fail(f"{feature_id}: algorithm identity or status mismatch")
    if algorithm.get("ir_ref") != expected_ir_ref or algorithm.get("entrypoint") != source_ir.get("entrypoint"):
        fail(f"{feature_id}: algorithm does not conform to finalized/source IR entrypoint")
    if algorithm.get("unresolved_conserved", []) != source_unresolved:
        fail(f"{feature_id}: algorithm unresolved conservation mismatch")
    if not algorithm.get("pseudocode"):
        fail(f"{feature_id}: algorithm has no pseudocode")
    if oracle.get("feature_id") != feature_id or oracle.get("status") != STATUS:
        fail(f"{feature_id}: oracle identity or status mismatch")
    if oracle.get("ir_ref") != expected_ir_ref or oracle.get("algorithm_ref") != expected_algorithm_ref:
        fail(f"{feature_id}: oracle IR/algorithm links are incoherent")
    if oracle.get("source_test_plan_ref") != row["test_plan_ref"] or oracle.get("entrypoint") != source_ir.get("entrypoint"):
        fail(f"{feature_id}: oracle source-test or entrypoint traceability mismatch")
    if oracle.get("unresolved_tests", {}).get("expected", []) != source_unresolved:
        fail(f"{feature_id}: oracle unresolved expectation mismatch")
    for required_section in ("acceptance_cases", "error_cases", "property_tests", "metamorphic_tests", "dependency_tests", "forbidden_outputs"):
        if not oracle.get(required_section):
            fail(f"{feature_id}: oracle section {required_section} is empty")

# Ensure there are no missing or additional feature directories.
for relative_root in ("registry/optimized-ir/virtues", "registry/algorithms/virtues", "registry/oracles/virtues"):
    root = ROOT / relative_root
    actual = {path.name for path in root.iterdir() if path.is_dir()} if root.is_dir() else set()
    if actual != EXPECTED_SET:
        fail(f"{relative_root} directory population mismatch: {sorted(actual)}")

# Validate all newly introduced YAML documents.
for root in (
    ROOT / "registry/domain-finalization/virtues",
    ROOT / "registry/optimized-ir/virtues",
    ROOT / "registry/algorithms/virtues",
    ROOT / "registry/oracles/virtues",
):
    for path in root.rglob("*.yaml"):
        load_yaml(path)

# Git diff scope and source-preservation checks.
base = manifest.get("main_head")
if not isinstance(base, str) or len(base) < 7:
    fail("manifest main_head is missing or invalid")
else:
    diff = run_git("diff", "--name-only", f"{base}...HEAD")
    if diff.returncode != 0:
        fail(f"cannot inspect changed paths: {diff.stderr.strip()}")
        changed_paths: list[str] = []
    else:
        changed_paths = [line.strip() for line in diff.stdout.splitlines() if line.strip()]
    allowed_prefixes = (
        "registry/domain-finalization/virtues/",
        "registry/optimized-ir/virtues/",
        "registry/algorithms/virtues/",
        "registry/oracles/virtues/",
        "reports/domain-finalization/virtues/",
    )
    allowed_exact = {
        "tools/domain-finalization/validate_virtues_finalization.py",
        ".github/workflows/validate-virtues-finalization-temp.yml",
    }
    for path in changed_paths:
        if path not in allowed_exact and not path.startswith(allowed_prefixes):
            fail(f"modified path is outside Virtues finalization scope: {path}")
        if path.startswith("maths/"):
            fail(f"scientific source modified: {path}")
        if path.startswith("registry/global-reconciliation/"):
            fail(f"global registry modified: {path}")
        if path.startswith(("registry/math-contracts/", "registry/ir/", "registry/test-plans/")):
            fail(f"source contract, IR, or test plan modified: {path}")
        suffix = Path(path).suffix.lower()
        if suffix in {".cpp", ".cc", ".cxx", ".h", ".hh", ".hpp", ".pyi"}:
            fail(f"forbidden implementation or binding file introduced: {path}")
        lowered = path.lower()
        if "reference-implementation" in lowered or "reference_implementation" in lowered or "/bindings/" in lowered:
            fail(f"forbidden reference implementation or binding path introduced: {path}")

    diff_check = run_git("diff", "--check", f"{base}...HEAD")
    if diff_check.returncode != 0:
        fail(f"git diff --check failed:\n{diff_check.stdout}{diff_check.stderr}")

if ERRORS:
    print("VIRTUES FINALIZATION VALIDATION FAILED")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print(
    "VIRTUES FINALIZATION VALIDATION PASSED: exactly 10 active features; "
    "10 preserved source contracts; 10 preserved source IRs; 10 source test plans; "
    "10 finalized IRs; 10 algorithms; 10 oracles; complete traceability; "
    "no rejected feature, invented scientific behavior, source modification, global-registry change, "
    "other-domain change, C++ code, Python binding, or reference implementation."
)
