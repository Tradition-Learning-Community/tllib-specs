#!/usr/bin/env python3
"""Audit unresolved semantic governance and shared structural contracts.

The canonical handoff catalog is the sole population authority. This validator
never adjudicates scientific truth: it inventories already-published structural
signals, rejects silent semantic disappearance, and audits shared-contract
identity, dependency, version, closure, cardinality, ordering, error, provider,
and neutrality properties.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from collections import Counter
from typing import Any, Iterable

ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOG = pathlib.PurePosixPath("handoff/catalog.json")
RESOLUTIONS = pathlib.PurePosixPath("handoff/semantic-resolutions.json")
CLASSIFICATIONS = {"unknown", "contested", "external_provider", "blocker", "opacity"}
IMPLEMENTATION_IMPACT = {
    "executable": "executable",
    "conditionally_executable": "conditional",
    "structural_only": "structural_only",
}
SHARED_REF_RE = re.compile(r"^(TLC-HC-[A-Z0-9-]+)@([0-9]+\.[0-9]+\.[0-9]+)$")
SCIENTIFIC_ID_RE = re.compile(r"TLC-(?:FC|SO|SR)-")


class AuditFailure(RuntimeError):
    pass


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    if check and proc.returncode:
        raise AuditFailure(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def read_text(path: pathlib.PurePosixPath, ref: str | None = None) -> str:
    if ref is None:
        try:
            return ROOT.joinpath(*path.parts).read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise AuditFailure(f"missing file: {path}") from exc
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path.as_posix()}"], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if proc.returncode:
        raise AuditFailure(f"cannot read {path} at {ref}: {proc.stderr.strip()}")
    return proc.stdout


def load_json(path: pathlib.PurePosixPath, ref: str | None = None) -> dict[str, Any]:
    try:
        value = json.loads(read_text(path, ref))
    except json.JSONDecodeError as exc:
        where = f"{ref}:" if ref else ""
        raise AuditFailure(f"invalid JSON: {where}{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise AuditFailure(f"expected JSON object: {path}")
    return value


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_id(feature_id: str, kind: str, payload: Any) -> str:
    digest = hashlib.sha256(canonical([feature_id, kind, payload]).encode("utf-8")).hexdigest()[:24]
    return f"SEM-{digest}"


def parse_ref(value: str) -> tuple[str, str]:
    match = SHARED_REF_RE.fullmatch(value)
    if not match:
        raise AuditFailure(f"invalid shared contract reference: {value!r}")
    return match.group(1), match.group(2)


def iter_dicts(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_dicts(child)


def iter_shared_refs(value: Any) -> Iterable[tuple[str, str]]:
    for row in iter_dicts(value):
        ref = row.get("shared_contract_ref")
        if isinstance(ref, str):
            yield parse_ref(ref)


def dependency_rows(raw: Any, *, label: str, require_purpose: bool = False) -> set[tuple[str, str]]:
    if not isinstance(raw, list):
        raise AuditFailure(f"{label} must be a list")
    result: set[tuple[str, str]] = set()
    for row in raw:
        if not isinstance(row, dict):
            raise AuditFailure(f"{label} entry must be an object")
        ident, version = row.get("shared_contract_id"), row.get("version")
        if not isinstance(ident, str) or not isinstance(version, str):
            raise AuditFailure(f"{label} identity/version must be strings")
        if require_purpose and (not isinstance(row.get("purpose"), str) or not row["purpose"].strip()):
            raise AuditFailure(f"{label} {ident}@{version} requires a non-empty purpose")
        pair = (ident, version)
        if pair in result:
            raise AuditFailure(f"duplicate {label}: {ident}@{version}")
        result.add(pair)
    return result


def manifest_dependencies(manifest: dict[str, Any]) -> set[tuple[str, str]]:
    return dependency_rows(manifest.get("shared_dependencies"), label="manifest shared_dependencies")


def contract_dependencies(contract: dict[str, Any]) -> set[tuple[str, str]]:
    return dependency_rows(contract.get("dependencies"), label="contract dependencies", require_purpose=True)


def package_docs(path: str, manifest: dict[str, Any], ref: str | None) -> list[dict[str, Any]]:
    names = manifest.get("files")
    if not isinstance(names, list) or not names:
        raise AuditFailure(f"invalid files list in {path}/manifest.json")
    docs: list[dict[str, Any]] = []
    for name in names:
        if isinstance(name, str) and name.endswith(".json") and name != "manifest.json":
            docs.append(load_json(pathlib.PurePosixPath(path, name), ref))
    return docs


def authority_paths(path: str, ref: str | None) -> list[str]:
    trace = load_json(pathlib.PurePosixPath(path, "traceability.json"), ref)
    found = {
        row["path"] for row in iter_dicts(trace)
        if isinstance(row.get("path"), str) and row["path"]
    }
    return sorted(found) or [f"{path}/manifest.json"]


def explicit_unresolved_values(contract: dict[str, Any]) -> set[str]:
    found: set[str] = set()
    for row in iter_dicts(contract):
        context = " ".join(str(row.get(key, "")) for key in ("name", "semantic_role", "purpose")).lower()
        values = row.get("allowed_values")
        if "unresolved" in context and isinstance(values, list):
            found.update(item for item in values if isinstance(item, str) and item)
        unresolved_id = row.get("unresolved_id")
        if isinstance(unresolved_id, str) and unresolved_id:
            found.add(unresolved_id)
    return found


def explicit_classifications(docs: Iterable[dict[str, Any]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for doc in docs:
        for row in iter_dicts(doc):
            classification, unresolved_id = row.get("classification"), row.get("unresolved_id")
            if classification in CLASSIFICATIONS and isinstance(unresolved_id, str) and unresolved_id:
                result[unresolved_id] = classification
    return result


def blocker_payloads(docs: Iterable[dict[str, Any]]) -> list[Any]:
    unique: dict[str, Any] = {}
    for doc in docs:
        for row in iter_dicts(doc):
            for key, value in row.items():
                if "blocker" in str(key).lower() and value not in (None, "", [], {}, False):
                    unique[canonical(value)] = value
    return [unique[key] for key in sorted(unique)]


def classify_feature(scientific: str, dependencies: set[tuple[str, str]]) -> str:
    if scientific == "external_provider_required":
        return "external_provider"
    if any(ident == "TLC-HC-OPAQUE-VALUE" for ident, _ in dependencies):
        return "opacity"
    return "unknown"


def semantic_inventory(catalog: dict[str, Any], ref: str | None) -> list[dict[str, Any]]:
    features = catalog.get("features")
    if not isinstance(features, list):
        raise AuditFailure("catalog features must be a list")
    inventory: dict[str, dict[str, Any]] = {}
    for feature in features:
        if not isinstance(feature, dict):
            raise AuditFailure("catalog feature entry must be an object")
        feature_id, domain, path = feature.get("feature_id"), feature.get("domain"), feature.get("path")
        statuses = feature.get("statuses")
        if not all(isinstance(v, str) for v in (feature_id, domain, path)) or not isinstance(statuses, dict):
            raise AuditFailure("invalid catalog feature descriptor")
        scientific, execution = statuses.get("scientific"), statuses.get("execution")
        if not isinstance(scientific, str) or execution not in IMPLEMENTATION_IMPACT:
            raise AuditFailure(f"invalid statuses for {feature_id}")
        manifest = load_json(pathlib.PurePosixPath(path, "manifest.json"), ref)
        dependencies = manifest_dependencies(manifest)
        contract = load_json(pathlib.PurePosixPath(path, "contract.json"), ref)
        docs = package_docs(path, manifest, ref)
        classifications = explicit_classifications(docs)
        common = {
            "domain": domain,
            "feature_id": feature_id,
            "authority": authority_paths(path, ref),
            "execution_status": execution,
            "implementation_impact": IMPLEMENTATION_IMPACT[execution],
            "source_package": path,
        }
        if scientific != "defined":
            item_id = stable_id(feature_id, "scientific_status", scientific)
            inventory[item_id] = {
                "item_id": item_id,
                "kind": "scientific_boundary",
                "classification": classify_feature(scientific, dependencies),
                "scientific_status": scientific,
                "status": "active",
                **common,
            }
        for unresolved in sorted(explicit_unresolved_values(contract)):
            item_id = stable_id(feature_id, "unresolved_id", unresolved)
            inventory[item_id] = {
                "item_id": item_id,
                "kind": "unresolved_item",
                "unresolved_id": unresolved,
                "classification": classifications.get(unresolved, classify_feature(scientific, dependencies)),
                "scientific_status": scientific,
                "status": "active",
                **common,
            }
        for payload in blocker_payloads(docs):
            item_id = stable_id(feature_id, "blocker", payload)
            inventory[item_id] = {
                "item_id": item_id,
                "kind": "blocker",
                "classification": "blocker",
                "scientific_status": scientific,
                "status": "active",
                "payload_sha256": hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest(),
                **common,
            }
    return [inventory[key] for key in sorted(inventory)]


def validate_resolutions(current_ids: set[str], disappeared: set[str]) -> tuple[list[dict[str, Any]], list[str]]:
    ledger = load_json(RESOLUTIONS)
    rows = ledger.get("resolutions")
    if ledger.get("schema_version") != "1.0" or not isinstance(rows, list):
        raise AuditFailure("invalid handoff/semantic-resolutions.json")
    seen: set[str] = set()
    errors: list[str] = []
    normalized: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, dict):
            errors.append("resolution entry is not an object")
            continue
        item_id = row.get("item_id")
        if not isinstance(item_id, str) or not item_id:
            errors.append("resolution entry has no item_id")
            continue
        if item_id in seen:
            errors.append(f"duplicate resolution entry: {item_id}")
        seen.add(item_id)
        if row.get("status") != "resolved":
            errors.append(f"resolution {item_id} must have status=resolved")
        if not isinstance(row.get("resolution_ref"), str) or not row["resolution_ref"]:
            errors.append(f"resolution {item_id} requires resolution_ref")
        authority = row.get("authority")
        valid_authority = (
            isinstance(authority, str) and bool(authority)
        ) or (
            isinstance(authority, list) and bool(authority)
            and all(isinstance(value, str) and value for value in authority)
        )
        if not valid_authority:
            errors.append(f"resolution {item_id} requires explicit authority")
        if item_id in current_ids:
            errors.append(f"resolved semantic item is still active: {item_id}")
        normalized.append(row)
    unresolved = sorted(disappeared - seen)
    if unresolved:
        errors.append("semantic items disappeared without explicit resolution: " + ", ".join(unresolved))
    return normalized, errors


def validate_cardinality_order_errors(value: Any, label: str, errors: list[str], counters: Counter[str]) -> None:
    for row in iter_dicts(value):
        cardinality = row.get("cardinality")
        if isinstance(cardinality, dict):
            counters["cardinality"] += 1
            minimum, maximum = cardinality.get("minimum"), cardinality.get("maximum")
            if minimum is not None and (isinstance(minimum, bool) or not isinstance(minimum, int) or minimum < 0):
                errors.append(f"invalid minimum cardinality in {label}")
            if maximum is not None and (isinstance(maximum, bool) or not isinstance(maximum, int) or maximum < 0):
                errors.append(f"invalid maximum cardinality in {label}")
            if isinstance(minimum, int) and isinstance(maximum, int) and maximum < minimum:
                errors.append(f"maximum cardinality below minimum in {label}")
        if "ordering" in row:
            counters["ordering"] += 1
            if not isinstance(row.get("ordering"), str) or not row["ordering"]:
                errors.append(f"invalid ordering declaration in {label}")
        error_contract = row.get("error_contract")
        if isinstance(error_contract, list):
            counters["error_contracts"] += len(error_contract)
            local_codes: set[str] = set()
            for error in error_contract:
                if not isinstance(error, dict):
                    errors.append(f"invalid error contract in {label}")
                    continue
                code = error.get("code")
                if not isinstance(code, str) or not code:
                    errors.append(f"error contract without code in {label}")
                elif code in local_codes:
                    errors.append(f"duplicate error code within one error contract in {label}: {code}")
                else:
                    local_codes.add(code)


def audit_contracts(catalog: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    shared_rows, feature_rows = catalog.get("shared_contracts"), catalog.get("features")
    if not isinstance(shared_rows, list) or not isinstance(feature_rows, list):
        raise AuditFailure("catalog shared_contracts/features must be lists")

    shared: dict[str, dict[str, Any]] = {}
    graph: dict[str, set[str]] = {}
    counters: Counter[str] = Counter()

    for entry in shared_rows:
        if not isinstance(entry, dict):
            errors.append("invalid shared contract catalog entry")
            continue
        ident, version, path = entry.get("shared_contract_id"), entry.get("version"), entry.get("path")
        if not all(isinstance(v, str) for v in (ident, version, path)):
            errors.append("shared contract catalog identity/version/path is invalid")
            continue
        manifest = load_json(pathlib.PurePosixPath(path, "manifest.json"))
        contract = load_json(pathlib.PurePosixPath(path, "contract.json"))
        if manifest.get("shared_contract_id") != ident or manifest.get("package_version") != version:
            errors.append(f"shared contract identity/version mismatch: {ident}")
        statuses = manifest.get("statuses")
        if not isinstance(statuses, dict) or statuses.get("execution") != "structural_only":
            errors.append(f"shared contract is not structural_only: {ident}")
        declared = manifest_dependencies(manifest)
        structural_refs = set(iter_shared_refs(contract))
        structural_refs = {pair for pair in structural_refs if pair[0] != ident}
        if declared != structural_refs:
            errors.append(
                f"shared direct dependency mismatch for {ident}: "
                f"declared={sorted(declared)} refs={sorted(structural_refs)}"
            )
        catalog_deps = dependency_rows(entry.get("dependencies", []), label=f"catalog dependencies for {ident}")
        if declared != catalog_deps:
            errors.append(f"shared catalog dependency mismatch for {ident}")
        if SCIENTIFIC_ID_RE.search(canonical(contract)):
            errors.append(f"shared contract contains feature/object/relation scientific identity: {ident}")
        validate_cardinality_order_errors(contract, ident, errors, counters)
        shared[ident] = {"version": version, "deps": declared, "path": path}
        graph[ident] = {dep for dep, _ in declared}

    for ident, node in shared.items():
        for dep, version in node["deps"]:
            target = shared.get(dep)
            if target is None:
                errors.append(f"missing shared dependency target: {ident} -> {dep}@{version}")
            elif target["version"] != version:
                errors.append(
                    f"incompatible shared dependency version: {ident} -> {dep}@{version}, "
                    f"available={target['version']}"
                )

    closures: dict[str, list[str]] = {}
    def closure(start: str, stack: tuple[str, ...] = ()) -> set[str]:
        if start in stack:
            errors.append("shared dependency cycle: " + " -> ".join((*stack, start)))
            return set()
        result: set[str] = set()
        for dep in sorted(graph.get(start, set())):
            result.add(dep)
            result.update(closure(dep, (*stack, start)))
        return result

    for ident in sorted(shared):
        closures[ident] = sorted(closure(ident))

    feature_closure_sizes: Counter[int] = Counter()
    candidate_markers = 0
    external_provider_features = 0

    for entry in feature_rows:
        if not isinstance(entry, dict):
            errors.append("invalid feature catalog entry")
            continue
        feature_id, path = entry.get("feature_id"), entry.get("path")
        if not isinstance(feature_id, str) or not isinstance(path, str):
            errors.append("invalid feature identity/path")
            continue
        manifest = load_json(pathlib.PurePosixPath(path, "manifest.json"))
        contract = load_json(pathlib.PurePosixPath(path, "contract.json"))
        declared = manifest_dependencies(manifest)
        contract_declared = contract_dependencies(contract)
        if declared != contract_declared:
            errors.append(
                f"feature dependency declaration mismatch for {feature_id}: "
                f"manifest={sorted(declared)} contract={sorted(contract_declared)}"
            )
        catalog_deps = dependency_rows(entry.get("shared_dependencies", []), label=f"catalog dependencies for {feature_id}")
        if declared != catalog_deps:
            errors.append(f"feature catalog dependency mismatch for {feature_id}")
        operational_refs = set(iter_shared_refs(contract))
        undeclared_refs = operational_refs - declared
        if undeclared_refs:
            errors.append(f"undeclared shared references for {feature_id}: {sorted(undeclared_refs)}")

        closure_ids: set[str] = set()
        for dep, version in declared:
            target = shared.get(dep)
            if target is None:
                errors.append(f"missing feature dependency target: {feature_id} -> {dep}@{version}")
                continue
            if target["version"] != version:
                errors.append(
                    f"incompatible feature dependency version: {feature_id} -> {dep}@{version}, "
                    f"available={target['version']}"
                )
            closure_ids.add(dep)
            closure_ids.update(closures.get(dep, []))
        feature_closure_sizes[len(closure_ids)] += 1

        docs = package_docs(path, manifest, None)
        for doc in docs:
            validate_cardinality_order_errors(doc, feature_id, errors, counters)
            for row in iter_dicts(doc):
                marker = row.get("shared_contract_candidate")
                if marker not in (None, False, "", [], {}):
                    candidate_markers += 1

        declared_ids = {ident for ident, _ in declared}
        has_errors = any(
            isinstance(row.get("error_contract"), list) and bool(row["error_contract"])
            for row in iter_dicts(contract)
        )
        if has_errors and "TLC-HC-STRUCTURED-ERROR" not in declared_ids:
            errors.append(f"feature error boundary lacks TLC-HC-STRUCTURED-ERROR: {feature_id}")
        counters["structured_error_boundaries"] += int("TLC-HC-STRUCTURED-ERROR" in declared_ids)
        counters["opaque_provider_boundaries"] += int("TLC-HC-OPAQUE-VALUE" in declared_ids)
        statuses = entry.get("statuses")
        if isinstance(statuses, dict) and statuses.get("scientific") == "external_provider_required":
            external_provider_features += 1

    return {
        "shared_contract_count": len(shared),
        "shared_dependency_closures": closures,
        "feature_count": len(feature_rows),
        "feature_closure_size_distribution": {str(k): v for k, v in sorted(feature_closure_sizes.items())},
        "cardinality_declarations_audited": counters["cardinality"],
        "ordering_declarations_audited": counters["ordering"],
        "error_contract_entries_audited": counters["error_contracts"],
        "structured_error_boundaries": counters["structured_error_boundaries"],
        "opaque_provider_boundaries": counters["opaque_provider_boundaries"],
        "external_provider_features": external_provider_features,
        "explicit_shared_contract_candidate_markers": candidate_markers,
        "dependency_exactness_rule": "feature manifest == feature contract dependency declaration; shared manifest == direct structural refs; catalog mirrors manifests",
        "scientific_neutrality_rule": "shared contracts are structural_only and contain no feature/object/relation scientific identities",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=pathlib.Path, help="write deterministic JSON evidence outside the checkout")
    args = parser.parse_args()
    errors: list[str] = []
    current_commit = git("rev-parse", "HEAD")
    parent = git("rev-parse", "HEAD^", check=False) or None
    catalog = load_json(CATALOG)
    current = semantic_inventory(catalog, None)
    current_ids = {row["item_id"] for row in current}
    previous: list[dict[str, Any]] = []
    if parent:
        try:
            previous = semantic_inventory(load_json(CATALOG, parent), parent)
        except AuditFailure as exc:
            errors.append(f"cannot audit previous semantic inventory: {exc}")
    previous_ids = {row["item_id"] for row in previous}
    added = current_ids - previous_ids if parent else set()
    disappeared = previous_ids - current_ids if parent else set()
    resolutions, resolution_errors = validate_resolutions(current_ids, disappeared)
    errors.extend(resolution_errors)
    contract_evidence = audit_contracts(catalog, errors)

    summary = catalog.get("summary")
    if not isinstance(summary, dict):
        errors.append("catalog summary must be an object")
        summary = {}
    class_counts = Counter(row["classification"] for row in current)
    execution_counts = Counter(row["execution_status"] for row in current)
    unique_unresolved = sorted({
        row["unresolved_id"] for row in current
        if row.get("kind") == "unresolved_item" and isinstance(row.get("unresolved_id"), str)
    })
    evidence = {
        "schema_version": "1.0",
        "status": "pass" if not errors else "fail",
        "spec_commit": current_commit,
        "compared_parent": parent,
        "population": {
            "domains": summary.get("domain_count"),
            "features": summary.get("feature_count"),
            "shared_contracts": summary.get("shared_contract_count"),
        },
        "semantic_governance": {
            "inventory_count": len(current),
            "unique_unresolved_identifier_count": len(unique_unresolved),
            "unique_unresolved_identifiers": unique_unresolved,
            "classification_counts": dict(sorted(class_counts.items())),
            "execution_status_counts": dict(sorted(execution_counts.items())),
            "added_since_parent": sorted(added),
            "disappeared_since_parent": sorted(disappeared),
            "explicit_resolution_count": len(resolutions),
            "inventory": current,
        },
        "shared_contract_audit": contract_evidence,
        "errors": errors,
        "commands": [
            "python tools/handoff/generate_catalog.py --check",
            "python tools/pipeline/validate_semantic_contract_governance.py --evidence <path>",
        ],
    }
    rendered = json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.evidence:
        args.evidence.parent.mkdir(parents=True, exist_ok=True)
        args.evidence.write_text(rendered, encoding="utf-8")
    print(json.dumps({
        "status": evidence["status"],
        "spec_commit": current_commit,
        "domains": evidence["population"]["domains"],
        "features": evidence["population"]["features"],
        "semantic_items": len(current),
        "unique_unresolved_identifiers": len(unique_unresolved),
        "added": len(added),
        "disappeared": len(disappeared),
        "shared_contracts": contract_evidence["shared_contract_count"],
        "errors": errors,
    }, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AuditFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
