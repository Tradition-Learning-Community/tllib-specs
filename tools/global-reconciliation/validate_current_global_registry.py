#!/usr/bin/env python3
"""Validate the current sixteen-domain TLC registry through the IR layer."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from typing import Any

import yaml


EXPECTED_ORDER = [
    "master",
    "disciple",
    "community",
    "huit-dimensions",
    "invariants",
    "dynamics",
    "theorems",
    "message",
    "principle",
    "values",
    "virtues",
    "capacities",
    "competencies",
    "practice",
    "lived-experience",
    "relations",
]
EXPECTED_FEATURES = 166
FORBIDDEN_FEATURE_FRAGMENTS = ("-NODE-", "-SOURCE-OBJECT-", "-OP-UNRESOLVED")


def load(path: pathlib.Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def git(root: pathlib.Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.root.resolve()
    registry = root / "registry/global-reconciliation"
    errors: list[str] = []

    required = [
        "current-baseline.yaml",
        "status-taxonomy.yaml",
        "domain-registry.yaml",
        "domain-feature-matrix.yaml",
        "feature-contract-matrix.yaml",
        "feature-ir-matrix.yaml",
        "readiness-registry.yaml",
        "dependency-graph.yaml",
        "cycle-registry.yaml",
        "blocker-registry.yaml",
        "existing-artifact-audit.yaml",
        "domain-review-sequence.yaml",
        "manifest.yaml",
    ]
    for name in required:
        if not (registry / name).is_file():
            errors.append(f"missing required artifact: {name}")

    if errors:
        print(json.dumps({"status": "failed", "errors": errors}, indent=2))
        return 1

    baseline = load(registry / "current-baseline.yaml")
    domains = baseline.get("domains", [])
    order = [row.get("domain_id") for row in domains]
    if order != EXPECTED_ORDER:
        errors.append(f"domain order mismatch: {order}")
    if baseline.get("totals", {}).get("domains") != 16:
        errors.append("baseline does not contain exactly 16 domains")
    if baseline.get("totals", {}).get("active_features") != EXPECTED_FEATURES:
        errors.append(
            f"active feature count mismatch: {baseline.get('totals', {}).get('active_features')}"
        )
    if not baseline.get("all_domains_reach_ir_layer"):
        errors.append("all_domains_reach_ir_layer is not true")
    if baseline.get("scientific_decisions_made_by_this_build"):
        errors.append("baseline build records scientific decisions")
    if baseline.get("math_sources_modified"):
        errors.append("baseline records maths source modification")

    domain_matrix = load(registry / "domain-feature-matrix.yaml")
    feature_rows = domain_matrix.get("rows", [])
    feature_ids = [row.get("feature_id") for row in feature_rows]
    if len(feature_ids) != EXPECTED_FEATURES:
        errors.append(f"feature matrix count mismatch: {len(feature_ids)}")
    if len(set(feature_ids)) != len(feature_ids):
        errors.append("duplicate feature identifiers")
    for feature_id in feature_ids:
        if not isinstance(feature_id, str) or not feature_id.startswith("TLC-FC-"):
            errors.append(f"invalid feature identifier: {feature_id}")
            continue
        if any(fragment in feature_id for fragment in FORBIDDEN_FEATURE_FRAGMENTS):
            errors.append(f"internal identifier counted as feature: {feature_id}")

    required_flags = (
        "contract_present",
        "ir_artifact_present",
        "test_plan_present",
        "ir_layer_complete",
    )
    for row in feature_rows:
        for flag in required_flags:
            if row.get(flag) is not True:
                errors.append(f"{row.get('feature_id')} has {flag}={row.get(flag)!r}")

    by_domain = {slug: 0 for slug in EXPECTED_ORDER}
    for row in feature_rows:
        domain = row.get("domain")
        if domain not in by_domain:
            errors.append(f"unknown domain in matrix: {domain}")
        else:
            by_domain[domain] += 1
    for row in domains:
        domain = row.get("domain_id")
        if row.get("feature_count") != by_domain.get(domain):
            errors.append(
                f"domain count mismatch for {domain}: {row.get('feature_count')} vs {by_domain.get(domain)}"
            )
        if not row.get("ir_layer_complete"):
            errors.append(f"domain does not reach IR layer: {domain}")
        if row.get("ir_layer_complete_features") != row.get("feature_count"):
            errors.append(f"incomplete IR feature coverage for {domain}")

    contract_rows = load(registry / "feature-contract-matrix.yaml").get("rows", [])
    ir_rows = load(registry / "feature-ir-matrix.yaml").get("rows", [])
    if {row.get("feature_id") for row in contract_rows} != set(feature_ids):
        errors.append("contract matrix coverage mismatch")
    if {row.get("feature_id") for row in ir_rows} != set(feature_ids):
        errors.append("IR matrix coverage mismatch")

    manifest = load(registry / "manifest.yaml")
    if manifest.get("canonical_commit") != baseline.get("canonical_commit"):
        errors.append("manifest and baseline canonical commits differ")
    if manifest.get("prohibited_outputs_created"):
        errors.append("manifest records prohibited outputs")
    if manifest.get("source_preparations_modified"):
        errors.append("manifest records source preparation modifications")
    if manifest.get("math_sources_modified"):
        errors.append("manifest records maths source modifications")
    if manifest.get("scientific_decisions_made"):
        errors.append("manifest records scientific decisions")

    sequence = load(registry / "domain-review-sequence.yaml")
    sequence_order = [row.get("domain_id") for row in sequence.get("domain_order", [])]
    if sequence_order != EXPECTED_ORDER:
        errors.append("domain review sequence mismatch")
    if sequence.get("first_domain") != "master":
        errors.append("first review domain is not master")

    taxonomy = load(registry / "status-taxonomy.yaml")
    levels = [row.get("level") for row in taxonomy.get("levels", [])]
    if len(levels) != 8 or len(set(levels)) != 8:
        errors.append("status taxonomy must define eight unique maturity levels")

    try:
        base = git(root, "merge-base", "HEAD", "origin/main")
        changed = git(root, "diff", "--name-only", f"{base}...HEAD").splitlines()
        maths_changes = [path for path in changed if path.startswith("maths/")]
        if maths_changes:
            errors.append(f"maths sources changed: {maths_changes}")
    except Exception as exc:
        errors.append(f"could not verify changed paths: {exc}")

    result = {
        "status": "ok" if not errors else "failed",
        "canonical_commit": baseline.get("canonical_commit"),
        "domains": len(domains),
        "features": len(feature_rows),
        "all_domains_reach_ir_layer": baseline.get("all_domains_reach_ir_layer"),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
