#!/usr/bin/env python3
"""Validate the Dynamics domain finalization package without scientific inference."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
MAIN_HEAD = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
STATUS = "selected_for_dynamics_implementation_specification"
FEATURES = [f"TLC-FC-05-DYNAMICS-{index:03d}" for index in range(1, 8)]
FEATURE_SET = set(FEATURES)

CONTRACT_HASHES = {
    "TLC-FC-05-DYNAMICS-001": "6f15adbcf612114c7a717cddbfe983b799367a3d",
    "TLC-FC-05-DYNAMICS-002": "f83108cc6bd317a10af1db66544025d514e8e887",
    "TLC-FC-05-DYNAMICS-003": "d0bc5e1ec63bd435f64270b3e6b80512c49f27d0",
    "TLC-FC-05-DYNAMICS-004": "7abd6136fbe6e748d31ba6e2bc3682611816d3a1",
    "TLC-FC-05-DYNAMICS-005": "198284c9d011fb5d705237b213055ea848e0cddc",
    "TLC-FC-05-DYNAMICS-006": "8a1419aee3f758a993d1959557c91ac9d7d12c85",
    "TLC-FC-05-DYNAMICS-007": "b457d55b23cfd26fd1a80c87a7259b4bfb7ca352",
}
IR_HASHES = {
    "TLC-FC-05-DYNAMICS-001": "08b1895c65105a06271ae8e812478831e768d72b",
    "TLC-FC-05-DYNAMICS-002": "19336495c61517fdfbc5e92fdbab2391b4186be3",
    "TLC-FC-05-DYNAMICS-003": "e977a716848715abb1684fb98b58ec7973aa377c",
    "TLC-FC-05-DYNAMICS-004": "1dccad2ebb42cde593d888459691b5902c953c1c",
    "TLC-FC-05-DYNAMICS-005": "375f866040370e0d463d2a1bee6df1674bed4e04",
    "TLC-FC-05-DYNAMICS-006": "aa78ab09789b807f3314dfc712af4aca9ab09c85",
    "TLC-FC-05-DYNAMICS-007": "831607dcc7a5bb00dfe11352c905579aaeba0144",
}
TEST_PLAN_HASHES = {
    "TLC-FC-05-DYNAMICS-001": "2e105e41b55b7bbd3570e0dd3fc3b8bf7e738fe7",
    "TLC-FC-05-DYNAMICS-002": "582d038a6795af22d43091e0054e03aca02fbc19",
    "TLC-FC-05-DYNAMICS-003": "c370ae428f2b3e01e69c609ed42f50a14626ada1",
    "TLC-FC-05-DYNAMICS-004": "4e96a44950138b4756279dc8cb6a80c23499071a",
    "TLC-FC-05-DYNAMICS-005": "889dee6be363b8eaf3065afbca34f3c2eb63b499",
    "TLC-FC-05-DYNAMICS-006": "1e065a2725c7469c26fab72fc81ce0e5f9fcc8b7",
    "TLC-FC-05-DYNAMICS-007": "11571b146606a366fb1410e029b956c4bd026c29",
}
MATHS_HASH = "09abf8d06093aca40ca8506f2ed4cdedef573911"

TOP_LEVEL_FILES = {
    "registry/domain-finalization/dynamics/manifest.yaml",
    "registry/domain-finalization/dynamics/feature-status.yaml",
    "registry/domain-finalization/dynamics/patterns.yaml",
    "registry/domain-finalization/dynamics/module-specification.yaml",
    "registry/domain-finalization/dynamics/implementation-tasks.yaml",
    "registry/domain-finalization/dynamics/decision-required.yaml",
    "reports/domain-finalization/dynamics/finalization-report.md",
    "tools/domain-finalization/validate_dynamics_finalization.py",
}


def run_git(*args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if check and completed.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed: {completed.stdout}{completed.stderr}"
        )
    return completed.stdout.strip()


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def declaration_strings(items: list[dict[str, Any]]) -> list[str]:
    return [f"{item['name']}: {item['type']}" for item in items]


def flatten_strings(value: Any) -> list[str]:
    result: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            result.append(str(key))
            result.extend(flatten_strings(nested))
    elif isinstance(value, list):
        for nested in value:
            result.extend(flatten_strings(nested))
    elif value is not None:
        result.append(str(value))
    return result


def main() -> int:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(run_git("merge-base", "--is-ancestor", MAIN_HEAD, "HEAD", check=False) == "", "HEAD is not descended from the recorded main HEAD")

    matrix = load_yaml(ROOT / "registry/global-reconciliation/domain-feature-matrix.yaml")
    dynamics_rows = [row for row in matrix.get("rows", []) if row.get("domain") == "dynamics"]
    baseline_ids = {row.get("feature_id") for row in dynamics_rows}
    require(len(dynamics_rows) == 7, f"baseline Dynamics count is {len(dynamics_rows)}, expected 7")
    require(baseline_ids == FEATURE_SET, f"baseline Dynamics population mismatch: {sorted(baseline_ids)}")
    for row in dynamics_rows:
        require(row.get("contract_present") is True, f"missing source contract in baseline: {row.get('feature_id')}")
        require(row.get("ir_artifact_present") is True, f"missing source IR in baseline: {row.get('feature_id')}")
        require(row.get("test_plan_present") is True, f"missing source test plan in baseline: {row.get('feature_id')}")

    manifest = load_yaml(ROOT / "registry/domain-finalization/dynamics/manifest.yaml")
    feature_status = load_yaml(ROOT / "registry/domain-finalization/dynamics/feature-status.yaml")
    patterns = load_yaml(ROOT / "registry/domain-finalization/dynamics/patterns.yaml")
    module = load_yaml(ROOT / "registry/domain-finalization/dynamics/module-specification.yaml")
    tasks = load_yaml(ROOT / "registry/domain-finalization/dynamics/implementation-tasks.yaml")
    decisions = load_yaml(ROOT / "registry/domain-finalization/dynamics/decision-required.yaml")

    require(manifest.get("baseline", {}).get("main_head") == MAIN_HEAD, "manifest main HEAD mismatch")
    require(set(manifest.get("feature_ids", [])) == FEATURE_SET, "manifest population mismatch")
    require(manifest.get("closure", {}).get("rejected_features") == [], "a feature was rejected in manifest")
    require(manifest.get("closure", {}).get("implementation_package_complete") is True, "manifest package is not complete")

    status_features = feature_status.get("features", [])
    require(len(status_features) == 7, "feature-status does not contain seven entries")
    require({item.get("feature_id") for item in status_features} == FEATURE_SET, "feature-status population mismatch")
    require(feature_status.get("summary", {}).get("features_rejected") == 0, "feature-status rejects a feature")
    require(len(module.get("public_operations", [])) == 7, "module does not expose seven public operations")
    require({item.get("feature_id") for item in module.get("public_operations", [])} == FEATURE_SET, "module public-operation population mismatch")
    require(len(tasks.get("feature_tasks", [])) == 7, "implementation tasks do not cover seven features")
    require({item.get("feature_id") for item in tasks.get("feature_tasks", [])} == FEATURE_SET, "implementation task population mismatch")
    require(decisions.get("current_package_blocked") is False, "current structural package is marked blocked")
    require(decisions.get("closure_decision", {}).get("features_rejected") == 0, "decisions reject a feature")
    require(bool(patterns.get("patterns")), "patterns analysis is empty")

    required_ir_fields = {
        "feature_id", "source_contract_ref", "source_ir_ref", "source_ir_status",
        "source_ir_nature", "finalized_ir_nature", "inputs", "outputs", "types",
        "opaque_values", "states", "initial_state", "terminal_state", "preconditions",
        "transition_conditions", "operations", "execution_order", "control_flow",
        "transitions", "effects", "postconditions", "invariants", "stop_conditions",
        "errors", "determinism", "stochasticity", "seed_management", "dependencies",
        "unresolved_propagated", "reservations", "transformations_applied",
        "preservation_obligations", "algorithm_ref", "oracle_ref", "implementation_aptitude",
    }

    for feature_id in FEATURES:
        contract_path = ROOT / f"registry/math-contracts/{feature_id}/contract.yaml"
        source_ir_path = ROOT / f"ir/{feature_id}/ir.prototype.json"
        source_test_path = ROOT / f"registry/test-plans/{feature_id}/test-plan.yaml"
        final_ir_path = ROOT / f"registry/optimized-ir/dynamics/{feature_id}/ir.yaml"
        algorithm_path = ROOT / f"registry/algorithms/dynamics/{feature_id}/algorithm.yaml"
        oracle_path = ROOT / f"registry/oracles/dynamics/{feature_id}/oracle.yaml"

        for path in (contract_path, source_ir_path, source_test_path, final_ir_path, algorithm_path, oracle_path):
            require(path.is_file(), f"missing artifact: {path.relative_to(ROOT)}")
        if not all(path.is_file() for path in (contract_path, source_ir_path, source_test_path, final_ir_path, algorithm_path, oracle_path)):
            continue

        contract = load_yaml(contract_path)
        source_ir = load_json(source_ir_path)
        source_test = load_yaml(source_test_path)
        final_ir = load_yaml(final_ir_path)
        algorithm = load_yaml(algorithm_path)
        oracle = load_yaml(oracle_path)

        require(contract.get("feature_id") == feature_id, f"contract feature mismatch: {feature_id}")
        require(source_ir.get("feature_id") == feature_id, f"source IR feature mismatch: {feature_id}")
        require(source_test.get("feature_id") == feature_id, f"source test feature mismatch: {feature_id}")
        require(final_ir.get("feature_id") == feature_id, f"final IR feature mismatch: {feature_id}")
        require(algorithm.get("feature_id") == feature_id, f"algorithm feature mismatch: {feature_id}")
        require(oracle.get("feature_id") == feature_id, f"oracle feature mismatch: {feature_id}")

        missing_fields = required_ir_fields - set(final_ir)
        require(not missing_fields, f"final IR missing fields for {feature_id}: {sorted(missing_fields)}")
        require(final_ir.get("status") == STATUS, f"final IR status mismatch: {feature_id}")
        require(final_ir.get("source_ir_preserved") is True, f"source IR not preserved: {feature_id}")
        require(final_ir.get("source_contract_preserved") is True, f"source contract not preserved: {feature_id}")
        require(final_ir.get("replaces_source_ir") is False, f"final IR replaces source IR: {feature_id}")
        require(final_ir.get("scientific_source_modified") is False, f"scientific source marked modified: {feature_id}")
        require(final_ir.get("source_ir_status") == source_ir.get("status"), f"raw source IR status mismatch: {feature_id}")
        require(final_ir.get("source_contract_ref") == f"registry/math-contracts/{feature_id}/contract.yaml", f"contract trace mismatch: {feature_id}")
        require(final_ir.get("source_ir_ref") == f"ir/{feature_id}/ir.prototype.json", f"source IR trace mismatch: {feature_id}")
        require(final_ir.get("source_test_plan_ref") == f"registry/test-plans/{feature_id}/test-plan.yaml", f"test-plan trace mismatch: {feature_id}")

        require(declaration_strings(final_ir.get("inputs", [])) == source_ir.get("inputs"), f"inputs changed: {feature_id}")
        require(declaration_strings(final_ir.get("outputs", [])) == source_ir.get("outputs"), f"outputs changed: {feature_id}")
        source_operation = source_ir.get("operations", [{}])[0].get("kind")
        final_operations = [item.get("kind") for item in final_ir.get("operations", [])]
        require(source_operation in final_operations, f"source operation missing: {feature_id}")
        require(set(source_ir.get("errors", [])) <= set(final_ir.get("errors", [])), f"source errors not conserved: {feature_id}")
        require(final_ir.get("unresolved_propagated") == source_ir.get("unresolved_propagated"), f"unresolved changed in final IR: {feature_id}")
        require(final_ir.get("states") == [], f"explicit state invented: {feature_id}")
        require(final_ir.get("transitions") == [], f"transition invented: {feature_id}")
        require(final_ir.get("transition_conditions") == [], f"transition condition invented: {feature_id}")
        require(final_ir.get("stop_conditions") == [], f"stop condition invented: {feature_id}")
        require(final_ir.get("initial_state") in {"not_defined", "not_applicable"}, f"initial state invented: {feature_id}")
        require(final_ir.get("terminal_state") in {"not_defined", "not_applicable"}, f"terminal state invented: {feature_id}")
        require(set(final_ir.get("traceability", {}).get("source_objects", [])) == set(contract.get("objects_covered", [])), f"source objects changed: {feature_id}")
        require(set(final_ir.get("traceability", {}).get("source_relations", [])) == set(contract.get("relations_covered", [])), f"source relations changed: {feature_id}")

        expected_algorithm_ref = f"registry/algorithms/dynamics/{feature_id}/algorithm.yaml"
        expected_oracle_ref = f"registry/oracles/dynamics/{feature_id}/oracle.yaml"
        expected_ir_ref = f"registry/optimized-ir/dynamics/{feature_id}/ir.yaml"
        require(final_ir.get("algorithm_ref") == expected_algorithm_ref, f"IR-algorithm link mismatch: {feature_id}")
        require(final_ir.get("oracle_ref") == expected_oracle_ref, f"IR-oracle link mismatch: {feature_id}")
        require(algorithm.get("ir_ref") == expected_ir_ref, f"algorithm-IR link mismatch: {feature_id}")
        require(algorithm.get("transitions") == [], f"algorithm invents transition: {feature_id}")
        require(bool(algorithm.get("signature")), f"algorithm signature missing: {feature_id}")
        require(bool(algorithm.get("pseudocode")), f"algorithm pseudocode missing: {feature_id}")
        require(algorithm.get("unresolved_preserved") == source_ir.get("unresolved_propagated"), f"algorithm unresolved mismatch: {feature_id}")
        require(oracle.get("ir_ref") == expected_ir_ref, f"oracle-IR link mismatch: {feature_id}")
        require(oracle.get("algorithm_ref") == expected_algorithm_ref, f"oracle-algorithm link mismatch: {feature_id}")
        require(oracle.get("source_test_plan_ref") == f"registry/test-plans/{feature_id}/test-plan.yaml", f"oracle test-plan link mismatch: {feature_id}")
        require(bool(oracle.get("acceptance_cases")), f"oracle cases missing: {feature_id}")
        oracle_text = set(flatten_strings(oracle))
        for unresolved in source_ir.get("unresolved_propagated", []):
            require(unresolved in oracle_text, f"oracle does not propagate {unresolved}: {feature_id}")

        require(run_git("hash-object", str(contract_path.relative_to(ROOT))) == CONTRACT_HASHES[feature_id], f"source contract modified: {feature_id}")
        require(run_git("hash-object", str(source_ir_path.relative_to(ROOT))) == IR_HASHES[feature_id], f"source IR modified: {feature_id}")
        require(run_git("hash-object", str(source_test_path.relative_to(ROOT))) == TEST_PLAN_HASHES[feature_id], f"source test plan modified: {feature_id}")

    require(run_git("hash-object", "maths/05-dynamics.md") == MATHS_HASH, "maths/05-dynamics.md was modified")

    changed_paths = set(filter(None, run_git("diff", "--name-only", f"{MAIN_HEAD}...HEAD").splitlines()))
    allowed_prefixes = (
        "registry/domain-finalization/dynamics/",
        "registry/optimized-ir/dynamics/",
        "registry/algorithms/dynamics/",
        "registry/oracles/dynamics/",
        "reports/domain-finalization/dynamics/",
    )
    allowed_exact = {
        "tools/domain-finalization/validate_dynamics_finalization.py",
        ".github/workflows/dynamics-finalization-validation.yml",
    }
    forbidden = sorted(
        path for path in changed_paths
        if path not in allowed_exact and not path.startswith(allowed_prefixes)
    )
    require(not forbidden, f"out-of-scope changed paths: {forbidden}")
    require(not any(path.startswith("maths/") for path in changed_paths), "maths path changed")
    require(not any(path.startswith("registry/global-reconciliation/") for path in changed_paths), "global registry changed")
    require(not any(
        path.startswith("registry/domain-finalization/") and not path.startswith("registry/domain-finalization/dynamics/")
        for path in changed_paths
    ), "another domain finalization path changed")
    require(not any(Path(path).suffix.lower() in {".cpp", ".cc", ".cxx", ".h", ".hpp", ".pyi"} for path in changed_paths), "C++ or binding artifact present")
    require(not any("reference-implementation" in path or "reference_implementation" in path for path in changed_paths), "reference implementation artifact present")

    expected_generated = set(TOP_LEVEL_FILES)
    for feature_id in FEATURES:
        expected_generated.update({
            f"registry/optimized-ir/dynamics/{feature_id}/ir.yaml",
            f"registry/algorithms/dynamics/{feature_id}/algorithm.yaml",
            f"registry/oracles/dynamics/{feature_id}/oracle.yaml",
        })
    missing_generated = sorted(path for path in expected_generated if not (ROOT / path).is_file())
    require(not missing_generated, f"generated artifacts missing: {missing_generated}")

    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{MAIN_HEAD}...HEAD"], cwd=ROOT,
        text=True, capture_output=True, check=False,
    )
    require(diff_check.returncode == 0, f"git diff --check failed: {diff_check.stdout}{diff_check.stderr}")

    if errors:
        print("Dynamics finalization validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Dynamics finalization validation OK")
    print("- authoritative features: 7")
    print("- finalized IRs: 7")
    print("- algorithms: 7")
    print("- oracles: 7")
    print("- source contracts, source IRs, source test plans, and maths preserved")
    print("- changed paths limited to Dynamics finalization, report, validator, and temporary workflow")
    return 0


if __name__ == "__main__":
    sys.exit(main())
