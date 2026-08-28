#!/usr/bin/env python3
"""Emit commit-pinned publication evidence from the canonical handoff catalog."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "handoff" / "catalog.json"


class SnapshotFailure(RuntimeError):
    pass


def load_catalog() -> dict[str, Any]:
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SnapshotFailure(f"cannot read handoff/catalog.json: {exc}") from exc
    if not isinstance(catalog, dict):
        raise SnapshotFailure("handoff/catalog.json must be a JSON object")
    return catalog


def catalog_sha256() -> str:
    try:
        return hashlib.sha256(CATALOG_PATH.read_bytes()).hexdigest()
    except OSError as exc:
        raise SnapshotFailure(f"cannot hash handoff/catalog.json: {exc}") from exc


def git_sha() -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if proc.returncode != 0:
        raise SnapshotFailure("cannot determine git HEAD")
    value = proc.stdout.strip()
    if len(value) != 40:
        raise SnapshotFailure(f"invalid git HEAD: {value!r}")
    return value


def validated_population(catalog: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    domains = catalog.get("domains")
    features = catalog.get("features")
    shared = catalog.get("shared_contracts")
    summary = catalog.get("summary")
    if not all(isinstance(value, list) for value in (domains, features, shared)) or not isinstance(summary, dict):
        raise SnapshotFailure("catalog must contain domains, features, shared_contracts, and summary")
    if any(not isinstance(row, dict) for row in domains + features + shared):
        raise SnapshotFailure("catalog populations must contain objects only")

    domain_names = [row.get("domain") for row in domains]
    feature_ids = [row.get("feature_id") for row in features]
    shared_ids = [row.get("shared_contract_id") for row in shared]
    if any(not isinstance(value, str) or not value for value in domain_names + feature_ids + shared_ids):
        raise SnapshotFailure("catalog contains invalid population identities")
    if len(domain_names) != len(set(domain_names)):
        raise SnapshotFailure("catalog contains duplicate domains")
    if len(feature_ids) != len(set(feature_ids)):
        raise SnapshotFailure("catalog contains duplicate features")
    if len(shared_ids) != len(set(shared_ids)):
        raise SnapshotFailure("catalog contains duplicate shared contracts")

    observed = {
        "domain_count": len(domains),
        "feature_count": len(features),
        "shared_contract_count": len(shared),
    }
    for key, value in observed.items():
        if summary.get(key) != value:
            raise SnapshotFailure(
                f"catalog summary mismatch for {key}: declared={summary.get(key)!r}, observed={value}"
            )

    domain_counts: dict[str, int] = {}
    for row in domains:
        name = row.get("domain")
        count = row.get("feature_count")
        if not isinstance(name, str) or isinstance(count, bool) or not isinstance(count, int) or count < 1:
            raise SnapshotFailure(f"invalid domain population row: {row!r}")
        domain_counts[name] = count
    if sum(domain_counts.values()) != len(features):
        raise SnapshotFailure(
            "domain feature counts do not sum to catalog feature population: "
            f"declared={sum(domain_counts.values())}, observed={len(features)}"
        )
    observed_by_domain = {domain: 0 for domain in domain_counts}
    for row in features:
        domain = row.get("domain")
        if domain not in observed_by_domain:
            raise SnapshotFailure(f"feature references unknown domain: {row.get('feature_id')} -> {domain}")
        observed_by_domain[domain] += 1
    if observed_by_domain != domain_counts:
        raise SnapshotFailure(
            f"domain feature populations differ: declared={domain_counts}, observed={observed_by_domain}"
        )
    return domains, features, shared


def matrix_from_domains(domains: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    include: list[dict[str, Any]] = []
    for row in domains:
        domain = row.get("domain")
        count = row.get("feature_count")
        if not isinstance(domain, str) or not domain:
            raise SnapshotFailure(f"invalid matrix domain: {domain!r}")
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            raise SnapshotFailure(f"invalid matrix feature count for {domain}: {count!r}")
        include.append({"domain": domain, "count": count})
    return {"include": include}


def snapshot() -> dict[str, Any]:
    catalog = load_catalog()
    domains, features, shared = validated_population(catalog)
    return {
        "spec_commit": git_sha(),
        "catalog_sha256": catalog_sha256(),
        "schema_version": catalog.get("schema_version"),
        "model_version": catalog.get("model_version"),
        "catalog_status": catalog.get("catalog_status"),
        "population": {
            "domain_count": len(domains),
            "feature_count": len(features),
            "shared_contract_count": len(shared),
        },
        "domains": [
            {
                "domain": row["domain"],
                "domain_index": row.get("domain_index"),
                "feature_count": row["feature_count"],
                "catalog_path": row.get("catalog_path"),
                "catalog_sha256": row.get("catalog_sha256"),
            }
            for row in domains
        ],
    }


def run_self_test() -> None:
    baseline = [{"domain": "alpha", "feature_count": 2}]
    extended = baseline + [{"domain": "new-domain", "feature_count": 3}]
    if matrix_from_domains(baseline) != {"include": [{"domain": "alpha", "count": 2}]}:
        raise SnapshotFailure("matrix self-test failed for baseline catalog")
    if matrix_from_domains(extended) != {
        "include": [
            {"domain": "alpha", "count": 2},
            {"domain": "new-domain", "count": 3},
        ]
    }:
        raise SnapshotFailure("matrix self-test failed to include a newly catalogued domain")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write formatted evidence JSON to this path")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--matrix", action="store_true", help="emit a GitHub Actions include matrix")
    mode.add_argument("--self-test", action="store_true", help="prove matrix population changes require no YAML edits")
    args = parser.parse_args()
    try:
        if args.self_test:
            run_self_test()
            print("Catalog-driven matrix evolution self-test: PASS")
            return 0

        evidence = snapshot()
        payload: Any = matrix_from_domains(evidence["domains"]) if args.matrix else evidence
        rendered = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        print(rendered)
        if args.output:
            args.output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0
    except SnapshotFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
