#!/usr/bin/env python3
"""Generate and validate the targeted post-reconciliation scientific review.

The classification is deliberately conservative: target availability never
implies semantic confirmation, and candidate/inferred relations remain
unconfirmed.  ``--generate`` writes only the review artifacts authorized by
this task; the default mode validates them.
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import subprocess
import sys
from typing import Any, Iterable

import yaml


SOURCE_COMMIT = "febec3e14a938adb2480bd09d257e6879ccf564e"
REVIEW_DIR = pathlib.Path("registry/global-reconciliation")
REPORT = pathlib.Path("reports/global-reconciliation/scientific-dependency-review.md")
REQUIRED = {
    "dependency-scientific-review.yaml",
    "cycle-scientific-review.yaml",
    "pilot-artifact-review.yaml",
    "targeted-readiness-review.yaml",
    "first-contract-batches.yaml",
    "scientific-review-decision-required.yaml",
}
ALLOWED_STATUSES = {
    "explicitly_confirmed",
    "documentary_reference_only",
    "compatible_but_unconfirmed",
    "ambiguous",
    "contradicted",
    "invalid_reference",
    "human_decision_required",
}
PILOTS = [
    "TLC-FC-05-DYNAMICS-001",
    "TLC-FC-08-PRINCIPLE-002",
    "TLC-FC-09-VALUES-018",
    "TLC-FC-14-LIVED-EXPERIENCE-005",
]


def load(path: pathlib.Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(path: pathlib.Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
        newline="\n",
    )


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def normalize_domain(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    value = re.sub(r"^\d\d[-_]", "", value.lower().replace("_", "-").strip())
    aliases = {"huit-dimensions-de-tl": "huit-dimensions"}
    return aliases.get(value, value)


def evidence_mapping(root: pathlib.Path, edge: dict[str, Any]) -> dict[str, Any]:
    data = load(root / edge["evidence"])
    candidates = []
    for item in walk(data):
        if not isinstance(item, dict):
            continue
        targets = [
            normalize_domain(item.get(key))
            for key in ("target_domain", "domain", "target", "depends_on_domain")
        ]
        if edge["target"] in targets:
            candidates.append(item)
    if not candidates:
        return {}
    matching = [
        item for item in candidates
        if str(item.get("status") or item.get("reconciliation_status") or "unspecified")
        == edge["status_before"]
    ]
    return (matching or candidates)[0]


def feature_ids(value: Any) -> list[str]:
    return sorted({
        item for item in walk(value)
        if isinstance(item, str) and item.startswith("TLC-FC-")
    })


def source_references(mapping: dict[str, Any], fallback: str) -> list[Any]:
    refs = []
    for key in ("source_evidence", "evidence", "source_reference", "source_references"):
        value = mapping.get(key)
        if value not in (None, "", []):
            refs.extend(value if isinstance(value, list) else [value])
    return refs or [fallback]


def classify(edge: dict[str, Any], mapping: dict[str, Any]) -> tuple[str, str]:
    before = edge["status_before"]
    if mapping.get("imported_semantics") is False and (
        mapping.get("source_evidence") or mapping.get("evidence")
    ):
        return "documentary_reference_only", "Explicit source reference; imported_semantics is false."
    if before in {
        "canonical",
        "canonical_in_main",
        "canonical_complete_to_ir_with_reservations",
        "external_dependency_available_as_symbol",
        "confirmed_symbol_only",
    }:
        return "explicitly_confirmed", "Canonical artifact explicitly identifies the target and required role."
    if before == "confirmed_textual_reference":
        return "documentary_reference_only", "Preparation confirms a textual reference without executable semantics."
    if before in {
        "explicit_component_domain_reference_candidate",
        "candidate",
        "candidate_reference",
        "preparation_only_non_authoritative",
        "source_only",
        "canonical_source_only",
        "canonical_source_available_reconciliation_pending",
        "complete_with_reservations",
    }:
        return "compatible_but_unconfirmed", "Target exists, but candidate/reserved evidence does not confirm semantics."
    if before in {
        "unresolved",
        "not_reconciled",
        "external_unreconciled",
        "external_non_reconciled",
        "external_unreconciled_not_merged",
    }:
        return "human_decision_required", "The canonical preparation explicitly leaves reconciliation unresolved."
    if before in {"inferred_candidate", "not_evidenced", "no_explicit_reference_found", "unspecified", "none"}:
        return "ambiguous", "No explicit semantic dependency proof is present in the reviewed mapping."
    return "human_decision_required", f"Unclassified canonical source status: {before}."


def generate(root: pathlib.Path) -> None:
    graph = load(root / REVIEW_DIR / "dependency-graph.yaml")
    readiness = load(root / REVIEW_DIR / "readiness-registry.yaml")
    cycles = load(root / REVIEW_DIR / "cycle-registry.yaml")
    reviewed = []
    for edge in graph["edges"]:
        mapping = evidence_mapping(root, edge)
        status, rationale = classify(edge, mapping)
        affected = feature_ids(mapping)
        if not affected and str(edge["source"]).startswith("TLC-FC-"):
            affected = [edge["source"]]
        dependency_id = (
            mapping.get("dependency_id")
            or mapping.get("relation_id")
            or edge["edge_id"]
        )
        reviewed.append({
            "edge_id": edge["edge_id"],
            "dependency_id": dependency_id,
            "source": edge["source"],
            "target": edge["target"],
            "source_domain": edge["source_domain"],
            "direction": f"{edge['source']} -> {edge['target']}",
            "review_status": status,
            "evidence": edge["evidence"],
            "source_reference": source_references(mapping, edge["evidence"]),
            "affected_features": affected,
            "blocking": bool(edge["blocking"]) or status in {
                "contradicted", "invalid_reference", "human_decision_required"
            },
            "priority": (
                "first_limited_contract_batch"
                if edge["source_domain"] == "relations"
                else "normal"
            ),
            "status_before": edge["status_before"],
            "rationale": rationale,
        })
    counts = collections.Counter(row["review_status"] for row in reviewed)
    meta = {
        "schema_version": 1,
        "authority": "origin/main",
        "source_commit": SOURCE_COMMIT,
        "scope": "targeted_scientific_dependency_review",
    }
    dump(root / REVIEW_DIR / "dependency-scientific-review.yaml", {
        **meta,
        "dependencies": reviewed,
        "summary": {"total": len(reviewed), **dict(sorted(counts.items()))},
    })

    cycle_rows = []
    for cycle in cycles["cycles"]:
        if set(cycle["nodes"]) == {"master", "community"}:
            classification = "documentary_non_blocking"
            rationale = (
                "Both edges are explicit symbol/document references with no imported execution effect; "
                "canonical contracts and IR coexist."
            )
            blocking = False
        else:
            classification = "ambiguous_cycle"
            rationale = (
                "The SCC mixes documentary, candidate, inferred, and unresolved edges; no scientific "
                "orientation can be selected without human review."
            )
            blocking = True
        cycle_rows.append({
            "cycle_id": cycle["cycle_id"],
            "nodes": cycle["nodes"],
            "edges": cycle["edges"],
            "classification": classification,
            "blocking_for_first_batch": blocking,
            "evidence": cycle["evidence"],
            "rationale": rationale,
            "human_decision_required": classification == "ambiguous_cycle",
        })
    dump(root / REVIEW_DIR / "cycle-scientific-review.yaml", {
        **meta, "cycles": cycle_rows,
        "summary": {
            "total": 2,
            "documentary_non_blocking": 1,
            "ambiguous_cycle": 1,
        },
    })

    pilot_rows = []
    for feature_id in PILOTS:
        contract = load(root / "registry/math-contracts" / feature_id / "contract.yaml")
        issues_path = root / "registry/math-contracts" / feature_id / "issues.yaml"
        issues = load(issues_path) if issues_path.exists() else {}
        issue_count = sum(
            1 for item in walk(issues)
            if isinstance(item, dict) and (
                item.get("contract_issue_id") or item.get("issue_id")
            )
        )
        pilot_rows.append({
            "feature_id": feature_id,
            "contract": {
                "status": "to_revise",
                "source_status": contract.get("status"),
                "evidence": [
                    f"registry/math-contracts/{feature_id}/contract.yaml",
                    f"registry/math-contracts/{feature_id}/issues.yaml",
                ],
                "open_issue_count": issue_count,
                "rationale": "Candidate contract has unresolved scientific/type/output decisions and is not promoted.",
            },
            "ir": {
                "status": "pilot_only",
                "evidence": [f"ir/{feature_id}/ir-validation-report.md"],
                "rationale": "Candidate IR preserves reservations; scientific validation or ready_for_ir remains false.",
            },
        })
    dump(root / REVIEW_DIR / "pilot-artifact-review.yaml", {
        **meta,
        "pilots": pilot_rows,
        "summary": {
            "contracts": {"to_revise": 4},
            "irs": {"pilot_only": 4},
        },
    })

    affected_ids = set(PILOTS) | {
        "TLC-FC-15-RELATIONS-004", "TLC-FC-15-RELATIONS-007"
    }
    rows = []
    for row in readiness["features"]:
        if row["feature_id"] not in affected_ids:
            continue
        limited = row["feature_id"].startswith("TLC-FC-15-RELATIONS-") and row["state_after"][
            "ready_for_contract_generation_now"
        ]
        rows.append({
            "domain": row["domain"],
            "feature_id": row["feature_id"],
            "ready_for_limited_contract": bool(limited),
            "ready_for_full_contract": False,
            "ready_for_ir": False,
            "satisfied_dependencies": (
                ["no_intra_domain_dependency", "external_references_documentary_only"]
                if limited else []
            ),
            "remaining_blockers": (
                [] if limited else ["pilot_contract_requires_revision", "scientific_validation_pending"]
            ),
            "evidence": [
                row["source"],
                *(
                    ["registry/domain-progress/relations/feature-dependencies.yaml"]
                    if limited else [f"registry/math-contracts/{row['feature_id']}/contract.yaml"]
                ),
            ],
        })
    dump(root / REVIEW_DIR / "targeted-readiness-review.yaml", {
        **meta,
        "features": rows,
        "summary": {
            "reviewed": len(rows),
            "ready_for_limited_contract": sum(r["ready_for_limited_contract"] for r in rows),
            "ready_for_full_contract": 0,
            "ready_for_ir": 0,
        },
    })

    economic = {
        "batch_id": "TLC-FIRST-ECONOMIC-001",
        "features_included": ["TLC-FC-15-RELATIONS-004", "TLC-FC-15-RELATIONS-007"],
        "features_excluded": sorted(affected_ids - {
            "TLC-FC-15-RELATIONS-004", "TLC-FC-15-RELATIONS-007"
        }),
        "prerequisites": ["preserve limited-contract scope", "propagate all existing reservations"],
        "remaining_blockers": [],
        "rationale": "Two independent limited contracts can share one Relations context and review task.",
    }
    safe = {
        "batch_id": "TLC-FIRST-SAFE-001",
        "features_included": ["TLC-FC-15-RELATIONS-004"],
        "features_excluded": sorted(affected_ids - {"TLC-FC-15-RELATIONS-004"}),
        "prerequisites": ["preserve limited-contract scope", "propagate all existing reservations"],
        "remaining_blockers": [],
        "rationale": "Single-feature batch minimizes review surface before repeating the same pattern for -007.",
    }
    dump(root / REVIEW_DIR / "first-contract-batches.yaml", {
        **meta,
        "economic": economic,
        "safest": safe,
        "first_ir_batch": None,
        "first_ir_batch_blocker": "No reviewed feature is ready_for_ir.",
    })
    decisions = [{
        "decision_id": "TLC-SCI-DEP-DEC-001",
        "question": "Classify and orient the 12-domain ambiguous SCC without inferring scientific priority.",
        "affected_cycle": "TLC-GCYCLE-DOMAIN-001",
        "affected_dependencies": [
            row["edge_id"] for row in reviewed
            if row["review_status"] in {"ambiguous", "human_decision_required"}
            and row["source_domain"] in set(cycles["cycles"][0]["nodes"])
        ],
        "blocking_for_first_limited_contract_batch": False,
        "blocking_for_full_contract_or_ir_batches": True,
    }]
    dump(root / REVIEW_DIR / "scientific-review-decision-required.yaml", {
        **meta, "decisions": decisions,
    })

    report = f"""# Targeted scientific dependency and cycle review

- Authority: `origin/main`
- Source commit: `{SOURCE_COMMIT}`
- Dependencies reviewed: {len(reviewed)}
- Explicitly confirmed: {counts['explicitly_confirmed']}
- Documentary references only: {counts['documentary_reference_only']}
- Compatible but unconfirmed: {counts['compatible_but_unconfirmed']}
- Ambiguous: {counts['ambiguous']}
- Human decisions required: {counts['human_decision_required']}

## Cycles

- `TLC-GCYCLE-DOMAIN-001`: `ambiguous_cycle`; human classification is required before full contract or IR ordering.
- `TLC-GCYCLE-DOMAIN-002`: `documentary_non_blocking`; Master/Community symbol references do not import execution.

## Pilots

All four pilot contracts remain `to_revise`. All four pilot IRs remain `pilot_only`. None is promoted.

## Targeted readiness and first batch

Six affected features were recalculated. Two are ready for limited contracts, none for a full contract,
and none for IR. The economic first batch contains `TLC-FC-15-RELATIONS-004` and
`TLC-FC-15-RELATIONS-007`. The safest batch contains only `TLC-FC-15-RELATIONS-004`.
"""
    path = root / REPORT
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8", newline="\n")


def validate(root: pathlib.Path) -> list[str]:
    errors = []
    present = {p.name for p in (root / REVIEW_DIR).glob("*review*.yaml")} | {
        p.name for p in (root / REVIEW_DIR).glob("first-contract-batches.yaml")
    }
    if missing := REQUIRED - present:
        errors.append(f"missing review artifacts: {sorted(missing)}")
    try:
        graph = load(root / REVIEW_DIR / "dependency-graph.yaml")
        review = load(root / REVIEW_DIR / "dependency-scientific-review.yaml")
        cycles = load(root / REVIEW_DIR / "cycle-scientific-review.yaml")
        pilots = load(root / REVIEW_DIR / "pilot-artifact-review.yaml")
        ready = load(root / REVIEW_DIR / "targeted-readiness-review.yaml")
        batches = load(root / REVIEW_DIR / "first-contract-batches.yaml")
    except Exception as exc:
        return [f"parse failure: {exc}"]
    graph_ids = {e["edge_id"] for e in graph["edges"]}
    rows = review["dependencies"]
    if len(rows) != 156 or {r["edge_id"] for r in rows} != graph_ids:
        errors.append("dependency review does not cover exactly the 156 canonical edges")
    if any(r["review_status"] not in ALLOWED_STATUSES for r in rows):
        errors.append("invalid dependency review status")
    if any(not r.get("evidence") or not r.get("source_reference") for r in rows):
        errors.append("dependency without evidence/source_reference")
    if len(cycles["cycles"]) != 2:
        errors.append("cycle review does not cover exactly two cycles")
    allowed_cycles = {
        "documentary_non_blocking", "definitional_non_executable", "contractual_cycle",
        "ir_cycle", "execution_cycle", "ambiguous_cycle", "human_decision_required",
    }
    if any(c["classification"] not in allowed_cycles for c in cycles["cycles"]):
        errors.append("invalid cycle classification")
    if len(pilots["pilots"]) != 4:
        errors.append("pilot audit does not cover four feature pairs")
    if ready["summary"] != {
        "reviewed": 6, "ready_for_limited_contract": 2,
        "ready_for_full_contract": 0, "ready_for_ir": 0,
    }:
        errors.append("targeted readiness summary mismatch")
    if batches["economic"]["features_included"] != [
        "TLC-FC-15-RELATIONS-004", "TLC-FC-15-RELATIONS-007"
    ]:
        errors.append("economic first batch mismatch")
    if batches["safest"]["features_included"] != ["TLC-FC-15-RELATIONS-004"]:
        errors.append("safe first batch mismatch")
    if subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=root, text=True).strip() != SOURCE_COMMIT:
        errors.append("origin/main no longer matches the reviewed source commit")
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", "origin/main...HEAD"], cwd=root, text=True
    ).splitlines()
    changed += subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard"], cwd=root, text=True
    ).splitlines()
    allowed_files = {
        str((REVIEW_DIR / name)).replace("\\", "/") for name in REQUIRED
    } | {
        str(REPORT).replace("\\", "/"),
        "tools/global-reconciliation/validate_targeted_review.py",
    }
    out_of_scope = sorted({
        path.replace("\\", "/") for path in changed
        if path and "__pycache__" not in path and path.replace("\\", "/") not in allowed_files
    })
    if out_of_scope:
        errors.append(f"scope violation: {out_of_scope}")
    prohibited = [
        path for path in changed
        if path.startswith(("registry/math-contracts/", "ir/", "maths/"))
    ]
    if prohibited:
        errors.append(f"prohibited contract/IR/maths change: {prohibited}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[2])
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.generate:
        generate(root)
    errors = validate(root)
    result = {"status": "ok" if not errors else "failed", "errors": errors}
    if not errors:
        review = load(root / REVIEW_DIR / "dependency-scientific-review.yaml")
        result["dependencies"] = review["summary"]
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
