#!/usr/bin/env python3
"""Static validator for the TLC-FC-08-PRINCIPLE-002 candidate contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required to validate contract YAML files") from exc

FEATURE = "TLC-FC-08-PRINCIPLE-002"
CONTRACT = "TLC-MC-TLC-FC-08-PRINCIPLE-002"
OBJECT = "TLC-SO-PRINCIPLE-087"
POSITION = 3
ROOT = Path(__file__).resolve().parents[3]
CONTRACT_DIR = ROOT / "registry" / "math-contracts" / FEATURE
REPORT_DIR = ROOT / "reports" / "math-contracts" / FEATURE
TOOL_DIR = ROOT / "tools" / "math-contracts" / FEATURE

REQUIRED = [
    CONTRACT_DIR / "contract.yaml",
    CONTRACT_DIR / "symbol-table.yaml",
    CONTRACT_DIR / "normalized-equations.tex",
    CONTRACT_DIR / "type-constraints.yaml",
    CONTRACT_DIR / "coverage.yaml",
    CONTRACT_DIR / "issues.yaml",
    CONTRACT_DIR / "implementation-decisions-required.yaml",
    CONTRACT_DIR / "open-math-questions.yaml",
    REPORT_DIR / "contract-report.md",
    REPORT_DIR / "decision_required.yaml",
    TOOL_DIR / "validate_contract.py",
    TOOL_DIR / "README.md",
]


def load(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.is_file():
            errors.append(f"missing required artifact: {path.relative_to(ROOT)}")

    yaml_paths = [path for path in REQUIRED if path.suffix == ".yaml" and path.is_file()]
    parsed = {}
    for path in yaml_paths:
        try:
            parsed[path] = load(path)
        except Exception as exc:  # reports precise parser failure
            errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")
    if errors:
        return finish(errors)

    wave = load(ROOT / "registry/math-contract-entry/contract-wave-1.yaml")
    features = wave.get("feature_ids", [])
    if FEATURE not in features:
        errors.append("target feature is absent from CONTRACT_WAVE_1")
    elif features.index(FEATURE) + 1 != POSITION:
        errors.append(f"target feature position is {features.index(FEATURE) + 1}, expected {POSITION}")

    contractable = load(ROOT / "registry/math-contract-entry/contractable-features.yaml")
    entry = next((x for x in contractable.get("features", []) if x.get("feature_id") == FEATURE), None)
    if not entry:
        errors.append("target feature is absent from contractable-features.yaml")
    elif entry.get("contract_entry_status") != "READY_FOR_MATH_CONTRACT":
        errors.append("target feature is not READY_FOR_MATH_CONTRACT")

    contract = parsed.get(CONTRACT_DIR / "contract.yaml", {})
    symbols_doc = parsed.get(CONTRACT_DIR / "symbol-table.yaml", {})
    if contract.get("feature_id") != FEATURE or contract.get("contract_id") != CONTRACT:
        errors.append("contract identity mismatch")

    own_files = [p for base in (CONTRACT_DIR, REPORT_DIR, TOOL_DIR) for p in base.rglob("*") if p.is_file() and p.suffix != ".pyc"]
    for path in own_files:
        text = path.read_text(encoding="utf-8")
        foreign = set(re.findall(r"TLC-FC-[A-Z0-9-]+", text)) - {FEATURE}
        if foreign:
            errors.append(f"other feature id(s) in {path.relative_to(ROOT)}: {sorted(foreign)}")

    all_ids: dict[str, Path] = {}
    definition_keys = {
        "equation_id", "postcondition_id", "compatibility_id", "coverage_id",
        "contract_issue_id", "decision_id", "question_id", "type_id",
    }
    for path, document in parsed.items():
        for mapping in walk(document):
            for key, value in mapping.items():
                if key in definition_keys and isinstance(value, str):
                    if value in all_ids and value not in {FEATURE, CONTRACT, OBJECT}:
                        errors.append(f"duplicate identifier {value}")
                    else:
                        all_ids[value] = path

    snapshot_text = (ROOT / "registry/functional-decomposition/decomposition-input-snapshot.yaml").read_text(encoding="utf-8")
    for obj in contract.get("scientific_objects", []):
        object_id = obj.get("object_id")
        if not object_id or object_id not in snapshot_text:
            errors.append(f"scientific object does not exist in authorized snapshot: {object_id}")
    if contract.get("scientific_relations"):
        errors.append("feature lineage authorizes no scientific relation")

    symbol_ids = [item.get("symbol_id") for item in symbols_doc.get("symbols", [])]
    if len(symbol_ids) != len(set(symbol_ids)):
        errors.append("symbol identifiers are not unique")
    declared = set(symbol_ids)
    for equation in contract.get("equations", []):
        used = set(equation.get("symbols_used", []))
        if not used <= declared:
            errors.append(f"equation references undeclared symbols: {sorted(used - declared)}")
        if equation.get("equivalence_status") not in {"exact_copy", "syntactic_normalization_only", "equivalence_verified", "unresolved"}:
            errors.append("equation has invalid or missing equivalence_status")
        expected = r"\frac{dP}{dt} = \mathcal{E}(P,D,t)"
        if equation.get("source_form") != expected or equation.get("normalized_latex") != expected:
            errors.append("source equation or normalized equation was not preserved exactly")

    for section in ("postconditions", "constraints", "preconditions", "invariants"):
        for item in contract.get(section, []):
            used = set(item.get("symbols_used", []))
            if not used <= declared:
                errors.append(f"{section} references undeclared symbols: {sorted(used - declared)}")
            if not item.get("source_evidence"):
                errors.append(f"{section} item lacks source evidence")

    if contract.get("executable_oracle", {}).get("status") != "not_produced":
        errors.append("executable oracle must be not_produced")

    scanned = [path for path in own_files if path.suffix in {".yaml", ".tex", ".md"}]
    combined = "\n".join(path.read_text(encoding="utf-8") for path in scanned)
    forbidden = ["numpy", "eigen", "float32", "float64", "runge-kutta", "euler method", "time step =", "backend:"]
    for term in forbidden:
        if term in combined.lower():
            errors.append(f"forbidden implementation choice found: {term}")

    for item in symbols_doc.get("symbols", []):
        for field in ("shape", "dimensions", "units"):
            value = item.get(field)
            if not isinstance(value, dict) or value.get("status") != "unresolved":
                errors.append(f"{item.get('symbol_id')}.{field} must be explicitly unresolved")

    source_lines = (ROOT / "maths/08-principle.md").read_text(encoding="utf-8").splitlines()
    source_passage = "\n".join(source_lines[197:200])
    if r"\frac{dP}{dt} = \mathcal{E}(P,D,t)" not in source_passage:
        errors.append("authorized source passage no longer contains the preserved equation")

    return finish(errors)


def finish(errors: list[str]) -> int:
    if errors:
        print("CONTRACT VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("CONTRACT VALIDATION PASSED")
    print(f"feature={FEATURE} wave_position={POSITION} artifacts={len(REQUIRED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
