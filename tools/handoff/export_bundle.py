#!/usr/bin/env python3
"""Resolve Feature Handoff packages into deterministic standalone bundles."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.handoff.model import (  # noqa: E402
    EXPECTED_FEATURE_COUNT,
    EXPORTER_VERSION,
    MODEL_VERSION,
)

HANDOFF = ROOT / "handoff"


class ExportFailure(RuntimeError):
    """Raised when a bundle cannot be resolved or reproduced safely."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExportFailure(f"cannot read {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ExportFailure(f"expected JSON object: {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_hashes(path: Path) -> dict[str, str]:
    return {
        item.relative_to(path).as_posix(): sha256_file(item)
        for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file())
    }


def declared_files(package_dir: Path, manifest: dict[str, Any]) -> list[Path]:
    names = manifest.get("files")
    if not isinstance(names, list) or not names:
        raise ExportFailure(f"invalid declared file list in {package_dir.relative_to(ROOT)}")
    files = [package_dir / name for name in names]
    for path in files:
        if not path.is_file():
            raise ExportFailure(f"declared file is missing: {path.relative_to(ROOT)}")
    extra_files = sorted(
        path.relative_to(package_dir).as_posix()
        for path in package_dir.rglob("*")
        if path.is_file() and path not in files
    )
    if extra_files:
        raise ExportFailure(f"undeclared package files in {package_dir.relative_to(ROOT)}: {extra_files}")
    return sorted(files, key=lambda item: item.relative_to(package_dir).as_posix())


def dependency_records(manifest: dict[str, Any]) -> list[dict[str, str]]:
    dependencies = manifest.get("shared_dependencies")
    if not isinstance(dependencies, list):
        raise ExportFailure("shared_dependencies is not a list")
    records: list[dict[str, str]] = []
    for dependency in dependencies:
        if not isinstance(dependency, dict):
            raise ExportFailure("shared dependency is not an object")
        contract_id = dependency.get("shared_contract_id")
        version = dependency.get("version")
        if not isinstance(contract_id, str) or not isinstance(version, str):
            raise ExportFailure("shared dependency identity or version is invalid")
        records.append({"shared_contract_id": contract_id, "version": version})
    if len(records) != len({item["shared_contract_id"] for item in records}):
        raise ExportFailure("duplicate shared dependency identity")
    return sorted(records, key=lambda item: item["shared_contract_id"])


def resolve_shared_contracts(root_manifest: dict[str, Any]) -> list[tuple[str, str, Path, dict[str, Any]]]:
    resolved: dict[str, tuple[str, Path, dict[str, Any]]] = {}
    pending = dependency_records(root_manifest)
    while pending:
        dependency = pending.pop(0)
        contract_id = dependency["shared_contract_id"]
        required_version = dependency["version"]
        previous = resolved.get(contract_id)
        if previous is not None:
            if previous[0] != required_version:
                raise ExportFailure(
                    f"conflicting shared dependency versions for {contract_id}: {previous[0]} and {required_version}"
                )
            continue
        shared_dir = HANDOFF / "shared" / contract_id
        if not shared_dir.is_dir():
            raise ExportFailure(f"missing shared dependency: {contract_id}")
        manifest = load_json(shared_dir / "manifest.json")
        if manifest.get("shared_contract_id") != contract_id:
            raise ExportFailure(f"shared dependency identity mismatch: {contract_id}")
        actual_version = manifest.get("package_version")
        if actual_version != required_version:
            raise ExportFailure(
                f"shared dependency version mismatch for {contract_id}: required {required_version}, found {actual_version}"
            )
        declared_files(shared_dir, manifest)
        resolved[contract_id] = (actual_version, shared_dir, manifest)
        pending.extend(dependency_records(manifest))
        pending.sort(key=lambda item: item["shared_contract_id"])
    return [
        (contract_id, version, shared_dir, manifest)
        for contract_id, (version, shared_dir, manifest) in sorted(resolved.items())
    ]


def file_record(source: Path, bundle_path: str) -> dict[str, str]:
    source_path = source.relative_to(ROOT).as_posix()
    if not (
        source_path.startswith("handoff/features/")
        or source_path.startswith("handoff/shared/")
    ):
        raise ExportFailure(f"bundle source escapes finalized handoff artifacts: {source_path}")
    return {
        "source_path": source_path,
        "bundle_path": bundle_path,
        "sha256": sha256_file(source),
    }


def resolve(feature_id: str) -> tuple[Path, dict[str, Any], list[tuple[str, str, Path, dict[str, Any]]], list[dict[str, str]]]:
    feature_dir = HANDOFF / "features" / feature_id
    if not feature_dir.is_dir():
        raise ExportFailure(f"unknown feature package: {feature_id}")
    manifest = load_json(feature_dir / "manifest.json")
    if manifest.get("feature_id") != feature_id:
        raise ExportFailure(f"feature manifest identity mismatch: {feature_id}")
    feature_files = declared_files(feature_dir, manifest)
    dependencies = resolve_shared_contracts(manifest)

    records = [
        file_record(path, f"feature/{path.relative_to(feature_dir).as_posix()}")
        for path in feature_files
    ]
    for contract_id, _, shared_dir, shared_manifest in dependencies:
        for path in declared_files(shared_dir, shared_manifest):
            records.append(
                file_record(path, f"shared/{contract_id}/{path.relative_to(shared_dir).as_posix()}")
            )
    records.sort(key=lambda item: item["bundle_path"])
    if len(records) != len({item["bundle_path"] for item in records}):
        raise ExportFailure(f"duplicate bundle path while resolving {feature_id}")
    return feature_dir, manifest, dependencies, records


def aggregate_package_hash(records: Iterable[dict[str, str]]) -> str:
    digest = hashlib.sha256()
    for record in sorted(records, key=lambda item: item["bundle_path"]):
        digest.update(record["bundle_path"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(record["sha256"]))
        digest.update(b"\n")
    return digest.hexdigest()


def build_lock(
    feature_id: str,
    manifest: dict[str, Any],
    dependencies: list[tuple[str, str, Path, dict[str, Any]]],
    files: list[dict[str, str]],
) -> dict[str, Any]:
    shared_contracts: list[dict[str, str]] = []
    for contract_id, version, shared_dir, shared_manifest in dependencies:
        shared_records = [
            record for record in files if record["bundle_path"].startswith(f"shared/{contract_id}/")
        ]
        shared_contracts.append(
            {
                "shared_contract_id": contract_id,
                "version": version,
                "source_path": shared_dir.relative_to(ROOT).as_posix(),
                "bundle_path": f"shared/{contract_id}",
                "package_sha256": aggregate_package_hash(shared_records),
                "declared_dependency_count": len(dependency_records(shared_manifest)),
            }
        )
    return {
        "schema_version": "1.0",
        "model_version": MODEL_VERSION,
        "feature_id": feature_id,
        "package_version": manifest["package_version"],
        "generation": {
            "tool": "tools/handoff/export_bundle.py",
            "tool_version": EXPORTER_VERSION,
            "deterministic": True,
            "volatile_fields_present": False,
        },
        "resolved_shared_contracts": shared_contracts,
        "files": files,
        "bundle_sha256": aggregate_package_hash(files),
    }


def export(feature_id: str, output: Path | None, check_only: bool) -> dict[str, Any]:
    feature_dir, manifest, dependencies, files = resolve(feature_id)
    lock = build_lock(feature_id, manifest, dependencies, files)
    if check_only:
        return lock
    if output is None:
        raise ExportFailure("output directory is required for bundle creation")
    if output.exists():
        raise ExportFailure(f"output already exists: {output}")
    output.mkdir(parents=True)
    shutil.copytree(feature_dir, output / "feature")
    shared_output = output / "shared"
    shared_output.mkdir()
    for contract_id, _, shared_dir, _ in dependencies:
        shutil.copytree(shared_dir, shared_output / contract_id)
    (output / "bundle-lock.json").write_text(
        json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if set(path.name for path in output.iterdir()) != {"feature", "shared", "bundle-lock.json"}:
        raise ExportFailure(f"invalid exported root structure for {feature_id}")
    return lock


def feature_ids_from_catalog() -> list[str]:
    catalog = load_json(HANDOFF / "catalog.json")
    features = catalog.get("features")
    if not isinstance(features, list):
        raise ExportFailure("global catalog features is not a list")
    feature_ids = [entry.get("feature_id") for entry in features if isinstance(entry, dict)]
    if len(feature_ids) != EXPECTED_FEATURE_COUNT or any(not isinstance(item, str) for item in feature_ids):
        raise ExportFailure(
            f"global catalog must contain exactly {EXPECTED_FEATURE_COUNT} feature identities"
        )
    if len(feature_ids) != len(set(feature_ids)):
        raise ExportFailure("global catalog contains duplicate feature identities")
    return feature_ids


def verify_determinism(feature_id: str) -> None:
    with tempfile.TemporaryDirectory(prefix="tllib-handoff-a-") as first_temp, tempfile.TemporaryDirectory(
        prefix="tllib-handoff-b-"
    ) as second_temp:
        first = Path(first_temp) / "bundle"
        second = Path(second_temp) / "bundle"
        first_lock = export(feature_id, first, check_only=False)
        second_lock = export(feature_id, second, check_only=False)
        if first_lock != second_lock or tree_hashes(first) != tree_hashes(second):
            raise ExportFailure(f"non-deterministic bundle generation detected for {feature_id}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_id", nargs="?", help="Feature package identifier to resolve")
    parser.add_argument("output", nargs="?", type=Path, help="New output directory for one feature")
    parser.add_argument("--all", action="store_true", help="validate every feature in the finalized catalog")
    parser.add_argument("--check", action="store_true", help="resolve and hash without retaining bundle output")
    parser.add_argument(
        "--verify-determinism",
        action="store_true",
        help="generate each selected bundle twice in temporary directories and compare every byte hash",
    )
    arguments = parser.parse_args()
    if arguments.all and arguments.feature_id is not None:
        parser.error("feature_id cannot be combined with --all")
    if not arguments.all and arguments.feature_id is None:
        parser.error("provide feature_id or --all")
    if arguments.all and arguments.output is not None:
        parser.error("output cannot be combined with --all")
    if not arguments.all and not arguments.check and arguments.output is None:
        parser.error("output is required unless --check is used")
    return arguments


def main() -> int:
    arguments = parse_args()
    try:
        feature_ids = feature_ids_from_catalog() if arguments.all else [arguments.feature_id]
        assert all(isinstance(item, str) for item in feature_ids)
        for feature_id in feature_ids:
            lock = export(
                feature_id,
                None if arguments.all or arguments.check else arguments.output,
                check_only=arguments.all or arguments.check,
            )
            if arguments.verify_determinism:
                verify_determinism(feature_id)
            if not arguments.all and arguments.check:
                print(json.dumps(lock, ensure_ascii=False, indent=2))
        if arguments.all:
            detail = " with byte-for-byte deterministic regeneration" if arguments.verify_determinism else ""
            print(f"Validated standalone resolution for {len(feature_ids)} feature bundles{detail}.")
        elif not arguments.check:
            print(f"Exported {feature_ids[0]} to {arguments.output}")
        return 0
    except ExportFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
