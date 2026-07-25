#!/usr/bin/env python3
"""Validate the authoritative sixteen-domain TLC registry through the IR layer."""

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
HISTORICAL_REVIEW_FILES = (
    "cycle-scientific-review.yaml",
    "dependency-scientific-review.yaml",
    "first-contract-batches.yaml",
    "pilot-artifact-review.yaml",
    "scientific-review-decision-required.yaml",
    "targeted-readiness-review.yaml",
)


def load(path: pathlib.Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def git(root: pathlib.Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def collect_feature_ids(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, str) and value.startswith("TLC-FC-"):
        found.add(value)
    elif isinstance(value, dict):
        for child in value.values():
            found.update(collect_feature_ids(child))
    elif isinstance(value, list):
        for child in value:
            found.update(collect_feature_ids(child))
    return found


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
        "contract-execution-plan.yaml",
        "ir-execution-plan.yaml",
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
    totals = baseline.get("totals", {})
    if [row.get("domain_id") for row in domains] != EXPECTED_ORDER:
        errors.append("domain order mismatch")
    if totals.get("domains") != 16:
        errors.append("baseline does not contain exactly 16 domains")
    if totals.get("active_features") != EXPECTED_FEATURES:
        errors.append(f"active feature count mismatch: {totals.get('active_features')}")
    if totals.get("contracts_present") != EXPECTED_FEATURES:
        errors.append("not every active feature has a contract")
    if totals.get("ir_artifacts_present") != EXPECTED_FEATURES:
        errors.append("not every active feature has an IR artifact")
    if totals.get("test_plans_present") != EXPECTED_FEATURES:
        errors.append("not every active feature has a test plan")
    if totals.get("ir_layer_complete_features") != EXPECTED_FEATURES:
        errors.append("IR-layer feature total is incomplete")
    if not baseline.get("all_domains_reach_ir_layer"):
        errors.append("all_domains_reach_ir_layer is not true")
    if baseline.get("scientific_decisions_made_by_this_build"):
        errors.append("baseline build records scientific decisions")
    if baseline.get("math_sources_modified"):
        errors.append("baseline records maths source modification")

    feature_rows = load(registry / "domain-feature-matrix.yaml").get("rows", [])
    feature_ids = [row.get("feature_id") for row in feature_rows]
    active_ids = set(feature_ids)
    if len(feature_ids) != EXPECTED_FEATURES:
        errors.append(f"feature matrix count mismatch: {len(feature_ids)}")
    if len(active_ids) != len(feature_ids):
        errors.append("duplicate feature identifiers")
    for feature_id in feature_ids:
        if not isinstance(feature_id, str) or not feature_id.startswith("TLC-FC-"):
            errors.append(f"invalid feature identifier: {feature_id}")
            continue
        if any(fragment in feature_id for fragment in FORBIDDEN_FEATURE_FRAGMENTS):
            errors.append(f"internal identifier counted as feature: {feature_id}")
        if "TLC-FC-11-CAP-" in feature_id:
            errors.append(f"non-authoritative Capacities lineage counted as active: {feature_id}")

    for row in feature_rows:
        for flag in ("contract_present", "ir_artifact_present", "test_plan_present", "ir_layer_complete"):
            if row.get(flag) is not True:
                errors.append(f"{row.get('feature_id')} has {flag}={row.get(flag)!r}")

    by_domain = {slug: 0 for slug in EXPECTED_ORDER}
    for row in feature_rows:
        domain = row.get("domain")
        if domain not in by_domain:
            errors.append(f"unknown domain in feature matrix: {domain}")
        else:
            by_domain[domain] += 1
    for row in domains:
        domain = row.get("domain_id")
        if row.get("feature_count") != by_domain.get(domain):
            errors.append(f"domain count mismatch for {domain}")
        if not row.get("ir_layer_complete"):
            errors.append(f"domain does not reach IR layer: {domain}")
        if row.get("ir_layer_complete_features") != row.get("feature_count"):
            errors.append(f"incomplete IR feature coverage for {domain}")

    contract_rows = load(registry / "feature-contract-matrix.yaml").get("rows", [])
    ir_rows = load(registry / "feature-ir-matrix.yaml").get("rows", [])
    readiness_rows = load(registry / "readiness-registry.yaml").get("features", [])
    audit_rows = load(registry / "existing-artifact-audit.yaml").get("artifacts", [])
    for label, rows in (
        ("contract matrix", contract_rows),
        ("IR matrix", ir_rows),
        ("readiness registry", readiness_rows),
        ("artifact audit", audit_rows),
    ):
        if {row.get("feature_id") for row in rows} != active_ids:
            errors.append(f"{label} coverage mismatch")

    blockers = load(registry / "blocker-registry.yaml")
    blocker_rows = blockers.get("blockers", [])
    blocker_ids = {row.get("blocker_id") for row in blocker_rows}
    if not {row.get("feature_id") for row in blocker_rows}.issubset(active_ids):
        errors.append("blocker registry contains non-authoritative features")
    if blockers.get("summary", {}).get("total") != len(blocker_rows):
        errors.append("blocker summary total mismatch")
    if sum(blockers.get("summary", {}).get(key, 0) for key in ("critical", "major", "minor")) != len(blocker_rows):
        errors.append("blocker severity summary mismatch")

    dependency_graph = load(registry / "dependency-graph.yaml")
    edge_rows = dependency_graph.get("edges", [])
    edge_ids = {row.get("edge_id") for row in edge_rows}
    for edge in edge_rows:
        if edge.get("dependency_type") == "feature_dependency":
            if edge.get("source") not in active_ids or edge.get("target") not in active_ids:
                errors.append(f"non-authoritative feature dependency: {edge.get('edge_id')}")
        elif edge.get("dependency_type") == "domain_dependency":
            if edge.get("source_domain") not in EXPECTED_ORDER or edge.get("target") not in EXPECTED_ORDER:
                errors.append(f"invalid domain dependency: {edge.get('edge_id')}")
        else:
            errors.append(f"unknown dependency type: {edge.get('edge_id')}")
    if dependency_graph.get("summary", {}).get("total") != len(edge_rows):
        errors.append("dependency summary total mismatch")

    cycles = load(registry / "cycle-registry.yaml").get("cycles", [])
    for cycle in cycles:
        if cycle.get("level") == "feature" and not set(cycle.get("nodes", [])).issubset(active_ids):
            errors.append(f"feature cycle contains non-authoritative nodes: {cycle.get('cycle_id')}")
        if cycle.get("level") == "domain" and not set(cycle.get("nodes", [])).issubset(set(EXPECTED_ORDER)):
            errors.append(f"domain cycle contains unknown nodes: {cycle.get('cycle_id')}")
        if not set(cycle.get("edges", [])).issubset(edge_ids):
            errors.append(f"cycle references missing edges: {cycle.get('cycle_id')}")

    for name in ("contract-execution-plan.yaml", "ir-execution-plan.yaml"):
        plan = load(registry / name)
        if not collect_feature_ids(plan).issubset(active_ids):
            errors.append(f"{name} contains non-authoritative features")
        for batch in plan.get("batches", []):
            if not set(batch.get("blockers", [])).issubset(blocker_ids):
                errors.append(f"{name} references missing blockers in {batch.get('batch_id')}")
        if plan.get("superseded_by") != "registry/global-reconciliation/domain-review-sequence.yaml":
            errors.append(f"{name} is not marked superseded by the domain sequence")

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
    manifest_artifacts = set(manifest.get("artifacts", []))
    for name in HISTORICAL_REVIEW_FILES:
        if f"registry/global-reconciliation/{name}" in manifest_artifacts:
            errors.append(f"historical review incorrectly claimed as current output: {name}")
        historical = load(registry / name)
        if "generated_from_tool_commit" in historical:
            errors.append(f"historical review provenance overwritten: {name}")

    sequence = load(registry / "domain-review-sequence.yaml")
    if [row.get("domain_id") for row in sequence.get("domain_order", [])] != EXPECTED_ORDER:
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
        "blockers": len(blocker_rows),
        "dependencies": len(edge_rows),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
