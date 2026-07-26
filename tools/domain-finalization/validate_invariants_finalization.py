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
VALIDATOR = Path(__file__).resolve()
EXPECTED_STATUS = "selected_for_invariants_implementation_specification"
errors: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_yaml(path: Path) -> Any:
    if not path.exists():
        errors.append(f"Missing YAML: {rel(path)}")
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"YAML parse failure: {rel(path)}: {exc}")
        return {}


def load_json(path: Path) -> Any:
    if not path.exists():
        errors.append(f"Missing JSON: {rel(path)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
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


def values(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def feature_map(records: Any) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in values(records):
        if isinstance(item, dict):
            feature_id = item.get("feature_id")
            if isinstance(feature_id, str) and feature_id.startswith(PREFIX):
                result[feature_id] = item
    return result


def ids(records: Any, key: str = "id") -> set[str]:
    return {
        item[key]
        for item in values(records)
        if isinstance(item, dict) and isinstance(item.get(key), str)
    }


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)


# Authoritative population from the current baseline and domain matrix.
baseline = load_yaml(BASELINE)
matrix = load_yaml(DOMAIN_MATRIX)
baseline_domains = baseline.get("domains", []) if isinstance(baseline, dict) else []
invariant_domains = [
    item for item in baseline_domains
    if isinstance(item, dict) and item.get("domain_id") == "invariants"
]
if len(invariant_domains) != 1:
    errors.append(f"Expected one Invariants domain in baseline, found {len(invariant_domains)}")
    baseline_count = None
else:
    baseline_count = invariant_domains[0].get("feature_count")

expected_features = sorted({
    item["feature_id"]
    for item in walk(matrix)
    if isinstance(item, dict)
    and item.get("domain") == "invariants"
    and isinstance(item.get("feature_id"), str)
    and item["feature_id"].startswith(PREFIX)
})
expected_sequence = [f"{PREFIX}{index:03d}" for index in range(1, 11)]
if baseline_count != 10:
    errors.append(f"Current baseline does not confirm exactly 10 features: {baseline_count!r}")
if expected_features != expected_sequence:
    errors.append(f"Authoritative Invariants population mismatch: {expected_features}")
if len(expected_features) != len(set(expected_features)):
    errors.append("Duplicate authoritative Invariants feature IDs")

# Required permanent artifacts.
required_files = [
    FINAL / "manifest.yaml",
    FINAL / "feature-status.yaml",
    FINAL / "patterns.yaml",
    FINAL / "module-specification.yaml",
    FINAL / "implementation-tasks.yaml",
    FINAL / "decision-required.yaml",
    REPORT,
    VALIDATOR,
]
for path in required_files:
    if not path.exists():
        errors.append(f"Missing required artifact: {rel(path)}")

manifest = load_yaml(FINAL / "manifest.yaml")
status_registry = load_yaml(FINAL / "feature-status.yaml")
patterns = load_yaml(FINAL / "patterns.yaml")
module = load_yaml(FINAL / "module-specification.yaml")
tasks = load_yaml(FINAL / "implementation-tasks.yaml")
decisions = load_yaml(FINAL / "decision-required.yaml")

if sorted(manifest.get("authoritative_population", {}).get("feature_ids", [])) != expected_features:
    errors.append("Manifest population differs from authoritative population")
if manifest.get("authoritative_population", {}).get("expected_count") != 10:
    errors.append("Manifest expected_count is not 10")
if manifest.get("counts", {}).get("optimized_irs") != 10:
    errors.append("Manifest optimized IR count is not 10")
if manifest.get("counts", {}).get("algorithms") != 10:
    errors.append("Manifest algorithm count is not 10")
if manifest.get("counts", {}).get("oracles") != 10:
    errors.append("Manifest oracle count is not 10")

status_entries = feature_map(status_registry.get("features", []))
if sorted(status_entries) != expected_features:
    errors.append("Feature-status registry does not contain exactly the authoritative population")
if status_registry.get("population_count") != 10:
    errors.append("Feature-status population_count is not 10")
if decisions.get("blocking_count") != 0 or decisions.get("blocking_decisions") not in ([], None):
    errors.append("Decision registry contains a real blocker")
if decisions.get("closure", {}).get("observable_behavior_defined_for_all_features") is not True:
    errors.append("Observable behavior is not closed for all features")
if not patterns.get("shared_patterns") or not patterns.get("normalizations_applied"):
    errors.append("Pattern or optimization registry is empty")

if sorted(module.get("active_features", [])) != expected_features:
    errors.append("Module active population differs from authoritative population")
public_operations = feature_map(module.get("public_operations", []))
if sorted(public_operations) != expected_features:
    errors.append("Module does not expose exactly one public operation per feature")

# Exact generated directory population.
for label, root in (
    ("optimized IR", OPTIMIZED),
    ("algorithm", ALGORITHMS),
    ("oracle", ORACLES),
):
    actual = sorted(path.name for path in root.glob(f"{PREFIX}*") if path.is_dir())
    if actual != expected_features:
        errors.append(f"{label} directory population mismatch: {actual}")

module_text = json.dumps(module, ensure_ascii=False, sort_keys=True)

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
        if not isinstance(document, dict) or document.get("feature_id") != feature_id:
            errors.append(f"{feature_id}: {label} feature_id mismatch")

    status_entry = status_entries.get(feature_id, {})
    if status_entry.get("finalization_status") != EXPECTED_STATUS:
        errors.append(f"{feature_id}: invalid finalization status")
    if status_entry.get("rejected_by_finalization") is not False:
        errors.append(f"{feature_id}: feature rejected or rejection flag absent")
    if status_entry.get("source_contract") != rel(contract_path):
        errors.append(f"{feature_id}: feature-status source contract mismatch")
    if status_entry.get("source_ir") != rel(source_ir_path):
        errors.append(f"{feature_id}: feature-status source IR mismatch")
    if status_entry.get("source_test_plan") != rel(source_test_path):
        errors.append(f"{feature_id}: feature-status source test-plan mismatch")

    required_ir_keys = {
        "feature_id", "source_contract_ref", "source_ir_ref", "source_test_plan_ref",
        "source_ir_raw_status", "nature", "invariant_referenced", "scope", "inputs", "outputs",
        "types", "opaque_values", "preconditions", "conditions_of_application", "operations",
        "execution_order", "control_flow", "state_before", "state_after", "effects", "postconditions",
        "conditions_of_conservation", "conditions_of_violation", "errors", "determinism", "dependencies",
        "unresolved_propagated", "reservations", "transformations_applied",
        "obligations_of_preservation", "algorithm_ref", "oracle_ref", "implementation_aptitude",
        "source_ir_preserved", "source_contract_preserved", "replaces_source_ir",
        "scientific_source_modified",
    }
    missing = sorted(required_ir_keys - set(final_ir))
    if missing:
        errors.append(f"{feature_id}: finalized IR missing fields {missing}")
    if final_ir.get("status") != EXPECTED_STATUS:
        errors.append(f"{feature_id}: finalized IR status mismatch")
    if final_ir.get("source_contract_ref") != rel(contract_path):
        errors.append(f"{feature_id}: finalized IR source contract reference mismatch")
    if final_ir.get("source_ir_ref") != rel(source_ir_path):
        errors.append(f"{feature_id}: finalized IR source IR reference mismatch")
    if final_ir.get("source_test_plan_ref") != rel(source_test_path):
        errors.append(f"{feature_id}: finalized IR source test-plan reference mismatch")
    if final_ir.get("source_ir_raw_status") != source_ir.get("ir_kind"):
        errors.append(f"{feature_id}: source IR raw status changed")
    if final_ir.get("source_catalogue_status") != source_ir.get("catalogue_status_preserved"):
        errors.append(f"{feature_id}: source catalogue status changed")
    if final_ir.get("source_ir_preserved") is not True:
        errors.append(f"{feature_id}: source_ir_preserved is not true")
    if final_ir.get("source_contract_preserved") is not True:
        errors.append(f"{feature_id}: source_contract_preserved is not true")
    if final_ir.get("replaces_source_ir") is not False:
        errors.append(f"{feature_id}: replaces_source_ir is not false")
    if final_ir.get("scientific_source_modified") is not False:
        errors.append(f"{feature_id}: scientific_source_modified is not false")
    if not final_ir.get("opaque_values"):
        errors.append(f"{feature_id}: finalized IR has no opaque-value conservation declaration")

    source_preconditions = ids(source_ir.get("preconditions"))
    final_preconditions = ids(final_ir.get("preconditions"))
    if not source_preconditions.issubset(final_preconditions):
        errors.append(f"{feature_id}: source precondition IDs not conserved")

    source_unresolved = sorted(source_ir.get("unresolved_propagated", []))
    if sorted(final_ir.get("unresolved_propagated", [])) != source_unresolved:
        errors.append(f"{feature_id}: finalized IR unresolved set differs from source IR")
    if sorted(algorithm.get("unresolved_conserved", [])) != source_unresolved:
        errors.append(f"{feature_id}: algorithm unresolved set differs from source IR")
    oracle_text = json.dumps(oracle, ensure_ascii=False, sort_keys=True)
    for unresolved_id in source_unresolved:
        if unresolved_id not in oracle_text:
            errors.append(f"{feature_id}: oracle does not preserve {unresolved_id}")

    source_assumptions = sorted(source_ir.get("provisional_assumptions_propagated", []))
    if sorted(final_ir.get("provisional_assumptions_propagated", [])) != source_assumptions:
        errors.append(f"{feature_id}: provisional assumptions changed")

    final_ir_text = final_ir_path.read_text(encoding="utf-8")
    for opaque_type in source_ir.get("opaque_types", []):
        if opaque_type not in final_ir_text and opaque_type not in module_text:
            errors.append(f"{feature_id}: opaque source type not represented: {opaque_type}")

    source_interface = source_ir.get("interface", {})
    source_operations = source_ir.get("operations", [])
    source_operation_name = source_operations[0].get("name") if source_operations else None
    signature = algorithm.get("signature", {})
    if signature.get("name") != source_interface.get("minimal_function_or_class"):
        errors.append(f"{feature_id}: algorithm callable differs from source interface")
    if signature.get("name") != source_operation_name:
        errors.append(f"{feature_id}: algorithm callable differs from source operation")
    if signature.get("input") != source_interface.get("input_type"):
        errors.append(f"{feature_id}: algorithm input type differs from source IR")
    if signature.get("output") != source_interface.get("output_type"):
        errors.append(f"{feature_id}: algorithm output type differs from source IR")
    if not algorithm.get("pseudocode") or not algorithm.get("ordered_steps"):
        errors.append(f"{feature_id}: algorithm is not directly implementable")

    if final_ir.get("algorithm_ref") != rel(algorithm_path):
        errors.append(f"{feature_id}: finalized IR to algorithm link mismatch")
    if final_ir.get("oracle_ref") != rel(oracle_path):
        errors.append(f"{feature_id}: finalized IR to oracle link mismatch")
    if algorithm.get("optimized_ir_ref") != rel(final_ir_path):
        errors.append(f"{feature_id}: algorithm to finalized IR link mismatch")
    if algorithm.get("oracle_ref") != rel(oracle_path):
        errors.append(f"{feature_id}: algorithm to oracle link mismatch")
    if oracle.get("optimized_ir_ref") != rel(final_ir_path):
        errors.append(f"{feature_id}: oracle to finalized IR link mismatch")
    if oracle.get("algorithm_ref") != rel(algorithm_path):
        errors.append(f"{feature_id}: oracle to algorithm link mismatch")
    if oracle.get("source_test_plan_ref") != rel(source_test_path):
        errors.append(f"{feature_id}: oracle source test-plan link mismatch")
    if oracle.get("operation_under_test") != source_interface.get("minimal_function_or_class"):
        errors.append(f"{feature_id}: oracle operation differs from source interface")
    if source_test.get("operation_under_test") != source_interface.get("minimal_function_or_class"):
        errors.append(f"{feature_id}: source test plan differs from source interface")
    if not oracle.get("tests"):
        errors.append(f"{feature_id}: oracle contains no acceptance tests")
    if oracle.get("numeric_expected_results") not in ([], None):
        errors.append(f"{feature_id}: oracle invents numeric expected results")

# Module unresolved conservation and implementation task coverage.
module_unresolved = module.get("unresolved_conservation", {})
for feature_id in expected_features:
    source_ir = load_json(ROOT / f"ir/{feature_id}/ir.prototype.json")
    expected = sorted(source_ir.get("unresolved_propagated", []))
    actual = sorted(module_unresolved.get(feature_id, []))
    if expected and actual != expected:
        errors.append(f"{feature_id}: module unresolved mapping mismatch")
    if not expected and actual:
        errors.append(f"{feature_id}: module adds unresolved identifiers")

task_features = sorted(
    item.get("feature_id")
    for item in tasks.get("tasks", [])
    if isinstance(item, dict) and isinstance(item.get("feature_id"), str)
)
if task_features != expected_features:
    errors.append("Implementation tasks do not cover exactly the authoritative population")

# Validate every generated YAML file.
for path in sorted(
    list(FINAL.rglob("*.yaml"))
    + list(OPTIMIZED.rglob("*.yaml"))
    + list(ALGORITHMS.rglob("*.yaml"))
    + list(ORACLES.rglob("*.yaml"))
):
    load_yaml(path)

# Branch diff scope and source preservation.
diff = run(["git", "diff", "--name-only", "origin/main...HEAD"])
if diff.returncode != 0:
    errors.append(f"Unable to read branch diff: {diff.stderr.strip()}")
    changed: list[str] = []
else:
    changed = [line.strip().replace("\\", "/") for line in diff.stdout.splitlines() if line.strip()]

allowed_prefixes = (
    "registry/domain-finalization/invariants/",
    "registry/optimized-ir/invariants/",
    "registry/algorithms/invariants/",
    "registry/oracles/invariants/",
    "reports/domain-finalization/invariants/",
)
allowed_exact = {
    "tools/domain-finalization/validate_invariants_finalization.py",
    ".github/workflows/validate-invariants-finalization.yml",
}
for path in changed:
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
        marker in path
        for marker in (
            "domain-finalization/master/",
            "domain-finalization/disciple/",
            "domain-finalization/community/",
            "domain-finalization/huit-dimensions/",
            "optimized-ir/master/",
            "optimized-ir/disciple/",
            "optimized-ir/community/",
            "optimized-ir/huit-dimensions/",
            "algorithms/master/",
            "algorithms/disciple/",
            "algorithms/community/",
            "algorithms/huit-dimensions/",
            "oracles/master/",
            "oracles/disciple/",
            "oracles/community/",
            "oracles/huit-dimensions/",
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

if not changed:
    errors.append("No Invariants finalization changes detected")

whitespace = run(["git", "diff", "--check", "origin/main...HEAD"])
if whitespace.returncode != 0:
    errors.append(f"git diff --check failed:\n{whitespace.stdout}{whitespace.stderr}")

try:
    py_compile.compile(str(VALIDATOR), doraise=True)
except Exception as exc:
    errors.append(f"Validator compilation failed: {exc}")

if errors:
    print("Invariants domain finalization validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    "Invariants domain finalization validation: PASS "
    "(10 features, 10 optimized IRs, 10 algorithms, 10 oracles, "
    "0 rejected, 0 source modifications, 0 real blockers)"
)
