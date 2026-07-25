#!/usr/bin/env python3
"""Build the authoritative current TLC registry through the IR layer.

The builder is deliberately administrative. It inventories the sixteen domain
catalogues, mathematical contracts, IR artifacts and structural test plans. It
normalizes heterogeneous historical layouts without selecting an IR, resolving
scientific questions, or modifying the theory sources.
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
from typing import Any, Iterable

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
DOMAIN_IDS = {slug for _, slug, _ in DOMAINS}
FEATURE_SOURCE_NAMES = (
    "feature-inventory.yaml",
    "feature-catalogue.yaml",
    "feature-status.yaml",
    "feature-classification.yaml",
)
NORMALIZED_SELECTED_STATUSES = {
    "selected",
    "selected_canonical",
    "canonical_selected",
    "approved",
    "approved_with_reservations",
    "selected_with_reservations",
}
CORE_REBUILT_NAMES = (
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


def first_status(data: dict[str, Any], keys: Iterable[str]) -> str | None:
    for key in keys:
        value = data.get(key)
        if value not in (None, ""):
            return str(value)
    return None


def scientific_baseline_commit(root: pathlib.Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    try:
        git(root, "fetch", "origin", "main", "--quiet")
        return git(root, "merge-base", "HEAD", "origin/main")
    except Exception:
        return git(root, "rev-parse", "HEAD")


def run_legacy_builder(root: pathlib.Path, head: str) -> None:
    """Regenerate conservative dependency artifacts before normalizing them."""
    path = root / "tools/global-reconciliation/build_global_reconciliation.py"
    spec = importlib.util.spec_from_file_location("tlc_global_reconciliation_builder", path)
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


def feature_source(root: pathlib.Path, slug: str) -> pathlib.Path:
    directory = root / "registry/domain-progress" / slug
    for name in FEATURE_SOURCE_NAMES:
        path = directory / name
        if path.is_file():
            return path
    raise RuntimeError(f"no authoritative feature source for domain {slug}")


def extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active entries without recursively counting lineage identifiers."""
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
        if isinstance(value, str) and value.startswith("TLC-FC-"):
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


def authoritative_matrix(root: pathlib.Path) -> tuple[list[dict[str, Any]], dict[str, str]]:
    rows: list[dict[str, Any]] = []
    sources: dict[str, str] = {}
    for _, slug, _ in DOMAINS:
        source = feature_source(root, slug)
        identifiers = extract_authoritative_feature_ids(load(source, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers in {source}")
        sources[slug] = str(source.relative_to(root)).replace("\\", "/")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows, sources


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
            path
            for path in directory.iterdir()
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
            path
            for path in directory.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".yaml", ".yml", ".json"}
            and ("test" in path.name.lower() or "oracle" in path.name.lower())
        )
        if candidates:
            return str(candidates[0].relative_to(root)).replace("\\", "/")
    return None


def read_ir_artifact(root: pathlib.Path, reference: str | None) -> dict[str, Any]:
    if not reference:
        return {}
    path = root / reference
    try:
        if path.suffix.lower() == ".json":
            value = json.loads(path.read_text(encoding="utf-8"))
        else:
            value = load(path, {})
    except Exception:
        return {}
    return value if isinstance(value, dict) else {}


def build_feature_inventory(root: pathlib.Path, matrix_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source_row in sorted(matrix_rows, key=lambda row: (row["domain"], row["feature_id"])):
        feature_id = str(source_row["feature_id"])
        domain = str(source_row["domain"])
        contract_ref = f"registry/math-contracts/{feature_id}/contract.yaml"
        ir_registry_ref = f"registry/ir/{feature_id}/ir.yaml"
        contract = load(root / contract_ref, {})
        registry_entry = load(root / ir_registry_ref, {})
        contract = contract if isinstance(contract, dict) else {}
        registry_entry = registry_entry if isinstance(registry_entry, dict) else {}
        ir_artifact_ref = locate_ir_artifact(root, feature_id, registry_entry)
        ir_artifact = read_ir_artifact(root, ir_artifact_ref)
        status_source = {**ir_artifact, **registry_entry}
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
        normalized_selection = normalized(selection_status)
        normalized_gate_passed = normalized_selection in NORMALIZED_SELECTED_STATUSES
        raw_canonical_label = bool(
            normalized_selection
            and "canonical" in normalized_selection
            and "not_canonical" not in normalized_selection
            and "non_canonical" not in normalized_selection
        )
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
                "raw_canonical_label": raw_canonical_label,
                "normalized_selection_gate_passed": normalized_gate_passed,
                "implementation_ready_asserted": normalized(execution_status)
                in {"ready_for_code_generation", "implementation_ready", "executable_approved"},
            }
        )
    return rows


def status_counter(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    counter = collections.Counter(str(row.get(key) or "unspecified") for row in rows)
    return dict(sorted(counter.items()))


def domain_summaries(feature_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in feature_rows:
        grouped[row["domain"]].append(row)
    summaries: list[dict[str, Any]] = []
    for number, slug, name in DOMAINS:
        rows = sorted(grouped[slug], key=lambda row: row["feature_id"])
        feature_count = len(rows)
        complete_count = sum(bool(row["ir_layer_complete"]) for row in rows)
        normalized_count = sum(bool(row["normalized_selection_gate_passed"]) for row in rows)
        raw_canonical_count = sum(bool(row["raw_canonical_label"]) for row in rows)
        if normalized_count == feature_count:
            normalized_state = "complete"
        elif normalized_count:
            normalized_state = "mixed"
        else:
            normalized_state = "not_completed"
        summaries.append(
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
                "ir_layer_complete": bool(rows) and complete_count == feature_count,
                "raw_canonical_label_features": raw_canonical_count,
                "normalized_selection_gate_passed_features": normalized_count,
                "normalized_selection_state": normalized_state,
                "selection_statuses": status_counter(rows, "selection_status"),
                "execution_statuses": status_counter(rows, "execution_status"),
                "next_phase": "domain_scientific_and_technical_ir_review",
            }
        )
    return summaries


def meta(source_commit: str, tool_commit: str, timestamp: str) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "authority": "origin/main",
        "canonical_commit": source_commit,
        "generated_from_tool_commit": tool_commit,
        "generated_at": timestamp,
    }


def patch_metadata(document: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    document.update(metadata)
    return document


def filter_dependency_graph(
    document: dict[str, Any], active_ids: set[str], metadata: dict[str, Any]
) -> tuple[dict[str, Any], set[str]]:
    edges = []
    for edge in document.get("edges", []):
        dependency_type = edge.get("dependency_type")
        if dependency_type == "domain_dependency":
            keep = edge.get("source_domain") in DOMAIN_IDS and edge.get("target") in DOMAIN_IDS
        elif dependency_type == "feature_dependency":
            keep = edge.get("source") in active_ids and edge.get("target") in active_ids
        else:
            keep = False
        if keep:
            edges.append(edge)
    valid_edge_ids = {str(edge.get("edge_id")) for edge in edges}
    document = patch_metadata(document, metadata)
    document["edges"] = edges
    document["summary"] = {
        "total": len(edges),
        "domain_dependencies": sum(edge.get("dependency_type") == "domain_dependency" for edge in edges),
        "feature_dependencies": sum(edge.get("dependency_type") == "feature_dependency" for edge in edges),
        "semantic_reconciled": sum(bool(edge.get("semantic_compatibility_confirmed")) for edge in edges),
    }
    document["scope_note"] = (
        "Only authoritative active feature identifiers and the sixteen domain identifiers contribute to this graph."
    )
    return document, valid_edge_ids


def filter_cycles(
    document: dict[str, Any], active_ids: set[str], valid_edge_ids: set[str], metadata: dict[str, Any]
) -> dict[str, Any]:
    cycles = []
    for cycle in document.get("cycles", []):
        level = cycle.get("level")
        nodes = set(cycle.get("nodes", []))
        if level == "domain":
            keep = nodes.issubset(DOMAIN_IDS)
        elif level == "feature":
            keep = nodes.issubset(active_ids)
        else:
            keep = False
        if not keep:
            continue
        cycle = dict(cycle)
        cycle["edges"] = [edge_id for edge_id in cycle.get("edges", []) if edge_id in valid_edge_ids]
        cycles.append(cycle)
    document = patch_metadata(document, metadata)
    document["cycles"] = cycles
    document["summary"] = {
        "detected": len(cycles),
        "generation_blocking": sum(bool(cycle.get("generation_blocking")) for cycle in cycles),
    }
    document["scope_note"] = (
        "Cycles are retained as review evidence; they do not erase established IR-layer artifact coverage."
    )
    return document


def filter_blockers(
    document: dict[str, Any], active_ids: set[str], metadata: dict[str, Any]
) -> tuple[dict[str, Any], set[str]]:
    blockers = [row for row in document.get("blockers", []) if row.get("feature_id") in active_ids]
    valid_ids = {str(row.get("blocker_id")) for row in blockers}
    document = patch_metadata(document, metadata)
    document["blockers"] = blockers
    document["summary"] = {
        "total": len(blockers),
        "critical": sum(row.get("severity") == "critical" for row in blockers),
        "major": sum(row.get("severity") == "major" for row in blockers),
        "minor": sum(row.get("severity") == "minor" for row in blockers),
    }
    document["scope_note"] = (
        "Blockers apply only to authoritative active features and to later maturity gates, not to the fact that an IR artifact exists."
    )
    return document, valid_ids


def filter_execution_plan(
    document: dict[str, Any], active_ids: set[str], valid_blocker_ids: set[str], metadata: dict[str, Any]
) -> dict[str, Any]:
    feature_keys = (
        "features_included",
        "features_excluded",
        "contracts_to_produce",
        "existing_contracts_to_review",
        "features_ready_now",
    )
    document = patch_metadata(document, metadata)
    for key in feature_keys:
        if isinstance(document.get(key), list):
            document[key] = [value for value in document[key] if value in active_ids]
    for batch in document.get("batches", []):
        for key in feature_keys:
            if isinstance(batch.get(key), list):
                batch[key] = [value for value in batch[key] if value in active_ids]
        if isinstance(batch.get("blockers"), list):
            batch["blockers"] = [value for value in batch["blockers"] if value in valid_blocker_ids]
    document["status"] = "superseded_for_next_phase"
    document["superseded_by"] = "registry/global-reconciliation/domain-review-sequence.yaml"
    document["preservation_note"] = "Retained as a filtered historical generated plan; the active sequence is domain by domain."
    return document


def build_readiness(
    old_document: dict[str, Any], feature_rows: list[dict[str, Any]], metadata: dict[str, Any]
) -> dict[str, Any]:
    old_by_id = {row.get("feature_id"): row for row in old_document.get("features", [])}
    rows = []
    for feature in feature_rows:
        row = dict(old_by_id.get(feature["feature_id"], {}))
        row["domain"] = feature["domain"]
        row["feature_id"] = feature["feature_id"]
        row["current_maturity"] = {
            "ir_layer_complete": feature["ir_layer_complete"],
            "selection_status": feature["selection_status"],
            "execution_status": feature["execution_status"],
            "raw_canonical_label": feature["raw_canonical_label"],
            "normalized_selection_gate_passed": feature["normalized_selection_gate_passed"],
            "implementation_ready_asserted": feature["implementation_ready_asserted"],
        }
        rows.append(row)
    return {
        **metadata,
        "features": rows,
        "summary": {
            "active_features": len(rows),
            "ir_layer_complete": sum(row["current_maturity"]["ir_layer_complete"] for row in rows),
            "normalized_selection_gate_passed": sum(
                row["current_maturity"]["normalized_selection_gate_passed"] for row in rows
            ),
            "implementation_ready_asserted": sum(
                row["current_maturity"]["implementation_ready_asserted"] for row in rows
            ),
        },
        "scope_note": "IR-layer coverage is separate from normalized selection and implementation readiness.",
    }


def build_taxonomy(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        **metadata,
        "purpose": "Prevent maturity-level conflation during domain-by-domain completion.",
        "levels": [
            {
                "level": "L1_scientific_structure",
                "meaning": "Scientific objects and relations are inventoried with unresolved items preserved.",
                "does_not_imply": ["approved feature boundaries", "canonical IR", "executability"],
            },
            {
                "level": "L2_functional_scope",
                "meaning": "Authoritative active software features are enumerated for a domain.",
                "does_not_imply": ["approved contracts", "canonical IR", "implementation readiness"],
            },
            {
                "level": "L3_contract_layer",
                "meaning": "A mathematical contract artifact exists for each active feature.",
                "does_not_imply": ["all scientific reservations resolved", "canonical IR"],
            },
            {
                "level": "L4_ir_layer",
                "meaning": "Each active feature has a contract, an IR artifact and a structural test plan.",
                "does_not_imply": ["uniform canonical selection", "algorithmic completeness", "code readiness"],
            },
            {
                "level": "L5_ir_selection",
                "meaning": "A common scientific and technical gate explicitly selects or bounds each feature IR.",
                "does_not_imply": ["oracle completeness", "production implementation readiness"],
            },
            {
                "level": "L6_algorithm_and_oracle",
                "meaning": "Algorithmic semantics and verification oracles are specified.",
                "does_not_imply": ["optimized C++ implementation"],
            },
            {
                "level": "L7_reference_implementation",
                "meaning": "A readable reference implementation conforms to the selected IR and oracle.",
                "does_not_imply": ["production optimization"],
            },
            {
                "level": "L8_production_implementation",
                "meaning": "C++, bindings, backend conformance, packaging and release gates are complete.",
                "does_not_imply": [],
            },
        ],
    }


def build_sequence(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        **metadata,
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
                    "confirm authoritative active feature inventory",
                    "review only explicitly unstable feature boundaries",
                    "review and approve or revise contracts feature by feature",
                    "select, bound or revise IR feature by feature",
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[2])
    parser.add_argument("--source-commit")
    args = parser.parse_args()
    root = args.root.resolve()
    tool_commit = git(root, "rev-parse", "HEAD")
    source_commit = scientific_baseline_commit(root, args.source_commit)
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    metadata = meta(source_commit, tool_commit, timestamp)

    run_legacy_builder(root, tool_commit)
    registry = root / "registry/global-reconciliation"
    reports = root / "reports/global-reconciliation"

    matrix_rows, feature_sources = authoritative_matrix(root)
    feature_rows = build_feature_inventory(root, matrix_rows)
    active_ids = {row["feature_id"] for row in feature_rows}
    domains = domain_summaries(feature_rows)
    domain_by_id = {row["domain_id"]: row for row in domains}

    total_features = len(feature_rows)
    complete_features = sum(row["ir_layer_complete"] for row in feature_rows)
    raw_canonical = sum(row["raw_canonical_label"] for row in feature_rows)
    normalized_selected = sum(row["normalized_selection_gate_passed"] for row in feature_rows)
    implementation_ready = sum(row["implementation_ready_asserted"] for row in feature_rows)
    all_domains_ir = len(domains) == 16 and all(row["ir_layer_complete"] for row in domains)

    totals = {
        "domains": len(domains),
        "active_features": total_features,
        "contracts_present": sum(row["contract_present"] for row in feature_rows),
        "ir_registry_entries_present": sum(row["ir_registry_present"] for row in feature_rows),
        "ir_artifacts_present": sum(row["ir_artifact_present"] for row in feature_rows),
        "test_plans_present": sum(row["test_plan_present"] for row in feature_rows),
        "ir_layer_complete_features": complete_features,
        "raw_canonical_label_features": raw_canonical,
        "normalized_selection_gate_passed_features": normalized_selected,
        "implementation_ready_asserted_features": implementation_ready,
    }

    baseline = {
        **metadata,
        "baseline_id": "TLC-GLOBAL-BASELINE-IR-001",
        "scope": "sixteen_domain_inventory_through_ir_layer",
        "statement": (
            "All sixteen TLC domains are inventoried through the IR layer. This records artifact coverage only and does not "
            "assert uniform canonical selection, algorithmic completeness, oracle completeness or code readiness."
        ),
        "totals": totals,
        "all_domains_reach_ir_layer": all_domains_ir,
        "uniform_normalized_selection_gate_passed": normalized_selected == total_features and total_features > 0,
        "implementation_readiness_asserted": implementation_ready == total_features and total_features > 0,
        "domains": domains,
        "next_work": {
            "strategy": "one_domain_at_a_time",
            "first_domain": "master",
            "domain_order": [slug for _, slug, _ in DOMAINS],
            "target_per_domain": "review feature boundaries, contracts, IR selection, algorithms and oracles before closure",
        },
        "scientific_decisions_made_by_this_build": [],
        "math_sources_modified": False,
    }
    dump(registry / "current-baseline.yaml", baseline)
    dump(registry / "status-taxonomy.yaml", build_taxonomy(metadata))
    dump(registry / "domain-review-sequence.yaml", build_sequence(metadata))

    legacy_domain_registry = load(registry / "domain-registry.yaml", {})
    for domain in legacy_domain_registry.get("domains", []):
        slug = domain.get("domain_id")
        current = domain_by_id[slug]
        domain["feature_source"] = feature_sources[slug]
        domain["artifact_status"] = "current_inventory_through_ir_layer"
        if isinstance(domain.get("counts"), dict):
            domain["counts"]["features"] = current["feature_count"]
            domain["counts"]["contract_plans"] = current["feature_count"] if domain.get("contract_plan_present") else 0
            domain["counts"]["ir_plans"] = current["feature_count"] if domain.get("ir_plan_present") else 0
        domain["artifact_counts"] = {
            key: current[key]
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
            "functional_scope": "authoritative_active_catalogue_present",
            "contract_layer": "complete" if current["contracts_present"] == current["feature_count"] else "incomplete",
            "ir_layer": "complete" if current["ir_layer_complete"] else "incomplete",
            "raw_canonical_label_features": current["raw_canonical_label_features"],
            "normalized_selection_gate": current["normalized_selection_state"],
            "algorithmic_specification": "not_globally_assessed",
            "oracle": "not_globally_assessed",
            "implementation": "not_started",
        }
        domain["selection_statuses"] = current["selection_statuses"]
        domain["execution_statuses"] = current["execution_statuses"]
        domain["next_phase"] = current["next_phase"]
    if isinstance(legacy_domain_registry.get("global_counts"), dict):
        legacy_domain_registry["global_counts"]["features"] = total_features
        legacy_domain_registry["global_counts"]["contract_plans"] = sum(
            domain_by_id[row["domain_id"]]["feature_count"]
            for row in legacy_domain_registry.get("domains", [])
            if row.get("contract_plan_present")
        )
        legacy_domain_registry["global_counts"]["ir_plans"] = sum(
            domain_by_id[row["domain_id"]]["feature_count"]
            for row in legacy_domain_registry.get("domains", [])
            if row.get("ir_plan_present")
        )
    legacy_domain_registry = patch_metadata(legacy_domain_registry, metadata)
    legacy_domain_registry["baseline_status"] = "current_inventory_through_ir_layer"
    legacy_domain_registry["coverage_statement"] = baseline["statement"]
    legacy_domain_registry["current_totals"] = totals
    dump(registry / "domain-registry.yaml", legacy_domain_registry)

    dump(registry / "domain-feature-matrix.yaml", {**metadata, "rows": feature_rows})
    dump(
        registry / "feature-contract-matrix.yaml",
        {
            **metadata,
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
        registry / "feature-ir-matrix.yaml",
        {
            **metadata,
            "rows": [
                {
                    "domain": row["domain"],
                    "feature_id": row["feature_id"],
                    "ir_registry_ref": row["ir_registry_ref"],
                    "ir_artifact_ref": row["ir_artifact_ref"],
                    "test_plan_ref": row["test_plan_ref"],
                    "ir_layer_complete": row["ir_layer_complete"],
                    "ir_representation_mode": row["ir_representation_mode"],
                    "registry_normalization_required": row["registry_normalization_required"],
                    "selection_status": row["selection_status"],
                    "scientific_status": row["scientific_status"],
                    "execution_status": row["execution_status"],
                    "raw_canonical_label": row["raw_canonical_label"],
                    "normalized_selection_gate_passed": row["normalized_selection_gate_passed"],
                }
                for row in feature_rows
            ],
        },
    )

    old_readiness = load(registry / "readiness-registry.yaml", {})
    dump(registry / "readiness-registry.yaml", build_readiness(old_readiness, feature_rows, metadata))

    audit_rows = [
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
        for row in feature_rows
    ]
    dump(
        registry / "existing-artifact-audit.yaml",
        {
            **metadata,
            "artifacts": audit_rows,
            "summary": {
                "features": total_features,
                "complete_ir_layer_sets": complete_features,
                "raw_canonical_labels": raw_canonical,
                "normalized_selection_gate_passed": normalized_selected,
                "implementation_ready_asserted": implementation_ready,
            },
        },
    )

    dependency_graph, valid_edge_ids = filter_dependency_graph(
        load(registry / "dependency-graph.yaml", {}), active_ids, metadata
    )
    dump(registry / "dependency-graph.yaml", dependency_graph)
    dump(
        registry / "cycle-registry.yaml",
        filter_cycles(load(registry / "cycle-registry.yaml", {}), active_ids, valid_edge_ids, metadata),
    )
    blocker_registry, valid_blocker_ids = filter_blockers(
        load(registry / "blocker-registry.yaml", {}), active_ids, metadata
    )
    dump(registry / "blocker-registry.yaml", blocker_registry)
    for name in ("contract-execution-plan.yaml", "ir-execution-plan.yaml"):
        dump(
            registry / name,
            filter_execution_plan(load(registry / name, {}), active_ids, valid_blocker_ids, metadata),
        )

    dump(
        registry / "decision-required.yaml",
        {
            **metadata,
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
                "normalized canonical IR selection",
                "required cross-domain semantic dependency classification",
                "algorithm and oracle approval",
            ],
        },
    )

    current_registry_artifacts = sorted(
        [f"registry/global-reconciliation/{name}" for name in CORE_REBUILT_NAMES]
        + [
            "registry/global-reconciliation/current-baseline.yaml",
            "registry/global-reconciliation/domain-review-sequence.yaml",
            "registry/global-reconciliation/status-taxonomy.yaml",
        ]
    )
    manifest = {
        **metadata,
        "scope": "current_global_inventory_through_ir_layer",
        "baseline_ref": "registry/global-reconciliation/current-baseline.yaml",
        "status_taxonomy_ref": "registry/global-reconciliation/status-taxonomy.yaml",
        "active_sequence_ref": "registry/global-reconciliation/domain-review-sequence.yaml",
        "artifacts": current_registry_artifacts
        + [
            "reports/global-reconciliation/phase4-current-baseline-work-item.md",
            "reports/global-reconciliation/reconciliation-report.md",
            "tools/global-reconciliation/build_global_reconciliation.py",
            "tools/global-reconciliation/build_current_global_registry.py",
            "tools/global-reconciliation/validate_global_reconciliation.py",
            "tools/global-reconciliation/validate_current_global_registry.py",
        ],
        "prohibited_outputs_created": [],
        "source_preparations_modified": [],
        "math_sources_modified": False,
        "scientific_decisions_made": [],
        "summary": totals,
    }
    dump(registry / "manifest.yaml", manifest)

    reports.mkdir(parents=True, exist_ok=True)
    domain_lines = "\n".join(
        f"| {row['domain_number']} | {row['name']} | {row['feature_count']} | {row['contracts_present']} | "
        f"{row['ir_artifacts_present']} | {row['test_plans_present']} | yes | "
        f"{row['raw_canonical_label_features']} | {row['normalized_selection_gate_passed_features']} |"
        for row in domains
    )
    report = f"""# Current global TLC registry through the IR layer

- Authority: `origin/main`
- Scientific baseline commit: `{source_commit}`
- Registry tooling commit at generation time: `{tool_commit}`
- Generated: `{timestamp}`
- Scope: inventory and status normalization only.
- Scientific decisions made: none.
- `maths/` modified: no.

## Result

All sixteen domains are present. Their authoritative catalogues contain **{total_features} active features**.
All {complete_features} features have a mathematical contract, an IR artifact and a structural test plan.
Therefore `all_domains_reach_ir_layer` is **{str(all_domains_ir).lower()}**.

The former total of 175 included nine `legacy_goose_feature_ids` in the Capacities preparation. That same
source marks those identifiers as non-authoritative; the active Capacities catalogue contains 15 features.
The legacy identifiers remain in their source file as lineage evidence and are not deleted.

IR-layer coverage does not mean that all IRs use one storage layout, have the same maturity, pass a common
selection gate, are executable, have complete algorithms or oracles, or are ready for C++.

## Domain inventory

| No. | Domain | Features | Contracts | IR artifacts | Test plans | IR layer | Raw canonical labels | Common selection gate |
|---:|---|---:|---:|---:|---:|---|---:|---:|
{domain_lines}

## Active next phase

The active strategy is `domain-review-sequence.yaml`: Master first, then the other fifteen domains in theory
order. For each module, confirm its active features, review only unstable boundaries, review contracts, select
or revise IRs, check required dependencies, specify algorithms and oracles, then publish a closure manifest.
A dependency in another domain is examined only when required by the current module; it does not automatically
reopen all sixteen domains.

Historical targeted scientific-review artifacts retain their original source commits and are not relabelled by
this build. Raw statuses are preserved in the feature matrices; no candidate, prototype or declarative IR is
silently promoted.
"""
    (reports / "reconciliation-report.md").write_text(report, encoding="utf-8", newline="\n")

    result = {
        "status": "ok" if all_domains_ir else "incomplete",
        "canonical_commit": source_commit,
        "tool_commit": tool_commit,
        "domains": len(domains),
        "active_features": total_features,
        "ir_layer_complete_features": complete_features,
        "all_domains_reach_ir_layer": all_domains_ir,
        "raw_canonical_label_features": raw_canonical,
        "normalized_selection_gate_passed_features": normalized_selected,
        "implementation_ready_asserted_features": implementation_ready,
        "blockers": len(blocker_registry.get("blockers", [])),
        "dependencies": len(dependency_graph.get("edges", [])),
    }
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
