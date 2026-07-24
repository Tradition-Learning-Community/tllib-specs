#!/usr/bin/env python3
"""Validate the candidate mathematical-contract entry package."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "registry/math-contract-entry"
REPORTS = ROOT / "reports/math-contract-entry"
ALLOWED = {
    "READY_FOR_MATH_CONTRACT",
    "READY_WITH_CONTRACT_RESERVATIONS",
    "REQUIRES_TARGETED_SOURCE_REVIEW",
    "REQUIRES_SCIENTIFIC_DECISION",
    "NOT_CONTRACTABLE_AS_FEATURE",
}
DEPENDENCY_TYPES = {
    "requires_state_definition",
    "requires_data_definition",
    "requires_operator_definition",
    "requires_constraint",
    "requires_invariant",
    "requires_parameter_definition",
    "requires_other_contract",
    "no_contract_dependency",
    "unresolved",
}
BASIS_KEYS = {"equations", "invariants", "constraints", "theorems", "properties", "examples", "structural_rules", "missing_elements"}


def load(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def fail(errors: list[str], message: str):
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    yaml_paths = sorted(REGISTRY.glob("*.yaml")) + sorted(REPORTS.glob("*.yaml"))
    docs = {}
    for path in yaml_paths:
        try:
            docs[path.name] = load(path)
        except Exception as exc:
            fail(errors, f"Unreadable YAML {path.relative_to(ROOT)}: {exc}")

    required = {"contractable-features.yaml", "contract-dependencies.yaml", "oracle-basis.yaml", "contract-wave-1.yaml", "deferred-features.yaml", "decision_required.yaml"}
    missing = required - docs.keys()
    if missing:
        fail(errors, f"Missing YAML artifacts: {sorted(missing)}")
        return report(errors)

    features = docs["contractable-features.yaml"]["features"]
    ids = [x["feature_id"] for x in features]
    if len(ids) != 66 or len(set(ids)) != 66:
        fail(errors, "The 66 retained-with-reservations features must be classified exactly once.")
    for feature in features:
        fid = feature["feature_id"]
        if feature.get("contract_entry_status") not in ALLOWED:
            fail(errors, f"{fid}: invalid contract entry status")
        if not feature.get("identifiable_contract_behavior"):
            fail(errors, f"{fid}: missing identifiable behavior")
        if not feature.get("sources"):
            fail(errors, f"{fid}: missing cited sources")
        if not feature.get("oracle_basis_available"):
            fail(errors, f"{fid}: missing oracle basis marker")
        if feature.get("status") != "candidate":
            fail(errors, f"{fid}: status must remain candidate")

    basis_records = docs["oracle-basis.yaml"]["features"]
    basis_ids = [x["feature_id"] for x in basis_records]
    if set(basis_ids) != set(ids) or len(basis_ids) != len(set(basis_ids)):
        fail(errors, "Oracle-basis coverage must match classified features exactly once.")
    for record in basis_records:
        fid = record["feature_id"]
        basis = record.get("oracle_basis", {})
        if set(basis) != BASIS_KEYS:
            fail(errors, f"{fid}: malformed oracle_basis keys")
        if not any(basis[key] for key in BASIS_KEYS - {"missing_elements"}):
            fail(errors, f"{fid}: empty source-grounded oracle basis")
        if record.get("test_oracle_available") is not False:
            fail(errors, f"{fid}: executable test oracle must not be claimed")

    dependency_records = docs["contract-dependencies.yaml"]["contract_dependencies"]
    dependency_ids = [x["feature_id"] for x in dependency_records]
    if set(dependency_ids) != set(ids) or len(dependency_ids) != len(set(dependency_ids)):
        fail(errors, "Contract dependency coverage must match classified features exactly once.")
    for record in dependency_records:
        for dependency in record.get("dependencies", []):
            if dependency.get("type") not in DEPENDENCY_TYPES:
                fail(errors, f"{record['feature_id']}: invalid dependency type")
            if not dependency.get("justification") or not dependency.get("evidence"):
                fail(errors, f"{record['feature_id']}: unjustified dependency")

    wave = docs["contract-wave-1.yaml"]
    wave_ids = wave["feature_ids"]
    if not 3 <= len(wave_ids) <= 8 or len(wave_ids) != len(set(wave_ids)):
        fail(errors, "CONTRACT_WAVE_1 must contain 3 to 8 unique features.")
    by_id = {x["feature_id"]: x for x in features}
    for fid in wave_ids:
        feature = by_id.get(fid)
        if not feature:
            fail(errors, f"{fid}: wave feature is not classified")
        elif feature.get("blocking_human_decisions") or feature["contract_entry_status"] == "REQUIRES_SCIENTIFIC_DECISION":
            fail(errors, f"{fid}: blocking scientific decision in CONTRACT_WAVE_1")

    serialized = "\n".join(path.read_text(encoding="utf-8") for path in sorted(REGISTRY.glob("*.yaml")))
    forbidden = ("executable_oracle:", "reference_value:", "test_fixture:", "expected_numeric_value:")
    for marker in forbidden:
        if marker in serialized:
            fail(errors, f"Invented executable oracle/test marker found: {marker}")

    diff = subprocess.run(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", "diff", "--name-only", "--", "maths", "algorithms", "registry/features", "reports/functional-decomposition-revision", "reviews"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if diff.returncode != 0 or diff.stdout.strip():
        fail(errors, "A protected scientific/revision input path was modified.")
    return report(errors)


def report(errors: list[str]) -> int:
    if errors:
        print("Contract-entry validation: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Contract-entry validation: OK")
    print("- 66 features classified exactly once")
    print("- sources, behaviors, oracle bases, dependencies, wave constraints, protected paths, and YAML verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
