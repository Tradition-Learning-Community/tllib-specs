#!/usr/bin/env python3
"""Validate progressive Feature Handoff Package v1.0 populations."""

from __future__ import annotations

import copy
import json
import re
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterable

from jsonschema import Draft202012Validator
from yaml import YAMLError, safe_load

ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "handoff"
SCHEMAS = HANDOFF / "schemas"
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
PILOT_ID = "TLC-FC-00-MASTER-005"
FEATURE_ID_PATTERN = re.compile(r"^TLC-FC-(?P<index>[0-9]{2})-(?P<domain>[A-Z][A-Z0-9-]*)-[0-9]{3}$")
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


class ValidationFailure(RuntimeError):
    pass


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


def package_files(package_dir: Path, manifest: dict[str, Any]) -> None:
    required = {"README.md", "manifest.json", "contract.json", "acceptance.json", "traceability.json"}
    declared = set(manifest["files"])
    if not required.issubset(declared):
        fail(f"{package_dir.relative_to(ROOT)} does not declare every required file")
    for filename in declared:
        if not (package_dir / filename).is_file():
            fail(f"declared file is missing: {(package_dir / filename).relative_to(ROOT)}")
    examples = manifest["examples"]
    exists = (package_dir / "examples.json").exists()
    if examples["present"] != exists:
        fail(f"examples declaration mismatch in {package_dir.relative_to(ROOT)}")
    if exists and "examples.json" not in declared:
        fail(f"examples.json exists but is not declared in {package_dir.relative_to(ROOT)}")


def validate_trace_paths(trace: dict[str, Any], path: Path, require_nonempty: bool) -> None:
    for category in REQUIRED_TRACE_CATEGORIES:
        if category not in trace:
            fail(f"missing traceability category {category} in {path.relative_to(ROOT)}")
        refs = trace[category]
        if require_nonempty and not refs:
            fail(f"{category} must be non-empty in {path.relative_to(ROOT)}")
        for ref in refs:
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
    for operation in contract.get("operations", []):
        strategy = operation["strategy_contract"]
        steps = set(strategy["steps"])
        for edge in strategy["partial_order"]:
            if edge["before"] not in steps or edge["after"] not in steps:
                fail(f"partial-order edge references an unknown step in {path.relative_to(ROOT)}")
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
    local: set[str] = set()
    for test in acceptance["tests"]:
        test_id = test["test_id"]
        if test_id in local or test_id in global_ids:
            fail(f"duplicate test_id {test_id} in {path.relative_to(ROOT)}")
        local.add(test_id)
        global_ids.add(test_id)


def validate_pilot(contract: dict[str, Any], acceptance: dict[str, Any], manifest: dict[str, Any]) -> None:
    if contract["feature"]["feature_id"] != PILOT_ID:
        fail("pilot contract feature_id mismatch")
    if manifest["statuses"] != {"package": "pilot", "scientific": "partially_defined", "execution": "structural_only"}:
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
    strategy = contract["operations"][0]["strategy_contract"]
    if strategy["mode"] != "partially_constrained":
        fail("pilot must preserve internal strategy freedom with a partially constrained strategy")
    test_ids = {test["test_id"] for test in acceptance["tests"]}
    if not {f"MASTER-005-A{i:02d}" for i in range(1, 9)}.issubset(test_ids):
        fail("pilot does not preserve all eight oracle acceptance identifiers")


def feature_identity(feature_id: str) -> tuple[int, str]:
    match = FEATURE_ID_PATTERN.fullmatch(feature_id)
    if match is None:
        fail(f"invalid feature identifier: {feature_id}")
    return int(match.group("index")), match.group("domain").lower()


def register_feature_owner(owners: dict[str, str], feature_id: str, domain: str) -> None:
    previous = owners.get(feature_id)
    if previous is not None:
        fail(f"feature {feature_id} is declared by both {previous} and {domain}")
    owners[feature_id] = domain


def validate_progressive_population(actual_feature_ids: set[str], declared_owners: dict[str, str]) -> None:
    expected_feature_ids = set(declared_owners) | {PILOT_ID}
    missing = sorted(expected_feature_ids - actual_feature_ids)
    orphaned = sorted(actual_feature_ids - expected_feature_ids)
    if missing or orphaned:
        parts: list[str] = []
        if missing:
            parts.append(f"missing declared packages: {missing}")
        if orphaned:
            parts.append(f"orphan packages without a domain catalog: {orphaned}")
        fail("progressive feature population mismatch: " + "; ".join(parts))


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
    if inventory.get("domain") != domain:
        fail(f"authoritative inventory domain mismatch for {domain}")
    authoritative_features = inventory.get("features")
    if not isinstance(authoritative_features, list):
        fail(f"authoritative inventory has no feature list for domain {domain}")
    authoritative_ids = [item.get("feature_id") for item in authoritative_features if isinstance(item, dict)]
    if len(authoritative_ids) != len(authoritative_features) or any(not isinstance(item, str) for item in authoritative_ids):
        fail(f"authoritative inventory contains an invalid feature entry for domain {domain}")
    if inventory.get("feature_count") != len(authoritative_ids):
        fail(f"authoritative inventory feature count mismatch for domain {domain}")
    if catalog["ordered_feature_ids"] != authoritative_ids:
        fail(f"domain catalog population or order differs from authoritative inventory for {domain}")

    for feature_id in authoritative_ids:
        required_artifacts = (
            ROOT / "registry" / "optimized-ir" / domain / feature_id / "ir.yaml",
            ROOT / "registry" / "algorithms" / domain / feature_id / "algorithm.yaml",
            ROOT / "registry" / "oracles" / domain / feature_id / "oracle.yaml",
        )
        for artifact in required_artifacts:
            if not artifact.is_file():
                fail(f"authoritative feature artifact is missing: {artifact.relative_to(ROOT)}")


def discover_domain_catalogs(
    schema: dict[str, Any], shared_versions: dict[str, str]
) -> tuple[dict[str, dict[str, Any]], dict[str, str], dict[str, dict[str, Any]]]:
    domains_root = HANDOFF / "domains"
    if not domains_root.exists():
        return {}, {}, {}
    if not domains_root.is_dir():
        fail("handoff/domains must be a directory when present")

    non_directories = sorted(path.name for path in domains_root.iterdir() if not path.is_dir())
    if non_directories:
        fail(f"handoff/domains contains non-directory entries: {non_directories}")

    catalogs: dict[str, dict[str, Any]] = {}
    owners: dict[str, str] = {}
    package_entries: dict[str, dict[str, Any]] = {}
    for domain_dir in sorted(path for path in domains_root.iterdir() if path.is_dir()):
        catalog_path = domain_dir / "catalog.json"
        if not catalog_path.is_file():
            fail(f"domain directory lacks catalog.json: {domain_dir.relative_to(ROOT)}")
        catalog = load_json(catalog_path)
        validate_schema(catalog, schema, catalog_path)
        domain = domain_dir.name
        if catalog["domain"] != domain:
            fail(f"domain catalog identity mismatch in {catalog_path.relative_to(ROOT)}")

        ordered_ids = catalog["ordered_feature_ids"]
        entries = catalog["feature_packages"]
        if catalog["expected_feature_count"] != len(ordered_ids):
            fail(f"expected_feature_count does not match ordered_feature_ids for domain {domain}")
        if len(entries) != len(ordered_ids):
            fail(f"feature_packages count does not match ordered_feature_ids for domain {domain}")
        if [entry["feature_id"] for entry in entries] != ordered_ids:
            fail(f"feature_packages must match ordered_feature_ids exactly and in order for domain {domain}")

        for feature_id, entry in zip(ordered_ids, entries, strict=True):
            domain_index, identifier_domain = feature_identity(feature_id)
            if domain_index != catalog["domain_index"]:
                fail(f"feature {feature_id} has the wrong domain index for catalog {domain}")
            if identifier_domain != domain:
                fail(f"feature {feature_id} is declared in the wrong domain catalog {domain}")
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

    return catalogs, owners, package_entries


def validate_global_foundation_catalog() -> None:
    catalog = load_json(HANDOFF / "catalog.json")
    if catalog.get("model_version") != "1.0.0" or catalog.get("complete_166_feature_catalog_finalized") is not False:
        fail("catalog foundation status is incorrect")
    if {entry["shared_contract_id"] for entry in catalog["shared_contracts"]} != EXPECTED_SHARED:
        fail("catalog shared contract population mismatch")
    feature_ids = [entry["feature_id"] for entry in catalog["features"]]
    if len(feature_ids) != len(set(feature_ids)):
        fail("catalog contains duplicate feature entries")
    if PILOT_ID not in feature_ids:
        fail("catalog does not preserve the foundation pilot")
    for entry in catalog["shared_contracts"] + catalog["features"]:
        if not safe_repo_path(entry["path"]) or not (ROOT / entry["path"]).is_dir():
            fail(f"catalog path does not resolve: {entry['path']}")


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
    }
    schemas = {name: load_json(SCHEMAS / filename) for name, filename in schema_names.items()}
    for name, schema in schemas.items():
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # jsonschema exposes several schema exception types
            fail(f"invalid {name} schema: {exc}")

    for path in sorted(HANDOFF.rglob("*.json")):
        load_json(path)

    shared_dirs = sorted(path for path in (HANDOFF / "shared").iterdir() if path.is_dir())
    shared_ids = {path.name for path in shared_dirs}
    if shared_ids != EXPECTED_SHARED:
        fail(f"shared contract population mismatch: expected {sorted(EXPECTED_SHARED)}, found {sorted(shared_ids)}")

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
        if manifest["shared_contract_id"] != package_id or contract["shared_contract"]["shared_contract_id"] != package_id or acceptance["applies_to"] != package_id or trace["applies_to"] != package_id:
            fail(f"shared_contract_id mismatch in {package_dir.relative_to(ROOT)}")
        if manifest["package_version"] != contract["package_version"] or manifest["package_version"] != acceptance["package_version"] or manifest["package_version"] != trace["package_version"]:
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
            if dependency_id not in shared_versions:
                fail(f"unresolved shared dependency {dependency_id} in {package_dir.relative_to(ROOT)}")
            if dependency["version"] != shared_versions[dependency_id]:
                fail(f"incompatible shared dependency {dependency_id} in {package_dir.relative_to(ROOT)}")

    catalogs, declared_owners, catalog_package_entries = discover_domain_catalogs(
        schemas["domain_catalog"], shared_versions
    )

    features_root = HANDOFF / "features"
    if not features_root.is_dir():
        fail("handoff/features directory is missing")
    non_feature_entries = sorted(path.name for path in features_root.iterdir() if not path.is_dir())
    if non_feature_entries:
        fail(f"handoff/features contains non-directory entries: {non_feature_entries}")
    feature_dirs = sorted(path for path in features_root.iterdir() if path.is_dir())
    actual_feature_ids = {path.name for path in feature_dirs}
    validate_progressive_population(actual_feature_ids, declared_owners)

    domain_dependency_unions: dict[str, set[tuple[str, str]]] = {domain: set() for domain in catalogs}
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
        if manifest["feature_id"] != feature_id or contract["feature"]["feature_id"] != feature_id or acceptance["applies_to"] != feature_id or trace["applies_to"] != feature_id or (examples and examples["applies_to"] != feature_id):
            fail(f"feature_id mismatch in {package_dir.relative_to(ROOT)}")
        versions = {manifest["package_version"], contract["package_version"], acceptance["package_version"], trace["package_version"]}
        if examples:
            versions.add(examples["package_version"])
        if len(versions) != 1:
            fail(f"package version mismatch in {package_dir.relative_to(ROOT)}")

        owner = declared_owners.get(feature_id)
        expected_domain = owner if owner is not None else "master"
        if manifest["domain"] != expected_domain or contract["feature"]["domain"] != expected_domain:
            fail(f"feature {feature_id} package domain does not match {expected_domain}")
        if owner is not None:
            catalog_entry = catalog_package_entries[feature_id]
            if catalog_entry["package_version"] != manifest["package_version"]:
                fail(f"domain catalog package version mismatch for {feature_id}")
            if catalog_entry["status"] != manifest["statuses"]["package"]:
                fail(f"domain catalog package status mismatch for {feature_id}")

        package_files(package_dir, manifest)
        validate_trace_paths(trace, package_dir / "traceability.json", require_nonempty=True)
        validate_acceptance_ids(acceptance, global_test_ids, package_dir / "acceptance.json")
        validate_error_uniqueness(contract, package_dir / "contract.json")
        validate_strategy(contract, trace, package_dir / "contract.json")
        validate_no_normative_language_code(package_dir)
        manifest_dependencies = {(item["shared_contract_id"], item["version"]) for item in manifest["shared_dependencies"]}
        contract_dependencies = {(item["shared_contract_id"], item["version"]) for item in contract["dependencies"]}
        if manifest_dependencies != contract_dependencies:
            fail(f"manifest and contract dependencies differ in {package_dir.relative_to(ROOT)}")
        for dependency_id, version in manifest_dependencies:
            if shared_versions.get(dependency_id) != version:
                fail(f"unresolved or incompatible dependency {dependency_id}@{version} in {package_dir.relative_to(ROOT)}")
        if owner is not None:
            domain_dependency_unions[owner].update(manifest_dependencies)

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

    validate_global_foundation_catalog()

    print("Feature Handoff Package v1.0 progressive validation passed.")
    print(
        f"Validated {len(shared_dirs)} shared contracts, {len(feature_dirs)} feature packages, "
        f"and {len(catalogs)} complete domain catalogs."
    )
    return 0


def expect_failure(action: Callable[[], None], scenario: str) -> None:
    try:
        action()
    except ValidationFailure:
        return
    fail(f"logical self-test {scenario} did not reject invalid input")


def run_progressive_self_tests() -> int:
    master_ids = {f"TLC-FC-00-MASTER-{index:03d}" for index in range(1, 17)}
    disciple_ids = {f"TLC-FC-01-DISCIPLE-{index:03d}" for index in range(1, 11)}
    master_owners = {feature_id: "master" for feature_id in master_ids}
    two_domain_owners = {**master_owners, **{feature_id: "disciple" for feature_id in disciple_ids}}

    validate_progressive_population({PILOT_ID}, {})  # A: foundation only
    validate_progressive_population(master_ids, master_owners)  # B: complete Master
    expect_failure(
        lambda: validate_progressive_population(set(sorted(master_ids)[:-1]), master_owners),
        "C incomplete Master catalog",
    )
    expect_failure(
        lambda: validate_progressive_population({PILOT_ID, "TLC-FC-01-DISCIPLE-001"}, {}),
        "D orphan package",
    )
    validate_progressive_population(master_ids, master_owners)  # E: progressive Master only
    validate_progressive_population(master_ids | disciple_ids, two_domain_owners)  # F: two domains

    collision_owners: dict[str, str] = {}
    register_feature_owner(collision_owners, PILOT_ID, "master")
    expect_failure(lambda: register_feature_owner(collision_owners, PILOT_ID, "disciple"), "G collision")

    pilot_dir = HANDOFF / "features" / PILOT_ID
    pilot_contract = load_json(pilot_dir / "contract.json")
    pilot_acceptance = load_json(pilot_dir / "acceptance.json")
    pilot_manifest = load_json(pilot_dir / "manifest.json")
    validate_pilot(pilot_contract, pilot_acceptance, pilot_manifest)
    altered_contract = copy.deepcopy(pilot_contract)
    altered_contract["operations"][0]["strategy_contract"]["mode"] = "open"
    expect_failure(
        lambda: validate_pilot(altered_contract, pilot_acceptance, pilot_manifest),
        "H altered pilot",
    )

    print("Progressive validation logical self-tests A-H passed.")
    return 0


def entrypoint() -> int:
    arguments = sys.argv[1:]
    if not arguments:
        return main()
    if arguments == ["--self-test"]:
        return run_progressive_self_tests()
    fail(f"unsupported arguments: {arguments}")


if __name__ == "__main__":
    try:
        raise SystemExit(entrypoint())
    except ValidationFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
