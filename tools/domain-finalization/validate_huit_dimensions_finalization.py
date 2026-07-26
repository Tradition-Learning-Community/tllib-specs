#!/usr/bin/env python3
"""Validate the Huit Dimensions implementation-specification package."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "huit-dimensions"
PREFIX = "TLC-FC-03-HUIT-DIMENSIONS-DE-TL-"
EXPECTED_STATUS = "selected_for_huit_dimensions_implementation_specification"
TEMP_WORKFLOW = ".github/workflows/huit-dimensions-finalization-validation.yml"
ALLOWED_PREFIXES = (
    "registry/domain-finalization/huit-dimensions/",
    "registry/optimized-ir/huit-dimensions/",
    "registry/algorithms/huit-dimensions/",
    "registry/oracles/huit-dimensions/",
    "reports/domain-finalization/huit-dimensions/",
)
ALLOWED_EXACT = {
    "tools/domain-finalization/validate_huit_dimensions_finalization.py",
    TEMP_WORKFLOW,
}
FORBIDDEN_PATH_PARTS = (
    "/master/",
    "/disciple/",
    "/community/",
    "registry/global-reconciliation/",
    "maths/",
    "reference-implementation",
    "reference_implementation",
    "bindings/",
)
CPP_SUFFIXES = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx"}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")


def required_feature_paths(feature_id: str) -> dict[str, Path]:
    return {
        "contract": ROOT / f"registry/math-contracts/{feature_id}/contract.yaml",
        "source_ir": ROOT / f"ir/{feature_id}/ir.prototype.json",
        "test_plan": ROOT / f"ir/{feature_id}/test-plan.yaml",
        "final_ir": ROOT / f"registry/optimized-ir/huit-dimensions/{feature_id}/ir.yaml",
        "algorithm": ROOT / f"registry/algorithms/huit-dimensions/{feature_id}/algorithm.yaml",
        "oracle": ROOT / f"registry/oracles/huit-dimensions/{feature_id}/oracle.yaml",
    }


def validate_changed_paths() -> list[str]:
    git("diff", "--check", "origin/main...HEAD")
    changed = [line for line in git("diff", "--name-only", "origin/main...HEAD").stdout.splitlines() if line]
    if not changed:
        fail("no changed paths found")
    for path in changed:
        allowed = path in ALLOWED_EXACT or any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)
        if not allowed:
            fail(f"changed path outside mission scope: {path}")
        normalized = f"/{path.lower()}"
        if any(part in normalized for part in FORBIDDEN_PATH_PARTS):
            fail(f"forbidden path modified: {path}")
        if Path(path).suffix.lower() in CPP_SUFFIXES:
            fail(f"C/C++ artifact is forbidden: {path}")
        if path.endswith(".py") and path != "tools/domain-finalization/validate_huit_dimensions_finalization.py":
            fail(f"Python implementation or binding is forbidden: {path}")
        if "__pycache__" in path or path.endswith(".status") or "/cache" in normalized or "/logs" in normalized:
            fail(f"temporary artifact is forbidden: {path}")
    return changed


def main() -> int:
    manifest_path = ROOT / "registry/domain-finalization/huit-dimensions/manifest.yaml"
    status_path = ROOT / "registry/domain-finalization/huit-dimensions/feature-status.yaml"
    patterns_path = ROOT / "registry/domain-finalization/huit-dimensions/patterns.yaml"
    module_path = ROOT / "registry/domain-finalization/huit-dimensions/module-specification.yaml"
    tasks_path = ROOT / "registry/domain-finalization/huit-dimensions/implementation-tasks.yaml"
    decisions_path = ROOT / "registry/domain-finalization/huit-dimensions/decision-required.yaml"
    report_path = ROOT / "reports/domain-finalization/huit-dimensions/finalization-report.md"
    for path in (manifest_path, status_path, patterns_path, module_path, tasks_path, decisions_path, report_path):
        require_file(path)

    manifest = load_yaml(manifest_path)
    feature_status = load_yaml(status_path)
    module = load_yaml(module_path)
    tasks = load_yaml(tasks_path)
    decisions = load_yaml(decisions_path)

    entries = manifest.get("active_features", [])
    expected_ids = [entry["feature_id"] for entry in entries]
    if manifest.get("active_feature_count") != 11 or len(expected_ids) != 11 or len(set(expected_ids)) != 11:
        fail("manifest must contain exactly eleven distinct active features")

    baseline = load_yaml(ROOT / "registry/global-reconciliation/current-baseline.yaml")
    baseline_rows = [
        item for item in walk(baseline)
        if isinstance(item, dict) and item.get("domain_id") == DOMAIN
    ]
    if len(baseline_rows) != 1:
        fail("unable to identify exactly one Huit Dimensions baseline row")
    if baseline_rows[0].get("feature_count") != 11:
        fail("baseline does not confirm exactly eleven active features")

    matrix = load_yaml(ROOT / "registry/global-reconciliation/domain-feature-matrix.yaml")
    matrix_ids = {
        item["feature_id"] for item in walk(matrix)
        if isinstance(item, dict)
        and isinstance(item.get("feature_id"), str)
        and item["feature_id"].startswith(PREFIX)
    }
    if matrix_ids != set(expected_ids):
        fail(f"domain-feature matrix population mismatch: {sorted(matrix_ids)}")

    status_ids = [entry["feature_id"] for entry in feature_status.get("features", [])]
    if status_ids != expected_ids:
        fail("feature-status population or order differs from manifest")
    if feature_status.get("summary", {}).get("rejected") != 0:
        fail("a feature was rejected")
    for entry in feature_status["features"]:
        if entry.get("final_status") != EXPECTED_STATUS:
            fail(f"feature not selected: {entry['feature_id']}")

    source_locks = {entry["feature_id"]: entry for entry in entries}
    public_operations = {entry["feature_id"]: entry["name"] for entry in module.get("public_operations", [])}
    task_features = {entry["feature_id"] for entry in tasks.get("feature_tasks", [])}
    if set(public_operations) != set(expected_ids) or task_features != set(expected_ids):
        fail("module public operations or implementation tasks do not cover the exact population")
    if decisions.get("blocking") not in ([], None):
        fail("blocking decisions remain")

    for feature_id in expected_ids:
        paths = required_feature_paths(feature_id)
        for path in paths.values():
            require_file(path)

        lock = source_locks[feature_id]
        for key, ref_key, sha_key in (
            ("contract", "contract_ref", "contract_blob_sha"),
            ("source_ir", "source_ir_ref", "source_ir_blob_sha"),
            ("test_plan", "source_test_plan_ref", "source_test_plan_blob_sha"),
        ):
            expected_path = ROOT / lock[ref_key]
            if paths[key] != expected_path:
                fail(f"source path mismatch for {feature_id}: {key}")
            if git_blob_sha(expected_path) != lock[sha_key]:
                fail(f"source blob changed for {feature_id}: {expected_path.relative_to(ROOT)}")

        contract = load_yaml(paths["contract"])
        source_ir = load_json(paths["source_ir"])
        test_plan = load_yaml(paths["test_plan"])
        final_ir = load_yaml(paths["final_ir"])
        algorithm = load_yaml(paths["algorithm"])
        oracle = load_yaml(paths["oracle"])

        for artifact_name, artifact in (
            ("contract", contract),
            ("source_ir", source_ir),
            ("test_plan", test_plan),
            ("final_ir", final_ir),
            ("algorithm", algorithm),
            ("oracle", oracle),
        ):
            if artifact.get("feature_id") != feature_id:
                fail(f"{artifact_name} feature id mismatch for {feature_id}")

        source_operation = contract.get("primary_operation", {}).get("name")
        ir_operations = source_ir.get("operations", [])
        final_operations = final_ir.get("operations", [])
        if not source_operation or not ir_operations or not final_operations:
            fail(f"missing operation trace for {feature_id}")
        operations = {
            source_operation,
            ir_operations[0].get("name"),
            test_plan.get("primary_operation"),
            final_operations[0].get("name"),
            algorithm.get("operation"),
            oracle.get("operation"),
            public_operations.get(feature_id),
        }
        if len(operations) != 1:
            fail(f"IR -> algorithm -> oracle operation mismatch for {feature_id}: {operations}")

        contract_output = contract.get("outputs", [{}])[0].get("type")
        source_output = source_ir.get("outputs", [{}])[0].get("type")
        final_output = final_ir.get("outputs", [{}])[0].get("type")
        if len({contract_output, source_output, final_output}) != 1:
            fail(f"output type mismatch for {feature_id}")

        required_ir_fields = (
            "inputs", "outputs", "types", "opaque_values", "preconditions", "operations",
            "order_of_execution", "control_flow", "states_and_effects", "postconditions",
            "invariants", "errors", "determinism", "dependencies", "unresolved_propagated",
            "reservations", "transformations_applied", "preservation_obligations",
            "algorithm_ref", "oracle_ref", "implementation_readiness",
        )
        for field in required_ir_fields:
            if field not in final_ir:
                fail(f"final IR field {field} missing for {feature_id}")
        if final_ir.get("status") != EXPECTED_STATUS:
            fail(f"invalid final IR status for {feature_id}")
        for field, expected in (
            ("source_ir_preserved", True),
            ("source_contract_preserved", True),
            ("replaces_source_ir", False),
            ("scientific_source_modified", False),
        ):
            if final_ir.get(field) is not expected:
                fail(f"preservation flag {field} invalid for {feature_id}")

        source_unresolved = set(source_ir.get("unresolved_propagated", []))
        contract_unresolved = set(contract.get("scientific_reservations", []))
        final_unresolved = set(final_ir.get("unresolved_propagated", []))
        algorithm_unresolved = set(algorithm.get("unresolved_conserved", []))
        if not source_unresolved or not (source_unresolved == contract_unresolved == final_unresolved == algorithm_unresolved):
            fail(f"unresolved propagation mismatch for {feature_id}")

        categories = {test.get("category") for test in oracle.get("tests", [])}
        required_categories = {"nominal", "determinism", "opaque_propagation", "unresolved_propagation", "contract_ir_algorithm_conformance"}
        if not required_categories.issubset(categories):
            fail(f"oracle categories incomplete for {feature_id}: {required_categories - categories}")
        if oracle.get("numeric_expected_results") != []:
            fail(f"arbitrary numeric oracle values detected for {feature_id}")
        if not algorithm.get("pseudocode") or not algorithm.get("signature"):
            fail(f"algorithm is not directly specified for {feature_id}")
        if not final_ir.get("opaque_values"):
            fail(f"opaque value conservation missing for {feature_id}")

    for artifact_root in (
        ROOT / "registry/optimized-ir/huit-dimensions",
        ROOT / "registry/algorithms/huit-dimensions",
        ROOT / "registry/oracles/huit-dimensions",
    ):
        actual = {path.name for path in artifact_root.iterdir() if path.is_dir()}
        if actual != set(expected_ids):
            fail(f"unexpected feature directories under {artifact_root.relative_to(ROOT)}")

    changed = validate_changed_paths()
    print("Huit Dimensions finalization validation: PASS")
    print(f"Active features: {len(expected_ids)}")
    print(f"Finalized IRs: {len(expected_ids)}")
    print(f"Algorithms: {len(expected_ids)}")
    print(f"Oracles: {len(expected_ids)}")
    print(f"Changed paths checked: {len(changed)}")
    print("Source contracts, source IRs, test plans, maths, global registry, and other domains preserved.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, FileNotFoundError, KeyError, TypeError, ValueError) as exc:
        print(f"Huit Dimensions finalization validation: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
