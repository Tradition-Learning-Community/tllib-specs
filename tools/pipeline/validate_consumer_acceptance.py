#!/usr/bin/env python3
"""Validate standalone handoff bundles from a neutral consumer perspective.

The consumer reads only exported bundle content. Provenance may name upstream
repository paths, but those paths are never dereferenced while consuming a
bundle. Scientific execution is never attempted by this validator.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.handoff.export_bundle import export, sha256_file, tree_hashes  # noqa: E402

HANDOFF = ROOT / "handoff"
CATALOG = HANDOFF / "catalog.json"

SCIENTIFIC_STATUSES = {
    "defined",
    "partially_defined",
    "preserved_unresolved",
    "external_provider_required",
    "not_applicable",
}
EXECUTION_STATUSES = {
    "executable",
    "conditionally_executable",
    "structural_only",
    "unsupported",
}


class ConsumerFailure(RuntimeError):
    """Raised when an exported bundle is not independently consumable."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConsumerFailure(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ConsumerFailure(f"expected JSON object: {path}")
    return value


def git_commit() -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        raise ConsumerFailure(proc.stderr.strip() or "cannot resolve git commit")
    return proc.stdout.strip()


def list_items(value: Any, key: str) -> list[Any]:
    if not isinstance(value, dict):
        return []
    result = value.get(key, [])
    if result is None:
        return []
    if not isinstance(result, list):
        raise ConsumerFailure(f"{key} must be a list")
    return result


def execution_gate(status: str) -> dict[str, Any]:
    if status == "executable":
        return {
            "gate": "eligible",
            "error": None,
            "message": "Execution is permitted by package status; scientific behavior remains contract-defined.",
        }
    if status == "conditionally_executable":
        return {
            "gate": "conditional",
            "error": "TLLIB_CONSUMER_CONDITIONS_REQUIRED",
            "message": "Execution requires the conditions explicitly published by the bundle.",
        }
    if status == "structural_only":
        return {
            "gate": "blocked",
            "error": "TLLIB_CONSUMER_EXECUTION_NOT_AVAILABLE",
            "message": "The package is structural-only and exposes no scientific execution capability.",
        }
    if status == "unsupported":
        return {
            "gate": "blocked",
            "error": "TLLIB_CONSUMER_UNSUPPORTED_EXECUTION",
            "message": "The package explicitly marks execution as unsupported.",
        }
    raise ConsumerFailure(f"unknown execution status: {status!r}")


def verify_lock(bundle: Path, lock: dict[str, Any]) -> None:
    records = lock.get("files")
    if not isinstance(records, list) or not records:
        raise ConsumerFailure(f"bundle lock has no files: {bundle}")
    seen: set[str] = set()
    for row in records:
        if not isinstance(row, dict):
            raise ConsumerFailure("bundle lock file record is not an object")
        bundle_path = row.get("bundle_path")
        source_path = row.get("source_path")
        expected_hash = row.get("sha256")
        if not all(isinstance(item, str) and item for item in (bundle_path, source_path, expected_hash)):
            raise ConsumerFailure("bundle lock file record is incomplete")
        if bundle_path in seen:
            raise ConsumerFailure(f"duplicate bundle path: {bundle_path}")
        seen.add(bundle_path)
        if not (
            source_path.startswith("handoff/features/")
            or source_path.startswith("handoff/shared/")
        ):
            raise ConsumerFailure(f"bundle depends on non-handoff source: {source_path}")
        actual = bundle / bundle_path
        if not actual.is_file():
            raise ConsumerFailure(f"locked bundle file is missing: {bundle_path}")
        if sha256_file(actual) != expected_hash:
            raise ConsumerFailure(f"bundle file hash mismatch: {bundle_path}")

    actual_files = {
        path.relative_to(bundle).as_posix()
        for path in bundle.rglob("*")
        if path.is_file() and path.name != "bundle-lock.json"
    }
    if actual_files != seen:
        raise ConsumerFailure(
            f"bundle lock/file mismatch: missing={sorted(seen - actual_files)}, "
            f"unlocked={sorted(actual_files - seen)}"
        )


def consume_bundle(bundle: Path, catalog_entry: dict[str, Any]) -> dict[str, Any]:
    # Every file read below is rooted inside the exported bundle.
    lock = load_json(bundle / "bundle-lock.json")
    verify_lock(bundle, lock)

    manifest = load_json(bundle / "feature" / "manifest.json")
    contract = load_json(bundle / "feature" / "contract.json")
    acceptance = load_json(bundle / "feature" / "acceptance.json")
    traceability = load_json(bundle / "feature" / "traceability.json")

    feature_id = catalog_entry.get("feature_id")
    if manifest.get("feature_id") != feature_id or lock.get("feature_id") != feature_id:
        raise ConsumerFailure(f"feature identity mismatch in standalone bundle: {feature_id}")
    if manifest.get("package_version") != catalog_entry.get("package_version"):
        raise ConsumerFailure(f"feature package version mismatch: {feature_id}")

    statuses = manifest.get("statuses")
    if not isinstance(statuses, dict):
        raise ConsumerFailure(f"missing statuses in bundle: {feature_id}")
    scientific = statuses.get("scientific")
    execution = statuses.get("execution")
    if scientific not in SCIENTIFIC_STATUSES:
        raise ConsumerFailure(f"unknown scientific status for {feature_id}: {scientific!r}")
    if execution not in EXECUTION_STATUSES:
        raise ConsumerFailure(f"unknown execution status for {feature_id}: {execution!r}")
    if statuses != catalog_entry.get("statuses"):
        raise ConsumerFailure(f"catalog/manifest status mismatch: {feature_id}")

    scope = contract.get("scope")
    if not isinstance(scope, dict):
        raise ConsumerFailure(f"contract scope is missing: {feature_id}")
    operations = list_items(contract, "operations")
    acceptance_tests = list_items(acceptance, "tests")
    implementation_modes = list_items(contract, "implementation_modes")
    global_invariants = list_items(contract, "global_invariants")
    required = list_items(scope, "required")
    forbidden = list_items(scope, "forbidden")
    deferred = list_items(scope, "deferred")

    error_contracts = 0
    for operation in operations:
        if not isinstance(operation, dict):
            raise ConsumerFailure(f"operation is not an object: {feature_id}")
        error_contracts += len(list_items(operation, "error_contract"))

    if not acceptance_tests:
        raise ConsumerFailure(f"bundle exposes no acceptance obligations: {feature_id}")
    if not traceability:
        raise ConsumerFailure(f"bundle exposes no traceability document: {feature_id}")

    gate = execution_gate(execution)
    if execution in {"structural_only", "unsupported"} and not gate["error"]:
        raise ConsumerFailure(f"non-executable package has no explicit consumer error: {feature_id}")

    return {
        "feature_id": feature_id,
        "domain": catalog_entry.get("domain"),
        "package_version": manifest.get("package_version"),
        "scientific_status": scientific,
        "execution_status": execution,
        "execution_gate": gate,
        "obligations": {
            "required": len(required),
            "forbidden": len(forbidden),
            "deferred": len(deferred),
            "operations": len(operations),
            "acceptance_tests": len(acceptance_tests),
            "implementation_modes": len(implementation_modes),
            "global_invariants": len(global_invariants),
            "error_contracts": error_contracts,
        },
        "resolved_shared_contracts": len(lock.get("resolved_shared_contracts", [])),
        "bundle_sha256": lock.get("bundle_sha256"),
        "bundle_file_count": len(lock.get("files", [])),
        "upstream_reads_required": False,
    }


def audit() -> dict[str, Any]:
    catalog = load_json(CATALOG)
    features = catalog.get("features")
    domains = catalog.get("domains")
    shared = catalog.get("shared_contracts")
    if not isinstance(features, list) or not isinstance(domains, list) or not isinstance(shared, list):
        raise ConsumerFailure("catalog population is invalid")

    records: list[dict[str, Any]] = []
    scientific_counts: Counter[str] = Counter()
    execution_counts: Counter[str] = Counter()
    total_obligations: Counter[str] = Counter()

    for entry in features:
        if not isinstance(entry, dict) or not isinstance(entry.get("feature_id"), str):
            raise ConsumerFailure("catalog feature entry is invalid")
        feature_id = entry["feature_id"]
        with tempfile.TemporaryDirectory(prefix="tllib-consumer-a-") as first_tmp, tempfile.TemporaryDirectory(
            prefix="tllib-consumer-b-"
        ) as second_tmp:
            first = Path(first_tmp) / "bundle"
            second = Path(second_tmp) / "bundle"
            first_lock = export(feature_id, first, check_only=False)
            second_lock = export(feature_id, second, check_only=False)
            if first_lock != second_lock or tree_hashes(first) != tree_hashes(second):
                raise ConsumerFailure(f"bundle regeneration is not deterministic: {feature_id}")
            record = consume_bundle(first, entry)
        records.append(record)
        scientific_counts[record["scientific_status"]] += 1
        execution_counts[record["execution_status"]] += 1
        total_obligations.update(record["obligations"])

    summary = catalog.get("summary")
    if not isinstance(summary, dict):
        raise ConsumerFailure("catalog summary is invalid")
    if dict(sorted(scientific_counts.items())) != summary.get("scientific_statuses"):
        raise ConsumerFailure("consumer scientific-status counts differ from catalog summary")
    if dict(sorted(execution_counts.items())) != summary.get("execution_statuses"):
        raise ConsumerFailure("consumer execution-status counts differ from catalog summary")

    return {
        "schema_version": "1.0",
        "audit": "standalone-consumer-acceptance",
        "spec_commit": git_commit(),
        "population": {
            "domains": len(domains),
            "features": len(features),
            "shared_contracts": len(shared),
        },
        "scientific_statuses": dict(sorted(scientific_counts.items())),
        "execution_statuses": dict(sorted(execution_counts.items())),
        "obligations": dict(sorted(total_obligations.items())),
        "bundle_regenerations_per_feature": 2,
        "consumer_reads_upstream_repository": False,
        "features": records,
        "status": "pass",
        "errors": [],
    }


def self_test() -> None:
    for status in sorted(EXECUTION_STATUSES):
        gate = execution_gate(status)
        if status in {"structural_only", "unsupported"}:
            assert gate["gate"] == "blocked" and gate["error"]
        elif status == "conditionally_executable":
            assert gate["gate"] == "conditional" and gate["error"]
        else:
            assert gate["gate"] == "eligible" and gate["error"] is None
    print("Standalone consumer gate self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, help="write deterministic JSON evidence")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            return 0
        result = audit()
        rendered = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.evidence:
            args.evidence.write_text(rendered, encoding="utf-8")
        print(
            "Standalone consumer acceptance: PASS "
            f"({result['population']['domains']} domains/"
            f"{result['population']['features']} features/"
            f"{result['population']['shared_contracts']} shared contracts)"
        )
        return 0
    except ConsumerFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
