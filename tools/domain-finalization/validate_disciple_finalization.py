from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_STATUS = "selected_for_disciple_implementation_specification"
EXPECTED_IDS = [f"TLC-FC-01-DISCIPLE-{index:03d}" for index in range(1, 11)]
TEMP_WORKFLOW = ".github/workflows/disciple-finalization-validation.yml"


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"expected mapping: {path}")
    return data


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"expected mapping: {path}")
    return data


def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, text=True, capture_output=True
    )
    return result.stdout.strip()


def changed_paths() -> list[str]:
    base = os.environ.get("GITHUB_BASE_SHA")
    if not base:
        try:
            base = git_output("merge-base", "HEAD", "origin/main")
        except Exception:
            base = git_output("rev-parse", "HEAD^")
    output = git_output("diff", "--name-only", f"{base}...HEAD")
    return [line for line in output.splitlines() if line]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    baseline = load_yaml(ROOT / "registry/global-reconciliation/current-baseline.yaml")
    disciple_domain = next(
        (item for item in baseline.get("domains", []) if item.get("domain_id") == "disciple"),
        None,
    )
    require(disciple_domain is not None, "disciple missing from current baseline", errors)
    if disciple_domain:
        require(disciple_domain.get("feature_count") == 10, "baseline Disciple feature count is not 10", errors)

    matrix = load_yaml(ROOT / "registry/global-reconciliation/domain-feature-matrix.yaml")
    matrix_ids = [row.get("feature_id") for row in matrix.get("rows", []) if row.get("domain") == "disciple"]
    require(matrix_ids == EXPECTED_IDS, f"authoritative Disciple IDs mismatch: {matrix_ids}", errors)

    source_feature_status = load_yaml(ROOT / "registry/domain-progress/disciple/feature-status.yaml")
    source_status_by_id = {item["feature_id"]: item for item in source_feature_status.get("features", [])}

    final_status = load_yaml(ROOT / "registry/domain-finalization/disciple/feature-status.yaml")
    final_features = final_status.get("features", [])
    final_ids = [item.get("feature_id") for item in final_features]
    require(final_status.get("feature_count") == 10, "final feature count is not 10", errors)
    require(final_ids == EXPECTED_IDS, f"final feature IDs mismatch: {final_ids}", errors)
    for item in final_features:
        require(item.get("disposition") == "preserved", f"feature not preserved: {item.get('feature_id')}", errors)

    manifest = load_yaml(ROOT / "registry/domain-finalization/disciple/manifest.yaml")
    require(manifest.get("active_feature_count") == 10, "manifest active_feature_count is not 10", errors)
    require(manifest.get("active_features") == EXPECTED_IDS, "manifest feature list mismatch", errors)

    module = load_yaml(ROOT / "registry/domain-finalization/disciple/module-specification.yaml")
    require(module.get("features") == EXPECTED_IDS, "module feature list mismatch", errors)
    module_operation_ids = [item.get("feature_id") for item in module.get("public_operations", [])]
    require(module_operation_ids == EXPECTED_IDS, "module public operation coverage mismatch", errors)

    tasks = load_yaml(ROOT / "registry/domain-finalization/disciple/implementation-tasks.yaml")
    task_ids = [item.get("feature_id") for item in tasks.get("feature_tasks", [])]
    require(task_ids == EXPECTED_IDS, "implementation task coverage mismatch", errors)

    decision = load_yaml(ROOT / "registry/domain-finalization/disciple/decision-required.yaml")
    non_blocking_009 = any(
        item.get("decision_id") == "TLC-DISCIPLE-NONBLOCK-002"
        and item.get("classification") == "composite_feature_with_internal_operations"
        for item in decision.get("non_blocking", [])
    )
    require(non_blocking_009, "009 boundary decision missing", errors)

    required_algorithm_fields = {
        "signature", "inputs", "outputs", "validations", "preconditions", "ordered_steps",
        "branches", "state_transitions", "errors", "postconditions", "invariants",
        "determinism", "effects", "edge_cases", "unresolved_preserved", "dependencies",
        "complexity", "pseudocode",
    }
    required_ir_fields = {
        "feature_id", "source_contract_ref", "source_ir_ref", "source_ir_status",
        "representation_type", "inputs", "outputs", "types", "opaque_values",
        "preconditions", "operations", "execution_order", "control_flow", "states",
        "effects", "postconditions", "invariants", "errors", "determinism",
        "dependencies", "unresolved_propagated", "reservations", "links_to_tests",
        "transformations_applied", "preservation_obligations", "implementation_readiness",
    }

    for feature_id in EXPECTED_IDS:
        source_contract_path = ROOT / f"registry/math-contracts/{feature_id}/contract.yaml"
        source_registry_path = ROOT / f"registry/ir/{feature_id}/ir.yaml"
        source_ir_path = ROOT / f"ir/{feature_id}/ir.candidate.json"
        source_test_path = ROOT / f"registry/test-plans/{feature_id}/test-plan.yaml"
        open_questions_path = ROOT / f"registry/math-contracts/{feature_id}/open-math-questions.yaml"
        optimized_path = ROOT / f"registry/optimized-ir/disciple/{feature_id}/ir.yaml"
        algorithm_path = ROOT / f"registry/algorithms/disciple/{feature_id}/algorithm.yaml"
        oracle_path = ROOT / f"registry/oracles/disciple/{feature_id}/oracle.yaml"

        for path in (
            source_contract_path, source_registry_path, source_ir_path, source_test_path,
            open_questions_path, optimized_path, algorithm_path, oracle_path,
        ):
            require(path.is_file(), f"missing artifact: {path.relative_to(ROOT)}", errors)
        if not all(path.is_file() for path in (source_contract_path, source_registry_path, source_ir_path, source_test_path, open_questions_path, optimized_path, algorithm_path, oracle_path)):
            continue

        contract = load_yaml(source_contract_path)
        registry_ir = load_yaml(source_registry_path)
        source_ir = load_json(source_ir_path)
        source_test = load_yaml(source_test_path)
        open_questions = load_yaml(open_questions_path)
        optimized = load_yaml(optimized_path)
        algorithm = load_yaml(algorithm_path)
        oracle = load_yaml(oracle_path)

        for label, data in (
            ("contract", contract), ("registry IR", registry_ir), ("source IR", source_ir),
            ("test plan", source_test), ("optimized IR", optimized),
            ("algorithm", algorithm), ("oracle", oracle),
        ):
            require(data.get("feature_id") == feature_id, f"{label} feature_id mismatch for {feature_id}", errors)

        require(optimized.get("status") == EXPECTED_STATUS, f"optimized IR status mismatch for {feature_id}", errors)
        require(required_ir_fields.issubset(optimized), f"optimized IR fields missing for {feature_id}: {sorted(required_ir_fields - set(optimized))}", errors)
        for key, expected in (
            ("source_ir_preserved", True), ("source_contract_preserved", True),
            ("scientific_source_modified", False), ("replaces_source_ir", False),
        ):
            require(optimized.get(key) is expected, f"{key} mismatch for {feature_id}", errors)

        expected_contract_ref = f"registry/math-contracts/{feature_id}/contract.yaml"
        expected_source_ir_ref = f"ir/{feature_id}/ir.candidate.json"
        expected_test_ref = f"registry/test-plans/{feature_id}/test-plan.yaml"
        require(optimized.get("source_contract_ref") == expected_contract_ref, f"contract traceability mismatch for {feature_id}", errors)
        require(optimized.get("source_ir_ref") == expected_source_ir_ref, f"source IR traceability mismatch for {feature_id}", errors)
        require(optimized.get("source_test_plan_ref") == expected_test_ref, f"test-plan traceability mismatch for {feature_id}", errors)

        opaque = optimized.get("opaque_values", {})
        require(opaque.get("policy") == "preserve_identity_without_interpretation", f"opaque policy mismatch for {feature_id}", errors)
        require("OpaqueScientificValue" in optimized.get("types", {}).get("shared", []), f"OpaqueScientificValue missing for {feature_id}", errors)

        expected_unresolved = list(source_ir.get("unresolved", [])) + list(open_questions.get("questions", []))
        actual_unresolved = optimized.get("unresolved_propagated", [])
        require(set(expected_unresolved).issubset(set(actual_unresolved)), f"unresolved not conserved for {feature_id}: expected {expected_unresolved}, got {actual_unresolved}", errors)

        expected_master = list(dict.fromkeys(list(source_ir.get("master_subsymbols_unresolved", [])) + list(open_questions.get("master_subsymbols_unresolved", []))))
        actual_master = opaque.get("master_subsymbols", [])
        require(expected_master == actual_master, f"opaque Master subsymbol mismatch for {feature_id}: expected {expected_master}, got {actual_master}", errors)

        expected_reservations = source_status_by_id.get(feature_id, {}).get("scientific_unresolved", [])
        actual_reservations = optimized.get("reservations", [])
        require(set(expected_reservations).issubset(set(actual_reservations)), f"catalogue reservations not conserved for {feature_id}", errors)

        require(required_algorithm_fields.issubset(algorithm), f"algorithm fields missing for {feature_id}: {sorted(required_algorithm_fields - set(algorithm))}", errors)
        require(algorithm.get("optimized_ir_ref") == f"registry/optimized-ir/disciple/{feature_id}/ir.yaml", f"algorithm IR link mismatch for {feature_id}", errors)
        require(oracle.get("optimized_ir_ref") == f"registry/optimized-ir/disciple/{feature_id}/ir.yaml", f"oracle IR link mismatch for {feature_id}", errors)
        require(oracle.get("algorithm_ref") == f"registry/algorithms/disciple/{feature_id}/algorithm.yaml", f"oracle algorithm link mismatch for {feature_id}", errors)
        require(oracle.get("source_test_plan_ref") == expected_test_ref, f"oracle test-plan link mismatch for {feature_id}", errors)
        require(bool(oracle.get("acceptance_tests")), f"oracle has no acceptance tests for {feature_id}", errors)
        require(oracle.get("numerical_expected_results") == [], f"arbitrary numerical result present for {feature_id}", errors)

    paths = changed_paths()
    allowed_prefixes = (
        "registry/domain-finalization/disciple/",
        "registry/optimized-ir/disciple/",
        "registry/algorithms/disciple/",
        "registry/oracles/disciple/",
        "reports/domain-finalization/disciple/",
    )
    allowed_exact = {"tools/domain-finalization/validate_disciple_finalization.py"}
    if os.environ.get("DISCIPLE_ALLOW_TEMP_WORKFLOW") == "1":
        allowed_exact.add(TEMP_WORKFLOW)

    for path in paths:
        allowed = path in allowed_exact or path.startswith(allowed_prefixes)
        require(allowed, f"modified path outside Disciple finalization scope: {path}", errors)
        require(not path.startswith("maths/"), f"maths source modified: {path}", errors)
        require("MASTER" not in path.upper(), f"Master artifact modified: {path}", errors)
        require(not path.startswith("registry/global-reconciliation/"), f"global registry modified: {path}", errors)
        require(not path.startswith("registry/math-contracts/"), f"source contract modified: {path}", errors)
        require(not path.startswith("registry/ir/"), f"source IR registry modified: {path}", errors)
        require(not path.startswith("ir/TLC-FC-01-DISCIPLE-"), f"source IR artifact modified: {path}", errors)
        suffix = Path(path).suffix.lower()
        require(suffix not in {".cpp", ".cc", ".cxx", ".h", ".hh", ".hpp", ".pyi"}, f"implementation or binding file produced: {path}", errors)
        lowered = path.lower()
        require("reference-implementation" not in lowered and "reference_implementation" not in lowered, f"reference implementation produced: {path}", errors)

    require(len(EXPECTED_IDS) == 10, "internal validator feature count error", errors)

    if errors:
        print("DISCIPLE FINALIZATION VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DISCIPLE FINALIZATION VALIDATION PASSED")
    print("features=10 optimized_irs=10 algorithms=10 oracles=10")
    print("source_contracts_preserved=true source_irs_preserved=true maths_modified=false")
    print("master_modified=false global_registry_regenerated=false features_rejected=false")
    print("scientific_execution_ready=false implementation_specification_ready=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
