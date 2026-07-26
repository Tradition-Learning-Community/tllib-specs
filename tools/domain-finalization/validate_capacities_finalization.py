#!/usr/bin/env python3
"""Validate the Capacities domain-finalization specification package.

This validator uses only the Python standard library and Git metadata. It does
not evaluate any scientific expression and does not modify repository files.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE_HEAD = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
FEATURES = [
    "TLC-FC-11-CAPACITIES-001",
    "TLC-FC-11-CAPACITIES-002",
    "TLC-FC-11-CAPACITIES-003",
    "TLC-FC-11-CAPACITIES-005",
    "TLC-FC-11-CAPACITIES-006",
    "TLC-FC-11-CAPACITIES-007",
    "TLC-FC-11-CAPACITIES-008",
    "TLC-FC-11-CAPACITIES-009",
    "TLC-FC-11-CAPACITIES-010",
    "TLC-FC-11-CAPACITIES-011",
    "TLC-FC-11-CAPACITIES-012",
    "TLC-FC-11-CAPACITIES-013",
    "TLC-FC-11-CAPACITIES-014",
    "TLC-FC-11-CAPACITIES-015",
    "TLC-FC-11-CAPACITIES-018",
]
DEFERRED = {
    "TLC-FC-11-CAPACITIES-002",
    "TLC-FC-11-CAPACITIES-003",
    "TLC-FC-11-CAPACITIES-006",
    "TLC-FC-11-CAPACITIES-007",
    "TLC-FC-11-CAPACITIES-009",
    "TLC-FC-11-CAPACITIES-011",
    "TLC-FC-11-CAPACITIES-012",
    "TLC-FC-11-CAPACITIES-014",
    "TLC-FC-11-CAPACITIES-015",
}
LEGACY = {f"TLC-FC-11-CAP-{index:03d}" for index in range(1, 10)}
TEMP_WORKFLOW = ".github/workflows/validate-capacities-finalization.yml"


class ValidationError(RuntimeError):
    pass


def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        raise ValidationError(f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def require_tokens(text: str, tokens: list[str], path: str) -> None:
    missing = [token for token in tokens if token not in text]
    require(not missing, f"{path}: missing required tokens: {missing}")


def git(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=ROOT, check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise ValidationError(
            f"git {' '.join(args)} failed: {completed.stderr.strip()}"
        )
    return completed.stdout


def changed_paths() -> list[str]:
    return [line for line in git("diff", "--name-only", f"{BASE_HEAD}...HEAD").splitlines() if line]


def validate_population() -> None:
    baseline = read("registry/global-reconciliation/current-baseline.yaml")
    matrix = read("registry/global-reconciliation/domain-feature-matrix.yaml")
    manifest = read("registry/domain-finalization/capacities/manifest.yaml")
    status = read("registry/domain-finalization/capacities/feature-status.yaml")

    matrix_ids = sorted(set(re.findall(
        r"feature_id:\s*(TLC-FC-11-CAPACITIES-\d+)", matrix
    )))
    manifest_ids = re.findall(
        r"^\s*-\s+(TLC-FC-11-CAPACITIES-\d+)\s*$", manifest, re.MULTILINE
    )
    status_ids = re.findall(
        r"^\s*- feature_id:\s*(TLC-FC-11-CAPACITIES-\d+)\s*$",
        status, re.MULTILINE,
    )

    require("feature_count: 15" in baseline, "baseline does not confirm 15 Capacities features")
    require(matrix_ids == FEATURES, f"authoritative matrix population mismatch: {matrix_ids}")
    require(manifest_ids == FEATURES, f"manifest population mismatch: {manifest_ids}")
    require(status_ids == FEATURES, f"feature-status population mismatch: {status_ids}")
    require(len(FEATURES) == 15, "validator feature population is not 15")
    require(not (set(manifest_ids) & LEGACY), "legacy Goose id counted as active")
    require("legacy_ids_counted_as_active: false" in manifest, "legacy active guard absent")
    require("legacy_ids_authoritative: false" in manifest, "legacy authority guard absent")


def validate_feature_artifacts() -> None:
    ir_required = [
        "status: selected_for_capacities_implementation_specification",
        "source_ir_status: prototype_ir_with_reservations",
        "capacity_or_reference:", "identity:", "scope:", "context:",
        "inputs:", "outputs:", "types:", "opaque_values:",
        "preconditions:", "conditions_of_application:",
        "relations_explicitly_defined:", "operations:", "execution_order:",
        "control_flow:", "activation:", "mobilization:", "development:",
        "comparison:", "effects:", "postconditions:", "invariants:",
        "errors:", "determinism:", "dependencies:",
        "unresolved_propagated:", "reservations:",
        "transformations_applied:", "obligations_of_preservation:",
        "implementation_fitness:",
        "source_ir_preserved: true", "source_contract_preserved: true",
        "replaces_source_ir: false", "scientific_source_modified: false",
        "capacity_invented: false", "measurement_invented: false",
        "ordering_invented: false", "legacy_feature_promoted: false",
    ]
    algorithm_required = [
        "status: selected_for_capacities_implementation_specification",
        "signature:", "inputs:", "outputs:", "validations:",
        "preconditions:", "conditions_of_application:", "steps:",
        "branching:", "capacity_handling:", "relations:", "activation:",
        "mobilization:", "development:", "comparison:", "effects:",
        "errors:", "postconditions:", "invariants:", "determinism:",
        "case_limits:", "unresolved_conserved:", "dependencies:",
        "pseudocode: |",
    ]
    oracle_required = [
        "status: selected_for_capacities_implementation_specification",
        "source_test_plan:", "algorithm:", "exact_result_available: false",
        "oracle_basis:", "acceptance_tests:", "properties:",
        "metamorphic_tests:", "composition_tests:", "dependency_tests:",
        "pass_condition:",
    ]

    for feature_id in FEATURES:
        contract = f"registry/math-contracts/{feature_id}/contract.yaml"
        source_ir = f"registry/ir/{feature_id}/ir.yaml"
        test_plan = f"registry/test-plans/{feature_id}/test-plan.yaml"
        final_ir = f"registry/optimized-ir/capacities/{feature_id}/ir.yaml"
        algorithm = f"registry/algorithms/capacities/{feature_id}/algorithm.yaml"
        oracle = f"registry/oracles/capacities/{feature_id}/oracle.yaml"

        contract_text = read(contract)
        source_ir_text = read(source_ir)
        test_plan_text = read(test_plan)
        final_ir_text = read(final_ir)
        algorithm_text = read(algorithm)
        oracle_text = read(oracle)

        require(f"feature_id: {feature_id}" in contract_text, f"{contract}: feature id mismatch")
        require(f"feature_id: {feature_id}" in source_ir_text, f"{source_ir}: feature id mismatch")
        require(f"feature_id: {feature_id}" in test_plan_text, f"{test_plan}: feature id mismatch")
        require(f"feature_id: {feature_id}" in final_ir_text, f"{final_ir}: feature id mismatch")
        require(f"feature_id: {feature_id}" in algorithm_text, f"{algorithm}: feature id mismatch")
        require(f"feature_id: {feature_id}" in oracle_text, f"{oracle}: feature id mismatch")

        require_tokens(final_ir_text, ir_required, final_ir)
        require_tokens(algorithm_text, algorithm_required, algorithm)
        require_tokens(oracle_text, oracle_required, oracle)

        require(f"source_contract: {contract}" in final_ir_text, f"{final_ir}: contract trace missing")
        require(f"source_ir: {source_ir}" in final_ir_text, f"{final_ir}: source IR trace missing")
        require(f"source_test_plan: {test_plan}" in final_ir_text, f"{final_ir}: source test trace missing")
        require(f"source_ir: {final_ir}" in algorithm_text, f"{algorithm}: finalized IR trace missing")
        require(f"algorithm: {algorithm}" in oracle_text, f"{oracle}: algorithm trace missing")
        require(f"source_test_plan: {test_plan}" in oracle_text, f"{oracle}: test plan trace missing")

        if feature_id in DEFERRED:
            require("scientific decision required" in final_ir_text, f"{final_ir}: unresolved blocker lost")
            require("scientific decision required" in algorithm_text, f"{algorithm}: unresolved blocker lost")
            require("scientific decision required" in oracle_text, f"{oracle}: unresolved blocker lost")

        combined = final_ir_text + algorithm_text + oracle_text
        require("invented: true" not in combined, f"{feature_id}: invented content flag found")
        require("legacy_feature_promoted: true" not in combined, f"{feature_id}: legacy promotion found")
        require("status: rejected" not in combined, f"{feature_id}: feature rejected")


def validate_module_package() -> None:
    required = [
        "registry/domain-finalization/capacities/manifest.yaml",
        "registry/domain-finalization/capacities/feature-status.yaml",
        "registry/domain-finalization/capacities/patterns.yaml",
        "registry/domain-finalization/capacities/module-specification.yaml",
        "registry/domain-finalization/capacities/implementation-tasks.yaml",
        "registry/domain-finalization/capacities/decision-required.yaml",
        "reports/domain-finalization/capacities/finalization-report.md",
        "tools/domain-finalization/validate_capacities_finalization.py",
    ]
    for path in required:
        read(path)

    module = read("registry/domain-finalization/capacities/module-specification.yaml")
    tasks = read("registry/domain-finalization/capacities/implementation-tasks.yaml")
    decisions = read("registry/domain-finalization/capacities/decision-required.yaml")
    patterns = read("registry/domain-finalization/capacities/patterns.yaml")

    for feature_id in FEATURES:
        require(feature_id in module, f"module specification missing {feature_id}")
        require(feature_id in tasks, f"implementation tasks missing {feature_id}")
    require("blocking_decisions: []" in decisions, "unexpected blocking decision recorded")
    require("blocking: 0" in decisions, "decision summary does not report zero blockers")
    require("internal_execution_dependencies: []" in patterns, "unexpected internal execution dependency")
    require("external_execution_dependencies: []" in patterns, "unexpected external execution dependency")
    require("computed_measurement: false" in module, "module permits computed measurement")
    require("activation_engine: implementation_out_of_scope" in module, "module permits activation engine")
    require("capacity_comparator: external_comparator_required" in module, "comparison boundary absent")


def validate_changed_paths() -> None:
    changed = changed_paths()
    require(changed, "no changed paths found")

    allowed_prefixes = (
        "registry/domain-finalization/capacities/",
        "registry/optimized-ir/capacities/",
        "registry/algorithms/capacities/",
        "registry/oracles/capacities/",
    )
    allowed_exact = {
        "reports/domain-finalization/capacities/finalization-report.md",
        "tools/domain-finalization/validate_capacities_finalization.py",
        TEMP_WORKFLOW,
    }
    disallowed = [
        path for path in changed
        if not path.startswith(allowed_prefixes) and path not in allowed_exact
    ]
    require(not disallowed, f"paths outside Capacities finalization scope: {disallowed}")

    forbidden_prefixes = (
        "maths/", "registry/global-reconciliation/", "registry/math-contracts/",
        "registry/ir/", "registry/test-plans/",
    )
    forbidden = [path for path in changed if path.startswith(forbidden_prefixes)]
    require(not forbidden, f"protected source/global paths modified: {forbidden}")

    domain_roots = (
        "registry/domain-finalization/",
        "reports/domain-finalization/",
    )
    other_domains = [
        path for path in changed
        if path.startswith(domain_roots) and "/capacities/" not in path
    ]
    require(not other_domains, f"other domain finalization artifacts modified: {other_domains}")

    compiled = [
        path for path in changed
        if Path(path).suffix.lower() in {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp"}
    ]
    require(not compiled, f"C or C++ files found: {compiled}")
    binding_paths = [path for path in changed if "binding" in path.lower() or "pybind" in path.lower()]
    require(not binding_paths, f"binding files found: {binding_paths}")
    python_files = [path for path in changed if path.endswith(".py")]
    require(python_files == ["tools/domain-finalization/validate_capacities_finalization.py"],
            f"unexpected Python implementation file: {python_files}")


def validate_diff_whitespace() -> None:
    completed = subprocess.run(
        ["git", "diff", "--check", f"{BASE_HEAD}...HEAD"],
        cwd=ROOT, check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    require(completed.returncode == 0,
            f"git diff --check failed: {completed.stdout}{completed.stderr}")


def main() -> int:
    checks = [
        ("population", validate_population),
        ("feature artifacts", validate_feature_artifacts),
        ("module package", validate_module_package),
        ("changed paths", validate_changed_paths),
        ("diff whitespace", validate_diff_whitespace),
    ]
    try:
        for name, check in checks:
            check()
            print(f"PASS: {name}")
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("CAPACITIES_FINALIZATION_VALIDATION: PASS")
    print(f"validated_features: {len(FEATURES)}")
    print(f"base_head: {BASE_HEAD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
