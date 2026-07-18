#!/usr/bin/env python3
"""Structural validator for TLC-FC-02-COMMUNITY-001 (not an oracle)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required to validate YAML artifacts") from exc

FEATURE = "TLC-FC-02-COMMUNITY-001"
POSITION = 1
ROOT = Path(__file__).resolve().parents[3]
CONTRACT_DIR = ROOT / "registry" / "math-contracts" / FEATURE
REPORT_DIR = ROOT / "reports" / "math-contracts" / FEATURE
EXPECTED_YAML = [
    CONTRACT_DIR / "contract.yaml", CONTRACT_DIR / "symbol-table.yaml",
    CONTRACT_DIR / "type-constraints.yaml", CONTRACT_DIR / "coverage.yaml",
    CONTRACT_DIR / "issues.yaml", CONTRACT_DIR / "implementation-decisions-required.yaml",
    CONTRACT_DIR / "open-math-questions.yaml", REPORT_DIR / "decision_required.yaml",
]

def load(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)

def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)

def main() -> int:
    errors: list[str] = []
    docs = {}
    for path in EXPECTED_YAML:
        try:
            docs[path.name] = load(path)
        except Exception as exc:
            errors.append(f"unreadable YAML {path}: {exc}")

    wave = load(ROOT / "registry/math-contract-entry/contract-wave-1.yaml")
    feature_ids = wave.get("feature_ids", [])
    require(FEATURE in feature_ids, "feature absent from authorized wave", errors)
    require(len(feature_ids) >= POSITION and feature_ids[POSITION - 1] == FEATURE,
            "feature/wave position mismatch", errors)
    contract = docs.get("contract.yaml", {}) or {}
    symbols_doc = docs.get("symbol-table.yaml", {}) or {}
    require(contract.get("feature_id") == FEATURE, "wrong contract feature", errors)
    require(contract.get("status") == "candidate", "contract status must be candidate", errors)
    require(contract.get("scientific_objects") == ["TLC-SO-COMMUNITY-008"],
            "scientific object scope differs from authorized singleton", errors)
    require(contract.get("scientific_relations") == [], "unauthorized relation introduced", errors)

    object_registry = (ROOT / "registry/scientific-objects/community/scientific-objects.candidate.yaml").read_text(encoding="utf-8")
    require("TLC-SO-COMMUNITY-008" in object_registry, "scientific object missing", errors)
    declared = {item.get("symbol_id") for item in symbols_doc.get("symbols", [])}
    require(len(declared) == len(symbols_doc.get("symbols", [])), "duplicate symbol ids", errors)
    referenced = set(contract.get("spaces", []) + contract.get("sets", []) + contract.get("variables", []) +
                     contract.get("constants", []) + contract.get("parameters", []) + contract.get("states", []) +
                     contract.get("inputs", []) + contract.get("operators", []))
    require(referenced <= declared, f"undeclared symbols: {sorted(referenced - declared)}", errors)

    tc = docs.get("type-constraints.yaml", {}) or {}
    for constraint in tc.get("constraints", []):
        require(set(constraint.get("referenced_symbols", [])) <= declared,
                f"constraint {constraint.get('constraint_id')} references undeclared symbol", errors)
    ids = []
    for key in ("preconditions", "postconditions", "invariants"):
        for item in contract.get(key, []):
            ids.append(next((v for k, v in item.items() if k.endswith("_id")), None))
            require(bool(item.get("source")), f"untraceable {key} item", errors)
    require(len(ids) == len(set(ids)), "duplicate contract element ids", errors)
    require(contract.get("dependencies", {}).get("required_contracts") == [], "unjustified dependency", errors)
    require(bool(contract.get("dependencies", {}).get("autonomy_evidence")), "missing autonomy evidence", errors)
    require(contract.get("executable_oracle", {}).get("status") == "not_produced", "executable oracle produced", errors)
    require(contract.get("equations") == [], "source declares no associated equations", errors)

    tex = (CONTRACT_DIR / "normalized-equations.tex").read_text(encoding="utf-8")
    require("Equivalence status: unresolved" in tex, "normalization equivalence status absent", errors)
    forbidden = re.compile(r"\b(?:numpy|Eigen|std::|float|double|Runge.Kutta|Euler step)\b", re.I)
    for path in list(CONTRACT_DIR.iterdir()) + list(REPORT_DIR.iterdir()):
        if path.is_file():
            require(not forbidden.search(path.read_text(encoding="utf-8")), f"implementation term in {path}", errors)
    other_contracts = [p.name for p in (ROOT / "registry/math-contracts").iterdir() if p.is_dir() and p.name != FEATURE]
    require(not other_contracts, f"other feature contract directories present: {other_contracts}", errors)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED: feature, scope, traceability, symbols, YAML and exclusions are consistent")
    return 0

if __name__ == "__main__":
    sys.exit(main())
