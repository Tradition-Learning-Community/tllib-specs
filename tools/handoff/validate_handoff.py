#!/usr/bin/env python3
"""Validate the finalized Feature Handoff Package v1.0 model.

This file is the only normative validation CLI. Historical metadata shapes are
accepted strictly in read mode, while all published handoff artifacts remain in
the canonical v1.0 form.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterable

from jsonschema import Draft202012Validator
from yaml import YAMLError, safe_load

ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "handoff"
SCHEMAS = HANDOFF / "schemas"
MODEL_VERSION = "1.0.0"
VALIDATOR_VERSION = "1.0.0"
PILOT_ID = "TLC-FC-00-MASTER-005"
DOMAIN_ORDER = (
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
)
EXPECTED_SHARED = {
    "TLC-HC-FEATURE-ID",
    "TLC-HC-SCIENTIFIC-REFERENCE",
    "TLC-HC-REFERENCE-COLLECTION",
    "TLC-HC-UNRESOLVED-ITEM",
    "TLC-HC-OPAQUE-VALUE",
    "TLC-HC-STRUCTURED-ERROR",
    "TLC-HC-TRACEABILITY",
    "TLC-HC-DESCRIPTOR-ENVELOPE",
}
FEATURE_ID_PATTERN = re.compile(
    r"^TLC-FC-(?P<index>[0-9]{2})-(?P<domain>[A-Z][A-Z0-9-]*)-[0-9]{3}$"
)
REQUIRED_TRACE_CATEGORIES = (
    "scientific_sources",
    "mathematical_contracts",
    "source_irs",
    "finalized_irs",
    "algorithm_specifications",
    "test_plans",
    "acceptance_oracles",
    "scientific_decisions",
)
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


class ValidationFailure(RuntimeError):
    """Raised whenever a normative validation rule is violated."""


def fail(message: str) -> None:
    raise ValidationFailure(message)


@lru_cache(maxsize=None)
def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationFailure(f"missing required file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationFailure(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


@lru_cache(maxsize=None)
def load_yaml(path: Path) -> Any:
    try:
        return safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationFailure(f"missing authoritative inventory: {path.relative_to(ROOT)}") from exc
    except YAMLError as exc:
        raise ValidationFailure(f"invalid YAML in {path.relative_to(ROOT)}: {exc}") from exc


def validate_schema(instance: Any, schema: Any, path: Path) -> None:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    if errors:
        details = "; ".join(
            f"{'/'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in errors[:10]
        )
        fail(f"schema validation failed for {path.relative_to(ROOT)}: {details}")


def safe_repo_path(value: str) -> bool:
    path = Path(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts and not value.startswith("~")


def walk_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)


def feature_identity(feature_id: str) -> tuple[int, str]:
    match = FEATURE_ID_PATTERN.fullmatch(feature_id)
    if match is None:
        fail(f"invalid feature identifier: {feature_id}")
    identifier_domain = match.group("domain").lower()
    historical_suffix = "-de-tl"
    if identifier_domain.endswith(historical_suffix):
        normalized = identifier_domain[: -len(historical_suffix)]
        if (ROOT / "registry" / "domain-finalization" / normalized).is_dir():
            identifier_domain = normalized
    return int(match.group("index")), identifier_domain


def register_feature_owner(owners: dict[str, str], feature_id: str, domain: str) -> None:
    previous = owners.get(feature_id)
    if previous is not None:
        fail(f"feature {feature_id} is declared by both {previous} and {domain}")
    owners[feature_id] = domain


def package_files(package_dir: Path, manifest: dict[str, Any]) -> None:
    required = {"README.md", "manifest.json", "contract.json", "acceptance.json", "traceability.json"}
    declared_values = manifest.get("files")
    if not isinstance(declared_values, list) or any(not isinstance(item, str) for item in declared_values):
        fail(f"invalid declared file list in {package_dir.relative_to(ROOT)}")
    declared = set(declared_values)
    examples = manifest.get("examples")
    if not isinstance(examples, dict) or not isinstance(examples.get("present"), bool):
        fail(f"invalid examples declaration in {package_dir.relative_to(ROOT)}")
    expected = set(required)
    if examples["present"]:
        expected.add("examples.json")
    if declared != expected:
        fail(
            f"declared package files must equal {sorted(expected)} in {package_dir.relative_to(ROOT)}, "
            f"found {sorted(declared)}"
        )
    actual = {
        path.relative_to(package_dir).as_posix()
        for path in package_dir.rglob("*")
        if path.is_file()
    }
    if actual != expected:
        fail(
            f"package file population mismatch in {package_dir.relative_to(ROOT)}: "
            f"expected {sorted(expected)}, found {sorted(actual)}"
        )


def validate_trace_paths(trace: dict[str, Any], path: Path, require_nonempty: bool) -> None:
    for category in REQUIRED_TRACE_CATEGORIES:
        if category not in trace:
            fail(f"missing traceability category {category} in {path.relative_to(ROOT)}")
        refs = trace[category]
        if not isinstance(refs, list):
            fail(f"traceability category {category} is not a list in {path.relative_to(ROOT)}")
        if require_nonempty and not refs:
            fail(f"{category} must be non-empty in {path.relative_to(ROOT)}")
        for ref in refs:
            if not isinstance(ref, dict) or not isinstance(ref.get("path"), str):
                fail(f"invalid traceability reference in {path.relative_to(ROOT)}")
            value = ref["path"]
            if not safe_repo_path(value):
                fail(f"unsafe traceability path {value!r} in {path.relative_to(ROOT)}")
            if not (ROOT / value).exists():
                fail(f"unresolved traceability path {value!r} in {path.relative_to(ROOT)}")


def validate_no_normative_language_code(package_dir: Path) -> None:
    patterns = (
        re.compile(r"```[ \t]*(?:c\+\+|cpp|rust|ruby|python)\b", re.IGNORECASE),
        re.compile(r"(?m)^\s*#include\s*[<\"]"),
        re.compile(r"(?m)^\s*(?:pub\s+)?fn\s+[A-Za-z_]\w*\s*\("),
        re.compile(r"(?m)^\s*def\s+[A-Za-z_]\w*[!?=]?\s*(?:\(|$)"),
        re.compile(r"\bstd::[A-Za-z_]\w*"),
    )
    for name in ("contract.json", "acceptance.json", "examples.json"):
        path = package_dir / name
        if not path.exists():
            continue
        document = load_json(path)
        if any(pattern.search(text) for text in walk_strings(document) for pattern in patterns):
            fail(f"normative programming-language code found in {path.relative_to(ROOT)}")


def validate_strategy(contract: dict[str, Any], trace: dict[str, Any], path: Path) -> None:
    operations = contract.get("operations")
    if not isinstance(operations, list) or not operations:
        fail(f"contract has no observable operation in {path.relative_to(ROOT)}")
    for operation in operations:
        strategy = operation["strategy_contract"]
        steps = strategy["steps"]
        if len(steps) != len(set(steps)):
            fail(f"duplicate strategy step in operation {operation['operation_id']} at {path.relative_to(ROOT)}")
        step_set = set(steps)
        for edge in strategy["partial_order"]:
            if edge["before"] not in step_set or edge["after"] not in step_set:
                fail(f"partial-order edge references an unknown step in {path.relative_to(ROOT)}")
            if edge["before"] == edge["after"]:
                fail(f"partial-order edge is reflexive in {path.relative_to(ROOT)}")
        if strategy["mode"] == "prescribed":
            if not strategy["prescription_basis"]:
                fail(f"prescribed strategy lacks an authoritative basis in {path.relative_to(ROOT)}")
            if not trace["algorithm_specifications"]:
                fail(f"prescribed strategy lacks algorithm traceability in {path.relative_to(ROOT)}")


def validate_error_uniqueness(contract: dict[str, Any], path: Path) -> None:
    for operation in contract.get("operations", []):
        codes = [item["code"] for item in operation["error_contract"]]
        if len(codes) != len(set(codes)):
            fail(f"duplicate error code in operation {operation['operation_id']} at {path.relative_to(ROOT)}")


def validate_acceptance_ids(acceptance: dict[str, Any], global_ids: set[str], path: Path) -> None:
    tests = acceptance.get("tests")
    if not isinstance(tests, list) or not tests:
        fail(f"acceptance plan has no test in {path.relative_to(ROOT)}")
    local: set[str] = set()
    for test in tests:
        test_id = test["test_id"]
        if test_id in local or test_id in global_ids:
            fail(f"duplicate test_id {test_id} in {path.relative_to(ROOT)}")
        local.add(test_id)
        global_ids.add(test_id)


def validate_feature_readme(package_dir: Path, feature_id: str) -> None:
    text = (package_dir / "README.md").read_text(encoding="utf-8")
    if len(text.strip()) < 200:
        fail(f"feature README for {feature_id} is too short in {package_dir.relative_to(ROOT)}")


def validate_pilot(contract: dict[str, Any], acceptance: dict[str, Any], manifest: dict[str, Any]) -> None:
    if contract["feature"]["feature_id"] != PILOT_ID:
        fail("pilot contract feature_id mismatch")
    if manifest["statuses"] != {
        "package": "pilot",
        "scientific": "partially_defined",
        "execution": "structural_only",
    }:
        fail("pilot multidimensional status mismatch")
    text = json.dumps(contract, sort_keys=True)
    required_tokens = {
        "TLC-SO-MASTER-008",
        "TLC-SR-MASTER-007",
        "TLC-SR-MASTER-008",
        "TLC-SR-MASTER-009",
        "TLC-SR-MASTER-010",
        "TLC-SR-MASTER-011",
        "MASTER_INVALID_FEATURE_ID",
        "MASTER_REFERENCE_SET_MISMATCH",
        "MASTER_PRESERVATION_VIOLATION",
        "MASTER_UNSUPPORTED_EXECUTION_MODE",
    }
    missing = sorted(token for token in required_tokens if token not in text)
    if missing:
        fail(f"pilot contract is missing required source-backed tokens: {missing}")
    if len(contract["operations"]) != 1:
        fail("pilot must expose exactly one structural operation in v1.0")
    if contract["operations"][0]["strategy_contract"]["mode"] != "partially_constrained":
        fail("pilot must preserve internal strategy freedom with a partially constrained strategy")
    test_ids = {test["test_id"] for test in acceptance["tests"]}
    if not {f"MASTER-005-A{i:02d}" for i in range(1, 9)}.issubset(test_ids):
        fail("pilot does not preserve all eight oracle acceptance identifiers")


def authoritative_feature_ids(inventory: dict[str, Any], domain: str) -> list[str]:
    features = inventory.get("features")
    if isinstance(features, list):
        identifiers = [item.get("feature_id") for item in features if isinstance(item, dict)]
        if len(identifiers) != len(features) or any(not isinstance(item, str) for item in identifiers):
            fail(f"authoritative inventory contains an invalid feature entry for domain {domain}")
        return identifiers
    if isinstance(features, dict):
        identifiers = list(features)
        if any(not isinstance(item, str) for item in identifiers) or any(
            not isinstance(value, dict) for value in features.values()
        ):
            fail(f"authoritative inventory contains an invalid feature mapping for domain {domain}")
        return identifiers
    fail(f"authoritative inventory has no feature list or mapping for domain {domain}")


def inventory_declared_counts(inventory: dict[str, Any]) -> list[Any]:
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
    manifest_path = ROOT / "registry" / "domain-finalization" / domain / "manifest.yaml"
    if not manifest_path.is_file():
        return []
    manifest = load_yaml(manifest_path)
    if not isinstance(manifest, dict):
        fail(f"domain finalization manifest is not an object for domain {domain}")
    population = manifest.get("population")
    if population is not None:
        if not isinstance(population, list) or any(not isinstance(item, str) for item in population):
            fail(f"domain finalization manifest has an invalid population for domain {domain}")
        if population != authoritative_ids:
            fail(f"domain finalization manifest population differs from authoritative inventory for {domain}")
    counts: list[Any] = []
    for path in MANIFEST_COUNT_PATHS:
        present, value = nested_value(manifest, path)
        if present:
            counts.append(value)
    return counts


def validate_declared_counts(domain: str, values: list[Any], actual_count: int) -> None:
    if not values or any(
        isinstance(value, bool) or not isinstance(value, int) or value != actual_count for value in values
    ):
        fail(f"authoritative inventory feature count mismatch for domain {domain}")


def validate_authoritative_inventory(domain: str, catalog: dict[str, Any]) -> None:
    inventory_value = catalog["metadata"]["authoritative_inventory"]
    expected_value = f"registry/domain-finalization/{domain}/feature-status.yaml"
    if inventory_value != expected_value:
        fail(f"domain {domain} must use authoritative inventory {expected_value}")
    if not safe_repo_path(inventory_value):
        fail(f"unsafe authoritative inventory path for domain {domain}: {inventory_value}")
    inventory = load_yaml(ROOT / inventory_value)
    if not isinstance(inventory, dict):
        fail(f"authoritative inventory is not an object for domain {domain}")
    declared_domains = [inventory[key] for key in ("domain", "domain_id") if key in inventory]
    if not declared_domains or any(value != domain for value in declared_domains):
        fail(f"authoritative inventory domain mismatch for {domain}")
    authoritative_ids = authoritative_feature_ids(inventory, domain)
    declared_counts = inventory_declared_counts(inventory)
    if not declared_counts:
        declared_counts = manifest_fallback_counts(domain, authoritative_ids)
    validate_declared_counts(domain, declared_counts, len(authoritative_ids))
    if catalog["ordered_feature_ids"] != authoritative_ids:
        fail(f"domain catalog population or order differs from authoritative inventory for {domain}")
    for feature_id in authoritative_ids:
        for artifact in (
            ROOT / "registry" / "optimized-ir" / domain / feature_id / "ir.yaml",
            ROOT / "registry" / "algorithms" / domain / feature_id / "algorithm.yaml",
            ROOT / "registry" / "oracles" / domain / feature_id / "oracle.yaml",
        ):
            if not artifact.is_file():
                fail(f"authoritative feature artifact is missing: {artifact.relative_to(ROOT)}")


def discover_domain_catalogs(
    schema: dict[str, Any], shared_versions: dict[str, str]
) -> tuple[dict[str, dict[str, Any]], dict[str, str], dict[str, dict[str, Any]]]:
    domains_root = HANDOFF / "domains"
    if not domains_root.is_dir():
        fail("handoff/domains must be a directory")
    non_directories = sorted(path.name for path in domains_root.iterdir() if not path.is_dir())
    if non_directories:
        fail(f"handoff/domains contains non-directory entries: {non_directories}")
    actual_domains = {path.name for path in domains_root.iterdir() if path.is_dir()}
    if actual_domains != set(DOMAIN_ORDER):
        fail(f"domain catalog population mismatch: expected {list(DOMAIN_ORDER)}, found {sorted(actual_domains)}")

    catalogs: dict[str, dict[str, Any]] = {}
    owners: dict[str, str] = {}
    package_entries: dict[str, dict[str, Any]] = {}
    for expected_index, domain in enumerate(DOMAIN_ORDER):
        catalog_path = domains_root / domain / "catalog.json"
        catalog = load_json(catalog_path)
        validate_schema(catalog, schema, catalog_path)
        if catalog["domain"] != domain or catalog["domain_index"] != expected_index:
            fail(f"domain catalog identity or index mismatch in {catalog_path.relative_to(ROOT)}")
        if catalog["statuses"] != {"population": "complete", "validation": "validated"}:
            fail(f"domain catalog is not globally validated: {domain}")
        ordered_ids = catalog["ordered_feature_ids"]
        entries = catalog["feature_packages"]
        if catalog["expected_feature_count"] != len(ordered_ids) or len(entries) != len(ordered_ids):
            fail(f"domain catalog count mismatch for {domain}")
        if [entry["feature_id"] for entry in entries] != ordered_ids:
            fail(f"feature_packages must match ordered_feature_ids exactly and in order for domain {domain}")
        for feature_id, entry in zip(ordered_ids, entries, strict=True):
            domain_index, identifier_domain = feature_identity(feature_id)
            if domain_index != expected_index or identifier_domain != domain:
                fail(f"feature {feature_id} is placed in the wrong domain catalog {domain}")
            expected_path = f"handoff/features/{feature_id}"
            if entry["path"] != expected_path:
                fail(f"feature package path mismatch for {feature_id}: expected {expected_path}")
            register_feature_owner(owners, feature_id, domain)
            package_entries[feature_id] = entry
        catalog_dependencies = {
            (item["shared_contract_id"], item["version"]) for item in catalog["shared_dependencies"]
        }
        for dependency_id, version in catalog_dependencies:
            if shared_versions.get(dependency_id) != version:
                fail(f"unresolved or incompatible domain dependency {dependency_id}@{version} for {domain}")
        validate_authoritative_inventory(domain, catalog)
        catalogs[domain] = catalog
    if len(owners) != 166:
        fail(f"authoritative domain union must contain 166 feature identities, found {len(owners)}")
    return catalogs, owners, package_entries


def validate_global_catalog(schema: dict[str, Any]) -> dict[str, Any]:
    catalog_path = HANDOFF / "catalog.json"
    catalog = load_json(catalog_path)
    validate_schema(catalog, schema, catalog_path)
    if catalog["validator"] != {
        "entrypoint": "tools/handoff/validate_handoff.py",
        "version": VALIDATOR_VERSION,
    }:
        fail("global catalog validator identity is not canonical")
    try:
        from generate_catalog import CatalogGenerationFailure, build_catalog

        generated = build_catalog()
    except (ImportError, CatalogGenerationFailure) as exc:
        fail(f"cannot reconstruct deterministic global catalog: {exc}")
    if catalog != generated:
        fail("handoff/catalog.json differs from the deterministic projection of finalized handoff artifacts")
    return catalog


def validate_population(actual_feature_ids: set[str], declared_owners: dict[str, str]) -> None:
    expected_feature_ids = set(declared_owners)
    missing = sorted(expected_feature_ids - actual_feature_ids)
    orphaned = sorted(actual_feature_ids - expected_feature_ids)
    if missing or orphaned:
        parts: list[str] = []
        if missing:
            parts.append(f"missing declared packages: {missing}")
        if orphaned:
            parts.append(f"orphan packages without a domain catalog: {orphaned}")
        fail("final feature population mismatch: " + "; ".join(parts))


def main() -> int:
    if not HANDOFF.is_dir():
        fail("handoff directory is missing")
    schema_names = {
        "manifest": "manifest.schema.json",
        "contract": "contract.schema.json",
        "acceptance": "acceptance.schema.json",
        "examples": "examples.schema.json",
        "traceability": "traceability.schema.json",
        "shared_contract": "shared-contract.schema.json",
        "domain_catalog": "domain-catalog.schema.json",
        "global_catalog": "global-catalog.schema.json",
    }
    schemas = {name: load_json(SCHEMAS / filename) for name, filename in schema_names.items()}
    for name, schema in schemas.items():
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            fail(f"invalid {name} schema: {exc}")
    for path in sorted(HANDOFF.rglob("*.json")):
        load_json(path)

    shared_root = HANDOFF / "shared"
    if not shared_root.is_dir():
        fail("handoff/shared directory is missing")
    shared_dirs = sorted(path for path in shared_root.iterdir() if path.is_dir())
    shared_ids = {path.name for path in shared_dirs}
    if shared_ids != EXPECTED_SHARED:
        fail(f"shared contract population mismatch: expected {sorted(EXPECTED_SHARED)}, found {sorted(shared_ids)}")
    if any(not path.is_dir() for path in shared_root.iterdir()):
        fail("handoff/shared contains non-directory entries")

    shared_versions: dict[str, str] = {}
    global_test_ids: set[str] = set()
    for package_dir in shared_dirs:
        manifest = load_json(package_dir / "manifest.json")
        contract = load_json(package_dir / "contract.json")
        acceptance = load_json(package_dir / "acceptance.json")
        trace = load_json(package_dir / "traceability.json")
        validate_schema(manifest, schemas["manifest"], package_dir / "manifest.json")
        validate_schema(contract, schemas["shared_contract"], package_dir / "contract.json")
        validate_schema(acceptance, schemas["acceptance"], package_dir / "acceptance.json")
        validate_schema(trace, schemas["traceability"], package_dir / "traceability.json")
        package_id = package_dir.name
        if not (
            manifest["shared_contract_id"] == package_id
            and contract["shared_contract"]["shared_contract_id"] == package_id
            and acceptance["applies_to"] == package_id
            and trace["applies_to"] == package_id
        ):
            fail(f"shared_contract_id mismatch in {package_dir.relative_to(ROOT)}")
        versions = {
            manifest["package_version"],
            contract["package_version"],
            acceptance["package_version"],
            trace["package_version"],
        }
        if len(versions) != 1:
            fail(f"package version mismatch in {package_dir.relative_to(ROOT)}")
        shared_versions[package_id] = manifest["package_version"]
        package_files(package_dir, manifest)
        validate_trace_paths(trace, package_dir / "traceability.json", require_nonempty=False)
        validate_acceptance_ids(acceptance, global_test_ids, package_dir / "acceptance.json")
        validate_no_normative_language_code(package_dir)

    for package_dir in shared_dirs:
        manifest = load_json(package_dir / "manifest.json")
        for dependency in manifest["shared_dependencies"]:
            dependency_id = dependency["shared_contract_id"]
            if dependency_id not in shared_versions or dependency["version"] != shared_versions[dependency_id]:
                fail(f"unresolved or incompatible shared dependency {dependency_id} in {package_dir.relative_to(ROOT)}")

    catalogs, declared_owners, catalog_entries = discover_domain_catalogs(
        schemas["domain_catalog"], shared_versions
    )
    features_root = HANDOFF / "features"
    if not features_root.is_dir():
        fail("handoff/features directory is missing")
    if any(not path.is_dir() for path in features_root.iterdir()):
        fail("handoff/features contains non-directory entries")
    feature_dirs = sorted(path for path in features_root.iterdir() if path.is_dir())
    actual_feature_ids = {path.name for path in feature_dirs}
    validate_population(actual_feature_ids, declared_owners)
    if len(feature_dirs) != 166:
        fail(f"expected exactly 166 feature package directories, found {len(feature_dirs)}")

    domain_dependency_unions: dict[str, set[tuple[str, str]]] = {domain: set() for domain in catalogs}
    package_statuses: Counter[str] = Counter()
    scientific_statuses: Counter[str] = Counter()
    execution_statuses: Counter[str] = Counter()
    examples_present = 0
    pilot_validated = False
    for package_dir in feature_dirs:
        manifest = load_json(package_dir / "manifest.json")
        contract = load_json(package_dir / "contract.json")
        acceptance = load_json(package_dir / "acceptance.json")
        trace = load_json(package_dir / "traceability.json")
        examples = load_json(package_dir / "examples.json") if (package_dir / "examples.json").exists() else None
        validate_schema(manifest, schemas["manifest"], package_dir / "manifest.json")
        validate_schema(contract, schemas["contract"], package_dir / "contract.json")
        validate_schema(acceptance, schemas["acceptance"], package_dir / "acceptance.json")
        validate_schema(trace, schemas["traceability"], package_dir / "traceability.json")
        if examples is not None:
            validate_schema(examples, schemas["examples"], package_dir / "examples.json")

        feature_id = package_dir.name
        if not (
            manifest["feature_id"] == feature_id
            and contract["feature"]["feature_id"] == feature_id
            and acceptance["applies_to"] == feature_id
            and trace["applies_to"] == feature_id
            and (examples is None or examples["applies_to"] == feature_id)
        ):
            fail(f"feature_id mismatch in {package_dir.relative_to(ROOT)}")
        versions = {
            manifest["package_version"],
            contract["package_version"],
            acceptance["package_version"],
            trace["package_version"],
        }
        if examples is not None:
            versions.add(examples["package_version"])
        if len(versions) != 1:
            fail(f"package version mismatch in {package_dir.relative_to(ROOT)}")

        owner = declared_owners[feature_id]
        if manifest["domain"] != owner or contract["feature"]["domain"] != owner:
            fail(f"feature {feature_id} package domain does not match {owner}")
        catalog_entry = catalog_entries[feature_id]
        if catalog_entry["package_version"] != manifest["package_version"]:
            fail(f"domain catalog package version mismatch for {feature_id}")
        if catalog_entry["status"] != manifest["statuses"]["package"]:
            fail(f"domain catalog package status mismatch for {feature_id}")

        package_files(package_dir, manifest)
        validate_feature_readme(package_dir, feature_id)
        validate_trace_paths(trace, package_dir / "traceability.json", require_nonempty=True)
        validate_acceptance_ids(acceptance, global_test_ids, package_dir / "acceptance.json")
        validate_error_uniqueness(contract, package_dir / "contract.json")
        validate_strategy(contract, trace, package_dir / "contract.json")
        validate_no_normative_language_code(package_dir)
        manifest_dependencies = {
            (item["shared_contract_id"], item["version"]) for item in manifest["shared_dependencies"]
        }
        contract_dependencies = {
            (item["shared_contract_id"], item["version"]) for item in contract["dependencies"]
        }
        if manifest_dependencies != contract_dependencies:
            fail(f"manifest and contract dependencies differ in {package_dir.relative_to(ROOT)}")
        for dependency_id, version in manifest_dependencies:
            if shared_versions.get(dependency_id) != version:
                fail(f"unresolved or incompatible dependency {dependency_id}@{version} in {package_dir.relative_to(ROOT)}")
        domain_dependency_unions[owner].update(manifest_dependencies)

        statuses = manifest["statuses"]
        package_statuses[statuses["package"]] += 1
        scientific_statuses[statuses["scientific"]] += 1
        execution_statuses[statuses["execution"]] += 1
        examples_present += int(examples is not None)
        if feature_id == PILOT_ID:
            validate_pilot(contract, acceptance, manifest)
            pilot_validated = True

    if not pilot_validated:
        fail("foundation pilot was not validated")
    for domain, catalog in catalogs.items():
        catalog_dependencies = {
            (item["shared_contract_id"], item["version"]) for item in catalog["shared_dependencies"]
        }
        if catalog_dependencies != domain_dependency_unions[domain]:
            fail(f"domain catalog shared dependencies do not exactly match package dependencies for {domain}")

    global_catalog = validate_global_catalog(schemas["global_catalog"])
    expected_summary = {
        "domain_count": 16,
        "feature_count": 166,
        "shared_contract_count": 8,
        "package_statuses": dict(sorted(package_statuses.items())),
        "scientific_statuses": dict(sorted(scientific_statuses.items())),
        "execution_statuses": dict(sorted(execution_statuses.items())),
        "examples_present": examples_present,
        "examples_absent": 166 - examples_present,
        "promoted_shared_contract_candidates": 0,
    }
    if global_catalog["summary"] != expected_summary:
        fail("global catalog status or examples summary differs from validated package manifests")

    print("Feature Handoff Package v1.0 finalized validation passed.")
    print("Validated 8 shared contracts, 166 feature packages, and 16 complete domain catalogs.")
    print(
        json.dumps(
            {
                "package_statuses": dict(sorted(package_statuses.items())),
                "scientific_statuses": dict(sorted(scientific_statuses.items())),
                "execution_statuses": dict(sorted(execution_statuses.items())),
                "examples_present": examples_present,
                "examples_absent": 166 - examples_present,
            },
            sort_keys=True,
        )
    )
    return 0


def expect_failure(action: Callable[[], None], scenario: str) -> None:
    try:
        action()
    except ValidationFailure:
        return
    fail(f"logical self-test {scenario} did not reject invalid input")


def run_self_tests() -> int:
    master_ids = {f"TLC-FC-00-MASTER-{index:03d}" for index in range(1, 17)}
    disciple_ids = {f"TLC-FC-01-DISCIPLE-{index:03d}" for index in range(1, 11)}
    master_owners = {feature_id: "master" for feature_id in master_ids}
    two_domain_owners = {**master_owners, **{feature_id: "disciple" for feature_id in disciple_ids}}

    validate_population(master_ids, master_owners)  # A: complete Master fixture
    expect_failure(
        lambda: validate_population(set(sorted(master_ids)[:-1]), master_owners),
        "B incomplete catalog",
    )
    expect_failure(
        lambda: validate_population(master_ids | {"TLC-FC-01-DISCIPLE-001"}, master_owners),
        "C orphan package",
    )
    validate_population(master_ids | disciple_ids, two_domain_owners)  # D: complete two-domain fixture

    collision_owners: dict[str, str] = {}
    register_feature_owner(collision_owners, PILOT_ID, "master")
    expect_failure(lambda: register_feature_owner(collision_owners, PILOT_ID, "disciple"), "E collision")

    pilot_dir = HANDOFF / "features" / PILOT_ID
    pilot_contract = load_json(pilot_dir / "contract.json")
    pilot_acceptance = load_json(pilot_dir / "acceptance.json")
    pilot_manifest = load_json(pilot_dir / "manifest.json")
    validate_pilot(pilot_contract, pilot_acceptance, pilot_manifest)
    altered_contract = copy.deepcopy(pilot_contract)
    altered_contract["operations"][0]["strategy_contract"]["mode"] = "open"
    expect_failure(
        lambda: validate_pilot(altered_contract, pilot_acceptance, pilot_manifest),
        "F altered pilot",
    )

    list_inventory = {"features": [{"feature_id": "A"}, {"feature_id": "B"}]}
    mapping_inventory = {"features": {"A": {}, "B": {}}}
    if authoritative_feature_ids(list_inventory, "test-list") != ["A", "B"]:
        fail("logical self-test G failed for list-form features")
    if authoritative_feature_ids(mapping_inventory, "test-mapping") != ["A", "B"]:
        fail("logical self-test H failed for mapping-form features")
    validate_declared_counts("test-counts", [2, 2], 2)
    expect_failure(
        lambda: validate_declared_counts("test-conflict", [2, 3], 2),
        "I conflicting historical count aliases",
    )
    expect_failure(
        lambda: validate_declared_counts("test-missing", [], 2),
        "J missing count evidence",
    )
    if feature_identity("TLC-FC-03-HUIT-DIMENSIONS-DE-TL-001") != (3, "huit-dimensions"):
        fail("logical self-test K failed for reversible historical domain slug normalization")

    print("Finalized validation logical self-tests A-K passed.")
    return 0


def entrypoint() -> int:
    arguments = sys.argv[1:]
    if not arguments:
        return main()
    if arguments == ["--self-test"]:
        return run_self_tests()
    fail(f"unsupported arguments: {arguments}")


if __name__ == "__main__":
    try:
        raise SystemExit(entrypoint())
    except ValidationFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
