#!/usr/bin/env python3
"""Run the handoff validator with backward-compatible inventory normalization."""

from __future__ import annotations

import sys
from typing import Any

import validate_handoff as core


_original_feature_identity = core.feature_identity

ROOT_COUNT_KEYS = (
    "feature_count",
    "population_count",
    "active_feature_count",
    "authoritative_feature_count",
    "authoritative_population_count",
    "expected_count",
    "expected_active_count",
    "expected_feature_count",
    "expected_active_feature_count",
)
SUMMARY_COUNT_KEYS = (
    "active_features",
    "selected_features",
    "feature_count",
    "population_count",
)
MANIFEST_COUNT_PATHS = (
    ("feature_count",),
    ("population_count",),
    ("expected_feature_count",),
    ("expected_active_feature_count",),
    ("baseline", "expected_feature_count"),
    ("baseline", "expected_active_feature_count"),
)


def feature_identity(feature_id: str) -> tuple[int, str]:
    """Normalize historical ``-de-tl`` identifier tokens only when reversible."""
    domain_index, identifier_domain = _original_feature_identity(feature_id)
    suffix = "-de-tl"
    if identifier_domain.endswith(suffix):
        normalized_domain = identifier_domain[: -len(suffix)]
        finalization_dir = core.ROOT / "registry" / "domain-finalization" / normalized_domain
        if finalization_dir.is_dir():
            identifier_domain = normalized_domain
    return domain_index, identifier_domain


def authoritative_feature_ids(inventory: dict[str, Any], domain: str) -> list[str]:
    """Read either historical list-form or insertion-ordered mapping-form features."""
    features = inventory.get("features")
    if isinstance(features, list):
        identifiers = [item.get("feature_id") for item in features if isinstance(item, dict)]
        if len(identifiers) != len(features) or any(not isinstance(item, str) for item in identifiers):
            core.fail(f"authoritative inventory contains an invalid feature entry for domain {domain}")
        return identifiers
    if isinstance(features, dict):
        identifiers = list(features)
        if any(not isinstance(item, str) for item in identifiers) or any(
            not isinstance(value, dict) for value in features.values()
        ):
            core.fail(f"authoritative inventory contains an invalid feature mapping for domain {domain}")
        return identifiers
    core.fail(f"authoritative inventory has no feature list or mapping for domain {domain}")


def inventory_declared_counts(inventory: dict[str, Any]) -> list[Any]:
    """Collect every established count alias present in the authoritative inventory."""
    counts = [inventory[key] for key in ROOT_COUNT_KEYS if key in inventory]
    summary = inventory.get("summary")
    if isinstance(summary, dict):
        counts.extend(summary[key] for key in SUMMARY_COUNT_KEYS if key in summary)
    return counts


def nested_value(document: dict[str, Any], path: tuple[str, ...]) -> tuple[bool, Any]:
    current: Any = document
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return False, None
        current = current[key]
    return True, current


def manifest_fallback_counts(domain: str, authoritative_ids: list[str]) -> list[Any]:
    """Use a sibling finalization manifest only when the inventory has no count field."""
    manifest_path = core.ROOT / "registry" / "domain-finalization" / domain / "manifest.yaml"
    if not manifest_path.is_file():
        return []
    manifest = core.load_yaml(manifest_path)
    if not isinstance(manifest, dict):
        core.fail(f"domain finalization manifest is not an object for domain {domain}")

    population = manifest.get("population")
    if population is not None:
        if not isinstance(population, list) or any(not isinstance(item, str) for item in population):
            core.fail(f"domain finalization manifest has an invalid population for domain {domain}")
        if population != authoritative_ids:
            core.fail(f"domain finalization manifest population differs from authoritative inventory for {domain}")

    counts: list[Any] = []
    for path in MANIFEST_COUNT_PATHS:
        present, value = nested_value(manifest, path)
        if present:
            counts.append(value)
    return counts


def validate_counts(domain: str, values: list[Any], actual_count: int) -> None:
    """Require every supplied alias to be an integer equal to the real population."""
    if not values or any(
        isinstance(value, bool) or not isinstance(value, int) or value != actual_count for value in values
    ):
        core.fail(f"authoritative inventory feature count mismatch for domain {domain}")


def validate_authoritative_inventory(domain: str, catalog: dict[str, Any]) -> None:
    """Validate historical metadata without weakening exact population comparison."""
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

    authoritative_ids = authoritative_feature_ids(inventory, domain)
    declared_counts = inventory_declared_counts(inventory)
    if not declared_counts:
        declared_counts = manifest_fallback_counts(domain, authoritative_ids)
    validate_counts(domain, declared_counts, len(authoritative_ids))

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


def run_compatibility_self_tests() -> None:
    """Exercise historical list, mapping, and conflicting-count shapes."""
    list_inventory = {"features": [{"feature_id": "A"}, {"feature_id": "B"}]}
    mapping_inventory = {"features": {"A": {}, "B": {}}}
    if authoritative_feature_ids(list_inventory, "test-list") != ["A", "B"]:
        core.fail("compatibility self-test I failed for list-form features")
    if authoritative_feature_ids(mapping_inventory, "test-mapping") != ["A", "B"]:
        core.fail("compatibility self-test J failed for mapping-form features")
    validate_counts("test-counts", [2, 2], 2)
    core.expect_failure(
        lambda: validate_counts("test-conflict", [2, 3], 2),
        "K conflicting historical count aliases",
    )
    print("Inventory compatibility logical self-tests I-K passed.")


core.feature_identity = feature_identity
core.validate_authoritative_inventory = validate_authoritative_inventory


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--self-test"]:
            run_compatibility_self_tests()
        raise SystemExit(core.entrypoint())
    except core.ValidationFailure as exc:
        print(f"ERROR: {exc}", file=core.sys.stderr)
        raise SystemExit(1)
