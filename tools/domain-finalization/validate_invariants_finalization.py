#!/usr/bin/env python3
"""Validate the complete Invariants domain-finalization specification package."""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml


ROOT = Path(__file__).resolve().parents[2]
PREFIX = "TLC-FC-04-INVARIANTS-"
BASELINE = ROOT / "registry/global-reconciliation/current-baseline.yaml"
DOMAIN_MATRIX = ROOT / "registry/global-reconciliation/domain-feature-matrix.yaml"
FINAL = ROOT / "registry/domain-finalization/invariants"
OPTIMIZED = ROOT / "registry/optimized-ir/invariants"
ALGORITHMS = ROOT / "registry/algorithms/invariants"
ORACLES = ROOT / "registry/oracles/invariants"
REPORT = ROOT / "reports/domain-finalization/invariants/finalization-report.md"
errors: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_yaml(path: Path) -> Any:
    if not path.exists():
        errors.append(f"Missing YAML: {rel(path)}")
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        errors.append(f"YAML parse failure: {rel(path)}: {exc}")
        return {}


def load_json(path: Path) -> Any:
    if not path.exists():
        errors.append(f"Missing JSON: {rel(path)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        errors.append(f"JSON parse failure: {rel(path)}: {exc}")
        return {}


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def mapping_by_feature(data: Any) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for node in walk(data):
        if isinstance(node, dict):
            feature_id = node.get("feature_id")
            if isinstance(feature_id, str) and feature_id.startswith(PREFIX):
                result[feature_id] = node
    return result


def source_precondition_ids(source_ir: dict[str, Any]) -> set[str]:
    return {
        item.get("id")
        for item in list_value(source_ir.get("preconditions"))
        if isinstance(item, dict) and item.get("id")
    }


def final_precondition_ids(final_ir: dict[str, Any]) -> set[str]:
    return {
        item.get("id")
        for item in list_value(final_ir.get("preconditions"))
        if isinstance(item, dict) and item.get("id")
    }


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)


# Parse authoritative baseline and population.
baseline_data = load_yaml(BASELINE)
matrix_data = load_yaml(DOMAIN_MATRIX)
expected_features = sorted(
    {
        node["feature_id"]
        for node in walk(matrix_data)
        if isinstance(node, dict)
        and node.get("domain") == "invariants"
        and isinstance(node.get("feature_id"), str)
        and node["feature_id"].startswith(PREFIX)
    }
)
if not expected_features:
    # Support matrices with a parent domain node and child feature records.
    for node in walk(matrix_data):
        if isinstance(node, dict) and node.get("domain") == "invariants":
            expected_features.extend(
                child["feature_id"]
                for child in walk(node)
                if isinstance(child, dict)
                and isinstance(child.get("feature_id"), str)
                and child["feature_id"].startswith(PREFIX)
            )
    expected_features = sorted(set(expected_features))

baseline_counts = {
    int(node["feature_count"])
    for node in walk(baseline_data)
    if isinstance(node, dict)
    and node.get("domain") == "invariants"
    and isinstance(node.get("feature_count"), int)
}
if len(baseline_counts) != 1:
    errors.append(f"Expected one Invariants baseline feature_count, found {sorted(baseline_counts)}")
    baseline_count = None
else:
    baseline_count = next(iter(baseline_counts))

if len(expected_features) != len(set(expected_features)):
    errors.append("Duplicate feature IDs in authoritative Invariants population")
if baseline_count is not None and len(expected_features) != baseline_count:
    errors.append(
        f"Authoritative population mismatch: matrix has {len(expected_features)}, baseline has {baseline_count}"
    )
if baseline_count == 10 and len(expected_features) != 10:
    errors.append("Baseline confirms 10 Invariants features but authoritative population is not exactly 10")
if expected_features != [f"{PREFIX}{index:03d}" for index in range(1, 11)]:
    errors.append(f"Unexpected Invariants population: {expected_features}")

# Required domain-level artifacts.
required_domain_files = [
    FINAL / "manifest.yaml",
    FINAL / "feature-status.yaml",
    FINAL / "patterns.yaml",
    FINAL / "module-specification.yaml",
    FINAL / "implementation-tasks.yaml",
    FINAL / "decision-required.yaml",
    REPORT,
    Path(__file__).resolve(),
]
for path in required_domain_files:
    if not path.exists():
        errors.append(f"Missing required artifact: {rel(path)}")

manifest = load_yaml(FINAL / "manifest.yaml")
feature_status = load_yaml(FINAL / "feature-status.yaml")
patterns = load_yaml(FINAL / "patterns.yaml")
module = load_yaml(FINAL / "module-specification.yaml")
tasks = load_yaml(FINAL / "implementation-tasks.yaml")
decisions = load_yaml(FINAL / "decision-required.yaml")

manifest_population = sorted(manifest.get("authoritative_population", {}).get("feature_ids", []))
if manifest_population != expected_features:
    errors.append("Manifest population does not equal authoritative baseline population")
status_map = mapping_by_feature(feature_status)
if sorted(status_map) != expected_features:
    errors.append("Finalized feature-status population is incomplete or contains additions")
if feature_status.get("population_count") != len(expected_features):
    errors.append("Finalized feature-status population_count is inconsistent")
if decisions.get("blocking_count") != 0 or decisions.get("blocking_decisions") not in ([], None):
    errors.append("Decision registry claims a blocking decision")
if decisions.get("closure", {}).get("observable_behavior_defined_for_all_features") is not True:
    errors.append("Decision registry does not close observable behavior for all features")

module_features = sorted(module.get("active_features", []))
if module_features != expected_features:
    errors.append("Module specification active feature population is inconsistent")
public_ops = mapping_by_feature(module.get("public_operations", []))
if sorted(public_ops) != expected_features:
    errors.append("Module specification does not expose exactly one public operation per feature")

# Exact per-feature source and finalized package validation.
optimized_dirs = sorted(path.name for path in OPTIMIZED.glob(f"{PREFIX}*") if path.is_dir())
algorithm_dirs = sorted(path.name for path in ALGORITHMS.glob(f"{PREFIX}*") if path.is_dir())
oracle_dirs = sorted(path.name for path in ORACLES.glob(f"{PREFIX}*") if path.is_dir())
for label, actual in (
    ("optimized IR", optimized_dirs),
    ("algorithm", algorithm_dirs),
    ("oracle", oracle_dirs),
):
    if actual != expected_features:
        errors.append(f"{label} directories differ from authoritative population: {actual}")

for feature_id in expected_features:
    contract_path = ROOT / f"registry/math-contracts/{feature_id}/contract.yaml"
    traceability_path = ROOT / f"registry/math-contracts/{feature_id}/traceability.yaml"
    source_ir_path = ROOT / f"ir/{feature_id}/ir.prototype.json"
    source_test_path = ROOT / f"ir/{feature_id}/test-plan.yaml"
    final_ir_path = OPTIMIZED / feature_id / "ir.yaml"
    algorithm_path = ALGORITHMS / feature_id / "algorithm.yaml"
    oracle_path = ORACLES / feature_id / "oracle.yaml"

    contract = load_yaml(contract_path)
    traceability = load_yaml(traceability_path)
    source_ir = load_json(source_ir_path)
    source_test = load_yaml(source_test_path)
    final_ir = load_yaml(final_ir_path)
    algorithm = load_yaml(algorithm_path)
    oracle = load_yaml(oracle_path)

    for label, document in (
        ("contract", contract),
        ("traceability", traceability),
        ("source IR", source_ir),
        ("source test plan", source_test),
        ("final IR", final_ir),
        ("algorithm", algorithm),
        ("oracle", oracle),
    ):
        if document.get("feature_id") != feature_id:
            errors.append(f"{feature_id}: {label} feature_id mismatch")

    status_entry = status_map.get(feature_id, {})
    if status_entry.get("finalization_status") != "selected_for_invariants_implementation_specification":
        errors.append(f"{feature_id}: incorrect finalization status")
    if status_entry.get("rejected_by_finalization") is not False:
        errors.append(f"{feature_id}: feature was rejected or rejection state is missing")
    if status_entry.get("source_contract") != rel(contract_path):
        errors.append(f"{feature_id}: source contract path mismatch in feature status")
    if status_entry.get("source_ir") != rel(source_ir_path):
        errors.append(f"{feature_id}: source IR path mismatch in feature status")
    if status_entry.get("source_test_plan") != rel(source_test_path):
        errors.append(f"{feature_id}: source test-plan path mismatch in feature status")

    required_ir_keys = {
        "feature_id", "source_contract_ref", "source_ir_ref", "source_ir_raw_status", "nature",
        "invariant_referenced", "scope", "inputs", "outputs", "types", "opaque_values",
        "preconditions", "conditions_of_application", "operations", "execution_order", "control_flow",
        "state_before", "state_after", "effects", "postconditions", "conditions_of_conservation",
        "conditions_of_violation", "errors", "determinism", "dependencies", "unresolved_propagated",
        "reservations", "transformations_applied", "obligations_of_preservation", "algorithm_ref",
        "oracle_ref", "implementation_aptitude", "source_ir_preserved", "source_contract_preserved",
        "replaces_source_ir", "scientific_source_modified",
    }
    missing_ir_keys = sorted(required_ir_keys - set(final_ir))
    if missing_ir_keys:
        errors.append(f"{feature_id}: finalized IR missing keys {missing_ir_keys}")
    if final_ir.get("status") != "selected_for_invariants_implementation_specification":
        errors.append(f"{feature_id}: finalized IR status is incorrect")
    if final_ir.get("source_ir_raw_status") != source_ir.get("ir_kind"):
        errors.append(f"{feature_id}: source IR raw status not preserved")
    if final_ir.get("source_catalogue_status") != source_ir.get("catalogue_status_preserved"):
        errors.append(f"{feature_id}: source catalogue status not preserved")
    if final_ir.get("source_contract_ref") != rel(contract_path):
        errors.append(f"{feature_id}: finalized IR contract reference mismatch")
    if final_ir.get("source_ir_ref") != rel(source_ir_path):
        errors.append(f"{feature_id}: finalized IR source reference mismatch")
    if final_ir.get("source_ir_preserved") is not True:
        errors.append(f"{feature_id}: source_ir_preserved must be true")
    if final_ir.get("source_contract_preserved") is not True:
        errors.append(f"{feature_id}: source_contract_preserved must be true")
    if final_ir.get("replaces_source_ir") is not False:
        errors.append(f"{feature_id}: replaces_source_ir must be false")
    if final_ir.get("scientific_source_modified") is not False:
        errors.append(f"{feature_id}: scientific_source_modified must be false")

    if not source_precondition_ids(source_ir).issubset(final_precondition_ids(final_ir)):
        errors.append(f"{feature_id}: source precondition IDs were not conserved")
    source_unresolved = sorted(source_ir.get("unresolved_propagated", []))
    final_unresolved = sorted(final_ir.get("unresolved_propagated", []))
    algorithm_unresolved = sorted(algorithm.get("unresolved_conserved", []))
    if final_unresolved != source_unresolved:
        errors.append(f"{feature_id}: finalized IR unresolved set differs from source IR")
    if algorithm_unresolved != source_unresolved:
        errors.append(f"{feature_id}: algorithm unresolved set differs from source IR")
    if sorted(final_ir.get("provisional_assumptions_propagated", [])) != sorted(
        source_ir.get("provisional_assumptions_propagated", [])
    ):
        errors.append(f"{feature_id}: provisional assumptions not conserved")

    final_ir_text = final_ir_path.read_text(encoding="utf-8")
    for opaque_type in source_ir.get("opaque_types", []):
        if opaque_type not in final_ir_text and opaque_type not in json.dumps(module, ensure_ascii=False):
            errors.append(f"{feature_id}: opaque type {opaque_type} is not conserved")

    source_interface = source_ir.get("interface", {})
    signature = algorithm.get("signature", {})
    if signature.get("name") != source_interface.get("minimal_function_or_class"):
        errors.append(f"{feature_id}: algorithm callable differs from source IR")
    if signature.get("input") != source_interface.get("input_type"):
        errors.append(f"{feature_id}: algorithm input type differs from source IR")
    if signature.get("output") != source_interface.get("output_type"):
        errors.append(f"{feature_id}: algorithm output type differs from source IR")
    if final_ir.get("algorithm_ref") != rel(algorithm_path):
        errors.append(f"{feature_id}: final IR to algorithm link mismatch")
    if final_ir.get("oracle_ref") != rel(oracle_path):
        errors.append(f"{feature_id}: final IR to oracle link mismatch")
    if algorithm.get("optimized_ir_ref") != rel(final_ir_path):
        errors.append(f"{feature_id}: algorithm to final IR link mismatch")
    if algorithm.get("oracle_ref") != rel(oracle_path):
        errors.append(f"{feature_id}: algorithm to oracle link mismatch")
    if oracle.get("optimized_ir_ref") != rel(final_ir_path):
        errors.append(f"{feature_id}: oracle to final IR link mismatch")
    if oracle.get("algorithm_ref") != rel(algorithm_path):
        errors.append(f"{feature_id}: oracle to algorithm link mismatch")
    if oracle.get("operation_under_test") != source_interface.get("minimal_function_or_class"):
        errors.append(f"{feature_id}: oracle operation differs from source IR")
    if not algorithm.get("pseudocode"):
        errors.append(f"{feature_id}: directly implementable pseudocode is missing")
    if not oracle.get("tests"):
        errors.append(f"{feature_id}: oracle tests are missing")
    if oracle.get("numeric_expected_results") not in ([], None):
        errors.append(f"{feature_id}: oracle invents numeric expected results")

# Module-level unresolved conservation.
module_unresolved = module.get("unresolved_conservation", {})
for feature_id in expected_features:
    source_ir = load_json(ROOT / f"ir/{feature_id}/ir.prototype.json")
    expected = sorted(source_ir.get("unresolved_propagated", []))
    actual = sorted(module_unresolved.get(feature_id, []))
    if expected and actual != expected:
        errors.append(f"{feature_id}: module unresolved mapping is incomplete")
    if not expected and feature_id in module_unresolved and actual:
        errors.append(f"{feature_id}: module adds unresolved identifiers")

# Task coverage.
task_features = sorted(
    task.get("feature_id")
    for task in tasks.get("tasks", [])
    if isinstance(task, dict) and task.get("feature_id")
)
if task_features != expected_features:
    errors.append("Implementation tasks do not cover exactly the authoritative feature population")

# Validate all generated YAML and disallow feature rejection claims.
for path in sorted(
    list(FINAL.rglob("*.yaml"))
    + list(OPTIMIZED.rglob("*.yaml"))
    + list(ALGORITHMS.rglob("*.yaml"))
    + list(ORACLES.rglob("*.yaml"))
):
    data = load_yaml(path)
    if isinstance(data, dict) and data.get("rejected_by_finalization") is True:
        errors.append(f"Rejected finalized feature in {rel(path)}")

# Scope and source preservation from the GitHub branch diff.
diff_result = run(["git", "diff", "--name-only", "origin/main...HEAD"])
if diff_result.returncode != 0:
    errors.append(f"Unable to inspect origin/main...HEAD diff: {diff_result.stderr.strip()}")
    changed_paths: list[str] = []
else:
    changed_paths = [line.strip().replace("\\", "/") for line in diff_result.stdout.splitlines() if line.strip()]

allowed_prefixes = (
    "registry/domain-finalization/invariants/",
    "registry/optimized-ir/invariants/",
    "registry/algorithms/invariants/",
    "registry/oracles/invariants/",
    "reports/domain-finalization/invariants/",
)
allowed_exact = {
    "tools/domain-finalization/validate_invariants_finalization.py",
    ".github/workflows/validate-invariants-finalization.yml",  # permitted only for temporary GitHub execution
}
for path in changed_paths:
    if not path.startswith(allowed_prefixes) and path not in allowed_exact:
        errors.append(f"Out-of-scope modified path: {path}")
    if path.startswith("maths/"):
        errors.append(f"Scientific source modified: {path}")
    if path.startswith("registry/global-reconciliation/"):
        errors.append(f"Global reconciliation registry modified: {path}")
    if path.startswith(f"registry/math-contracts/{PREFIX}"):
        errors.append(f"Source contract modified: {path}")
    if path.startswith(f"ir/{PREFIX}"):
        errors.append(f"Source IR or source test plan modified: {path}")
    if any(
        segment in path
        for segment in (
            "/master/", "/disciple/", "/community/", "/huit-dimensions/",
            "domain-finalization/master", "domain-finalization/disciple",
            "domain-finalization/community", "domain-finalization/huit-dimensions",
        )
    ):
        errors.append(f"Other active domain modified: {path}")
    suffix = Path(path).suffix.lower()
    if suffix in {".cpp", ".cc", ".cxx", ".hpp", ".hh", ".hxx", ".h"}:
        errors.append(f"C++ artifact produced: {path}")
    if path.startswith(("bindings/", "python-bindings/")) or "binding" in path.lower():
        errors.append(f"Python binding artifact produced: {path}")
    if "reference-implementation" in path.lower() or "reference_implementation" in path.lower():
        errors.append(f"Reference implementation produced: {path}")

if not changed_paths:
    errors.append("No changed files detected for Invariants finalization")

# Whitespace and Python compilation checks.
diff_check = run(["git", "diff", "--check", "origin/main...HEAD"])
if diff_check.returncode != 0:
    errors.append(f"git diff --check failed:\n{diff_check.stdout}{diff_check.stderr}")
try:
    py_compile.compile(str(Path(__file__).resolve()), doraise=True)
except Exception as exc:  # pragma: no cover - diagnostic path
    errors.append(f"Validator compilation failed: {exc}")

if errors:
    print("Invariants domain finalization validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    "Invariants domain finalization validation: PASS "
    f"({len(expected_features)} features, 10 optimized IRs, 10 algorithms, 10 oracles, "
    "0 rejected, 0 source modifications, 0 real blockers)"
)
