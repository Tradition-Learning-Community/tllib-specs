#!/usr/bin/env python3
"""Validate the Master domain finalization package without interpreting science."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_FEATURES = [f"TLC-FC-00-MASTER-{index:03d}" for index in range(1, 17)]
STATUS = "selected_for_master_implementation_specification"
ALLOWED_PREFIXES = (
    "registry/domain-finalization/master/",
    "registry/optimized-ir/master/",
    "registry/algorithms/master/",
    "registry/oracles/master/",
    "reports/domain-finalization/master/",
    "tools/domain-finalization/validate_master_finalization.py",
)
PROTECTED_PREFIXES = (
    "maths/",
    "registry/math-contracts/TLC-FC-00-MASTER-",
    "registry/ir/TLC-FC-00-MASTER-",
    "ir/TLC-FC-00-MASTER-",
    "registry/test-plans/TLC-FC-00-MASTER-",
    "registry/scientific-objects/master/",
    "registry/domain-progress/master/",
)
FORBIDDEN_SUFFIXES = (".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx")


class ValidationError(RuntimeError):
    pass


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValidationError(f"missing YAML artifact: {path.relative_to(ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValidationError(f"expected YAML mapping: {path.relative_to(ROOT)}")
    return data


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValidationError(f"missing JSON artifact: {path.relative_to(ROOT)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValidationError(f"expected JSON object: {path.relative_to(ROOT)}")
    return data


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode != 0:
        raise ValidationError(
            f"git {' '.join(args)} failed ({result.returncode}): {result.stderr.strip()}"
        )
    return result.stdout


def validate_diff(base: str) -> list[str]:
    run_git("diff", "--check", f"{base}...HEAD")
    changed = [
        line.strip()
        for line in run_git("diff", "--name-only", f"{base}...HEAD").splitlines()
        if line.strip()
    ]
    allow_temp = os.environ.get("MASTER_ALLOW_TEMP_WORKFLOW") == "1"
    temp_workflow = ".github/workflows/master-finalization-validation.yml"
    for path in changed:
        if path.startswith(PROTECTED_PREFIXES):
            raise ValidationError(f"protected source changed: {path}")
        if path.endswith(FORBIDDEN_SUFFIXES):
            raise ValidationError(f"C++ artifact is forbidden in this phase: {path}")
        if "binding" in path.lower() or "pybind" in path.lower():
            raise ValidationError(f"binding artifact is forbidden in this phase: {path}")
        if path == temp_workflow and allow_temp:
            continue
        if not path.startswith(ALLOWED_PREFIXES):
            raise ValidationError(f"out-of-scope changed path: {path}")
    return changed


def ordered_source_sets(source_ir: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    nodes = source_ir.get("nodes")
    if not isinstance(nodes, list) or len(nodes) != 1 or not isinstance(nodes[0], dict):
        raise ValidationError(f"source IR must contain exactly one node: {source_ir.get('feature_id')}")
    node = nodes[0]
    objects = node.get("scientific_object_refs") or []
    relations = node.get("relation_refs") or []
    unresolved = source_ir.get("unresolved") or []
    if not all(isinstance(value, list) for value in (objects, relations, unresolved)):
        raise ValidationError(f"invalid source sets: {source_ir.get('feature_id')}")
    return objects, relations, unresolved


def validate_feature(entry: dict[str, Any]) -> None:
    feature_id = entry.get("feature_id")
    if feature_id not in EXPECTED_FEATURES:
        raise ValidationError(f"unexpected feature in manifest: {feature_id}")

    required_refs = (
        "contract_ref",
        "ir_registry_ref",
        "source_ir_ref",
        "source_test_plan_ref",
        "finalized_ir_ref",
        "algorithm_ref",
        "oracle_ref",
    )
    for key in required_refs:
        value = entry.get(key)
        if not isinstance(value, str) or not (ROOT / value).is_file():
            raise ValidationError(f"{feature_id}: missing or invalid {key}")

    contract = load_yaml(ROOT / entry["contract_ref"])
    source_ir = load_json(ROOT / entry["source_ir_ref"])
    finalized_ir = load_yaml(ROOT / entry["finalized_ir_ref"])
    algorithm = load_yaml(ROOT / entry["algorithm_ref"])
    oracle = load_yaml(ROOT / entry["oracle_ref"])
    test_plan = load_yaml(ROOT / entry["source_test_plan_ref"])

    identities = {
        contract.get("feature_id"),
        source_ir.get("feature_id"),
        finalized_ir.get("feature_id"),
        algorithm.get("feature_id"),
        oracle.get("feature_id"),
        test_plan.get("feature_id"),
    }
    if identities != {feature_id}:
        raise ValidationError(f"{feature_id}: inconsistent feature identity: {identities}")

    source_objects, source_relations, source_unresolved = ordered_source_sets(source_ir)
    contract_objects = contract.get("input_objects") or []
    contract_relations = contract.get("relations") or []
    contract_unresolved = contract.get("unresolved") or []
    if source_objects != contract_objects:
        raise ValidationError(f"{feature_id}: contract/source object mismatch")
    if source_relations != contract_relations:
        raise ValidationError(f"{feature_id}: contract/source relation mismatch")
    if source_unresolved != contract_unresolved:
        raise ValidationError(f"{feature_id}: contract/source unresolved mismatch")

    final_inputs = finalized_ir.get("inputs") or {}
    if final_inputs.get("scientific_object_refs", []) != source_objects:
        raise ValidationError(f"{feature_id}: finalized object references changed")
    if final_inputs.get("relation_refs", []) != source_relations:
        raise ValidationError(f"{feature_id}: finalized relation references changed")
    final_unresolved = finalized_ir.get("unresolved") or []
    if final_unresolved != source_unresolved:
        raise ValidationError(f"{feature_id}: finalized unresolved references changed")
    embedded_unresolved = final_inputs.get("unresolved_refs", [])
    if embedded_unresolved != source_unresolved:
        raise ValidationError(f"{feature_id}: finalized input unresolved references changed")

    if finalized_ir.get("status") != STATUS or algorithm.get("status") != STATUS:
        raise ValidationError(f"{feature_id}: implementation selection status missing")
    if "rejected" in json.dumps(finalized_ir).lower():
        raise ValidationError(f"{feature_id}: rejected status is forbidden")

    expected_final_ref = entry["finalized_ir_ref"]
    expected_algorithm_ref = entry["algorithm_ref"]
    if algorithm.get("finalized_ir_ref") != expected_final_ref:
        raise ValidationError(f"{feature_id}: algorithm/finalized IR link mismatch")
    if oracle.get("finalized_ir_ref") != expected_final_ref:
        raise ValidationError(f"{feature_id}: oracle/finalized IR link mismatch")
    if oracle.get("algorithm_ref") != expected_algorithm_ref:
        raise ValidationError(f"{feature_id}: oracle/algorithm link mismatch")

    source_has_operation = bool(source_ir.get("operations"))
    implementation_kind = (finalized_ir.get("representation") or {}).get("implementation_kind")
    oracle_text = json.dumps(oracle, sort_keys=True)
    if source_has_operation:
        if implementation_kind != "opaque_operation_adapter":
            raise ValidationError(f"{feature_id}: source operation lacks opaque adapter")
        if "provider" not in json.dumps(algorithm).lower():
            raise ValidationError(f"{feature_id}: algorithm lacks provider boundary")
        if "opaque" not in oracle_text.lower():
            raise ValidationError(f"{feature_id}: oracle lacks opaque preservation test")
    elif implementation_kind == "opaque_operation_adapter":
        raise ValidationError(f"{feature_id}: invented operation adapter for non-operation source")

    for field in ("preservation_obligations", "preconditions", "operations", "postconditions", "invariants", "errors", "determinism", "dependencies", "tests", "implementation_status"):
        if field not in finalized_ir:
            raise ValidationError(f"{feature_id}: finalized IR missing {field}")
    for field in ("signature", "inputs", "outputs", "validations", "steps", "branches", "errors", "invariants", "determinism", "effects", "edge_cases", "necessary_dependencies"):
        if field not in algorithm:
            raise ValidationError(f"{feature_id}: algorithm missing {field}")
    if not oracle.get("acceptance_tests"):
        raise ValidationError(f"{feature_id}: oracle has no acceptance tests")
    if oracle.get("scientific_values_invented") is not False:
        raise ValidationError(f"{feature_id}: oracle must declare no invented scientific values")


def validate_common(manifest: dict[str, Any]) -> None:
    features = manifest.get("features")
    if not isinstance(features, list) or len(features) != 16:
        raise ValidationError("manifest must contain exactly sixteen features")
    manifest_ids = [entry.get("feature_id") for entry in features]
    if manifest_ids != EXPECTED_FEATURES:
        raise ValidationError(f"manifest feature set/order mismatch: {manifest_ids}")
    if len(set(manifest_ids)) != 16:
        raise ValidationError("manifest contains duplicate features")
    if manifest.get("feature_count") != 16:
        raise ValidationError("manifest feature_count must equal sixteen")
    if manifest.get("protection_policy", {}).get("rejected_features") != []:
        raise ValidationError("no Master feature may be rejected")

    statuses = load_yaml(ROOT / "registry/domain-finalization/master/feature-status.yaml")
    status_entries = statuses.get("features") or []
    status_ids = [entry.get("feature_id") for entry in status_entries]
    if status_ids != EXPECTED_FEATURES or len(status_entries) != 16:
        raise ValidationError("feature-status must contain the exact sixteen features")
    if any(entry.get("status") != STATUS for entry in status_entries):
        raise ValidationError("every feature status must be selected for implementation specification")

    patterns = load_yaml(ROOT / "registry/domain-finalization/master/patterns.yaml")
    if len(patterns.get("patterns") or []) < 1:
        raise ValidationError("pattern library is empty")
    module = load_yaml(ROOT / "registry/domain-finalization/master/module-specification.yaml")
    interfaces = module.get("interfaces") or []
    if [entry.get("feature_id") for entry in interfaces] != EXPECTED_FEATURES:
        raise ValidationError("module interfaces must cover the exact sixteen features")
    tasks = load_yaml(ROOT / "registry/domain-finalization/master/implementation-tasks.yaml")
    feature_tasks = tasks.get("feature_tasks") or []
    if [entry.get("feature_id") for entry in feature_tasks] != EXPECTED_FEATURES:
        raise ValidationError("implementation tasks must cover the exact sixteen features")

    report = ROOT / "reports/domain-finalization/master/finalization-report.md"
    if not report.is_file():
        raise ValidationError("finalization report is missing")

    for entry in features:
        validate_feature(entry)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main", help="base ref or commit for scope and whitespace checks")
    args = parser.parse_args()
    try:
        changed = validate_diff(args.base)
        manifest = load_yaml(ROOT / "registry/domain-finalization/master/manifest.yaml")
        validate_common(manifest)
    except ValidationError as exc:
        print(f"master-finalization validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"master-finalization validation passed: 16 features, {len(changed)} changed files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
