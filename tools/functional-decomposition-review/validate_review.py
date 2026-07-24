#!/usr/bin/env python3
"""Deterministic validation for the functional-decomposition review."""
from __future__ import annotations

import subprocess
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reviews" / "functional-decomposition"
ALLOWED = {"ACCEPT_FOR_MATH_CONTRACT", "ACCEPT_WITH_RESERVATIONS", "REVISE_FEATURE_BOUNDARY", "REQUIRES_TARGETED_EXTRACTION", "REQUIRES_SCIENTIFIC_DECISION", "REJECT_AS_SOFTWARE_FEATURE"}
WORK_ITEM_ID = "TLC-FUNCTIONAL-DECOMPOSITION-REVIEW-001"


def read(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    required = ["scientific-review.yaml", "accepted-for-contract.yaml", "revision-required.yaml", "dependency-audit.yaml", "boundary-review.yaml", "variant-review.md", "contract-waves.yaml", "review-issues.yaml", "scientific-review-report.md", "decision_required.yaml"]
    require(all((OUT / n).is_file() for n in required), "missing output file")
    # Parsing every YAML is itself part of validation.
    yaml_docs = {p.name: read(p) for p in OUT.glob("*.yaml")}
    source = read(ROOT / "registry/features/feature-candidates.yaml")
    source_deps = read(ROOT / "registry/features/dependency-hints.yaml")
    reviews = yaml_docs["scientific-review.yaml"]["features"]
    require(yaml_docs["scientific-review.yaml"]["work_item_id"] == WORK_ITEM_ID, "incorrect work item ID")
    decision = yaml_docs["decision_required.yaml"]
    require(decision["work_item_id"] == WORK_ITEM_ID, "decision uses incorrect work item ID")
    previous = decision["human_decision_from_previous_stage"]
    require(previous["status"] == "approved_with_reservations", "previous-stage decision not preserved")
    require("No dependency is normative." in previous["comments"], "dependency non-normativity not preserved")
    ids = [r["feature_candidate_id"] for r in reviews]
    require(len(ids) == len(set(ids)) == 224, "224 feature IDs must appear exactly once")
    require(set(ids) == {f["candidate_feature_id"] for f in source["features"]}, "review/source feature mismatch")
    require(all(r["review_status"] in ALLOWED for r in reviews), "invalid review status")
    ready = {f["candidate_feature_id"] for f in source["features"] if f["readiness"]["status"] == "ready_for_math_contract"}
    require(len(ready) == 69 and ready <= set(ids), "all 69 ready features must be reviewed")
    for r in reviews:
        if r["feature_candidate_id"] in ready:
            require(r["input_output_justification"]["inputs"] and r["input_output_justification"]["outputs"], "ready feature lacks candidate I/O")
            require(r["testability_assessment"]["strategies"], "ready feature lacks test strategy")
        if r["review_status"] in {"ACCEPT_FOR_MATH_CONTRACT", "ACCEPT_WITH_RESERVATIONS"}:
            require(r["source_evidence"], "accepted feature lacks scientific evidence")
            require(r["input_output_justification"]["inputs"] and r["input_output_justification"]["outputs"], "accepted feature lacks I/O")
            require(r["testability_assessment"]["strategies"], "accepted feature lacks test strategy")
        require(r["status"] == "candidate", "review artifact marked other than candidate")
    boundaries = yaml_docs["boundary-review.yaml"]["boundary_issues"]
    require(len(boundaries) == 17 and len({b["boundary_issue_id"] for b in boundaries}) == 17, "17 boundaries required")
    variant_text = (OUT / "variant-review.md").read_text(encoding="utf-8")
    require(all(name in variant_text for name in ("minimal", "balanced", "fine")), "three variants not compared")
    deps = yaml_docs["dependency-audit.yaml"]["dependencies"]
    require(len(deps) == len(source_deps["dependencies"]) == 1365, "all dependencies must be audited")
    ready_linked = {d["dependency_candidate_id"] for d in source_deps["dependencies"] if d["from_feature"] in ready or d["to_feature"] in ready}
    full = {d["dependency_candidate_id"] for d in deps if d["evidence"]["review_scope"] == "full"}
    require(ready_linked == full, "every ready-linked dependency must receive full review")
    issues = yaml_docs["review-issues.yaml"]["review_issues"]
    require(all(i["severity"] in {"critical", "major", "minor"} for i in issues), "issue without valid severity")
    # Ensure no generated YAML contains an approved artifact status.
    require(all("status: approved\n" not in p.read_text(encoding="utf-8") for p in OUT.glob("*.yaml")), "approved artifact found")
    # Generated changes must not touch prohibited scientific/decomposition paths.
    changed = subprocess.run(["git", "diff", "--name-only", "--cached"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()
    prohibited = ("maths/", "algorithms/", "registry/scientific-objects/", "registry/features/", "registry/functional-decomposition/", "reports/functional-decomposition/", "reports/functional-decomposition-input/")
    require(not any(p.startswith(prohibited) for p in changed), "staged prohibited file modified")
    require(source.get("count") == 224 and source_deps.get("count") == 1365, "registry counts inconsistent")
    print("VALID: 224 features; 69 ready detailed; 17 boundaries; 3 variants; 1365 dependencies; YAML readable")


if __name__ == "__main__":
    main()
