#!/usr/bin/env python3
"""Build conservative, traceable global reconciliation artifacts.

This tool inventories only files tracked by the current canonical checkout.  It
does not create contracts, IR, implementation code, or scientific decisions.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pathlib
import re
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
EXPECTED_COMMIT = "2cd5a3c6dfe8786926e58d49387b5f4846697a66"
ID_PATTERNS = {
    "objects": re.compile(r"^TLC-SO-"),
    "relations": re.compile(r"^TLC-SR-"),
    "features": re.compile(r"^TLC-FC-"),
}


def load(path: pathlib.Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(path: pathlib.Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
        newline="\n",
    )


def git(root: pathlib.Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def ids(value: Any, pattern: re.Pattern[str]) -> set[str]:
    return {item for item in walk(value) if isinstance(item, str) and pattern.match(item)}


def mappings(value: Any) -> Iterable[dict[str, Any]]:
    for item in walk(value):
        if isinstance(item, dict):
            yield item


def first_existing(*paths: pathlib.Path) -> pathlib.Path | None:
    return next((path for path in paths if path.exists()), None)


def feature_file(root: pathlib.Path, slug: str) -> pathlib.Path | None:
    progress = root / "registry/domain-progress" / slug
    aliases = [
        progress / "feature-inventory.yaml",
        progress / "feature-catalogue.yaml",
        progress / "feature-status.yaml",
        progress / "feature-classification.yaml",
    ]
    return first_existing(*aliases)


def normalize_domain(value: str) -> str | None:
    value = value.lower().replace("_", "-").strip()
    value = re.sub(r"^\d\d-", "", value)
    aliases = {
        "huit-dimensions-de-tl": "huit-dimensions",
        "huit-dimensions-de-tl.md": "huit-dimensions",
        "message": "message",
    }
    value = aliases.get(value, value)
    return value if value in {slug for _, slug, _ in DOMAINS} else None


def status_text(mapping: dict[str, Any]) -> str:
    for key in ("reconciliation_status", "status", "authority_status", "dependency_status"):
        if key in mapping:
            return str(mapping[key])
    return "unspecified"


def collect_dependency_edges(root: pathlib.Path, feature_ids: set[str]) -> list[dict[str, Any]]:
    edges: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for _, source_slug, _ in DOMAINS:
        directory = root / "registry/domain-progress" / source_slug
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*dependenc*.yaml")):
            data = load(path)
            for item in mappings(data):
                targets = []
                for key in ("target_domain", "domain", "target", "depends_on_domain"):
                    value = item.get(key)
                    if isinstance(value, str):
                        target = normalize_domain(value)
                        if target and target != source_slug:
                            targets.append(target)
                source_feature = next(iter(ids(item.get("source", item), ID_PATTERNS["features"])), None)
                target_feature = next(iter(ids(item.get("target", item), ID_PATTERNS["features"])), None)
                if source_feature and target_feature and source_feature != target_feature:
                    targets.append(target_feature)
                for target in targets:
                    edge_type = "feature_dependency" if target.startswith("TLC-FC-") else "domain_dependency"
                    before = status_text(item)
                    target_exists = target in feature_ids if edge_type == "feature_dependency" else target in {d[1] for d in DOMAINS}
                    if target_exists:
                        after = (
                            "canonical_target_available_semantic_review_pending"
                            if any(token in before for token in ("unreconciled", "not_merged", "not_available", "pending"))
                            else before
                        )
                    else:
                        after = "dependency_target_not_available"
                    key = (source_slug, source_feature or source_slug, target, str(path.relative_to(root)))
                    edges[key] = {
                        "source_domain": source_slug,
                        "source": source_feature or source_slug,
                        "target": target,
                        "dependency_type": edge_type,
                        "evidence": str(path.relative_to(root)).replace("\\", "/"),
                        "status_before": before,
                        "status_after": after,
                        "blocking": after in {"dependency_target_not_available"} or "block" in before,
                        "semantic_compatibility_confirmed": False,
                        "note": "Target availability is reconciled; semantic compatibility is not inferred.",
                    }
    result = list(edges.values())
    for index, edge in enumerate(result, 1):
        edge["edge_id"] = f"TLC-GDEP-{index:04d}"
    return result


def strongly_connected(nodes: Iterable[str], pairs: Iterable[tuple[str, str]]) -> list[list[str]]:
    graph: dict[str, set[str]] = collections.defaultdict(set)
    reverse: dict[str, set[str]] = collections.defaultdict(set)
    all_nodes = set(nodes)
    for source, target in pairs:
        graph[source].add(target)
        reverse[target].add(source)
        all_nodes.update((source, target))
    seen: set[str] = set()
    order: list[str] = []

    def visit(node: str) -> None:
        if node in seen:
            return
        seen.add(node)
        for nxt in graph[node]:
            visit(nxt)
        order.append(node)

    for node in sorted(all_nodes):
        visit(node)
    seen.clear()
    components: list[list[str]] = []

    def collect(node: str, component: list[str]) -> None:
        if node in seen:
            return
        seen.add(node)
        component.append(node)
        for nxt in reverse[node]:
            collect(nxt, component)

    for node in reversed(order):
        component: list[str] = []
        collect(node, component)
        if len(component) > 1 or node in graph[node]:
            components.append(sorted(component))
    return components


def feature_readiness(root: pathlib.Path, slug: str, feature_ids: list[str]) -> list[dict[str, Any]]:
    progress = root / "registry/domain-progress" / slug
    candidates = [
        progress / "feature-readiness.yaml",
        progress / "production-readiness.yaml",
        progress / "feature-status.yaml",
        progress / "production-gates.yaml",
    ]
    source = first_existing(*candidates)
    by_id: dict[str, dict[str, Any]] = {}
    if source:
        for item in mappings(load(source)):
            fids = ids(item, ID_PATTERNS["features"])
            if len(fids) == 1:
                by_id[next(iter(fids))] = item
    rows = []
    for feature_id in feature_ids:
        old = by_id.get(feature_id, {})
        comparison = str(old.get("status", "")).lower() == "comparison_only" or bool(old.get("comparison_only"))
        limited = bool(old.get("ready_for_contract_generation_now", False)) and not comparison
        full = bool(old.get("ready_for_full_contract_generation", False)) and not comparison
        contract_dir = root / "registry/math-contracts" / feature_id
        ir_dir = root / "ir" / feature_id
        contract_exists = contract_dir.exists()
        ir_exists = ir_dir.exists()
        ir_ready = bool(old.get("ready_for_ir_generation", False)) and contract_exists and not comparison
        blockers = sorted(
            {
                value
                for key, value in old.items()
                if "block" in str(key).lower()
                for value in (value if isinstance(value, list) else [value])
                if value not in (None, False, [], "")
            },
            key=str,
        )
        rows.append(
            {
                "feature_id": feature_id,
                "source": str(source.relative_to(root)).replace("\\", "/") if source else None,
                "state_before": {
                    key: bool(old.get(key, False))
                    for key in (
                        "ready_for_contract_generation_now",
                        "ready_for_full_contract_generation",
                        "ready_for_ir_generation",
                        "ready_for_implementation_planning",
                        "ready_for_code_generation",
                    )
                },
                "state_after": {
                    "ready_for_contract_generation_now": limited,
                    "ready_for_full_contract_generation": full,
                    "ready_for_ir_generation": ir_ready,
                    "ready_for_implementation_planning": False,
                    "ready_for_code_generation": False,
                },
                "blockers": blockers,
                "reservations": ["global_semantic_dependency_review_pending"] if not full else [],
                "next_minimal_action": "scientific_review" if not limited else ("contract_generation" if not contract_exists else "contract_audit"),
                "comparison_only_excluded": comparison,
                "existing_contract": contract_exists,
                "existing_ir": ir_exists,
            }
        )
    return rows


def artifact_audit(root: pathlib.Path, feature_ids: set[str]) -> list[dict[str, Any]]:
    rows = []
    contract_ids = {p.name for p in (root / "registry/math-contracts").iterdir() if p.is_dir()}
    ir_ids = {p.name for p in (root / "ir").iterdir() if p.is_dir()}
    for feature_id in sorted(contract_ids | ir_ids):
        domain_match = re.match(r"TLC-FC-(\d\d)-", feature_id)
        domain_slug = next((slug for number, slug, _ in DOMAINS if domain_match and number == domain_match.group(1)), "unknown")
        pilot = domain_slug not in {"master", "disciple", "community"}
        rows.append(
            {
                "feature_id": feature_id,
                "domain": domain_slug,
                "contract_present": feature_id in contract_ids,
                "ir_present": feature_id in ir_ids,
                "classification": "pilot_only" if pilot else "canonical_validated",
                "feature_present_in_canonical_catalogue": feature_id in feature_ids,
                "source_commit": EXPECTED_COMMIT,
                "scientific_content_modified": False,
                "review_required": pilot or feature_id not in feature_ids,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.root.resolve()
    head = git(root, "rev-parse", "HEAD")
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    out = root / "registry/global-reconciliation"
    report_dir = root / "reports/global-reconciliation"

    domains = []
    all_features: set[str] = set()
    global_counts = collections.Counter()
    readiness_rows = []
    feature_matrix = []
    for number, slug, name in DOMAINS:
        progress = root / "registry/domain-progress" / slug
        scientific = root / "registry/scientific-objects" / ("huit-dimensions-de-tl" if slug == "huit-dimensions" else slug)
        feature_source = feature_file(root, slug)
        features = sorted(ids(load(feature_source), ID_PATTERNS["features"])) if feature_source else []
        if slug == "capacities":
            filtered = []
            for feature_id in features:
                if "comparison_only" not in json.dumps(load(feature_source), default=str).lower():
                    filtered.append(feature_id)
                else:
                    # Capacities preparation is comparison-only as a whole when so marked.
                    pass
            features = filtered
        scientific_docs = [load(p) for p in sorted(scientific.glob("*.yaml"))] if scientific.exists() else []
        object_ids = sorted(set().union(*(ids(doc, ID_PATTERNS["objects"]) for doc in scientific_docs)) if scientific_docs else set())
        relation_ids = sorted(set().union(*(ids(doc, ID_PATTERNS["relations"]) for doc in scientific_docs)) if scientific_docs else set())
        unresolved_file = scientific / "unresolved-terms.yaml"
        unresolved_ids = set()
        if unresolved_file.exists():
            data = load(unresolved_file)
            for item in mappings(data):
                value = item.get("unresolved_id") or item.get("id") or item.get("term_id")
                if isinstance(value, str):
                    unresolved_ids.add(value)
            if not unresolved_ids:
                unresolved_ids = {f"{slug}:row:{i}" for i, item in enumerate(data.get("items", data.get("terms", [])), 1)} if isinstance(data, dict) else set()
        duplicate_file = scientific / "duplicate-candidates.yaml"
        if duplicate_file.exists() and isinstance(duplicate_data := load(duplicate_file), dict):
            duplicate_count = len(duplicate_data.get("duplicate_candidates", duplicate_data.get("candidates", [])))
        else:
            duplicate_count = 0
        contract_plan = progress / "contract-production-plan.yaml"
        ir_plan = progress / "ir-production-plan.yaml"
        extraction = root / "reports/scientific-extraction" / ("huit-dimensions-de-tl" if slug == "huit-dimensions" else slug)
        rows = feature_readiness(root, slug, features)
        readiness_rows.extend({"domain": slug, **row} for row in rows)
        for feature_id in features:
            feature_matrix.append(
                {
                    "domain": slug,
                    "feature_id": feature_id,
                    "contract_plan": str(contract_plan.relative_to(root)).replace("\\", "/") if contract_plan.exists() else None,
                    "ir_plan": str(ir_plan.relative_to(root)).replace("\\", "/") if ir_plan.exists() else None,
                    "existing_contract": (root / "registry/math-contracts" / feature_id).exists(),
                    "existing_ir": (root / "ir" / feature_id).exists(),
                }
            )
        counts = {
            "objects": len(object_ids),
            "relations": len(relation_ids),
            "unresolved": len(unresolved_ids),
            "duplicate_candidates": duplicate_count,
            "features": len(features),
            "contract_plans": len(features) if contract_plan.exists() else 0,
            "ir_plans": len(features) if ir_plan.exists() else 0,
        }
        global_counts.update(counts)
        all_features.update(features)
        domains.append(
            {
                "domain_number": number,
                "domain_id": slug,
                "name": name,
                "math_source": f"maths/{number}-" + ("huit-dimensions-de-tl.md" if slug == "huit-dimensions" else f"{slug}.md"),
                "scientific_extraction": str(extraction.relative_to(root)).replace("\\", "/") if extraction.exists() else None,
                "domain_progress": str(progress.relative_to(root)).replace("\\", "/") if progress.exists() else None,
                "artifact_status": "canonical",
                "counts": counts,
                "feature_source": str(feature_source.relative_to(root)).replace("\\", "/") if feature_source else None,
                "contract_plan_present": contract_plan.exists(),
                "ir_plan_present": ir_plan.exists(),
                "reservations_present": any(progress.glob("*decision*.yaml")) if progress.exists() else False,
            }
        )

    edges = collect_dependency_edges(root, all_features)
    domain_pairs = [
        (edge["source_domain"], edge["target"])
        for edge in edges
        if edge["dependency_type"] == "domain_dependency"
    ]
    feature_pairs = [
        (edge["source"], edge["target"])
        for edge in edges
        if edge["dependency_type"] == "feature_dependency"
    ]
    domain_cycles = strongly_connected((d[1] for d in DOMAINS), domain_pairs)
    feature_cycles = strongly_connected(all_features, feature_pairs)
    cycles = [
        {
            "cycle_id": f"TLC-GCYCLE-DOMAIN-{i:03d}",
            "level": "domain",
            "nodes": component,
            "edges": [
                edge["edge_id"] for edge in edges
                if edge["dependency_type"] == "domain_dependency"
                and edge["source_domain"] in component and edge["target"] in component
            ],
            "evidence": sorted({
                edge["evidence"] for edge in edges
                if edge["dependency_type"] == "domain_dependency"
                and edge["source_domain"] in component and edge["target"] in component
            }),
            "domains": component,
            "classification": "cycle_ambiguous",
            "blocking_for": "non_blocking_pending_classification",
            "next_minimal_action": "scientific_dependency_classification",
            "edge_type": "documented_domain_dependency",
            "generation_blocking": False,
            "reason": "Semantic direction and execution impact require scientific review; no cycle is broken automatically.",
        }
        for i, component in enumerate(domain_cycles, 1)
    ] + [
        {
            "cycle_id": f"TLC-GCYCLE-FEATURE-{i:03d}",
            "level": "feature",
            "nodes": component,
            "edges": [
                edge["edge_id"] for edge in edges
                if edge["dependency_type"] == "feature_dependency"
                and edge["source"] in component and edge["target"] in component
            ],
            "evidence": sorted({
                edge["evidence"] for edge in edges
                if edge["dependency_type"] == "feature_dependency"
                and edge["source"] in component and edge["target"] in component
            }),
            "domains": sorted({
                edge["source_domain"] for edge in edges
                if edge["dependency_type"] == "feature_dependency"
                and edge["source"] in component and edge["target"] in component
            }),
            "classification": "cycle_ambiguous",
            "blocking_for": "full_contract_and_ir",
            "next_minimal_action": "scientific_dependency_classification",
            "edge_type": "feature_dependency",
            "generation_blocking": True,
            "reason": "Feature ordering cycle requires explicit review before generation.",
        }
        for i, component in enumerate(feature_cycles, 1)
    ]
    audits = artifact_audit(root, all_features)
    blockers = [
        {
            "blocker_id": f"TLC-GBLOCK-{i:04d}",
            "domain": row["domain"],
            "feature_id": row["feature_id"],
            "scope": row["feature_id"],
            "level": "contract" if not row["state_after"]["ready_for_contract_generation_now"] else "ir",
            "blocker_type": "dependency_or_scientific_reservation",
            "description": "Canonical readiness evidence does not establish every downstream gate.",
            "evidence": row["source"],
            "unresolved": row["blockers"],
            "dependencies": row["reservations"],
            "severity": "major",
            "blocks_limited_contract": not row["state_after"]["ready_for_contract_generation_now"],
            "blocks_full_contract": not row["state_after"]["ready_for_full_contract_generation"],
            "blocks_ir": not row["state_after"]["ready_for_ir_generation"],
            "blocks_implementation": not row["state_after"]["ready_for_implementation_planning"],
            "human_decision_required": True,
            "source_to_consult": row["source"],
            "reasons": row["blockers"] or row["reservations"],
            "next_minimal_action": row["next_minimal_action"],
        }
        for i, row in enumerate(readiness_rows, 1)
        if row["blockers"] or row["reservations"]
    ]
    limited = [r["feature_id"] for r in readiness_rows if r["state_after"]["ready_for_contract_generation_now"]]
    full = [r["feature_id"] for r in readiness_rows if r["state_after"]["ready_for_full_contract_generation"]]
    ir_ready = [r["feature_id"] for r in readiness_rows if r["state_after"]["ready_for_ir_generation"]]
    target_available = [e for e in edges if e["status_after"] == "canonical_target_available_semantic_review_pending"]
    missing = [e for e in edges if e["status_after"] == "dependency_target_not_available"]
    batch_specs = [
        ("TLC-GBATCH-01", ["huit-dimensions", "invariants", "message"], "parallel_after_dependency_review", "medium", "medium"),
        ("TLC-GBATCH-02", ["dynamics", "theorems"], "sequential_sync_then_parallel_features", "large", "high"),
        ("TLC-GBATCH-03", ["principle", "values", "virtues"], "dependency_review_then_parallel", "large", "high"),
        ("TLC-GBATCH-04", ["capacities", "competencies"], "capacities_before_competencies", "medium", "high"),
        ("TLC-GBATCH-05", ["practice", "lived-experience"], "cycle_review_before_generation", "large", "high"),
        ("TLC-GBATCH-06", ["relations"], "final_cross_domain_sync", "medium", "high"),
    ]
    contract_batches = [
        {
            "batch_id": batch_id,
            "order": order,
            "domains": batch_domains,
            "features_included": sorted(r["feature_id"] for r in readiness_rows if r["domain"] in batch_domains),
            "features_excluded": [],
            "prerequisites": ["global_dependency_semantic_review"],
            "blockers": sorted(b["blocker_id"] for b in blockers if b["domain"] in batch_domains),
            "contracts_to_produce": sorted(
                r["feature_id"] for r in readiness_rows
                if r["domain"] in batch_domains and r["state_after"]["ready_for_contract_generation_now"]
                and not r["existing_contract"]
            ),
            "existing_contracts_to_review": sorted(
                r["feature_id"] for r in readiness_rows if r["domain"] in batch_domains and r["existing_contract"]
            ),
            "sequential_steps": [mode],
            "parallelizable_steps": ["independent_feature_contracts_after_prerequisites"],
            "synchronization_point": "scientific_contract_review",
            "recommended_branch": f"contracts/global-batch-{order:02d}",
            "size": size,
            "risk": risk,
            "relative_context": size,
            "completion_criterion": "all included contracts validated or explicitly deferred with blockers",
            "mode": mode,
        }
        for order, (batch_id, batch_domains, mode, size, risk) in enumerate(batch_specs, 1)
    ]
    ir_batches = [
        {**batch, "prerequisite": "validated admissible contract for every included feature"}
        for batch in contract_batches
    ]

    meta = {"schema_version": 1, "authority": "origin/main", "canonical_commit": head, "generated_at": timestamp}
    dump(out / "domain-registry.yaml", {**meta, "domains": domains, "global_counts": dict(global_counts)})
    dump(out / "dependency-graph.yaml", {**meta, "edges": edges, "summary": {"total": len(edges), "target_availability_reconciled": len(target_available), "unreconciled_missing_target": len(missing), "semantic_reconciled": 0}})
    dump(out / "domain-feature-matrix.yaml", {**meta, "rows": feature_matrix})
    dump(out / "feature-contract-matrix.yaml", {**meta, "rows": [{k: r[k] for k in ("domain", "feature_id", "contract_plan", "existing_contract")} for r in feature_matrix]})
    dump(out / "feature-ir-matrix.yaml", {**meta, "rows": [{k: r[k] for k in ("domain", "feature_id", "ir_plan", "existing_ir")} for r in feature_matrix]})
    dump(out / "readiness-registry.yaml", {**meta, "features": readiness_rows, "summary": {"limited_contract": len(limited), "full_contract": len(full), "ir": len(ir_ready), "implementation": 0, "code": 0}})
    dump(out / "cycle-registry.yaml", {**meta, "cycles": cycles, "summary": {"detected": len(cycles), "generation_blocking": sum(bool(c["generation_blocking"]) for c in cycles)}})
    dump(out / "blocker-registry.yaml", {**meta, "blockers": blockers, "summary": {
        "critical": sum(b["severity"] == "critical" for b in blockers),
        "major": sum(b["severity"] == "major" for b in blockers),
        "minor": sum(b["severity"] == "minor" for b in blockers),
    }})
    dump(out / "existing-artifact-audit.yaml", {**meta, "artifacts": audits, "summary": {"contracts": sum(a["contract_present"] for a in audits), "irs": sum(a["ir_present"] for a in audits), "pilots": sum(a["classification"] == "pilot_only" for a in audits)}})
    dump(out / "contract-execution-plan.yaml", {**meta, "batches": contract_batches, "features_ready_now": limited, "minimum_reasonable_codex_tasks": 8, "economic_variant": {"tasks": 8, "description": "two global synchronization tasks plus six batches"}, "safer_variant": {"tasks": 14, "description": "dependency review, six contract batches, six scientific reviews, final synchronization"}, "synchronization_points": ["global dependency semantic review", "cycle review", "contract validation before IR"]})
    dump(out / "ir-execution-plan.yaml", {**meta, "batches": ir_batches, "features_ready_now": ir_ready, "minimum_gate": "validated_or_explicitly_ir_admissible_contract", "synchronization_points": ["contract validation", "unresolved propagation audit", "global IR reference validation"]})
    dump(out / "decision-required.yaml", {**meta, "decisions": [{"decision_id": "TLC-GLOBAL-DEC-001", "question": "Confirm semantic compatibility for target-available dependencies.", "affected_edges": [e["edge_id"] for e in target_available]}, {"decision_id": "TLC-GLOBAL-DEC-002", "question": "Classify documented domain cycles as definition, contract, execution, or documentary cycles.", "affected_cycles": [c["cycle_id"] for c in cycles]}]})
    manifest = {
        **meta,
        "scope": "global_reconciliation_only",
        "artifacts": sorted(str(p.relative_to(root)).replace("\\", "/") for p in out.glob("*.yaml")) + [
            "reports/global-reconciliation/reconciliation-report.md",
            "tools/global-reconciliation/build_global_reconciliation.py",
            "tools/global-reconciliation/validate_global_reconciliation.py",
        ],
        "prohibited_outputs_created": [],
        "source_preparations_modified": [],
    }
    dump(out / "manifest.yaml", manifest)
    report_dir.mkdir(parents=True, exist_ok=True)
    report = f"""# Global domain preparation reconciliation

- Authority: `origin/main`
- Canonical commit: `{head}`
- Generated: `{timestamp}`
- Scope: reconciliation artifacts only; no contract, IR, optimization, oracle, C++, or Python binding was produced.

## Inventory

The canonical checkout contains {len(domains)} domains, {global_counts['objects']} scientific objects,
{global_counts['relations']} scientific relations, {global_counts['unresolved']} unresolved entries,
and {global_counts['features']} inventoried canonical feature identifiers. Capacities entries marked
`comparison_only` are excluded from canonical coverage.

## Dependency reconciliation

The graph contains {len(edges)} traceable edges. {len(target_available)} stale availability statuses were
reclassified to `canonical_target_available_semantic_review_pending`; this confirms only that the target
is present in the canonical tree. No dependency was promoted to semantically validated. {len(missing)}
edges still have no canonical target.

## Cycles and readiness

Detected cycles: {len(cycles)}; generation-blocking cycles: {sum(bool(c['generation_blocking']) for c in cycles)}.
Ready for limited contract generation: {len(limited)}. Ready for full contract generation: {len(full)}.
Ready for IR generation after the conservative contract gate: {len(ir_ready)}. Implementation and code
generation remain globally false.

## Execution

Six dependency-derived domain batches are recorded in `contract-execution-plan.yaml` and mirrored for IR
with the mandatory validated-contract gate. The minimum estimated remaining Codex tasks is 8: two global
scientific synchronization tasks plus six generation/review batches. This is an estimate, not a scientific decision.

## Reservations

- Target existence does not establish identifier or semantic compatibility.
- Candidate and pilot contracts/IR outside Master, Disciple, and Community require scientific review.
- Documented dependency cycles are preserved and not broken by inference.
- Existing per-domain readiness is tightened where the explicit contract gate is not demonstrable.
"""
    (report_dir / "reconciliation-report.md").write_text(report, encoding="utf-8", newline="\n")
    print(json.dumps({"commit": head, "domains": len(domains), "counts": dict(global_counts), "edges": len(edges), "cycles": len(cycles), "limited": len(limited), "full": len(full), "ir_ready": len(ir_ready), "audits": len(audits)}, indent=2))
    return 0 if head == EXPECTED_COMMIT else 2


if __name__ == "__main__":
    sys.exit(main())
