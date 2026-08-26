#!/usr/bin/env python3
"""Generate or verify the Feature Handoff Package v1.0 catalog.

The committed ``handoff/catalog.json`` defines the published population at the
target commit. This generator reconstructs deterministic descriptors for that
population from finalized handoff artifacts and rejects missing or ghost
published artifacts. It emits no volatile timestamp.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.handoff.model import (  # noqa: E402
    CATALOG_GENERATOR_VERSION,
    DOMAIN_ORDER,
    EXPECTED_DOMAIN_COUNT,
    EXPECTED_FEATURE_COUNT,
    EXPORTER_VERSION,
    MODEL_VERSION,
    VALIDATOR_VERSION,
)

HANDOFF = ROOT / "handoff"
CATALOG_PATH = HANDOFF / "catalog.json"


class CatalogGenerationFailure(RuntimeError):
    """Raised when source handoff metadata is incomplete or inconsistent."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CatalogGenerationFailure(f"missing required file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise CatalogGenerationFailure(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise CatalogGenerationFailure(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def aggregate_fingerprint(paths: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda item: item.as_posix()):
        relative = path.relative_to(ROOT).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
        digest.update(b"\n")
    return digest.hexdigest()


def package_files(package_dir: Path, manifest: dict[str, Any]) -> list[Path]:
    declared = manifest.get("files")
    if not isinstance(declared, list) or not declared or any(not isinstance(item, str) for item in declared):
        raise CatalogGenerationFailure(f"invalid declared file list: {package_dir.relative_to(ROOT)}")
    paths = [package_dir / name for name in declared]
    missing = [path.relative_to(ROOT).as_posix() for path in paths if not path.is_file()]
    if missing:
        raise CatalogGenerationFailure(f"declared files are missing: {missing}")
    actual = {path for path in package_dir.rglob("*") if path.is_file()}
    if actual != set(paths):
        extra = sorted(path.relative_to(ROOT).as_posix() for path in actual - set(paths))
        raise CatalogGenerationFailure(f"undeclared package files in {package_dir.relative_to(ROOT)}: {extra}")
    return paths


def normalized_dependencies(manifest: dict[str, Any]) -> list[dict[str, str]]:
    dependencies = manifest.get("shared_dependencies")
    if not isinstance(dependencies, list):
        raise CatalogGenerationFailure("manifest shared_dependencies is not a list")
    normalized: list[dict[str, str]] = []
    for item in dependencies:
        if not isinstance(item, dict):
            raise CatalogGenerationFailure("manifest dependency is not an object")
        identifier = item.get("shared_contract_id")
        version = item.get("version")
        if not isinstance(identifier, str) or not isinstance(version, str):
            raise CatalogGenerationFailure("manifest dependency identity or version is invalid")
        normalized.append({"shared_contract_id": identifier, "version": version})
    if len(normalized) != len({item["shared_contract_id"] for item in normalized}):
        raise CatalogGenerationFailure("duplicate shared dependency identity")
    return sorted(normalized, key=lambda item: (item["shared_contract_id"], item["version"]))


def shared_catalog_entries() -> list[dict[str, Any]]:
    shared_root = HANDOFF / "shared"
    if not shared_root.is_dir():
        raise CatalogGenerationFailure("handoff/shared is missing")
    entries: list[dict[str, Any]] = []
    for package_dir in sorted(path for path in shared_root.iterdir() if path.is_dir()):
        manifest = load_json(package_dir / "manifest.json")
        shared_id = manifest.get("shared_contract_id")
        if shared_id != package_dir.name:
            raise CatalogGenerationFailure(f"shared contract identity mismatch: {package_dir.relative_to(ROOT)}")
        files = package_files(package_dir, manifest)
        entries.append(
            {
                "shared_contract_id": shared_id,
                "version": manifest["package_version"],
                "path": package_dir.relative_to(ROOT).as_posix(),
                "status": manifest["statuses"]["package"],
                "dependencies": normalized_dependencies(manifest),
                "package_sha256": aggregate_fingerprint(files),
            }
        )
    return entries


def build_catalog() -> dict[str, Any]:
    domains_root = HANDOFF / "domains"
    if not domains_root.is_dir():
        raise CatalogGenerationFailure("handoff/domains is missing")
    actual_domains = {path.name for path in domains_root.iterdir() if path.is_dir()}
    expected_domains = set(DOMAIN_ORDER)
    if actual_domains != expected_domains:
        raise CatalogGenerationFailure(
            "published domain population mismatch: "
            f"expected={sorted(expected_domains)}, observed={sorted(actual_domains)}"
        )

    domains: list[dict[str, Any]] = []
    features: list[dict[str, Any]] = []
    package_statuses: Counter[str] = Counter()
    scientific_statuses: Counter[str] = Counter()
    execution_statuses: Counter[str] = Counter()
    examples_present = 0
    seen: set[str] = set()
    seen_domain_indices: set[int] = set()

    for domain in DOMAIN_ORDER:
        catalog_path = domains_root / domain / "catalog.json"
        domain_catalog = load_json(catalog_path)
        domain_index = domain_catalog.get("domain_index")
        if domain_catalog.get("domain") != domain or isinstance(domain_index, bool) or not isinstance(domain_index, int):
            raise CatalogGenerationFailure(f"domain identity or index mismatch: {catalog_path.relative_to(ROOT)}")
        if domain_index in seen_domain_indices:
            raise CatalogGenerationFailure(f"duplicate domain index {domain_index}: {catalog_path.relative_to(ROOT)}")
        seen_domain_indices.add(domain_index)
        if domain_catalog.get("statuses") != {"population": "complete", "validation": "validated"}:
            raise CatalogGenerationFailure(f"domain is not publishable: {domain}")
        ordered_ids = domain_catalog.get("ordered_feature_ids")
        entries = domain_catalog.get("feature_packages")
        if not isinstance(ordered_ids, list) or not isinstance(entries, list):
            raise CatalogGenerationFailure(f"invalid domain population: {catalog_path.relative_to(ROOT)}")
        if domain_catalog.get("expected_feature_count") != len(ordered_ids) or len(entries) != len(ordered_ids):
            raise CatalogGenerationFailure(
                f"domain feature count mismatch for {domain}: expected={domain_catalog.get('expected_feature_count')}, "
                f"observed={len(ordered_ids)}"
            )
        if [entry.get("feature_id") for entry in entries if isinstance(entry, dict)] != ordered_ids:
            raise CatalogGenerationFailure(f"domain package order mismatch: {catalog_path.relative_to(ROOT)}")

        domains.append(
            {
                "domain": domain,
                "domain_index": domain_index,
                "catalog_path": catalog_path.relative_to(ROOT).as_posix(),
                "feature_count": len(ordered_ids),
                "catalog_sha256": sha256_file(catalog_path),
            }
        )

        for domain_entry in entries:
            if not isinstance(domain_entry, dict):
                raise CatalogGenerationFailure(f"invalid package entry in {catalog_path.relative_to(ROOT)}")
            feature_id = domain_entry.get("feature_id")
            if not isinstance(feature_id, str):
                raise CatalogGenerationFailure(f"invalid feature identity in {catalog_path.relative_to(ROOT)}")
            if feature_id in seen:
                raise CatalogGenerationFailure(f"duplicate feature identity: {feature_id}")
            seen.add(feature_id)
            path_value = domain_entry.get("path")
            if not isinstance(path_value, str):
                raise CatalogGenerationFailure(f"invalid package path for {feature_id}")
            package_dir = ROOT / path_value
            manifest_path = package_dir / "manifest.json"
            manifest = load_json(manifest_path)
            if manifest.get("feature_id") != feature_id or manifest.get("domain") != domain:
                raise CatalogGenerationFailure(f"feature identity or domain mismatch: {manifest_path.relative_to(ROOT)}")
            if manifest.get("package_version") != domain_entry.get("package_version"):
                raise CatalogGenerationFailure(f"feature package version mismatch: {feature_id}")
            if manifest.get("statuses", {}).get("package") != domain_entry.get("status"):
                raise CatalogGenerationFailure(f"feature package status mismatch: {feature_id}")

            files = package_files(package_dir, manifest)
            statuses = manifest["statuses"]
            examples = manifest["examples"]
            dependencies = normalized_dependencies(manifest)
            package_statuses[statuses["package"]] += 1
            scientific_statuses[statuses["scientific"]] += 1
            execution_statuses[statuses["execution"]] += 1
            examples_present += int(bool(examples["present"]))

            descriptor = {
                "feature_id": feature_id,
                "domain": domain,
                "path": path_value,
                "package_version": manifest["package_version"],
                "statuses": statuses,
                "examples_present": bool(examples["present"]),
                "shared_dependencies": dependencies,
                "package_sha256": aggregate_fingerprint(files),
            }
            features.append(
                {
                    **descriptor,
                    "manifest_path": manifest_path.relative_to(ROOT).as_posix(),
                    "descriptor_sha256": sha256_bytes(canonical_json(descriptor)),
                    "deprecation": None,
                    "substitution": None,
                }
            )

    feature_root = HANDOFF / "features"
    actual_features = {path.name for path in feature_root.iterdir() if path.is_dir()} if feature_root.is_dir() else set()
    expected_features = {entry["feature_id"] for entry in features}
    if actual_features != expected_features:
        raise CatalogGenerationFailure(
            "published feature population mismatch: "
            f"missing={sorted(expected_features - actual_features)}, orphan={sorted(actual_features - expected_features)}"
        )

    if len(domains) != EXPECTED_DOMAIN_COUNT or len(features) != EXPECTED_FEATURE_COUNT:
        raise CatalogGenerationFailure(
            "catalog-derived population changed while reconstructing artifacts: "
            f"expected={EXPECTED_DOMAIN_COUNT} domains/{EXPECTED_FEATURE_COUNT} features, "
            f"observed={len(domains)} domains/{len(features)} features"
        )

    shared_contracts = shared_catalog_entries()
    return {
        "schema_version": "1.0",
        "model_version": MODEL_VERSION,
        "catalog_status": "finalized",
        # Legacy v1.0 field retained for byte-compatible reconstruction of the
        # current catalog. Its name is historical and its value is not used to
        # derive or cap the published population.
        "complete_166_feature_catalog_finalized": True,
        "validator": {"entrypoint": "tools/handoff/validate_handoff.py", "version": VALIDATOR_VERSION},
        "exporter": {"entrypoint": "tools/handoff/export_bundle.py", "version": EXPORTER_VERSION},
        "generation": {
            "entrypoint": "tools/handoff/generate_catalog.py",
            "version": CATALOG_GENERATOR_VERSION,
            "deterministic": True,
            "volatile_fields_present": False,
        },
        "shared_contracts": shared_contracts,
        "domains": domains,
        "features": features,
        "summary": {
            "domain_count": len(domains),
            "feature_count": len(features),
            "shared_contract_count": len(shared_contracts),
            "package_statuses": dict(sorted(package_statuses.items())),
            "scientific_statuses": dict(sorted(scientific_statuses.items())),
            "execution_statuses": dict(sorted(execution_statuses.items())),
            "examples_present": examples_present,
            "examples_absent": len(features) - examples_present,
            "promoted_shared_contract_candidates": 0,
        },
    }


def rendered_catalog() -> str:
    return json.dumps(build_catalog(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="refresh deterministic fields for the canonical population")
    mode.add_argument("--check", action="store_true", help="verify the committed catalog is current")
    arguments = parser.parse_args()

    rendered = rendered_catalog()
    if arguments.write:
        CATALOG_PATH.write_text(rendered, encoding="utf-8")
        catalog = json.loads(rendered)
        print(
            "Wrote deterministic handoff catalog "
            f"({catalog['summary']['domain_count']} domains, {catalog['summary']['feature_count']} features)."
        )
        return 0

    try:
        current = CATALOG_PATH.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CatalogGenerationFailure("handoff/catalog.json is missing") from exc
    if current != rendered:
        raise CatalogGenerationFailure(
            "handoff/catalog.json is stale; regenerate with tools/handoff/generate_catalog.py --write"
        )
    summary = json.loads(current)["summary"]
    print("Deterministic handoff catalog is current.")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CatalogGenerationFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
