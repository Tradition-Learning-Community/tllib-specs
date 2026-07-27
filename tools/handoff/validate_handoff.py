#!/usr/bin/env python3
"""Validate the Feature Handoff Package v1.0 foundation."""

from __future__ import annotations

import json
import re
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

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
            dep_id = dependency["shared_contract_id"]
            if dep_id not in shared_versions:
                fail(f"unresolved shared dependency {dep_id} in {package_dir.relative_to(ROOT)}")
            if dependency["version"] != shared_versions[dep_id]:
                fail(f"incompatible shared dependency {dep_id} in {package_dir.relative_to(ROOT)}")

    feature_dirs = sorted(path for path in (HANDOFF / "features").iterdir() if path.is_dir())
    if {path.name for path in feature_dirs} != {PILOT_ID}:
        fail("v1.0 foundation must contain only the declared pilot feature")

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
        package_files(package_dir, manifest)
        validate_trace_paths(trace, package_dir / "traceability.json", require_nonempty=True)
        validate_acceptance_ids(acceptance, global_test_ids, package_dir / "acceptance.json")
        validate_error_uniqueness(contract, package_dir / "contract.json")
        validate_strategy(contract, trace, package_dir / "contract.json")
        validate_no_normative_language_code(package_dir)
        manifest_deps = {(item["shared_contract_id"], item["version"]) for item in manifest["shared_dependencies"]}
        contract_deps = {(item["shared_contract_id"], item["version"]) for item in contract["dependencies"]}
        if manifest_deps != contract_deps:
            fail(f"manifest and contract dependencies differ in {package_dir.relative_to(ROOT)}")
        for dep_id, version in manifest_deps:
            if shared_versions.get(dep_id) != version:
                fail(f"unresolved or incompatible dependency {dep_id}@{version} in {package_dir.relative_to(ROOT)}")
        validate_pilot(contract, acceptance, manifest)

    catalog = load_json(HANDOFF / "catalog.json")
    if catalog.get("model_version") != "1.0.0" or catalog.get("complete_166_feature_catalog_finalized") is not False:
        fail("catalog foundation status is incorrect")
    if {entry["shared_contract_id"] for entry in catalog["shared_contracts"]} != EXPECTED_SHARED:
        fail("catalog shared contract population mismatch")
    if {entry["feature_id"] for entry in catalog["features"]} != {PILOT_ID}:
        fail("catalog pilot population mismatch")
    for entry in catalog["shared_contracts"] + catalog["features"]:
        if not safe_repo_path(entry["path"]) or not (ROOT / entry["path"]).is_dir():
            fail(f"catalog path does not resolve: {entry['path']}")

    print("Feature Handoff Package v1.0 validation passed.")
    print(f"Validated {len(shared_dirs)} shared contracts and {len(feature_dirs)} feature package.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
