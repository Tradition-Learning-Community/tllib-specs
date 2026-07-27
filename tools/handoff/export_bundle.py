#!/usr/bin/env python3
"""Resolve one handoff feature and export a standalone directory bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "handoff"
MODEL_VERSION = "1.0.0"


class ExportFailure(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExportFailure(f"cannot read {path}: {exc}") from exc


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hash_tree(path: Path, logical_root: str) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for file_path in sorted(item for item in path.rglob("*") if item.is_file()):
        relative = file_path.relative_to(path).as_posix()
        hashes[f"{logical_root}/{relative}"] = sha256_file(file_path)
    return hashes


def resolve(feature_id: str) -> tuple[Path, dict[str, Any], list[tuple[str, str, Path]], dict[str, str]]:
    feature_dir = HANDOFF / "features" / feature_id
    if not feature_dir.is_dir():
        raise ExportFailure(f"unknown feature package: {feature_id}")
    manifest = load_json(feature_dir / "manifest.json")
    if manifest.get("feature_id") != feature_id:
        raise ExportFailure("feature manifest identity mismatch")

    dependencies: list[tuple[str, str, Path]] = []
    for dependency in manifest["shared_dependencies"]:
        contract_id = dependency["shared_contract_id"]
        required_version = dependency["version"]
        shared_dir = HANDOFF / "shared" / contract_id
        if not shared_dir.is_dir():
            raise ExportFailure(f"missing shared dependency: {contract_id}")
        shared_manifest = load_json(shared_dir / "manifest.json")
        actual_version = shared_manifest.get("package_version")
        if actual_version != required_version:
            raise ExportFailure(
                f"shared dependency version mismatch for {contract_id}: required {required_version}, found {actual_version}"
            )
        dependencies.append((contract_id, actual_version, shared_dir))

    hashes = hash_tree(feature_dir, "feature")
    for contract_id, _, shared_dir in dependencies:
        hashes.update(hash_tree(shared_dir, f"shared/{contract_id}"))
    return feature_dir, manifest, dependencies, hashes


def build_lock(feature_id: str, manifest: dict[str, Any], dependencies: list[tuple[str, str, Path]], hashes: dict[str, str]) -> dict[str, Any]:
    return {
        "model_version": MODEL_VERSION,
        "feature_id": feature_id,
        "package_version": manifest["package_version"],
        "resolved_dependencies": [
            {"shared_contract_id": contract_id, "version": version}
            for contract_id, version, _ in dependencies
        ],
        "hash_algorithm": "sha256",
        "hashes": dict(sorted(hashes.items())),
    }


def export(feature_id: str, output: Path, check_only: bool) -> dict[str, Any]:
    feature_dir, manifest, dependencies, hashes = resolve(feature_id)
    lock = build_lock(feature_id, manifest, dependencies, hashes)
    if check_only:
        return lock

    if output.exists():
        raise ExportFailure(f"output already exists: {output}")
    output.mkdir(parents=True)
    shutil.copytree(feature_dir, output / "feature")
    shared_output = output / "shared"
    shared_output.mkdir()
    for contract_id, _, shared_dir in dependencies:
        shutil.copytree(shared_dir, shared_output / contract_id)
    (output / "bundle-lock.json").write_text(
        json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return lock


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_id", help="Feature package identifier to resolve")
    parser.add_argument("output", nargs="?", type=Path, help="New output directory")
    parser.add_argument("--check", action="store_true", help="Resolve and hash without writing a bundle")
    args = parser.parse_args()
    if not args.check and args.output is None:
        parser.error("output is required unless --check is used")
    return args


def main() -> int:
    args = parse_args()
    try:
        lock = export(args.feature_id, args.output, args.check)
    except ExportFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.check:
        print(json.dumps(lock, indent=2, sort_keys=True))
    else:
        print(f"Exported {args.feature_id} to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
