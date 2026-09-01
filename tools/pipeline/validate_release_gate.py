#!/usr/bin/env python3
"""Certify one immutable tllib-specs commit as a consumable release candidate.

The release gate re-runs the catalog, scientific-boundary governance, handoff,
standalone consumer, compatibility, publication-drift, and global-finalization
controls on the same checked-out SHA. It records no volatile timestamp.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "handoff" / "catalog.json"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")


class ReleaseFailure(RuntimeError):
    """Raised when a candidate cannot be certified."""


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    if check and proc.returncode:
        raise ReleaseFailure(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReleaseFailure(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ReleaseFailure(f"expected JSON object: {path}")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_version(value: str) -> str:
    if not SEMVER.fullmatch(value):
        raise ReleaseFailure(f"release version must be MAJOR.MINOR.PATCH, observed {value!r}")
    return value


def validate_sha(value: str) -> str:
    value = value.lower()
    if not SHA40.fullmatch(value):
        raise ReleaseFailure(f"target SHA must be a full 40-character hexadecimal commit, observed {value!r}")
    return value


def command_spec(*parts: str) -> str:
    return " ".join(parts)


def run_python(name: str, args: list[str], *, display: str) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        diagnostic = (proc.stderr.strip() or proc.stdout.strip() or "no diagnostic")[-6000:]
        raise ReleaseFailure(f"{name} failed: {diagnostic}")
    return {"name": name, "command": display, "status": "pass"}


def run_git_check(name: str, args: list[str], *, display: str) -> dict[str, Any]:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    if proc.returncode:
        diagnostic = (proc.stderr.strip() or proc.stdout.strip() or "no diagnostic")[-6000:]
        raise ReleaseFailure(f"{name} failed: {diagnostic}")
    return {"name": name, "command": display, "status": "pass"}


def clean_status() -> None:
    dirty = git("status", "--short")
    if dirty:
        raise ReleaseFailure("release validation dirtied or started from a dirty checkout:\n" + dirty)


def certify(version: str, target_sha: str, compatibility_base: str | None) -> dict[str, Any]:
    version = validate_version(version)
    target_sha = validate_sha(target_sha)
    actual = git("rev-parse", "HEAD").lower()
    if actual != target_sha:
        raise ReleaseFailure(f"candidate checkout mismatch: requested={target_sha}, observed={actual}")
    clean_status()

    if compatibility_base:
        compatibility_base = validate_sha(git("rev-parse", compatibility_base).lower())
    else:
        compatibility_base = validate_sha(git("rev-parse", "HEAD^").lower())

    catalog = load_json(CATALOG_PATH)
    summary = catalog.get("summary")
    if not isinstance(summary, dict):
        raise ReleaseFailure("catalog summary is invalid")

    checks: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="tllib-release-gate-") as tmp:
        root = Path(tmp)
        drift_path = root / "publication-drift.json"
        semantic_path = root / "semantic-governance.json"
        consumer_path = root / "consumer-acceptance.json"
        compatibility_path = root / "compatibility.json"

        checks.append(run_python(
            "python-environment",
            ["tools/pipeline/validate_python_environment.py"],
            display="python tools/pipeline/validate_python_environment.py",
        ))
        checks.append(run_python(
            "repository-hygiene",
            ["tools/pipeline/validate_repository_hygiene.py"],
            display="python tools/pipeline/validate_repository_hygiene.py",
        ))
        checks.append(run_python(
            "ci-trigger-coverage",
            ["tools/pipeline/validate_ci_triggers.py"],
            display="python tools/pipeline/validate_ci_triggers.py",
        ))
        checks.append(run_python(
            "publication-drift-self-test",
            ["tools/pipeline/validate_publication_drift.py", "--self-test"],
            display="python tools/pipeline/validate_publication_drift.py --self-test",
        ))
        checks.append(run_python(
            "publication-drift",
            ["tools/pipeline/validate_publication_drift.py", "--check", "--evidence", str(drift_path)],
            display="python tools/pipeline/validate_publication_drift.py --check --evidence <path>",
        ))
        checks.append(run_python(
            "catalog-matrix-self-test",
            ["tools/pipeline/catalog_snapshot.py", "--self-test"],
            display="python tools/pipeline/catalog_snapshot.py --self-test",
        ))
        checks.append(run_python(
            "catalog-reconstruction",
            ["tools/handoff/generate_catalog.py", "--check"],
            display="python tools/handoff/generate_catalog.py --check",
        ))
        checks.append(run_python(
            "semantic-and-shared-contract-governance",
            ["tools/pipeline/validate_semantic_contract_governance.py", "--evidence", str(semantic_path)],
            display="python tools/pipeline/validate_semantic_contract_governance.py --evidence <path>",
        ))
        checks.append(run_python(
            "handoff-logical-self-test",
            ["tools/handoff/validate_handoff.py", "--self-test"],
            display="python tools/handoff/validate_handoff.py --self-test",
        ))
        checks.append(run_python(
            "handoff-validation",
            ["tools/handoff/validate_handoff.py"],
            display="python tools/handoff/validate_handoff.py",
        ))
        checks.append(run_python(
            "consumer-gate-self-test",
            ["tools/pipeline/validate_consumer_acceptance.py", "--self-test"],
            display="python tools/pipeline/validate_consumer_acceptance.py --self-test",
        ))
        checks.append(run_python(
            "standalone-consumer-and-double-export",
            ["tools/pipeline/validate_consumer_acceptance.py", "--evidence", str(consumer_path)],
            display="python tools/pipeline/validate_consumer_acceptance.py --evidence <path>",
        ))
        checks.append(run_python(
            "compatibility-self-test",
            ["tools/pipeline/validate_catalog_compatibility.py", "--self-test"],
            display="python tools/pipeline/validate_catalog_compatibility.py --self-test",
        ))
        checks.append(run_python(
            "catalog-compatibility",
            [
                "tools/pipeline/validate_catalog_compatibility.py",
                "--base", compatibility_base,
                "--target", target_sha,
                "--evidence", str(compatibility_path),
            ],
            display="python tools/pipeline/validate_catalog_compatibility.py --base <commit> --target <commit> --evidence <path>",
        ))
        checks.append(run_python(
            "global-finalization",
            ["tools/global-finalization/validate_global_finalization.py"],
            display="python tools/global-finalization/validate_global_finalization.py",
        ))
        checks.append(run_git_check("git-diff-check", ["diff", "--check"], display="git diff --check"))

        drift = load_json(drift_path)
        semantic = load_json(semantic_path)
        consumer = load_json(consumer_path)
        compatibility = load_json(compatibility_path)

    clean_status()

    expected_population = {
        "domains": summary.get("domain_count"),
        "features": summary.get("feature_count"),
        "shared_contracts": summary.get("shared_contract_count"),
    }
    for name, evidence in (
        ("publication drift", drift),
        ("semantic governance", semantic),
        ("consumer acceptance", consumer),
    ):
        if evidence.get("spec_commit") != target_sha:
            raise ReleaseFailure(f"{name} evidence is not pinned to target SHA")
        if evidence.get("population") != expected_population:
            raise ReleaseFailure(f"{name} evidence population differs from canonical catalog")
    if compatibility.get("target_commit") != target_sha:
        raise ReleaseFailure("compatibility evidence target differs from candidate SHA")
    if compatibility.get("base_commit") != compatibility_base:
        raise ReleaseFailure("compatibility evidence base differs from requested base")
    if compatibility.get("errors"):
        raise ReleaseFailure("compatibility evidence contains invalid/unversioned changes")
    if semantic.get("errors"):
        raise ReleaseFailure("semantic governance evidence contains release-blocking structural errors")
    if consumer.get("errors") or consumer.get("status") != "pass":
        raise ReleaseFailure("consumer evidence contains release-blocking errors")
    if drift.get("errors") or drift.get("status") != "pass":
        raise ReleaseFailure("publication-drift evidence contains release-blocking errors")

    semantic_governance = semantic.get("semantic_governance") or {}
    class_counts = semantic_governance.get("classification_counts") or {}
    evidence = {
        "schema_version": "1.0",
        "audit": "specification-release-gate",
        "release_version": version,
        "release_tag": f"tllib-specs-v{version}",
        "spec_commit": target_sha,
        "immutable_consumer_target": {
            "authority": "full_git_commit_sha",
            "value": target_sha,
            "tag_role": "discovery_alias_only",
        },
        "compatibility_base": compatibility_base,
        "catalog_sha256": sha256_file(CATALOG_PATH),
        "catalog_schema_version": catalog.get("schema_version"),
        "model_version": catalog.get("model_version"),
        "population": expected_population,
        "package_statuses": summary.get("package_statuses", {}),
        "scientific_statuses": summary.get("scientific_statuses", {}),
        "execution_statuses": summary.get("execution_statuses", {}),
        "semantic_boundaries": {
            "inventory_count": semantic_governance.get("inventory_count"),
            "unique_unresolved_identifier_count": semantic_governance.get("unique_unresolved_identifier_count"),
            "classification_counts": class_counts,
            "added_since_parent": semantic_governance.get("added_since_parent", []),
            "disappeared_since_parent": semantic_governance.get("disappeared_since_parent", []),
            "explicit_resolution_count": semantic_governance.get("explicit_resolution_count"),
            "release_policy": "governed unresolved science is publishable when explicit; only structural validation failures are release blockers",
        },
        "consumer_acceptance": {
            "status": consumer.get("status"),
            "features": len(consumer.get("features", [])),
            "bundle_regenerations_per_feature": consumer.get("bundle_regenerations_per_feature"),
            "consumer_reads_upstream_repository": consumer.get("consumer_reads_upstream_repository"),
            "obligations": consumer.get("obligations", {}),
        },
        "compatibility": {
            "classification": compatibility.get("compatibility"),
            "change_count": len(compatibility.get("changes", [])),
            "errors": compatibility.get("errors", []),
        },
        "publication_drift": {
            "status": drift.get("status"),
            "current_claim_count": drift.get("current_claim_count"),
            "historical_claim_count": drift.get("historical_claim_count"),
            "domain_changes_vs_parent": drift.get("domain_changes_vs_parent"),
        },
        "release_blockers": [],
        "checks": checks,
        "reproduction": {
            "environment": "CPython 3.12 + requirements.lock",
            "entrypoint": "python tools/pipeline/validate_release_gate.py --release-version <version> --target-sha <full-sha> --evidence <path>",
            "requires_clean_checkout": True,
        },
        "status": "pass",
    }
    return evidence


def self_test() -> None:
    assert validate_version("1.0.0") == "1.0.0"
    assert validate_sha("a" * 40) == "a" * 40
    for invalid in ("1.0", "v1.0.0", "1.0.0-beta"):
        try:
            validate_version(invalid)
        except ReleaseFailure:
            pass
        else:
            raise AssertionError(f"invalid release version accepted: {invalid}")
    try:
        validate_sha("abc")
    except ReleaseFailure:
        pass
    else:
        raise AssertionError("short SHA must not be accepted")
    print("Specification release gate logical scenarios: PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-version", required=False)
    parser.add_argument("--target-sha", required=False)
    parser.add_argument("--compatibility-base", required=False)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            return 0
        if not args.release_version or not args.target_sha:
            raise ReleaseFailure("--release-version and --target-sha are required for certification")
        result = certify(args.release_version, args.target_sha, args.compatibility_base)
        rendered = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.evidence:
            args.evidence.parent.mkdir(parents=True, exist_ok=True)
            args.evidence.write_text(rendered, encoding="utf-8")
        print(
            "Specification release gate: PASS "
            f"({result['release_tag']} -> {result['spec_commit']}; "
            f"{result['population']['domains']} domains/"
            f"{result['population']['features']} features/"
            f"{result['population']['shared_contracts']} shared contracts)"
        )
        return 0
    except ReleaseFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
