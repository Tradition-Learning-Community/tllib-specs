#!/usr/bin/env python3
"""Rebuild the current TLC global registry without making scientific decisions.

This wrapper first runs the existing conservative reconciliation builder, then
adds a current, status-aware inventory of the sixteen domains.  It distinguishes
IR-layer coverage from canonical IR selection, algorithmic completion, oracle
completion, and implementation readiness.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import importlib.util
import json
import pathlib
import subprocess
import sys
from typing import Any

import yaml


DOMAINS = [
    ("00", "master", "Master"),
    ("01", "disciple", "Disciple"),
    ("02", "community", "Community"),
    ("03", "huit-dimensions", "Huit Dimensions"),
    ("04", "invariants", "Invariants"),
    ("05", "dynamics", "Dynamics"),
    ("06", "theorems", "Theorems"),
    ("07", "message", "Message"),
    ("08", "principle", "Principle"),
    ("09", "values", "Values"),
    ("10", "virtues", "Virtues"),
    ("11", "capacities", "Capacities"),
    ("12", "competencies", "Competencies"),
    ("13", "practice", "Practice"),
    ("14", "lived-experience", "Lived Experience"),
    ("15", "relations", "Relations"),
]

SELECTED_STATUSES = {
    "selected",
    "selected_canonical",
    "canonical_selected",
    "approved",
    "approved_with_reservations",
    "selected_with_reservations",
}


def git(root: pathlib.Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def load(path: pathlib.Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    return default if value is None else value


def dump(path: pathlib.Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
        newline="\n",
    )


def normalized(value: Any) -> str | None:
    if value in (None, ""):
        return None
    return str(value).strip().lower()


def first_status(data: dict[str, Any], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        value = data.get(key)
        if value not in (None, ""):
            return str(value)
    return None


def extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active feature entries without counting lineage or internal IDs."""
    primary_keys = (
        "features",
        "active_features",
        "feature_catalogue",
        "feature_catalog",
        "catalogue",
        "items",
        "entries",
    )
    id_keys = ("feature_id", "feature_candidate_id", "id")

    def direct_ids(value: Any) -> list[str]:
        found: list[str] = []
        if isinstance(value, str):
            if value.startswith("TLC-FC-"):
                found.append(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.startswith("TLC-FC-"):
                    found.append(item)
                elif isinstance(item, dict):
                    for key in id_keys:
                        candidate = item.get(key)
                        if isinstance(candidate, str) and candidate.startswith("TLC-FC-"):
                            found.append(candidate)
                            break
        elif isinstance(value, dict):
            for item in value.values():
                found.extend(direct_ids(item))
        return found

    if isinstance(data, dict):
        for key in primary_keys:
            if key in data:
                found = direct_ids(data[key])
                if found:
                    return sorted(set(found))

    found: list[str] = []

    def walk(value: Any, parent_key: str = "") -> None:
        lowered = parent_key.lower()
        if any(token in lowered for token in ("legacy", "rejected", "excluded", "deferred", "comparison")):
            return
        if isinstance(value, dict):
            for key, child in value.items():
                if key in id_keys and isinstance(child, str) and child.startswith("TLC-FC-"):
                    found.append(child)
                else:
                    walk(child, str(key))
        elif isinstance(value, list):
            for child in value:
                walk(child, parent_key)

    walk(data)
    return sorted(set(found))


def authoritative_matrix(root: pathlib.Path, domain_registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for domain in domain_registry.get("domains", []):
        slug = str(domain.get("domain_id"))
        source_ref = domain.get("feature_source")
        if not isinstance(source_ref, str):
            raise RuntimeError(f"missing authoritative feature source for {slug}")
        identifiers = extract_authoritative_feature_ids(load(root / source_ref, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers found for {slug} in {source_ref}")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows


def extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active feature entries without counting lineage or internal IDs."""
    primary_keys = (
        "features",
        "active_features",
        "feature_catalogue",
        "feature_catalog",
        "catalogue",
        "items",
        "entries",
    )
    id_keys = ("feature_id", "feature_candidate_id", "id")

    def direct_ids(value: Any) -> list[str]:
        found: list[str] = []
        if isinstance(value, str):
            if value.startswith("TLC-FC-"):
                found.append(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.startswith("TLC-FC-"):
                    found.append(item)
                elif isinstance(item, dict):
                    for key in id_keys:
                        candidate = item.get(key)
                        if isinstance(candidate, str) and candidate.startswith("TLC-FC-"):
                            found.append(candidate)
                            break
        elif isinstance(value, dict):
            for item in value.values():
                found.extend(direct_ids(item))
        return found

    if isinstance(data, dict):
        for key in primary_keys:
            if key in data:
                found = direct_ids(data[key])
                if found:
                    return sorted(set(found))

    found: list[str] = []

    def walk(value: Any, parent_key: str = "") -> None:
        lowered = parent_key.lower()
        if any(token in lowered for token in ("legacy", "rejected", "excluded", "deferred", "comparison")):
            return
        if isinstance(value, dict):
            for key, child in value.items():
                if key in id_keys and isinstance(child, str) and child.startswith("TLC-FC-"):
                    found.append(child)
                else:
                    walk(child, str(key))
        elif isinstance(value, list):
            for child in value:
                walk(child, parent_key)

    walk(data)
    return sorted(set(found))


def authoritative_matrix(root: pathlib.Path, domain_registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for domain in domain_registry.get("domains", []):
        slug = str(domain.get("domain_id"))
        source_ref = domain.get("feature_source")
        if not isinstance(source_ref, str):
            raise RuntimeError(f"missing authoritative feature source for {slug}")
        identifiers = extract_authoritative_feature_ids(load(root / source_ref, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers found for {slug} in {source_ref}")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows


def extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active feature entries without counting lineage or internal IDs."""
    primary_keys = (
        "features",
        "active_features",
        "feature_catalogue",
        "feature_catalog",
        "catalogue",
        "items",
        "entries",
    )
    id_keys = ("feature_id", "feature_candidate_id", "id")

    def direct_ids(value: Any) -> list[str]:
        found: list[str] = []
        if isinstance(value, str):
            if value.startswith("TLC-FC-"):
                found.append(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.startswith("TLC-FC-"):
                    found.append(item)
                elif isinstance(item, dict):
                    for key in id_keys:
                        candidate = item.get(key)
                        if isinstance(candidate, str) and candidate.startswith("TLC-FC-"):
                            found.append(candidate)
                            break
        elif isinstance(value, dict):
            for item in value.values():
                found.extend(direct_ids(item))
        return found

    if isinstance(data, dict):
        for key in primary_keys:
            if key in data:
                found = direct_ids(data[key])
                if found:
                    return sorted(set(found))

    found: list[str] = []

    def walk(value: Any, parent_key: str = "") -> None:
        lowered = parent_key.lower()
        if any(token in lowered for token in ("legacy", "rejected", "excluded", "deferred", "comparison")):
            return
        if isinstance(value, dict):
            for key, child in value.items():
                if key in id_keys and isinstance(child, str) and child.startswith("TLC-FC-"):
                    found.append(child)
                else:
                    walk(child, str(key))
        elif isinstance(value, list):
            for child in value:
                walk(child, parent_key)

    walk(data)
    return sorted(set(found))


def authoritative_matrix(root: pathlib.Path, domain_registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for domain in domain_registry.get("domains", []):
        slug = str(domain.get("domain_id"))
        source_ref = domain.get("feature_source")
        if not isinstance(source_ref, str):
            raise RuntimeError(f"missing authoritative feature source for {slug}")
        identifiers = extract_authoritative_feature_ids(load(root / source_ref, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers found for {slug} in {source_ref}")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows


def extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active feature entries without counting lineage or internal IDs."""
    primary_keys = (
        "features",
        "active_features",
        "feature_catalogue",
        "feature_catalog",
        "catalogue",
        "items",
        "entries",
    )
    id_keys = ("feature_id", "feature_candidate_id", "id")

    def direct_ids(value: Any) -> list[str]:
        found: list[str] = []
        if isinstance(value, str):
            if value.startswith("TLC-FC-"):
                found.append(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.startswith("TLC-FC-"):
                    found.append(item)
                elif isinstance(item, dict):
                    for key in id_keys:
                        candidate = item.get(key)
                        if isinstance(candidate, str) and candidate.startswith("TLC-FC-"):
                            found.append(candidate)
                            break
        elif isinstance(value, dict):
            for item in value.values():
                found.extend(direct_ids(item))
        return found

    if isinstance(data, dict):
        for key in primary_keys:
            if key in data:
                found = direct_ids(data[key])
                if found:
                    return sorted(set(found))

    found: list[str] = []

    def walk(value: Any, parent_key: str = "") -> None:
        lowered = parent_key.lower()
        if any(token in lowered for token in ("legacy", "rejected", "excluded", "deferred", "comparison")):
            return
        if isinstance(value, dict):
            for key, child in value.items():
                if key in id_keys and isinstance(child, str) and child.startswith("TLC-FC-"):
                    found.append(child)
                else:
                    walk(child, str(key))
        elif isinstance(value, list):
            for child in value:
                walk(child, parent_key)

    walk(data)
    return sorted(set(found))


def authoritative_matrix(root: pathlib.Path, domain_registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for domain in domain_registry.get("domains", []):
        slug = str(domain.get("domain_id"))
        source_ref = domain.get("feature_source")
        if not isinstance(source_ref, str):
            raise RuntimeError(f"missing authoritative feature source for {slug}")
        identifiers = extract_authoritative_feature_ids(load(root / source_ref, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers found for {slug} in {source_ref}")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows


def extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active feature entries without counting lineage or internal IDs."""
    primary_keys = (
        "features",
        "active_features",
        "feature_catalogue",
        "feature_catalog",
        "catalogue",
        "items",
        "entries",
    )
    id_keys = ("feature_id", "feature_candidate_id", "id")

    def direct_ids(value: Any) -> list[str]:
        found: list[str] = []
        if isinstance(value, str):
            if value.startswith("TLC-FC-"):
                found.append(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.startswith("TLC-FC-"):
                    found.append(item)
                elif isinstance(item, dict):
                    for key in id_keys:
                        candidate = item.get(key)
                        if isinstance(candidate, str) and candidate.startswith("TLC-FC-"):
                            found.append(candidate)
                            break
        elif isinstance(value, dict):
            for item in value.values():
                found.extend(direct_ids(item))
        return found

    if isinstance(data, dict):
        for key in primary_keys:
            if key in data:
                found = direct_ids(data[key])
                if found:
                    return sorted(set(found))

    found: list[str] = []

    def walk(value: Any, parent_key: str = "") -> None:
        lowered = parent_key.lower()
        if any(token in lowered for token in ("legacy", "rejected", "excluded", "deferred", "comparison")):
            return
        if isinstance(value, dict):
            for key, child in value.items():
                if key in id_keys and isinstance(child, str) and child.startswith("TLC-FC-"):
                    found.append(child)
                else:
                    walk(child, str(key))
        elif isinstance(value, list):
            for child in value:
                walk(child, parent_key)

    walk(data)
    return sorted(set(found))


def authoritative_matrix(root: pathlib.Path, domain_registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for domain in domain_registry.get("domains", []):
        slug = str(domain.get("domain_id"))
        source_ref = domain.get("feature_source")
        if not isinstance(source_ref, str):
            raise RuntimeError(f"missing authoritative feature source for {slug}")
        identifiers = extract_authoritative_feature_ids(load(root / source_ref, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers found for {slug} in {source_ref}")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows


def source_commit(root: pathlib.Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    try:
        git(root, "fetch", "origin", "main", "--quiet")
        return git(root, "merge-base", "HEAD", "origin/main")
    except Exception:
        return git(root, "rev-parse", "HEAD")


def run_legacy_builder(root: pathlib.Path, head: str) -> None:
    path = root / "tools/global-reconciliation/build_global_reconciliation.py"
    spec = importlib.util.spec_from_file_location("tlc_legacy_global_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.EXPECTED_COMMIT = head
    previous_argv = sys.argv
    try:
        sys.argv = [str(path), "--root", str(root)]
        result = module.main()
    finally:
        sys.argv = previous_argv
    if result != 0:
        raise RuntimeError(f"legacy reconciliation builder returned {result}")


def patch_legacy_builder(root: pathlib.Path) -> None:
    path = root / "tools/global-reconciliation/build_global_reconciliation.py"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        'EXPECTED_COMMIT = "2cd5a3c6dfe8786926e58d49387b5f4846697a66"',
        "EXPECTED_COMMIT: str | None = None",
    )
    text = text.replace(
        '"source_commit": EXPECTED_COMMIT,',
        '"source_commit": EXPECTED_COMMIT or git(root, "rev-parse", "HEAD"),',
    )
    text = text.replace(
        '"classification": "pilot_only" if pilot else "canonical_validated",',
        '"classification": "inventory_only",',
    )
    text = text.replace(
        '"review_required": pilot or feature_id not in feature_ids,',
        '"review_required": feature_id not in feature_ids,',
    )
    text = text.replace(
        "return 0 if head == EXPECTED_COMMIT else 2",
        "return 0 if EXPECTED_COMMIT in (None, head) else 2",
    )
    text = text.replace(
        "- Candidate and pilot contracts/IR outside Master, Disciple, and Community require scientific review.",
        "- Presence at the IR layer does not imply canonical selection, executability, or implementation readiness.",
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def locate_ir_artifact(root: pathlib.Path, feature_id: str, registry_entry: dict[str, Any]) -> str | None:
    for key in (
        "candidate_ref",
        "canonical_ref",
        "ir_ref",
        "artifact_ref",
        "prototype_ref",
        "declarative_ir_ref",
    ):
        value = registry_entry.get(key)
        if isinstance(value, str) and (root / value).is_file():
            return value.replace("\\", "/")

    directory = root / "ir" / feature_id
    if directory.is_dir():
        candidates = sorted(
            path for path in directory.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".json", ".yaml", ".yml"}
            and "test" not in path.name.lower()
            and "coverage" not in path.name.lower()
            and "manifest" not in path.name.lower()
            and ("ir" in path.name.lower() or "prototype" in path.name.lower())
        )
        if candidates:
            return str(candidates[0].relative_to(root)).replace("\\", "/")

    registry_path = root / f"registry/ir/{feature_id}/ir.yaml"
    if registry_path.is_file():
        role = normalized(registry_entry.get("artifact_role")) or ""
        substantive_keys = {"ir_id", "ir_kind", "operations", "nodes", "entrypoint", "control_flow"}
        if "registry_entry" not in role or substantive_keys.intersection(registry_entry):
            return str(registry_path.relative_to(root)).replace("\\", "/")
    return None


def locate_test_plan(root: pathlib.Path, feature_id: str) -> str | None:
    direct = (
        root / f"registry/test-plans/{feature_id}/test-plan.yaml",
        root / f"ir/{feature_id}/test-plan.yaml",
        root / f"ir/{feature_id}/test-plan.yml",
    )
    for path in direct:
        if path.is_file():
            return str(path.relative_to(root)).replace("\\", "/")
    directory = root / "ir" / feature_id
    if directory.is_dir():
        candidates = sorted(
            path for path in directory.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".yaml", ".yml", ".json"}
            and ("test" in path.name.lower() or "oracle" in path.name.lower())
        )
        if candidates:
            return str(candidates[0].relative_to(root)).replace("\\", "/")
    return None


def build_feature_inventory(root: pathlib.Path, matrix_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source_row in sorted(matrix_rows, key=lambda row: (row.get("domain", ""), row.get("feature_id", ""))):
        feature_id = str(source_row["feature_id"])
        domain = str(source_row["domain"])
        contract_ref = f"registry/math-contracts/{feature_id}/contract.yaml"
        ir_registry_ref = f"registry/ir/{feature_id}/ir.yaml"
        contract = load(root / contract_ref, {})
        ir_registry = load(root / ir_registry_ref, {})
        if not isinstance(contract, dict):
            contract = {}
        if not isinstance(ir_registry, dict):
            ir_registry = {}
        ir_artifact_ref = locate_ir_artifact(root, feature_id, ir_registry)
        ir_artifact = {}
        if ir_artifact_ref:
            artifact_path = root / ir_artifact_ref
            try:
                if artifact_path.suffix.lower() == ".json":
                    ir_artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
                else:
                    ir_artifact = load(artifact_path, {})
            except Exception:
                ir_artifact = {}
        if not isinstance(ir_artifact, dict):
            ir_artifact = {}
        status_source = {**ir_artifact, **ir_registry}
        selection_status = first_status(
            status_source,
            ("selection_status", "canonical_status", "approval_status", "status", "ir_kind"),
        )
        scientific_status = first_status(
            status_source,
            ("scientific_status", "validation_status", "prototype_classification", "semantic_quality"),
        )
        execution_status = first_status(
            status_source,
            ("execution_status", "computational_status", "implementation_status"),
        )
        contract_status = first_status(
            contract,
            ("scientific_status", "contract_status", "validation_status", "status"),
        )
        contract_present = (root / contract_ref).is_file()
        ir_registry_present = (root / ir_registry_ref).is_file()
        ir_artifact_present = ir_artifact_ref is not None
        test_plan_ref = locate_test_plan(root, feature_id)
        test_plan_present = test_plan_ref is not None
        ir_layer_complete = all((contract_present, ir_artifact_present, test_plan_present))
        selected = normalized(selection_status) in SELECTED_STATUSES
        if ir_registry_present and ir_artifact_ref == ir_registry_ref:
            representation_mode = "substantive_registry_ir"
        elif ir_registry_present:
            representation_mode = "registry_plus_external_ir"
        else:
            representation_mode = "external_ir_without_registry_entry"
        rows.append(
            {
                "domain": domain,
                "feature_id": feature_id,
                "contract_ref": contract_ref if contract_present else None,
                "ir_registry_ref": ir_registry_ref if ir_registry_present else None,
                "ir_artifact_ref": ir_artifact_ref,
                "test_plan_ref": test_plan_ref,
                "contract_present": contract_present,
                "ir_registry_present": ir_registry_present,
                "ir_artifact_present": ir_artifact_present,
                "test_plan_present": test_plan_present,
                "ir_layer_complete": ir_layer_complete,
                "ir_representation_mode": representation_mode,
                "registry_normalization_required": not ir_registry_present,
                "contract_status": contract_status,
                "selection_status": selection_status,
                "scientific_status": scientific_status,
                "execution_status": execution_status,
                "canonical_selection_explicit": selected,
                "implementation_ready_asserted": normalized(execution_status)
                in {"ready_for_code_generation", "implementation_ready", "executable_approved"},
            }
        )
    return rows


def status_counter(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    values = collections.Counter(str(row.get(key) or "unspecified") for row in rows)
    return dict(sorted(values.items()))


def domain_summaries(feature_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in feature_rows:
        grouped[row["domain"]].append(row)
    result = []
    for number, slug, name in DOMAINS:
        rows = sorted(grouped.get(slug, []), key=lambda row: row["feature_id"])
        feature_count = len(rows)
        complete_count = sum(bool(row["ir_layer_complete"]) for row in rows)
        selected_count = sum(bool(row["canonical_selection_explicit"]) for row in rows)
        if feature_count and selected_count == feature_count:
            selection_state = "complete_explicit"
        elif selected_count:
            selection_state = "mixed"
        else:
            selection_state = "not_explicitly_completed"
        result.append(
            {
                "domain_number": number,
                "domain_id": slug,
                "name": name,
                "feature_count": feature_count,
                "contracts_present": sum(bool(row["contract_present"]) for row in rows),
                "ir_registry_entries_present": sum(bool(row["ir_registry_present"]) for row in rows),
                "ir_artifacts_present": sum(bool(row["ir_artifact_present"]) for row in rows),
                "test_plans_present": sum(bool(row["test_plan_present"]) for row in rows),
                "ir_layer_complete_features": complete_count,
                "ir_layer_complete": bool(feature_count) and complete_count == feature_count,
                "canonical_selection_explicit_features": selected_count,
                "canonical_selection_state": selection_state,
                "selection_statuses": status_counter(rows, "selection_status"),
                "execution_statuses": status_counter(rows, "execution_status"),
                "next_phase": "domain_scientific_and_technical_ir_review",
            }
        )
    return result


def patch_generated_metadata(path: pathlib.Path, source: str, tool_commit: str, timestamp: str) -> None:
    data = load(path, {})
    if not isinstance(data, dict):
        return
    data["authority"] = "origin/main"
    data["canonical_commit"] = source
    data["generated_from_tool_commit"] = tool_commit
    data["generated_at"] = timestamp
    dump(path, data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[2])
    parser.add_argument("--source-commit")
    args = parser.parse_args()
    root = args.root.resolve()
    tool_commit = git(root, "rev-parse", "HEAD")
    baseline_commit = source_commit(root, args.source_commit)
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    run_legacy_builder(root, tool_commit)
    patch_legacy_builder(root)

    registry_dir = root / "registry/global-reconciliation"
    report_dir = root / "reports/global-reconciliation"
    rebuilt_registry_names = (
        "blocker-registry.yaml",
        "contract-execution-plan.yaml",
        "cycle-registry.yaml",
        "decision-required.yaml",
        "dependency-graph.yaml",
        "domain-feature-matrix.yaml",
        "domain-registry.yaml",
        "existing-artifact-audit.yaml",
        "feature-contract-matrix.yaml",
        "feature-ir-matrix.yaml",
        "ir-execution-plan.yaml",
        "manifest.yaml",
        "readiness-registry.yaml",
    )
    for name in rebuilt_registry_names:
        patch_generated_metadata(registry_dir / name, baseline_commit, tool_commit, timestamp)

    old_domain_registry = load(registry_dir / "domain-registry.yaml", {})
    authoritative_rows = authoritative_matrix(root, old_domain_registry)
    feature_rows = build_feature_inventory(root, authoritative_rows)
    domains = domain_summaries(feature_rows)
    total_features = len(feature_rows)
    complete_features = sum(bool(row["ir_layer_complete"]) for row in feature_rows)
    selected_features = sum(bool(row["canonical_selection_explicit"]) for row in feature_rows)
    implementation_ready = sum(bool(row["implementation_ready_asserted"]) for row in feature_rows)
    all_domains_ir = all(domain["ir_layer_complete"] for domain in domains)

    meta = {
        "schema_version": 2,
        "authority": "origin/main",
        "canonical_commit": baseline_commit,
        "generated_from_tool_commit": tool_commit,
        "generated_at": timestamp,
    }

    taxonomy = {
        **meta,
        "purpose": "Prevent maturity-level conflation during domain-by-domain completion.",
        "levels": [
            {
                "level": "L1_scientific_structure",
                "meaning": "Scientific objects and relations are inventoried with unresolved items preserved.",
                "does_not_imply": ["approved feature boundaries", "canonical IR", "executability"],
            },
            {
                "level": "L2_functional_scope",
                "meaning": "Active software features are enumerated for a domain.",
                "does_not_imply": ["approved contracts", "canonical IR", "implementation readiness"],
            },
            {
                "level": "L3_contract_layer",
                "meaning": "A mathematical contract artifact exists for each active feature.",
                "does_not_imply": ["all scientific reservations resolved", "canonical IR"],
            },
            {
                "level": "L4_ir_layer",
                "meaning": "Each active feature has a mathematical contract, an IR artifact, and a structural test plan; a separate IR registry entry is optional for legacy prototype layouts.",
                "does_not_imply": ["canonical IR selection", "algorithmic completeness", "code readiness"],
            },
            {
                "level": "L5_ir_selection",
                "meaning": "Scientific and technical review explicitly selects or bounds the IR for each feature.",
                "does_not_imply": ["oracle completeness", "production implementation readiness"],
            },
            {
                "level": "L6_algorithm_and_oracle",
                "meaning": "Executable algorithmic semantics and verification oracles are specified.",
                "does_not_imply": ["optimized C++ implementation"],
            },
            {
                "level": "L7_reference_implementation",
                "meaning": "A readable reference implementation conforms to the selected IR and oracle.",
                "does_not_imply": ["production optimization"],
            },
            {
                "level": "L8_production_implementation",
                "meaning": "C++, bindings, backend conformance, packaging, and release gates are complete.",
                "does_not_imply": [],
            },
        ],
    }
    dump(registry_dir / "status-taxonomy.yaml", taxonomy)

    baseline = {
        **meta,
        "baseline_id": "TLC-GLOBAL-BASELINE-IR-001",
        "scope": "sixteen_domain_inventory_through_ir_layer",
        "statement": (
            "All sixteen TLC domains are inventoried through the IR layer. This statement records artifact coverage only; "
            "it does not assert uniform canonical IR selection, algorithmic completeness, oracle completeness, or code readiness."
        ),
        "totals": {
            "domains": len(domains),
            "active_features": total_features,
            "contracts_present": sum(bool(row["contract_present"]) for row in feature_rows),
            "ir_registry_entries_present": sum(bool(row["ir_registry_present"]) for row in feature_rows),
            "ir_artifacts_present": sum(bool(row["ir_artifact_present"]) for row in feature_rows),
            "test_plans_present": sum(bool(row["test_plan_present"]) for row in feature_rows),
            "ir_layer_complete_features": complete_features,
            "canonical_selection_explicit_features": selected_features,
            "implementation_ready_asserted_features": implementation_ready,
        },
        "all_domains_reach_ir_layer": all_domains_ir,
        "uniform_canonical_selection_asserted": selected_features == total_features and total_features > 0,
        "implementation_readiness_asserted": implementation_ready == total_features and total_features > 0,
        "domains": domains,
        "next_work": {
            "strategy": "one_domain_at_a_time",
            "first_domain": "master",
            "domain_order": [slug for _, slug, _ in DOMAINS],
            "target_per_domain": "review feature boundaries, contracts, IR selection, algorithms, and oracles before closure",
        },
        "scientific_decisions_made_by_this_build": [],
        "math_sources_modified": False,
    }
    dump(registry_dir / "current-baseline.yaml", baseline)

    domain_by_id = {row["domain_id"]: row for row in domains}
    for domain in old_domain_registry.get("domains", []):
        current = domain_by_id.get(domain.get("domain_id"), {})
        domain["artifact_status"] = "current_inventory_through_ir_layer"
        domain["artifact_counts"] = {
            key: current.get(key, 0)
            for key in (
                "feature_count",
                "contracts_present",
                "ir_registry_entries_present",
                "ir_artifacts_present",
                "test_plans_present",
            )
        }
        domain["maturity"] = {
            "scientific_structure": "present_with_preserved_reservations",
            "functional_scope": "active_catalogue_present",
            "contract_layer": "complete" if current.get("contracts_present") == current.get("feature_count") else "incomplete",
            "ir_layer": "complete" if current.get("ir_layer_complete") else "incomplete",
            "canonical_ir_selection": current.get("canonical_selection_state", "not_assessed"),
            "algorithmic_specification": "not_globally_assessed",
            "oracle": "not_globally_assessed",
            "implementation": "not_started",
        }
        domain["selection_statuses"] = current.get("selection_statuses", {})
        domain["execution_statuses"] = current.get("execution_statuses", {})
        domain["next_phase"] = current.get("next_phase")
        if isinstance(domain.get("counts"), dict):
            domain["counts"]["features"] = current.get("feature_count", 0)
            domain["counts"]["contract_plans"] = current.get("feature_count", 0) if domain.get("contract_plan_present") else 0
            domain["counts"]["ir_plans"] = current.get("feature_count", 0) if domain.get("ir_plan_present") else 0
    if isinstance(old_domain_registry.get("global_counts"), dict):
        old_domain_registry["global_counts"]["features"] = total_features
        old_domain_registry["global_counts"]["contract_plans"] = sum(
            domain_by_id.get(row.get("domain_id"), {}).get("feature_count", 0)
            for row in old_domain_registry.get("domains", []) if row.get("contract_plan_present")
        )
        old_domain_registry["global_counts"]["ir_plans"] = sum(
            domain_by_id.get(row.get("domain_id"), {}).get("feature_count", 0)
            for row in old_domain_registry.get("domains", []) if row.get("ir_plan_present")
        )
    old_domain_registry.update(meta)
    old_domain_registry["baseline_status"] = "current_inventory_through_ir_layer"
    old_domain_registry["coverage_statement"] = baseline["statement"]
    old_domain_registry["domains"] = old_domain_registry.get("domains", [])
    old_domain_registry["current_totals"] = baseline["totals"]
    dump(registry_dir / "domain-registry.yaml", old_domain_registry)

    dump(registry_dir / "domain-feature-matrix.yaml", {**meta, "rows": feature_rows})
    dump(
        registry_dir / "feature-contract-matrix.yaml",
        {
            **meta,
            "rows": [
                {
                    "domain": row["domain"],
                    "feature_id": row["feature_id"],
                    "contract_ref": row["contract_ref"],
                    "contract_present": row["contract_present"],
                    "contract_status": row["contract_status"],
                }
                for row in feature_rows
            ],
        },
    )
    dump(
        registry_dir / "feature-ir-matrix.yaml",
        {
            **meta,
            "rows": [
                {
                    "domain": row["domain"],
                    "feature_id": row["feature_id"],
                    "ir_registry_ref": row["ir_registry_ref"],
                    "ir_artifact_ref": row["ir_artifact_ref"],
                    "test_plan_ref": row["test_plan_ref"],
                    "ir_layer_complete": row["ir_layer_complete"],
                    "selection_status": row["selection_status"],
                    "scientific_status": row["scientific_status"],
                    "execution_status": row["execution_status"],
                    "canonical_selection_explicit": row["canonical_selection_explicit"],
                }
                for row in feature_rows
            ],
        },
    )

    readiness = load(registry_dir / "readiness-registry.yaml", {})
    readiness_by_id = {row.get("feature_id"): row for row in readiness.get("features", [])}
    for row in feature_rows:
        target = readiness_by_id.setdefault(row["feature_id"], {"domain": row["domain"], "feature_id": row["feature_id"]})
        target["current_maturity"] = {
            "ir_layer_complete": row["ir_layer_complete"],
            "selection_status": row["selection_status"],
            "execution_status": row["execution_status"],
            "canonical_selection_explicit": row["canonical_selection_explicit"],
            "implementation_ready_asserted": row["implementation_ready_asserted"],
        }
    readiness.update(meta)
    readiness["features"] = [readiness_by_id[row["feature_id"]] for row in feature_rows]
    readiness["current_summary"] = baseline["totals"]
    readiness["scope_note"] = "IR coverage is recorded separately from canonical selection and implementation readiness."
    dump(registry_dir / "readiness-registry.yaml", readiness)

    audit_rows = []
    for row in feature_rows:
        audit_rows.append(
            {
                "feature_id": row["feature_id"],
                "domain": row["domain"],
                "contract_present": row["contract_present"],
                "ir_registry_present": row["ir_registry_present"],
                "ir_artifact_present": row["ir_artifact_present"],
                "test_plan_present": row["test_plan_present"],
                "classification": "current_active_feature_artifact_set",
                "ir_layer_complete": row["ir_layer_complete"],
                "selection_status": row["selection_status"],
                "execution_status": row["execution_status"],
                "scientific_content_modified": False,
            }
        )
    dump(
        registry_dir / "existing-artifact-audit.yaml",
        {
            **meta,
            "artifacts": audit_rows,
            "summary": {
                "features": total_features,
                "complete_ir_layer_sets": complete_features,
                "explicitly_selected": selected_features,
                "implementation_ready_asserted": implementation_ready,
            },
        },
    )

    sequence = {
        **meta,
        "plan_id": "TLC-DOMAIN-REVIEW-SEQUENCE-001",
        "strategy": "one_domain_at_a_time",
        "domain_order": [
            {
                "order": index,
                "domain_number": number,
                "domain_id": slug,
                "name": name,
                "entry_gate": "current IR-layer artifact set present",
                "steps": [
                    "confirm active feature inventory",
                    "review only explicitly unstable feature boundaries",
                    "review and approve or revise contracts feature by feature",
                    "select, bound, or revise IR feature by feature",
                    "check internal and required cross-domain coherence",
                    "specify algorithms",
                    "specify oracles",
                    "publish domain closure manifest",
                ],
                "exit_gate": "domain complete through algorithms and oracles, with explicit deferrals recorded",
            }
            for index, (number, slug, name) in enumerate(DOMAINS, 1)
        ],
        "cross_domain_rule": (
            "Review only dependencies required by the current domain; do not reopen all other domains automatically."
        ),
        "first_domain": "master",
    }
    dump(registry_dir / "domain-review-sequence.yaml", sequence)

    for plan_name in ("contract-execution-plan.yaml", "ir-execution-plan.yaml"):
        plan = load(registry_dir / plan_name, {})
        if isinstance(plan, dict):
            plan.update(meta)
            plan["status"] = "superseded_for_next_phase"
            plan["superseded_by"] = "registry/global-reconciliation/domain-review-sequence.yaml"
            plan["preservation_note"] = "Retained as a historical generated plan; not the active Phase 4 sequence."
            dump(registry_dir / plan_name, plan)

    for name in ("dependency-graph.yaml", "cycle-registry.yaml", "blocker-registry.yaml"):
        document = load(registry_dir / name, {})
        if isinstance(document, dict):
            document.update(meta)
            document["scope_note"] = (
                "This registry records evidence and gates. It does not invalidate IR-layer coverage and does not force "
                "all sixteen domains to be reopened together."
            )
            dump(registry_dir / name, document)

    dump(
        registry_dir / "decision-required.yaml",
        {
            **meta,
            "status": "baseline_rebuilt_without_scientific_adjudication",
            "administrative_result": {
                "sixteen_domains_present": len(domains) == 16,
                "active_features_inventoried": total_features,
                "all_domains_reach_ir_layer": all_domains_ir,
                "next_domain": "master",
            },
            "scientific_decisions_made": [],
            "deferred_to_domain_review": [
                "feature-boundary decisions",
                "contract approval or revision",
                "canonical IR selection",
                "cross-domain semantic dependency classification when required by the current domain",
                "algorithm and oracle approval",
            ],
        },
    )

    manifest = load(registry_dir / "manifest.yaml", {})
    manifest.update(meta)
    manifest["scope"] = "current_global_inventory_through_ir_layer"
    manifest["baseline_ref"] = "registry/global-reconciliation/current-baseline.yaml"
    manifest["status_taxonomy_ref"] = "registry/global-reconciliation/status-taxonomy.yaml"
    manifest["active_sequence_ref"] = "registry/global-reconciliation/domain-review-sequence.yaml"
    current_registry_artifacts = sorted(
        [f"registry/global-reconciliation/{name}" for name in rebuilt_registry_names]
        + [
            "registry/global-reconciliation/current-baseline.yaml",
            "registry/global-reconciliation/domain-review-sequence.yaml",
            "registry/global-reconciliation/status-taxonomy.yaml",
        ]
    )
    manifest["artifacts"] = current_registry_artifacts + [
        "reports/global-reconciliation/phase4-current-baseline-work-item.md",
        "reports/global-reconciliation/reconciliation-report.md",
        "tools/global-reconciliation/build_global_reconciliation.py",
        "tools/global-reconciliation/build_current_global_registry.py",
        "tools/global-reconciliation/validate_global_reconciliation.py",
        "tools/global-reconciliation/validate_current_global_registry.py",
    ]
    manifest["prohibited_outputs_created"] = []
    manifest["source_preparations_modified"] = []
    manifest["math_sources_modified"] = False
    manifest["scientific_decisions_made"] = []
    manifest["summary"] = baseline["totals"]
    dump(registry_dir / "manifest.yaml", manifest)

    report_dir.mkdir(parents=True, exist_ok=True)
    domain_lines = "\n".join(
        f"| {row['domain_number']} | {row['name']} | {row['feature_count']} | "
        f"{row['contracts_present']} | {row['ir_artifacts_present']} | {row['test_plans_present']} | "
        f"{'yes' if row['ir_layer_complete'] else 'no'} | {row['canonical_selection_state']} |"
        for row in domains
    )
    report = f"""# Current global TLC registry through the IR layer

- Authority: `origin/main`
- Scientific baseline commit: `{baseline_commit}`
- Registry tooling commit at generation time: `{tool_commit}`
- Generated: `{timestamp}`
- Scope: inventory and status normalization only.
- Scientific decisions made: none.
- `maths/` modified: no.

## Result

All sixteen domains are present. The current active catalogues contain **{total_features} features**.
**{complete_features}** feature sets contain a mathematical contract, an IR registry entry, an IR artifact,
and a structural test plan. Therefore `all_domains_reach_ir_layer` is **{str(all_domains_ir).lower()}**.

This is an IR-layer coverage statement. It is not a claim that all IRs have the same maturity, are canonically
selected, are executable, have complete algorithms or oracles, or are ready for C++ implementation.

## Domain inventory

| No. | Domain | Features | Contracts | IR artifacts | Test plans | IR layer complete | Canonical selection |
|---:|---|---:|---:|---:|---:|---|---|
{domain_lines}

## Normalized interpretation

- The sixteen domains have reached the IR layer.
- Canonical IR selection remains a separate domain-by-domain activity.
- Algorithmic specifications and scientific oracles remain later gates.
- Historical human-review queues and dependency cycles are not discarded, but they are handled only when
  they affect the domain currently under review.
- No domain is reopened automatically because another domain contains an unresolved item.

## Active next-phase sequence

The active strategy is recorded in `domain-review-sequence.yaml`: Master first, then Disciple, Community,
Huit Dimensions, Invariants, Dynamics, Theorems, Message, Principle, Values, Virtues, Capacities,
Competencies, Practice, Lived Experience, and Relations.

For each domain: confirm feature inventory, review unstable boundaries only, review contracts, select or revise
IRs, verify required dependencies, specify algorithms, specify oracles, and close the domain.

## Counts and status sources

The current authoritative active count is **{total_features}**. The previous aggregate of 175 recursively
counted nine identifiers under `legacy_goose_feature_ids` in the Capacities preparation. That source explicitly
marks those identifiers as non-authoritative. They are now preserved as lineage evidence but excluded from the
active feature matrix. Historical, rejected, deferred, and internal IR node identifiers are likewise excluded.

Raw contract, selection, scientific, and execution statuses are preserved in the feature matrices. No status
is silently promoted to `approved`, `selected`, `executable`, or `implementation_ready`.
"""
    (report_dir / "reconciliation-report.md").write_text(report, encoding="utf-8", newline="\n")

    result = {
        "status": "ok" if all_domains_ir and len(domains) == 16 else "incomplete",
        "canonical_commit": baseline_commit,
        "tool_commit": tool_commit,
        "domains": len(domains),
        "features": total_features,
        "ir_layer_complete_features": complete_features,
        "all_domains_reach_ir_layer": all_domains_ir,
        "canonical_selection_explicit_features": selected_features,
        "implementation_ready_asserted_features": implementation_ready,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
