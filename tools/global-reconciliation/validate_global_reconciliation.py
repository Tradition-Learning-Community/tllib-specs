#!/usr/bin/env python3
"""Validate the global reconciliation without validating scientific truth."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

import yaml


EXPECTED_DOMAINS = {
    "master", "disciple", "community", "huit-dimensions", "invariants", "dynamics",
    "theorems", "message", "principle", "values", "virtues", "capacities",
    "competencies", "practice", "lived-experience", "relations",
}
REQUIRED = {
    "domain-registry.yaml", "dependency-graph.yaml", "domain-feature-matrix.yaml",
    "feature-contract-matrix.yaml", "feature-ir-matrix.yaml", "readiness-registry.yaml",
    "cycle-registry.yaml", "blocker-registry.yaml", "existing-artifact-audit.yaml",
    "contract-execution-plan.yaml", "ir-execution-plan.yaml", "decision-required.yaml",
    "manifest.yaml",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.root.resolve()
    registry = root / "registry/global-reconciliation"
    errors: list[str] = []
    files = {p.name for p in registry.glob("*.yaml")}
    if missing := REQUIRED - files:
        errors.append(f"missing artifacts: {sorted(missing)}")
    docs = {}
    for path in registry.glob("*.yaml"):
        try:
            docs[path.name] = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"YAML parse failure {path}: {exc}")
    domains = docs.get("domain-registry.yaml", {}).get("domains", [])
    actual_domains = {row.get("domain_id") for row in domains}
    if actual_domains != EXPECTED_DOMAINS:
        errors.append(f"domain set mismatch: {sorted(actual_domains)}")
    matrix = docs.get("domain-feature-matrix.yaml", {}).get("rows", [])
    feature_ids = [row.get("feature_id") for row in matrix]
    if len(feature_ids) != len(set(feature_ids)):
        errors.append("duplicate feature identifiers")
    if any(row.get("domain") not in EXPECTED_DOMAINS for row in matrix):
        errors.append("feature with unknown domain")
    contract_rows = docs.get("feature-contract-matrix.yaml", {}).get("rows", [])
    ir_rows = docs.get("feature-ir-matrix.yaml", {}).get("rows", [])
    if {r.get("feature_id") for r in contract_rows} != set(feature_ids):
        errors.append("contract plan coverage mismatch")
    if {r.get("feature_id") for r in ir_rows} != set(feature_ids):
        errors.append("IR plan coverage mismatch")
    readiness = docs.get("readiness-registry.yaml", {}).get("features", [])
    if {r.get("feature_id") for r in readiness} != set(feature_ids):
        errors.append("readiness coverage mismatch")
    for row in readiness:
        state = row.get("state_after", {})
        if state.get("ready_for_ir_generation") and not row.get("existing_contract"):
            errors.append(f"IR-ready without contract: {row.get('feature_id')}")
        if row.get("comparison_only_excluded") and any(state.values()):
            errors.append(f"comparison_only contributes to readiness: {row.get('feature_id')}")
    edges = docs.get("dependency-graph.yaml", {}).get("edges", [])
    edge_ids = [e.get("edge_id") for e in edges]
    if len(edge_ids) != len(set(edge_ids)):
        errors.append("duplicate dependency identifiers")
    for edge in edges:
        if edge.get("dependency_type") == "domain_dependency" and edge.get("target") not in EXPECTED_DOMAINS:
            errors.append(f"missing dependency target: {edge.get('edge_id')}")
        if edge.get("status_after") == "canonical_target_available_semantic_review_pending" and edge.get("semantic_compatibility_confirmed"):
            errors.append(f"incoherent dependency status: {edge.get('edge_id')}")
    audits = docs.get("existing-artifact-audit.yaml", {}).get("artifacts", [])
    for row in audits:
        if row.get("domain") not in EXPECTED_DOMAINS:
            errors.append(f"orphan contract/IR feature: {row.get('feature_id')}")
    manifest = docs.get("manifest.yaml", {})
    if manifest.get("prohibited_outputs_created") or manifest.get("source_preparations_modified"):
        errors.append("manifest records prohibited output or preparation modification")
    changed = subprocess.check_output(["git", "diff", "--name-only", "origin/main...HEAD"], cwd=root, text=True).splitlines()
    changed += subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], cwd=root, text=True).splitlines()
    changed = [p for p in changed if "/__pycache__/" not in p.replace("\\", "/")]
    allowed = ("registry/global-reconciliation/", "reports/global-reconciliation/", "tools/global-reconciliation/")
    out_of_scope = sorted({p.replace("\\", "/") for p in changed if p and not p.replace("\\", "/").startswith(allowed)})
    if out_of_scope:
        errors.append(f"Git scope violation: {out_of_scope}")
    prohibited_patterns = [r"(^|/)src/.*\.(cc|cpp|cxx|h|hpp)$", r"binding.*\.py$", r"oracle"]
    prohibited = [p for p in changed if any(re.search(pattern, p.replace("\\", "/"), re.I) for pattern in prohibited_patterns)]
    if prohibited:
        errors.append(f"prohibited artifacts changed: {prohibited}")
    result = {"status": "ok" if not errors else "failed", "domains": len(actual_domains), "features": len(feature_ids), "dependencies": len(edges), "cycles": len(docs.get("cycle-registry.yaml", {}).get("cycles", [])), "errors": errors}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
