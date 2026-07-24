#!/usr/bin/env python3
"""Structural validator; not an executable scientific oracle."""
from pathlib import Path
import re, sys, yaml

FEATURE, POSITION = "TLC-FC-05-DYNAMICS-001", 2
ROOT = Path(__file__).resolve().parents[3]
CD = ROOT / "registry/math-contracts" / FEATURE
RD = ROOT / "reports/math-contracts" / FEATURE
YAMLS = list(CD.glob("*.yaml")) + list(RD.glob("*.yaml"))

def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def main():
    errors = []
    docs = {}
    for path in YAMLS:
        try: docs[path.name] = load(path)
        except Exception as exc: errors.append(f"unreadable YAML {path}: {exc}")
    wave = load(ROOT / "registry/math-contract-entry/contract-wave-1.yaml")["feature_ids"]
    if len(wave) < POSITION or wave[POSITION-1] != FEATURE: errors.append("feature/wave position mismatch")
    c, s, tc = docs.get("contract.yaml", {}), docs.get("symbol-table.yaml", {}), docs.get("type-constraints.yaml", {})
    if c.get("feature_id") != FEATURE or c.get("status") != "candidate": errors.append("contract identity/status invalid")
    if c.get("scientific_objects") != ["TLC-SO-DYNAMICS-015"] or c.get("scientific_relations") != []: errors.append("object/relation scope invalid")
    registry = (ROOT / "registry/scientific-objects/dynamics/scientific-objects.candidate.yaml").read_text(encoding="utf-8")
    if "TLC-SO-DYNAMICS-015" not in registry: errors.append("authorized object missing")
    declared = {x["symbol_id"] for x in s.get("symbols", [])}
    if len(declared) != len(s.get("symbols", [])): errors.append("duplicate symbols")
    refs = set(c.get("sets", []) + c.get("variables", []) + c.get("parameters", []) + c.get("states", []) + c.get("inputs", []) + c.get("operators", []))
    if not refs <= declared: errors.append(f"undeclared contract symbols: {sorted(refs-declared)}")
    for x in tc.get("constraints", []):
        if not set(x.get("referenced_symbols", [])) <= declared: errors.append(f"undeclared constraint symbol in {x.get('constraint_id')}")
    if c.get("equations") != []: errors.append("unauthorized equations introduced")
    if c.get("dependencies", {}).get("required_contracts") != [] or not c.get("dependencies", {}).get("autonomy_evidence"): errors.append("dependency evidence invalid")
    if c.get("executable_oracle", {}).get("status") != "not_produced": errors.append("executable oracle produced")
    tex = (CD / "normalized-equations.tex").read_text(encoding="utf-8")
    for expression in ("|\\mathcal{A}(t)|", "\\lambda_2(L(\\mathcal{R}(t)))", "\\mathcal{V}_c(t)", "\\mathcal{N}(\\tau)"):
        if expression not in tex: errors.append(f"source expression missing: {expression}")
    forbidden = re.compile(r"\b(?:numpy|Eigen|std::|float|double|Runge.Kutta|Euler step)\b", re.I)
    for path in list(CD.iterdir()) + list(RD.iterdir()):
        if path.is_file() and forbidden.search(path.read_text(encoding="utf-8")): errors.append(f"implementation term in {path}")
    others = [p.name for p in (ROOT / "registry/math-contracts").iterdir() if p.is_dir() and p.name != FEATURE]
    if others: errors.append(f"other feature directories present: {others}")
    if errors:
        print("VALIDATION FAILED\n- " + "\n- ".join(errors)); return 1
    print(f"VALIDATION PASSED: {len(YAMLS)} YAML files; exact feature, symbols, constraints and exclusions verified"); return 0

if __name__ == "__main__": sys.exit(main())
