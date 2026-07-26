#!/usr/bin/env python3
"""Validate the Practice domain finalization package without executing science."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to validate YAML artifacts") from exc

ROOT = Path(__file__).resolve().parents[2]
BASE_HEAD = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
SELECTED = "selected_for_practice_implementation_specification"
FEATURES = [
    "TLC-FC-13-PRACTICE-001",
    "TLC-FC-13-PRACTICE-003",
    "TLC-FC-13-PRACTICE-004",
    "TLC-FC-13-PRACTICE-005",
    "TLC-FC-13-PRACTICE-006",
    "TLC-FC-13-PRACTICE-007",
    "TLC-FC-13-PRACTICE-008",
    "TLC-FC-13-PRACTICE-009",
    "TLC-FC-13-PRACTICE-010",
    "TLC-FC-13-PRACTICE-012",
]
REQUIRED_FLAGS = {
    "source_ir_preserved": True,
    "source_contract_preserved": True,
    "replaces_source_ir": False,
    "scientific_source_modified": False,
    "practice_invented": False,
    "sequence_invented": False,
    "duration_invented": False,
    "frequency_invented": False,
    "effect_invented": False,
}
EMPTY_PROCEDURAL_FIELDS = [
    "steps_explicitly_defined",
    "repetitions_declared",
    "transitions_declared",
    "stop_conditions_declared",
    "results_declared",
    "effects_declared",
]
TEMP_WORKFLOW = ".github/workflows/validate-practice-finalization-temp.yml"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_yaml(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing file: {relative}")
    with path.open("r", encoding="utf-8-sig") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        fail(f"expected mapping in {relative}")
    return data


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode != 0:
        fail(f"git {' '.join(args)} failed:\n{result.stdout}{result.stderr}")
    return result.stdout


def ids(items: list[dict[str, Any]], key: str) -> list[str]:
    return [str(item[key]) for item in items]


def normalize_statement(value: str) -> str:
    return value.strip().rstrip(".").lower()


def authoritative_population() -> list[str]:
    baseline = load_yaml("registry/global-reconciliation/current-baseline.yaml")
    practice_rows = [
        row for row in baseline.get("domains", []) if row.get("domain_id") == "practice"
    ]
    if len(practice_rows) != 1:
        fail("baseline must contain one Practice domain row")
    row = practice_rows[0]
    if row.get("feature_count") != 10:
        fail("baseline does not confirm exactly 10 Practice features")
    if row.get("contracts_present") != 10 or row.get("ir_artifacts_present") != 10:
        fail("baseline Practice source layer is incomplete")
    if row.get("test_plans_present") != 10:
        fail("baseline does not confirm 10 Practice test plans")

    matrix = load_yaml("registry/global-reconciliation/domain-feature-matrix.yaml")
    population = [
        str(item["feature_id"])
        for item in matrix.get("features", matrix.get("rows", []))
        if item.get("domain") == "practice"
    ]
    if population != FEATURES:
        fail(f"authoritative population mismatch: {population}")
    return population


def validate_module_files() -> None:
    manifest = load_yaml("registry/domain-finalization/practice/manifest.yaml")
    if manifest.get("features") != FEATURES or manifest.get("feature_count") != 10:
        fail("finalization manifest population mismatch")
    if manifest.get("status") != "ready_for_implementation_package":
        fail("manifest is not closed as implementation package")
    preservation = manifest.get("preservation", {})
    if preservation.get("rejected_features") != []:
        fail("a Practice feature was rejected")
    if preservation.get("declarative_irs_rejected_for_non_executability") != []:
        fail("a declarative IR was rejected for non-executability")

    status = load_yaml("registry/domain-finalization/practice/feature-status.yaml")
    rows = status.get("features", [])
    if ids(rows, "feature_id") != FEATURES:
        fail("feature-status population mismatch")
    if status.get("rejected_features") != []:
        fail("feature-status contains rejected features")
    for row in rows:
        if row.get("finalization_status") != SELECTED:
            fail(f"feature not selected: {row.get('feature_id')}")

    module = load_yaml("registry/domain-finalization/practice/module-specification.yaml")
    if module.get("feature_population") != FEATURES:
        fail("module population mismatch")
    if module.get("internal_dependencies", {}).get("canonical_functional_edges") != []:
        fail("an unsupported Practice functional dependency was introduced")
    procedural = module.get("explicitly_declared_procedural_elements", {})
    for value in procedural.values():
        if value != []:
            fail("module invents an executable procedural element")

    decisions = load_yaml("registry/domain-finalization/practice/decision-required.yaml")
    if decisions.get("blocking_for_structural_implementation") != []:
        fail("structural implementation is incorrectly blocked")
    if decisions.get("closure", {}).get("new_scientific_decision_made") is not False:
        fail("decision registry claims a new scientific decision")

    tasks = load_yaml("registry/domain-finalization/practice/implementation-tasks.yaml")
    task_features = [item["feature_id"] for item in tasks.get("feature_tasks", [])]
    if task_features != FEATURES:
        fail("implementation tasks do not cover the exact population")

    load_yaml("registry/domain-finalization/practice/patterns.yaml")


def validate_feature(feature_id: str) -> None:
    contract_ref = f"registry/math-contracts/{feature_id}/contract.yaml"
    source_ir_ref = f"registry/ir/{feature_id}/ir.yaml"
    test_plan_ref = f"registry/test-plans/{feature_id}/test-plan.yaml"
    optimized_ref = f"registry/optimized-ir/practice/{feature_id}/ir.yaml"
    algorithm_ref = f"registry/algorithms/practice/{feature_id}/algorithm.yaml"
    oracle_ref = f"registry/oracles/practice/{feature_id}/oracle.yaml"

    contract = load_yaml(contract_ref)
    source_ir = load_yaml(source_ir_ref)
    test_plan = load_yaml(test_plan_ref)
    optimized = load_yaml(optimized_ref)
    algorithm = load_yaml(algorithm_ref)
    oracle = load_yaml(oracle_ref)

    if contract.get("feature_id") != feature_id:
        fail(f"contract feature mismatch for {feature_id}")
    if source_ir.get("feature_id") != feature_id:
        fail(f"source IR feature mismatch for {feature_id}")
    if test_plan.get("feature_id") != feature_id:
        fail(f"test plan feature mismatch for {feature_id}")
    if test_plan.get("contract_ref") != contract_ref or test_plan.get("ir_ref") != source_ir_ref:
        fail(f"source test-plan traceability mismatch for {feature_id}")

    if optimized.get("feature_id") != feature_id or optimized.get("status") != SELECTED:
        fail(f"finalized IR identity or status mismatch for {feature_id}")
    if optimized.get("source_contract_ref") != contract_ref:
        fail(f"contract trace missing for {feature_id}")
    if optimized.get("source_ir_ref") != source_ir_ref:
        fail(f"source IR trace missing for {feature_id}")
    if optimized.get("source_test_plan_ref") != test_plan_ref:
        fail(f"test-plan trace missing for {feature_id}")
    if optimized.get("source_contract_status") != contract.get("status"):
        fail(f"raw contract status changed for {feature_id}")
    if optimized.get("source_ir_status") != source_ir.get("status"):
        fail(f"raw IR status changed for {feature_id}")

    for key, expected in REQUIRED_FLAGS.items():
        if optimized.get(key) is not expected:
            fail(f"{feature_id}: {key} must be {expected}")
    if optimized.get("step_invented") is not False or optimized.get("progression_invented") is not False:
        fail(f"{feature_id}: step or progression invention flag")
    for field in EMPTY_PROCEDURAL_FIELDS:
        if optimized.get(field) != []:
            fail(f"{feature_id}: undeclared procedural field {field} is not empty")
    if optimized.get("order_explicitly_defined") is not False:
        fail(f"{feature_id}: executable order was invented")

    source_objects = ids(contract.get("covered_objects", []), "object_id")
    final_objects = ids(optimized.get("practice_reference", {}).get("covered_objects", []), "object_id")
    if final_objects != source_objects:
        fail(f"covered object mismatch for {feature_id}: {final_objects} != {source_objects}")

    source_inputs = ids(contract.get("inputs", []), "input_id")
    final_inputs = ids(optimized.get("inputs", []), "input_id")
    source_outputs = ids(contract.get("outputs", []), "output_id")
    final_outputs = ids(optimized.get("outputs", []), "output_id")
    if final_inputs != source_inputs or final_outputs != source_outputs:
        fail(f"input/output mismatch for {feature_id}")

    source_unresolved = contract.get("unresolved_propagated", [])
    if optimized.get("unresolved_propagated") != source_unresolved:
        fail(f"unresolved values changed for {feature_id}")
    source_decisions = contract.get("scientific_decisions_required", [])
    if optimized.get("scientific_decisions_required") != source_decisions:
        fail(f"scientific decisions changed for {feature_id}")

    source_preconditions = contract.get("preconditions", [])
    final_preconditions = optimized.get("preconditions", [])
    if len(source_preconditions) != len(final_preconditions):
        fail(f"precondition count changed for {feature_id}")
    for source, final in zip(source_preconditions, final_preconditions):
        if normalize_statement(str(source)) != normalize_statement(str(final)):
            fail(f"precondition changed for {feature_id}")

    if optimized.get("scope", {}).get("kind") != "descriptive_scope":
        fail(f"scope is not preserved as descriptive for {feature_id}")
    if optimized.get("context", {}).get("kind") != "descriptive_context":
        fail(f"context is not preserved as descriptive for {feature_id}")

    if algorithm.get("feature_id") != feature_id or algorithm.get("status") != SELECTED:
        fail(f"algorithm identity/status mismatch for {feature_id}")
    if algorithm.get("ir_ref") != optimized_ref:
        fail(f"algorithm does not link to finalized IR for {feature_id}")
    for field in ["repetitions", "transitions", "stop_conditions", "effects"]:
        if algorithm.get(field) != []:
            fail(f"algorithm invents {field} for {feature_id}")
    if algorithm.get("ordered_steps_declared") is not False:
        fail(f"algorithm invents ordered steps for {feature_id}")

    if oracle.get("feature_id") != feature_id or oracle.get("status") != SELECTED:
        fail(f"oracle identity/status mismatch for {feature_id}")
    if oracle.get("ir_ref") != optimized_ref or oracle.get("algorithm_ref") != algorithm_ref:
        fail(f"oracle trace mismatch for {feature_id}")
    if oracle.get("source_test_plan_ref") != test_plan_ref:
        fail(f"oracle source test-plan trace mismatch for {feature_id}")
    if oracle.get("expected_object_ids") != source_objects:
        fail(f"oracle object set mismatch for {feature_id}")
    if oracle.get("expected_input_ids") != source_inputs:
        fail(f"oracle input set mismatch for {feature_id}")
    if oracle.get("expected_output_ids") != source_outputs:
        fail(f"oracle output set mismatch for {feature_id}")
    if oracle.get("expected_unresolved") != source_unresolved:
        fail(f"oracle unresolved set mismatch for {feature_id}")
    if oracle.get("expected_scientific_decisions") != source_decisions:
        fail(f"oracle decision set mismatch for {feature_id}")
    if oracle.get("scientific_execution_oracle_available") is not False:
        fail(f"oracle improperly claims scientific execution for {feature_id}")


def validate_changed_paths() -> None:
    changed = [line for line in run_git("diff", "--name-only", f"{BASE_HEAD}...HEAD").splitlines() if line]
    if not changed:
        fail("no finalization files changed")
    allowed_prefixes = (
        "registry/domain-finalization/practice/",
        "registry/optimized-ir/practice/",
        "registry/algorithms/practice/",
        "registry/oracles/practice/",
    )
    allowed_exact = {
        "reports/domain-finalization/practice/finalization-report.md",
        "tools/domain-finalization/validate_practice_finalization.py",
        TEMP_WORKFLOW,
    }
    for path in changed:
        if path in allowed_exact or path.startswith(allowed_prefixes):
            continue
        fail(f"path outside Practice finalization scope: {path}")
    forbidden_markers = (
        "maths/",
        "registry/global-reconciliation/",
        "registry/math-contracts/",
        "registry/ir/TLC-FC-13-PRACTICE-",
        "registry/test-plans/",
    )
    for path in changed:
        if path.startswith(forbidden_markers):
            fail(f"protected source path modified: {path}")
        if path.endswith((".cpp", ".cc", ".cxx", ".hpp", ".h")):
            fail(f"C++ file introduced: {path}")
        if "binding" in path.lower() or "reference_implementation" in path.lower():
            fail(f"binding or reference implementation introduced: {path}")
        if path.endswith(".status") or "__pycache__" in path or "/.cache/" in path:
            fail(f"temporary artifact introduced: {path}")
    run_git("diff", "--check", f"{BASE_HEAD}...HEAD")


def main() -> int:
    population = authoritative_population()
    if population != FEATURES or len(population) != 10:
        fail("Practice population is not exactly authoritative 10")
    validate_module_files()
    for feature_id in FEATURES:
        validate_feature(feature_id)
    validate_changed_paths()
    print("PASS: Practice finalization validated")
    print("PASS: exact authoritative population = 10")
    print("PASS: 10 finalized IRs, 10 algorithms, 10 oracles")
    print("PASS: source contracts, source IRs, test plans and maths are untouched")
    print("PASS: no feature rejected and no declarative IR rejected for non-executability")
    print("PASS: no invented practice, step, sequence, duration, frequency, progression or effect")
    print("PASS: no C++ code, Python binding or reference implementation")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
