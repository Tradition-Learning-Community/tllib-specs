#!/usr/bin/env python3
"""Classify compatibility between two published catalog revisions.

The validator is structural. It requires explicit version decisions for changed
versioned surfaces and emits a machine-readable diff before any future runtime
consumer attempts scientific execution.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG = PurePosixPath("handoff/catalog.json")
POLICY = PurePosixPath("handoff/compatibility-policy.json")
SEMVER = re.compile(r"^([0-9]+)\.([0-9]+)\.([0-9]+)$")
SCHEMA_VERSION = re.compile(r"^([0-9]+)\.([0-9]+)$")


class CompatibilityFailure(RuntimeError):
    pass


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    if check and proc.returncode:
        raise CompatibilityFailure(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def read_text(path: PurePosixPath, ref: str | None) -> str:
    if ref is None:
        try:
            return ROOT.joinpath(*path.parts).read_text(encoding="utf-8")
        except OSError as exc:
            raise CompatibilityFailure(f"cannot read {path}: {exc}") from exc
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path.as_posix()}"], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if proc.returncode:
        raise CompatibilityFailure(f"cannot read {path} at {ref}: {proc.stderr.strip()}")
    return proc.stdout


def load_json(path: PurePosixPath, ref: str | None) -> dict[str, Any]:
    try:
        value = json.loads(read_text(path, ref))
    except json.JSONDecodeError as exc:
        raise CompatibilityFailure(f"invalid JSON at {ref or 'working tree'}:{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CompatibilityFailure(f"expected JSON object: {path}")
    return value


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def require_semver(value: Any, label: str) -> tuple[int, int, int]:
    if not isinstance(value, str):
        raise CompatibilityFailure(f"{label} must be a semantic version")
    match = SEMVER.fullmatch(value)
    if not match:
        raise CompatibilityFailure(f"{label} is not semantic versioning: {value!r}")
    return tuple(int(item) for item in match.groups())


def require_schema_version(value: Any, label: str) -> tuple[int, int]:
    if not isinstance(value, str):
        raise CompatibilityFailure(f"{label} must be a schema version")
    match = SCHEMA_VERSION.fullmatch(value)
    if not match:
        raise CompatibilityFailure(f"{label} is not major.minor: {value!r}")
    return tuple(int(item) for item in match.groups())


def version_delta(old: str, new: str) -> str:
    before = require_semver(old, "old version")
    after = require_semver(new, "new version")
    if after < before:
        raise CompatibilityFailure(f"version regressed from {old} to {new}")
    if after == before:
        return "same"
    if after[0] != before[0]:
        return "major"
    if after[1] != before[1]:
        return "minor"
    return "patch"


def schema_delta(old: str, new: str) -> str:
    before = require_schema_version(old, "old schema version")
    after = require_schema_version(new, "new schema version")
    if after < before:
        raise CompatibilityFailure(f"schema version regressed from {old} to {new}")
    if after == before:
        return "same"
    return "major" if after[0] != before[0] else "minor"


def ref_sha(ref: str | None) -> str:
    return git("rev-parse", ref or "HEAD")


def schema_paths(ref: str | None) -> list[PurePosixPath]:
    if ref is None:
        return [
            PurePosixPath(path.relative_to(ROOT).as_posix())
            for path in sorted((ROOT / "handoff" / "schemas").glob("*.schema.json"))
        ]
    output = git("ls-tree", "-r", "--name-only", ref, "handoff/schemas")
    return [PurePosixPath(line) for line in output.splitlines() if line.endswith(".schema.json")]


def schema_version(doc: dict[str, Any], path: PurePosixPath) -> str:
    properties = doc.get("properties")
    if not isinstance(properties, dict):
        raise CompatibilityFailure(f"schema has no properties: {path}")
    schema_property = properties.get("schema_version")
    if not isinstance(schema_property, dict) or not isinstance(schema_property.get("const"), str):
        raise CompatibilityFailure(f"schema lacks machine-readable schema_version const: {path}")
    value = schema_property["const"]
    require_schema_version(value, f"{path} schema version")
    return value


def read_versioned_tool(entry: Any, ref: str | None, label: str) -> dict[str, str]:
    if not isinstance(entry, dict):
        raise CompatibilityFailure(f"catalog {label} entry is invalid")
    path = entry.get("entrypoint")
    version = entry.get("version")
    if not isinstance(path, str):
        raise CompatibilityFailure(f"catalog {label} entrypoint is invalid")
    require_semver(version, f"catalog {label}.version")
    source = read_text(PurePosixPath(path), ref)
    return {"entrypoint": path, "version": version, "sha256": sha256_text(source)}


def snapshot(ref: str | None) -> dict[str, Any]:
    catalog = load_json(CATALOG, ref)
    require_semver(catalog.get("model_version"), "catalog model_version")
    require_schema_version(catalog.get("schema_version"), "catalog schema_version")

    generation = catalog.get("generation")
    if not isinstance(generation, dict):
        raise CompatibilityFailure("catalog generation entry is invalid")

    tools = {
        "validator": read_versioned_tool(catalog.get("validator"), ref, "validator"),
        "exporter": read_versioned_tool(catalog.get("exporter"), ref, "exporter"),
        "generator": read_versioned_tool(
            {"entrypoint": generation.get("entrypoint"), "version": generation.get("version")},
            ref,
            "generation",
        ),
    }

    domains_raw = catalog.get("domains")
    features_raw = catalog.get("features")
    shared_raw = catalog.get("shared_contracts")
    if not isinstance(domains_raw, list) or not isinstance(features_raw, list) or not isinstance(shared_raw, list):
        raise CompatibilityFailure("catalog population is invalid")

    features: dict[str, dict[str, Any]] = {}
    feature_versions_by_domain: dict[str, list[tuple[str, str]]] = {}
    for entry in features_raw:
        if not isinstance(entry, dict):
            raise CompatibilityFailure("catalog feature entry is invalid")
        feature_id = entry.get("feature_id")
        domain = entry.get("domain")
        package_version = entry.get("package_version")
        path = entry.get("path")
        if not all(isinstance(item, str) and item for item in (feature_id, domain, package_version, path)):
            raise CompatibilityFailure("catalog feature identity/version/path is invalid")
        require_semver(package_version, f"{feature_id} package version")
        manifest = load_json(PurePosixPath(path, "manifest.json"), ref)
        contract = load_json(PurePosixPath(path, "contract.json"), ref)
        if manifest.get("package_version") != package_version or contract.get("package_version") != package_version:
            raise CompatibilityFailure(f"feature version surfaces disagree: {feature_id}")
        features[feature_id] = {
            "domain": domain,
            "package_version": package_version,
            "package_sha256": entry.get("package_sha256"),
            "descriptor_sha256": entry.get("descriptor_sha256"),
            "statuses": entry.get("statuses"),
            "deprecation": entry.get("deprecation"),
            "substitution": entry.get("substitution"),
        }
        feature_versions_by_domain.setdefault(domain, []).append((feature_id, package_version))

    domains: dict[str, dict[str, Any]] = {}
    seen_indices: set[int] = set()
    for entry in domains_raw:
        if not isinstance(entry, dict):
            raise CompatibilityFailure("catalog domain entry is invalid")
        domain = entry.get("domain")
        path = entry.get("catalog_path")
        index = entry.get("domain_index")
        if not isinstance(domain, str) or not isinstance(path, str) or not isinstance(index, int):
            raise CompatibilityFailure("catalog domain identity is invalid")
        if index in seen_indices:
            raise CompatibilityFailure(f"duplicate domain index: {index}")
        seen_indices.add(index)
        doc = load_json(PurePosixPath(path), ref)
        require_schema_version(doc.get("schema_version"), f"{domain} domain schema_version")
        require_semver(doc.get("package_model_version"), f"{domain} package_model_version")
        domains[domain] = {
            "domain_index": index,
            "schema_version": doc.get("schema_version"),
            "package_model_version": doc.get("package_model_version"),
            "catalog_sha256": entry.get("catalog_sha256"),
            "feature_versions": sorted(feature_versions_by_domain.get(domain, [])),
        }

    shared: dict[str, dict[str, Any]] = {}
    for entry in shared_raw:
        if not isinstance(entry, dict):
            raise CompatibilityFailure("catalog shared contract entry is invalid")
        ident = entry.get("shared_contract_id")
        version = entry.get("version")
        path = entry.get("path")
        if not all(isinstance(item, str) and item for item in (ident, version, path)):
            raise CompatibilityFailure("shared contract identity/version/path is invalid")
        require_semver(version, f"{ident} version")
        manifest = load_json(PurePosixPath(path, "manifest.json"), ref)
        contract = load_json(PurePosixPath(path, "contract.json"), ref)
        if manifest.get("package_version") != version or contract.get("package_version") != version:
            raise CompatibilityFailure(f"shared contract version surfaces disagree: {ident}")
        shared[ident] = {
            "version": version,
            "package_sha256": entry.get("package_sha256"),
        }

    schemas: dict[str, dict[str, str]] = {}
    for path in schema_paths(ref):
        text = read_text(path, ref)
        try:
            doc = json.loads(text)
        except json.JSONDecodeError as exc:
            raise CompatibilityFailure(f"invalid schema JSON {path}: {exc}") from exc
        if not isinstance(doc, dict):
            raise CompatibilityFailure(f"schema is not an object: {path}")
        schemas[path.as_posix()] = {
            "version": schema_version(doc, path),
            "sha256": sha256_text(text),
        }

    return {
        "commit": ref_sha(ref),
        "model_version": catalog["model_version"],
        "catalog_schema_version": catalog["schema_version"],
        "tools": tools,
        "domains": domains,
        "features": features,
        "shared_contracts": shared,
        "schemas": schemas,
    }


def append_change(changes: list[dict[str, Any]], kind: str, identity: str, compatibility: str, **detail: Any) -> None:
    changes.append({"kind": kind, "identity": identity, "compatibility": compatibility, **detail})


def validate_policy_fields(feature_id: str, row: dict[str, Any], policy: dict[str, Any]) -> None:
    deprecation = row.get("deprecation")
    if deprecation is not None:
        if not isinstance(deprecation, dict):
            raise CompatibilityFailure(f"{feature_id} deprecation must be an object or null")
        required = policy.get("deprecation", {}).get("required_fields", [])
        for field in required:
            if not isinstance(deprecation.get(field), str) or not deprecation[field].strip():
                raise CompatibilityFailure(f"{feature_id} deprecation missing {field}")
    substitution = row.get("substitution")
    if substitution is not None:
        if not isinstance(substitution, dict):
            raise CompatibilityFailure(f"{feature_id} substitution must be an object or null")
        required = policy.get("substitution", {}).get("required_fields", [])
        for field in required:
            if not isinstance(substitution.get(field), str) or not substitution[field].strip():
                raise CompatibilityFailure(f"{feature_id} substitution missing {field}")


def compare(base: dict[str, Any], target: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    changes: list[dict[str, Any]] = []
    errors: list[str] = []

    if base["model_version"] != target["model_version"]:
        delta = version_delta(base["model_version"], target["model_version"])
        append_change(changes, "model_version", "model", "incompatible" if delta == "major" else "compatible", delta=delta)
    if base["catalog_schema_version"] != target["catalog_schema_version"]:
        delta = schema_delta(base["catalog_schema_version"], target["catalog_schema_version"])
        append_change(changes, "catalog_schema_version", "catalog", "incompatible" if delta == "major" else "compatible", delta=delta)

    for name, current in target["tools"].items():
        previous = base["tools"].get(name)
        if previous is None:
            append_change(changes, "tool_added", name, "compatible", version=current["version"])
            continue
        if previous["sha256"] != current["sha256"]:
            if previous["version"] == current["version"]:
                errors.append(f"{name} implementation changed without version change")
            else:
                delta = version_delta(previous["version"], current["version"])
                append_change(changes, "tool_changed", name, "incompatible" if delta == "major" else "compatible", delta=delta)

    base_schemas, target_schemas = base["schemas"], target["schemas"]
    for path in sorted(set(target_schemas) - set(base_schemas)):
        append_change(changes, "schema_added", path, "compatible", version=target_schemas[path]["version"])
    for path in sorted(set(base_schemas) - set(target_schemas)):
        append_change(changes, "schema_removed", path, "incompatible", version=base_schemas[path]["version"])
    for path in sorted(set(base_schemas) & set(target_schemas)):
        old, new = base_schemas[path], target_schemas[path]
        if old["sha256"] != new["sha256"]:
            if old["version"] == new["version"]:
                errors.append(f"schema {path} changed without schema_version change")
            else:
                delta = schema_delta(old["version"], new["version"])
                append_change(changes, "schema_changed", path, "incompatible" if delta == "major" else "compatible", delta=delta)

    base_shared, target_shared = base["shared_contracts"], target["shared_contracts"]
    for ident in sorted(set(target_shared) - set(base_shared)):
        append_change(changes, "shared_contract_added", ident, "compatible", version=target_shared[ident]["version"])
    for ident in sorted(set(base_shared) - set(target_shared)):
        append_change(changes, "shared_contract_removed", ident, "incompatible", version=base_shared[ident]["version"])
    for ident in sorted(set(base_shared) & set(target_shared)):
        old, new = base_shared[ident], target_shared[ident]
        if old["package_sha256"] != new["package_sha256"]:
            if old["version"] == new["version"]:
                errors.append(f"shared contract {ident} changed without package version change")
            else:
                delta = version_delta(old["version"], new["version"])
                append_change(changes, "shared_contract_changed", ident, "incompatible" if delta == "major" else "compatible", delta=delta)

    base_features, target_features = base["features"], target["features"]
    for feature_id in sorted(set(target_features) - set(base_features)):
        validate_policy_fields(feature_id, target_features[feature_id], policy)
        append_change(changes, "feature_added", feature_id, "compatible", version=target_features[feature_id]["package_version"])
    for feature_id in sorted(set(base_features) - set(target_features)):
        append_change(changes, "feature_removed", feature_id, "incompatible", version=base_features[feature_id]["package_version"])
    for feature_id in sorted(set(base_features) & set(target_features)):
        old, new = base_features[feature_id], target_features[feature_id]
        validate_policy_fields(feature_id, new, policy)
        if old["domain"] != new["domain"]:
            errors.append(f"feature identity {feature_id} moved domains")
        changed = old["package_sha256"] != new["package_sha256"] or old["descriptor_sha256"] != new["descriptor_sha256"]
        if changed:
            if old["package_version"] == new["package_version"]:
                errors.append(f"feature {feature_id} changed without package version change")
            else:
                delta = version_delta(old["package_version"], new["package_version"])
                scientific_changed = (old.get("statuses") or {}).get("scientific") != (new.get("statuses") or {}).get("scientific")
                compatibility = "scientific_review_required" if scientific_changed else ("incompatible" if delta == "major" else "compatible")
                append_change(changes, "feature_changed", feature_id, compatibility, delta=delta, scientific_status_changed=scientific_changed)

    base_domains, target_domains = base["domains"], target["domains"]
    base_indices = {row["domain_index"]: name for name, row in base_domains.items()}
    for domain in sorted(set(target_domains) - set(base_domains)):
        index = target_domains[domain]["domain_index"]
        if index in base_indices and base_indices[index] != domain:
            errors.append(f"domain index {index} reused by {domain}")
        append_change(changes, "domain_added", domain, "compatible", domain_index=index)
    for domain in sorted(set(base_domains) - set(target_domains)):
        append_change(changes, "domain_removed", domain, "incompatible", domain_index=base_domains[domain]["domain_index"])
    for domain in sorted(set(base_domains) & set(target_domains)):
        old, new = base_domains[domain], target_domains[domain]
        if old["domain_index"] != new["domain_index"]:
            errors.append(f"domain {domain} changed domain_index")
        if old["catalog_sha256"] != new["catalog_sha256"]:
            append_change(
                changes,
                "domain_revision",
                domain,
                "compatible",
                package_model_version=new["package_model_version"],
                schema_version=new["schema_version"],
                feature_versions=new["feature_versions"],
            )

    levels = {row["compatibility"] for row in changes}
    if errors:
        compatibility = "invalid"
    elif "incompatible" in levels:
        compatibility = "incompatible"
    elif "scientific_review_required" in levels:
        compatibility = "scientific_review_required"
    else:
        compatibility = "compatible"

    return {
        "compatibility": compatibility,
        "changes": sorted(changes, key=lambda row: (row["kind"], row["identity"])),
        "errors": sorted(errors),
    }


def current_parent() -> str:
    parent = git("rev-parse", "HEAD^", check=False)
    if not parent:
        raise CompatibilityFailure("no parent commit available; provide --base")
    return parent


def self_test() -> None:
    assert version_delta("1.0.0", "1.0.1") == "patch"
    assert version_delta("1.0.0", "1.1.0") == "minor"
    assert version_delta("1.0.0", "2.0.0") == "major"
    assert schema_delta("1.0", "1.1") == "minor"
    assert schema_delta("1.0", "2.0") == "major"
    try:
        version_delta("2.0.0", "1.0.0")
    except CompatibilityFailure:
        pass
    else:
        raise AssertionError("version regression must fail")
    print("Catalog compatibility logical scenarios: PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="base commit/ref; defaults to first parent")
    parser.add_argument("--target", help="target commit/ref; defaults to current checkout")
    parser.add_argument("--evidence", type=Path, help="write deterministic compatibility diff JSON")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            return 0
        base_ref = args.base or current_parent()
        target_ref = args.target
        policy = load_json(POLICY, target_ref)
        require_semver(policy.get("policy_version"), "compatibility policy version")
        base = snapshot(base_ref)
        target = snapshot(target_ref)
        result = compare(base, target, policy)
        evidence = {
            "schema_version": "1.0",
            "audit": "catalog-compatibility",
            "policy_version": policy.get("policy_version"),
            "base_commit": base["commit"],
            "target_commit": target["commit"],
            "base_population": {
                "domains": len(base["domains"]),
                "features": len(base["features"]),
                "shared_contracts": len(base["shared_contracts"]),
            },
            "target_population": {
                "domains": len(target["domains"]),
                "features": len(target["features"]),
                "shared_contracts": len(target["shared_contracts"]),
            },
            "compatibility": result["compatibility"],
            "changes": result["changes"],
            "errors": result["errors"],
        }
        rendered = json.dumps(evidence, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.evidence:
            args.evidence.write_text(rendered, encoding="utf-8")
        print(
            "Catalog compatibility audit: "
            f"{result['compatibility'].upper()} "
            f"({len(result['changes'])} classified changes, {len(result['errors'])} errors)"
        )
        return 1 if result["errors"] else 0
    except CompatibilityFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
