#!/usr/bin/env python3
"""Validate the Theorems domain finalization package.

This validator is intentionally structural. It checks conservation and
traceability against the existing contracts, source IRs, test plans, domain
registries, and the current global baseline. It does not evaluate theorem
truth or proof correctness.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover - handled by CI setup
    raise SystemExit("PyYAML is required to run this validator") from exc

ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "theorems"
FEATURE_PREFIX = "TLC-FC-06-THEOREMS-"
MANIFEST_PATH = Path("registry/domain-finalization/theorems/manifest.yaml")
FEATURE_STATUS_PATH = Path("registry/domain-finalization/theorems/feature-status.yaml")
PATTERNS_PATH = Path("registry/domain-finalization/theorems/patterns.yaml")
MODULE_PATH = Path("registry/domain-finalization/theorems/module-specification.yaml")
TASKS_PATH = Path("registry/domain-finalization/theorems/implementation-tasks.yaml")
DECISIONS_PATH = Path("registry/domain-finalization/theorems/decision-required.yaml")
REPORT_PATH = Path("reports/domain-finalization/theorems/finalization-report.md")
VALIDATOR_PATH = Path("tools/domain-finalization/validate_theorems_finalization.py")
TEMP_WORKFLOW_PATH = Path(".github/workflows/validate-theorems-finalization-temp.yml")

REQUIRED_DOMAIN_FILES = [
    MANIFEST_PATH,
    FEATURE_STATUS_PATH,
    PATTERNS_PATH,
    MODULE_PATH,
    TASKS_PATH,
    DECISIONS_PATH,
    REPORT_PATH,
    VALIDATOR_PATH,
]

ALLOWED_PREFIXES = (
    "registry/domain-finalization/theorems/",
    "registry/optimized-ir/theorems/",
    "registry/algorithms/theorems/",
    "registry/oracles/theorems/",
    "reports/domain-finalization/theorems/",
)

FORBIDDEN_CHANGED_PREFIXES = (
    "maths/",
    "registry/global-reconciliation/",
    "registry/math-contracts/",
    "registry/ir/",
    "registry/test-plans/",
    "registry/domain-progress/master/",
    "registry/domain-progress/disciple/",
    "registry/domain-progress/community/",
    "registry/domain-progress/huit-dimensions/",
    "registry/domain-progress/invariants/",
    "registry/domain-progress/dynamics/",
)

CPP_SUFFIXES = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx"}
TEMPORARY_MARKERS = (".status", "__pycache__", ".pytest_cache", ".mypy_cache", ".cache")


class ValidationError(RuntimeError):
    """Raised when a package invariant is violated."""


def fail(message: str) -> None:
    raise ValidationError(message)


def load_yaml(relative_path: Path | str) -> Any:
    path = ROOT / Path(relative_path)
    if not path.is_file():
        fail(f"missing required YAML file: {relative_path}")
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def require_file(relative_path: Path | str) -> Path:
    path = ROOT / Path(relative_path)
    if not path.is_file():
        fail(f"missing required file: {relative_path}")
    return path


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def collect_feature_ids(value: Any) -> set[str]:
    found: set[str] = set()
    for node in walk(value):
        if isinstance(node, dict):
            feature_id = node.get("feature_id")
            if isinstance(feature_id, str) and feature_id.startswith(FEATURE_PREFIX):
                found.add(feature_id)
        elif isinstance(node, str) and node.startswith(FEATURE_PREFIX):
            found.add(node)
    return found


def baseline_feature_count(baseline: Any) -> int:
    candidate_counts: list[int] = []
    for node in walk(baseline):
        if not isinstance(node, dict):
            continue
        domain_marker = node.get("domain") or node.get("domain_id") or node.get("domain_slug")
        if domain_marker != DOMAIN:
            continue
        for subnode in walk(node):
            if not isinstance(subnode, dict):
                continue
            for key, value in subnode.items():
                normalized = str(key).lower()
                if isinstance(value, int) and normalized in {
                    "feature_count",
                    "features_count",
                    "total_features",
                    "active_feature_count",
                    "features",
                }:
                    candidate_counts.append(value)
    if 9 not in candidate_counts:
        fail(f"current baseline does not explicitly confirm nine Theorems features: {candidate_counts}")
    return 9


def run_git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        fail(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def resolve_base_ref() -> str:
    requested = os.environ.get("THEOREMS_BASE_REF", "origin/main")
    if subprocess.run(
        ["git", "rev-parse", "--verify", requested],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0:
        return requested
    if subprocess.run(
        ["git", "rev-parse", "--verify", "main"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0:
        return "main"
    fail("cannot resolve origin/main or main for changed-path validation")
    return ""  # unreachable


def changed_paths(base_ref: str) -> list[str]:
    output = run_git("diff", "--name-only", f"{base_ref}...HEAD")
    return [line for line in output.splitlines() if line]


def assert_changed_path_scope(paths: list[str]) -> None:
    allow_temp_workflow = os.environ.get("THEOREMS_ALLOW_TEMP_WORKFLOW") == "1"
    for path in paths:
        permitted = path == str(VALIDATOR_PATH) or any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)
        if allow_temp_workflow and path == str(TEMP_WORKFLOW_PATH):
            permitted = True
        if not permitted:
            fail(f"modified path is outside the permitted Theorems scope: {path}")
        if path.startswith(FORBIDDEN_CHANGED_PREFIXES):
            fail(f"source, global, or parallel-domain artifact was modified: {path}")
        if Path(path).suffix.lower() in CPP_SUFFIXES:
            fail(f"C or C++ artifact is forbidden: {path}")
        lowered = path.lower()
        if "binding" in lowered or "pybind" in lowered:
            fail(f"binding artifact is forbidden: {path}")
        if "reference-implementation" in lowered or "reference_implementation" in lowered:
            fail(f"reference implementation artifact is forbidden: {path}")
        if any(marker in path for marker in TEMPORARY_MARKERS):
            fail(f"temporary or cache artifact remains: {path}")
        if path.endswith(".py") and path != str(VALIDATOR_PATH):
            fail(f"unexpected Python implementation file: {path}")


def exact_set(actual: Any, expected: Iterable[str], label: str) -> None:
    if not isinstance(actual, list):
        fail(f"{label} must be a list")
    actual_set = set(actual)
    expected_set = set(expected)
    if actual_set != expected_set or len(actual) != len(expected_set):
        fail(f"{label} mismatch: actual={sorted(actual_set)}, expected={sorted(expected_set)}")


def assert_feature_artifacts(feature: dict[str, Any]) -> None:
    feature_id = feature["feature_id"]
    contract_path = Path(feature["contract"])
    source_ir_path = Path(feature["source_ir"])
    test_plan_path = Path(feature["source_test_plan"])
    finalized_ir_path = Path(feature["finalized_ir"])
    algorithm_path = Path(feature["algorithm"])
    oracle_path = Path(feature["oracle"])

    contract = load_yaml(contract_path)
    source_ir = load_yaml(source_ir_path)
    test_plan = load_yaml(test_plan_path)
    finalized = load_yaml(finalized_ir_path)
    algorithm = load_yaml(algorithm_path)
    oracle = load_yaml(oracle_path)

    if contract.get("feature_id") != feature_id:
        fail(f"contract feature mismatch for {feature_id}")
    if source_ir.get("feature_id") != feature_id:
        fail(f"source IR feature mismatch for {feature_id}")
    if test_plan.get("feature_id") != feature_id:
        fail(f"source test plan feature mismatch for {feature_id}")
    if source_ir.get("contract_id") != contract.get("contract_id"):
        fail(f"contract-to-source-IR link mismatch for {feature_id}")
    if test_plan.get("contract_id") != contract.get("contract_id"):
        fail(f"contract-to-test-plan link mismatch for {feature_id}")
    if test_plan.get("ir_id") != source_ir.get("ir_id"):
        fail(f"source-IR-to-test-plan link mismatch for {feature_id}")

    operation = source_ir.get("entrypoint", {}).get("callable")
    if not operation:
        fail(f"missing source operation for {feature_id}")
    if test_plan.get("operation_under_test") != operation:
        fail(f"source test-plan operation mismatch for {feature_id}")

    expected_finalized_fields = {
        "feature_id",
        "selection_status",
        "source_contract",
        "source_ir",
        "source_test_plan",
        "source_ir_raw_status",
        "nature",
        "statement",
        "scope",
        "quantifiers",
        "hypotheses",
        "preconditions",
        "conditions_of_application",
        "conclusion",
        "logical_relation",
        "dependencies",
        "operations_authorized",
        "execution_order",
        "control_flow",
        "effects",
        "postconditions",
        "errors",
        "determinism",
        "proof_status",
        "unresolved_propagated",
        "opaque_values",
        "reservations",
        "transformations_applied",
        "obligations_of_preservation",
        "algorithm_ref",
        "oracle_ref",
        "implementation_aptitude",
    }
    missing_fields = expected_finalized_fields - set(finalized)
    if missing_fields:
        fail(f"finalized IR for {feature_id} misses fields: {sorted(missing_fields)}")

    if finalized.get("feature_id") != feature_id:
        fail(f"finalized IR feature mismatch for {feature_id}")
    if finalized.get("selection_status") != "selected_for_theorems_implementation_specification":
        fail(f"invalid selected status for {feature_id}")
    if finalized.get("source_contract") != str(contract_path):
        fail(f"finalized contract trace mismatch for {feature_id}")
    if finalized.get("source_ir") != str(source_ir_path):
        fail(f"finalized source IR trace mismatch for {feature_id}")
    if finalized.get("source_test_plan") != str(test_plan_path):
        fail(f"finalized source test-plan trace mismatch for {feature_id}")
    if finalized.get("source_contract_id") != contract.get("contract_id"):
        fail(f"finalized contract ID mismatch for {feature_id}")
    if finalized.get("source_ir_id") != source_ir.get("ir_id"):
        fail(f"finalized source IR ID mismatch for {feature_id}")
    if finalized.get("source_ir_raw_status") != source_ir.get("ir_kind"):
        fail(f"source IR raw status was not preserved for {feature_id}")

    if finalized.get("preconditions") != contract.get("preconditions"):
        fail(f"source preconditions were not preserved for {feature_id}")
    if finalized.get("postconditions") != contract.get("postconditions"):
        fail(f"source postconditions were not preserved for {feature_id}")
    if finalized.get("errors") != source_ir.get("errors"):
        fail(f"source error codes were not preserved for {feature_id}")
    if finalized.get("unresolved_propagated") != source_ir.get("unresolved_propagated"):
        fail(f"source IR unresolved set was not preserved for {feature_id}")
    if finalized.get("unresolved_propagated") != contract.get("unresolved_propagated"):
        fail(f"contract unresolved set was not preserved for {feature_id}")
    if finalized.get("determinism") != source_ir.get("determinism_status"):
        fail(f"determinism status was not preserved for {feature_id}")

    source_assumptions = source_ir.get("provisional_assumptions_propagated", [])
    finalized_assumptions = finalized.get("hypotheses", {}).get("provisional_engineering", [])
    if finalized_assumptions != source_assumptions:
        fail(f"provisional assumptions were not preserved for {feature_id}")

    source_opaque_types = set(source_ir.get("opaque_types", []))
    finalized_opaque_types = set(finalized.get("opaque_values", {}).get("types", []))
    if not source_opaque_types.issubset(finalized_opaque_types):
        fail(f"opaque source types were not preserved for {feature_id}")

    for guard in (
        "source_ir_preserved",
        "source_contract_preserved",
    ):
        if finalized.get(guard) is not True:
            fail(f"{guard} must be true for {feature_id}")
    for guard in (
        "replaces_source_ir",
        "scientific_source_modified",
        "proof_invented",
    ):
        if finalized.get(guard) is not False:
            fail(f"{guard} must be false for {feature_id}")

    if finalized.get("algorithm_ref") != str(algorithm_path):
        fail(f"algorithm link mismatch for {feature_id}")
    if finalized.get("oracle_ref") != str(oracle_path):
        fail(f"oracle link mismatch for {feature_id}")

    if algorithm.get("feature_id") != feature_id or algorithm.get("operation") != operation:
        fail(f"algorithm identity mismatch for {feature_id}")
    if algorithm.get("preconditions") != contract.get("preconditions"):
        fail(f"algorithm preconditions mismatch for {feature_id}")
    if algorithm.get("errors") != source_ir.get("errors"):
        fail(f"algorithm errors mismatch for {feature_id}")
    if algorithm.get("unresolved_conserved") != source_ir.get("unresolved_propagated"):
        fail(f"algorithm unresolved mismatch for {feature_id}")
    signature = str(algorithm.get("signature", ""))
    if operation not in signature:
        fail(f"algorithm signature omits operation for {feature_id}")
    for output in source_ir.get("outputs", []):
        if str(output.get("type")) not in signature:
            fail(f"algorithm signature omits source output type for {feature_id}")
    pseudocode = algorithm.get("pseudocode")
    if not isinstance(pseudocode, str) or operation not in pseudocode:
        fail(f"directly implementable pseudocode missing for {feature_id}")

    if oracle.get("feature_id") != feature_id:
        fail(f"oracle feature mismatch for {feature_id}")
    if oracle.get("operation_under_test") != operation:
        fail(f"oracle operation mismatch for {feature_id}")
    if oracle.get("source_test_plan") != str(test_plan_path):
        fail(f"oracle test-plan trace mismatch for {feature_id}")
    if not oracle.get("acceptance_tests"):
        fail(f"oracle has no acceptance tests for {feature_id}")
    if oracle.get("properties", {}).get("proof_invented") is not False:
        fail(f"oracle must assert proof_invented false for {feature_id}")

    proof_status = finalized.get("proof_status", {})
    for node in walk(proof_status):
        if isinstance(node, dict):
            for key, value in node.items():
                if "status" in str(key).lower() and value == "complete":
                    fail(f"invented complete proof status in {feature_id}")


def assert_population_and_package() -> tuple[list[str], dict[str, Any]]:
    baseline = load_yaml("registry/global-reconciliation/current-baseline.yaml")
    matrix = load_yaml("registry/global-reconciliation/domain-feature-matrix.yaml")
    confirmed_count = baseline_feature_count(baseline)
    matrix_ids = sorted(collect_feature_ids(matrix))
    if len(matrix_ids) != confirmed_count:
        fail(f"Theorems matrix population count mismatch: {len(matrix_ids)} != {confirmed_count}")

    manifest = load_yaml(MANIFEST_PATH)
    if manifest.get("domain") != DOMAIN:
        fail("manifest domain is not theorems")
    if manifest.get("authoritative_feature_count") != confirmed_count:
        fail("manifest feature count does not match baseline")
    exact_set(manifest.get("active_features"), matrix_ids, "manifest active features")
    exact_set([item.get("feature_id") for item in manifest.get("features", [])], matrix_ids, "manifest feature entries")
    if manifest.get("population_confirmation", {}).get("rejected_features") != []:
        fail("a feature was rejected in the finalization manifest")

    for required in REQUIRED_DOMAIN_FILES:
        require_file(required)

    for root_name in ("optimized-ir", "algorithms", "oracles"):
        root = ROOT / "registry" / root_name / DOMAIN
        actual_dirs = sorted(path.name for path in root.iterdir() if path.is_dir()) if root.is_dir() else []
        if actual_dirs != matrix_ids:
            fail(f"{root_name} feature directories mismatch: {actual_dirs}")

    for feature in manifest.get("features", []):
        assert_feature_artifacts(feature)

    status = load_yaml(FEATURE_STATUS_PATH)
    exact_set([item.get("feature_id") for item in status.get("features", [])], matrix_ids, "feature-status population")
    if status.get("summary", {}).get("rejected_features") != 0:
        fail("feature-status reports a rejected feature")

    module = load_yaml(MODULE_PATH)
    exact_set([item.get("feature_id") for item in module.get("public_operations", [])], matrix_ids, "module public operations")
    if module.get("operation_boundaries", {}).get("prove_theorem", {}).get("supported") is not False:
        fail("module must not claim theorem-proving support")

    tasks = load_yaml(TASKS_PATH)
    exact_set([item.get("feature_id") for item in tasks.get("feature_tasks", [])], matrix_ids, "implementation-task population")

    decisions = load_yaml(DECISIONS_PATH)
    if decisions.get("blocking") != [] or decisions.get("summary", {}).get("blocking_count") != 0:
        fail("blocking decisions remain in the implementation specification package")

    patterns = load_yaml(PATTERNS_PATH)
    if patterns.get("analysis_scope", {}).get("source_irs") != 9:
        fail("patterns artifact does not cover all nine source IRs")
    if patterns.get("preservation_guards", {}).get("source_ir_modified") is not False:
        fail("patterns artifact does not preserve source IRs")

    return matrix_ids, manifest


def assert_proof_and_quantifier_conservation() -> None:
    result_semantics = load_yaml("registry/domain-progress/theorems/result-semantics.yaml")
    proof_inventory = load_yaml("registry/domain-progress/theorems/proof-inventory.yaml")
    module = load_yaml(MODULE_PATH)
    feature_006 = load_yaml("registry/optimized-ir/theorems/TLC-FC-06-THEOREMS-006/ir.yaml")

    summary = proof_inventory.get("summary", {})
    if summary.get("complete") != 0 or summary.get("partial") != 6 or summary.get("absent") != 1:
        fail("proof inventory summary is not conserved")
    if summary.get("mechanically_checkable_candidates") != 0:
        fail("mechanical proof support was invented")

    result_statuses = {
        item["result_id"]: item.get("proof_status")
        for item in result_semantics.get("results", [])
    }
    final_statuses = {
        item["result_id"]: item.get("status")
        for item in feature_006.get("proof_status", {}).get("per_result", [])
    }
    for result_id in [f"RESULT-THEOREMS-{number:03d}" for number in range(1, 7)]:
        if final_statuses.get(result_id) != result_statuses.get(result_id):
            fail(f"proof status mismatch for {result_id}")

    explicit_source_results = {
        item["result_id"]
        for item in result_semantics.get("results", [])
        if item.get("quantifiers") == "explicit"
    }
    module_explicit_results = {
        item["result_id"]
        for item in module.get("quantifiers", {}).get("explicit_source_results", [])
    }
    if module_explicit_results != explicit_source_results:
        fail("module quantifier metadata does not match source result semantics")


def assert_diff_integrity() -> list[str]:
    base_ref = resolve_base_ref()
    paths = changed_paths(base_ref)
    if not paths:
        fail("no changes found for Theorems finalization")
    assert_changed_path_scope(paths)

    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{base_ref}...HEAD"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if diff_check.returncode != 0:
        fail(f"git diff --check failed: {diff_check.stdout}{diff_check.stderr}")

    for forbidden_prefix in FORBIDDEN_CHANGED_PREFIXES:
        offenders = [path for path in paths if path.startswith(forbidden_prefix)]
        if offenders:
            fail(f"forbidden modified paths under {forbidden_prefix}: {offenders}")

    return paths


def main() -> int:
    try:
        matrix_ids, manifest = assert_population_and_package()
        assert_proof_and_quantifier_conservation()
        paths = assert_diff_integrity()
    except ValidationError as exc:
        print(f"THEOREMS FINALIZATION VALIDATION: FAIL\n- {exc}", file=sys.stderr)
        return 1

    print("THEOREMS FINALIZATION VALIDATION: PASS")
    print(f"- baseline-confirmed population: {len(matrix_ids)}")
    print(f"- features: {', '.join(matrix_ids)}")
    print("- source contracts: 9 preserved")
    print("- source IRs: 9 preserved")
    print("- source test plans: 9 preserved")
    print("- finalized IRs: 9")
    print("- algorithms: 9")
    print("- oracles: 9")
    print("- proofs invented: 0")
    print("- features rejected: 0")
    print("- blocking decisions: 0")
    print(f"- changed paths validated: {len(paths)}")
    print(f"- branch: {manifest.get('branch')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
