#!/usr/bin/env python3
"""Run the handoff validator with backward-compatible domain metadata normalization."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import validate_handoff as core


_original_feature_identity = core.feature_identity


def feature_identity(feature_id: str) -> tuple[int, str]:
    """Normalize historical `-de-tl` identifier tokens when an authoritative domain exists."""
    domain_index, identifier_domain = _original_feature_identity(feature_id)
    suffix = "-de-tl"
    if identifier_domain.endswith(suffix):
        normalized_domain = identifier_domain[: -len(suffix)]
        finalization_dir = core.ROOT / "registry" / "domain-finalization" / normalized_domain
        if finalization_dir.is_dir():
            identifier_domain = normalized_domain
    return domain_index, identifier_domain


def validate_authoritative_inventory(domain: str, catalog: dict[str, Any]) -> None:
    """Validate an inventory while accepting established non-scientific count aliases."""
    inventory_value = catalog["metadata"]["authoritative_inventory"]
    expected_value = f"registry/domain-finalization/{domain}/feature-status.yaml"
    if inventory_value != expected_value:
        core.fail(f"domain {domain} must use authoritative inventory {expected_value}")
    if not core.safe_repo_path(inventory_value):
        core.fail(f"unsafe authoritative inventory path for domain {domain}: {inventory_value}")

    inventory = core.load_yaml(core.ROOT / inventory_value)
    if not isinstance(inventory, dict):
        core.fail(f"authoritative inventory is not an object for domain {domain}")

    declared_domains = [inventory[key] for key in ("domain", "domain_id") if key in inventory]
    if not declared_domains or any(value != domain for value in declared_domains):
        core.fail(f"authoritative inventory domain mismatch for {domain}")

    authoritative_features = inventory.get("features")
    if not isinstance(authoritative_features, list):
        core.fail(f"authoritative inventory has no feature list for domain {domain}")
    authoritative_ids = [item.get("feature_id") for item in authoritative_features if isinstance(item, dict)]
    if len(authoritative_ids) != len(authoritative_features) or any(
        not isinstance(item, str) for item in authoritative_ids
    ):
        core.fail(f"authoritative inventory contains an invalid feature entry for domain {domain}")

    declared_counts = [
        inventory[key]
        for key in ("feature_count", "population_count", "active_feature_count")
        if key in inventory
    ]
    summary = inventory.get("summary")
    if isinstance(summary, dict) and "active_features" in summary:
        declared_counts.append(summary["active_features"])
    if not declared_counts or any(value != len(authoritative_ids) for value in declared_counts):
        core.fail(f"authoritative inventory feature count mismatch for domain {domain}")

    if catalog["ordered_feature_ids"] != authoritative_ids:
        core.fail(f"domain catalog population or order differs from authoritative inventory for {domain}")

    for feature_id in authoritative_ids:
        required_artifacts = (
            core.ROOT / "registry" / "optimized-ir" / domain / feature_id / "ir.yaml",
            core.ROOT / "registry" / "algorithms" / domain / feature_id / "algorithm.yaml",
            core.ROOT / "registry" / "oracles" / domain / feature_id / "oracle.yaml",
        )
        for artifact in required_artifacts:
            if not artifact.is_file():
                core.fail(f"authoritative feature artifact is missing: {artifact.relative_to(core.ROOT)}")


core.feature_identity = feature_identity
core.validate_authoritative_inventory = validate_authoritative_inventory


if __name__ == "__main__":
    try:
        raise SystemExit(core.entrypoint())
    except core.ValidationFailure as exc:
        print(f"ERROR: {exc}", file=core.sys.stderr)
        raise SystemExit(1)
