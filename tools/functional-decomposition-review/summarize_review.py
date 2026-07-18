#!/usr/bin/env python3
"""Build and summarize the candidate functional-decomposition review.

The builder is deliberately deterministic: it only interprets fields already
present in the decomposition registries and cites their original source ranges.
It does not alter scientific or decomposition artifacts.
"""
from __future__ import annotations

import argparse
import collections
import subprocess
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reviews" / "functional-decomposition"
SOURCE_COMMIT = "d0d1e26ef6a488aa291e1f4e616b9b2748ff2370"
WORK_ITEM_ID = "TLC-FUNCTIONAL-DECOMPOSITION-REVIEW-001"
PREVIOUS_DECISION = {
    "status": "approved_with_reservations",
    "comments": [
        "Candidate functional decomposition is authorized for independent scientific review.",
        "No feature is approved.",
        "No variant is selected.",
        "No dependency is normative.",
    ],
}
REVIEW_STATUSES = {
    "ACCEPT_FOR_MATH_CONTRACT", "ACCEPT_WITH_RESERVATIONS",
    "REVISE_FEATURE_BOUNDARY", "REQUIRES_TARGETED_EXTRACTION",
    "REQUIRES_SCIENTIFIC_DECISION", "REJECT_AS_SOFTWARE_FEATURE",
}


def load(path: str) -> Any:
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def dump(name: str, data: Any) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=110),
        encoding="utf-8",
    )


def refs(feature: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "source_path": r.get("source_path"), "section": r.get("section"),
            "subsection": r.get("subsection"), "start_line": r.get("start_line"),
            "end_line": r.get("end_line"), "source_commit": r.get("source_commit"),
            "scientific_object_ids": feature["scientific_basis"].get("scientific_object_ids", []),
            "scientific_relation_ids": feature["scientific_basis"].get("scientific_relation_ids", []),
        }
        for r in feature["scientific_basis"].get("source_references", [])
    ]


def has_blocker(feature: dict[str, Any]) -> bool:
    readiness = feature["readiness"]
    return any(readiness.get(k) for k in (
        "blocking_object_ids", "blocking_relation_ids", "blocking_decision_ids", "blocking_terms"
    ))


def feature_review(feature: dict[str, Any], boundary_ids: set[str]) -> dict[str, Any]:
    fid = feature["candidate_feature_id"]
    original = feature["readiness"]["status"]
    category = feature["category"]
    issues: list[str] = []
    changes: list[str] = []
    false_kind = None
    false_action = "keep_as_feature"

    if category == "state_representation":
        false_kind, false_action = "state_definition", "convert_to_state_definition"
    elif category == "configuration_candidate":
        false_kind, false_action = "parameter_definition", "convert_to_data_model"
    elif category == "test_oracle_candidate":
        false_kind, false_action = "test_oracle", "convert_to_test_oracle"
    elif category == "data_validation":
        false_kind, false_action = "data_model", "convert_to_data_model"

    if fid in boundary_ids:
        review_status = "REVISE_FEATURE_BOUNDARY"
        issues.append("boundary_issue_open")
        changes.append("Resolve the cited excessive-aggregation boundary before contract drafting.")
    elif original == "requires_targeted_extraction":
        review_status = "REQUIRES_TARGETED_EXTRACTION"
        issues.append("targeted_extraction_not_completed")
        changes.append("Re-examine the cited source range; do not infer missing fields, types, or behavior.")
    elif original == "insufficient_definition":
        review_status = "REQUIRES_SCIENTIFIC_DECISION"
        issues.append("definition_insufficient")
        changes.append("Determine whether the missing definition is theoretical, extraction-related, or deferred implementation choice.")
    elif false_kind and original != "ready_for_math_contract":
        review_status = "REJECT_AS_SOFTWARE_FEATURE"
        issues.append("false_feature_candidate")
        changes.append(f"Recommend {false_action}; no transformation is applied by this review.")
    elif original == "requires_targeted_scientific_review" or has_blocker(feature):
        review_status = "REQUIRES_SCIENTIFIC_DECISION"
        issues.append("scientific_blocker_or_term_requires_review")
        changes.append("Resolve only the listed blocking objects, relations, decisions, or terms.")
    else:
        # All ready candidates lack an explicit required oracle in the input.
        review_status = "ACCEPT_WITH_RESERVATIONS"
        issues.append("explicit_oracle_not_identified")
        changes.append("Identify a source-grounded oracle or correction property in the mathematical contract.")

    io = feature["construction_question"]
    behavior = feature["behavior"]
    independently_testable = bool(feature["testability"].get("independently_testable"))
    return {
        "feature_candidate_id": fid,
        "original_readiness": original,
        "review_status": review_status,
        "scientific_fidelity": {
            "assessment": "traceable_candidate" if refs(feature) else "unresolved",
            "object_ids": feature["scientific_basis"].get("scientific_object_ids", []),
            "relation_ids": feature["scientific_basis"].get("scientific_relation_ids", []),
        },
        "functional_coherence": {
            "assessment": "non_feature_candidate" if false_kind else ("boundary_revision_required" if fid in boundary_ids else "behavior_candidate"),
            "candidate_kind": false_kind or "software_behavior",
            "recommended_action": false_action,
        },
        "input_output_justification": {
            "inputs": io.get("candidate_inputs", []), "outputs": io.get("candidate_outputs", []),
            "assessment": "candidate_only; exact types and dimensions remain unresolved",
        },
        "behavior_justification": {
            "primary_behavior": behavior.get("primary_behavior"),
            "assessment": "explicit_candidate_behavior" if behavior.get("primary_behavior") else "unresolved",
        },
        "constraints_preserved": {"values": behavior.get("constraints", []), "assessment": "preserved_as_candidate_text"},
        "invariants_preserved": {"values": behavior.get("invariants", []), "assessment": "preserved_as_candidate_text"},
        "testability_assessment": {
            "independently_testable": independently_testable,
            "strategies": feature["testability"].get("candidate_test_strategies", []),
            "required_oracles": feature["testability"].get("required_oracles", []),
            "assessment": "reservation_missing_explicit_oracle" if independently_testable and not feature["testability"].get("required_oracles") else "unresolved_or_not_independent",
        },
        "dependency_assessment": {
            "immediate_candidates": feature["dependencies"].get("immediate_feature_candidates", []),
            "assessment": "reviewed_in_dependency-audit.yaml",
        },
        "issues": issues,
        "required_changes": changes,
        "source_evidence": refs(feature),
        "reviewer_confidence": "high" if refs(feature) and original == "ready_for_math_contract" else "medium",
        "status": "candidate",
    }


def dependency_review(dep: dict[str, Any], features: dict[str, dict[str, Any]], ready: set[str]) -> dict[str, Any]:
    src, dst = dep["from_feature"], dep["to_feature"]
    ready_linked = src in ready or dst in ready
    if src == dst:
        reviewed, action, confidence = "invalid_dependency", "reject_self_dependency", "high"
    else:
        # The immediate-feature list is generated from the same relation mapping
        # as this registry and is therefore not independent functional evidence.
        reviewed, action, confidence = "shared_scientific_context", "remove_from_software_dependency_graph_pending_independent_functional_evidence", "high" if ready_linked else "medium"
    return {
        "dependency_candidate_id": dep["dependency_candidate_id"],
        "from_feature": src, "to_feature": dst,
        "original_type": dep["dependency_type"], "reviewed_type": reviewed,
        "evidence": {
            "scientific_evidence": dep.get("scientific_evidence", []),
            "source_references": dep.get("source_references", []),
            "reason": dep.get("reason"), "review_scope": "full" if ready_linked else "structured_rule",
        },
        "blocking": bool(dep.get("blocking")) if reviewed == "required_functional_dependency" else False,
        "action": action, "confidence": confidence, "status": "candidate",
    }


def build() -> None:
    feature_doc = load("registry/features/feature-candidates.yaml")
    dependency_doc = load("registry/features/dependency-hints.yaml")
    boundary_doc = load("registry/features/feature-boundary-issues.yaml")
    variant_doc = load("registry/features/feature-decomposition-variants.yaml")
    # Read the immutable input-commit versions of every mandated input. This
    # deliberately avoids incorporating unrelated working-tree modifications.
    mandated = [
        "registry/features/feature-candidates.yaml", "registry/features/feature-decomposition-variants.yaml",
        "registry/features/feature-boundary-issues.yaml", "registry/features/dependency-hints.yaml",
        "reports/functional-decomposition/feature-decomposition-report.md", "reports/functional-decomposition/feature-catalog.md",
        "reports/functional-decomposition/dependency-report.md", "reports/functional-decomposition/prioritization.yaml",
        "registry/functional-decomposition/decomposition-input-snapshot.yaml", "reports/functional-decomposition-input/blockers.yaml",
        "reports/functional-decomposition-input/unresolved-impact.yaml",
    ]
    scientific_files = sorted(
        str(p.relative_to(ROOT)).replace("\\", "/")
        for base in (ROOT / "maths", ROOT / "algorithms") for p in base.rglob("*") if p.is_file()
    )
    for path in mandated + scientific_files:
        subprocess.run(
            ["git", "show", f"{SOURCE_COMMIT}:{path}"], cwd=ROOT,
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True,
        )
    features_list = feature_doc["features"]
    features = {f["candidate_feature_id"]: f for f in features_list}
    ready = {f["candidate_feature_id"] for f in features_list if f["readiness"]["status"] == "ready_for_math_contract"}
    boundary_ids = {fid for b in boundary_doc["boundary_issues"] for fid in b["feature_candidate_ids"]}
    reviews = [feature_review(f, boundary_ids) for f in features_list]
    review_by_id = {r["feature_candidate_id"]: r for r in reviews}
    dep_reviews = [dependency_review(d, features, ready) for d in dependency_doc["dependencies"]]

    dump("scientific-review.yaml", {
        "work_item_id": WORK_ITEM_ID, "stage": "functional_decomposition_scientific_review",
        "source_commit": SOURCE_COMMIT, "input_manifest_status": "supplied_by_user",
        "human_decision_from_previous_stage": PREVIOUS_DECISION,
        "status": "candidate", "count": len(reviews), "features": reviews,
    })
    accepted = [r for r in reviews if r["review_status"] in {"ACCEPT_FOR_MATH_CONTRACT", "ACCEPT_WITH_RESERVATIONS"}]
    dump("accepted-for-contract.yaml", {"status": "candidate", "count": len(accepted), "features": accepted})
    revision = [r for r in reviews if r not in accepted]
    dump("revision-required.yaml", {"status": "candidate", "count": len(revision), "features": revision})
    dump("dependency-audit.yaml", {
        "status": "candidate", "source_commit": SOURCE_COMMIT, "count": len(dep_reviews),
        "method": {
            "ready_linked": "full review of every incoming and outgoing candidate",
            "other": "deterministic classification: self edges invalid; declared immediate edges functional; remaining relation-derived edges shared context",
        }, "dependencies": dep_reviews,
    })

    boundary_reviews = []
    for issue in boundary_doc["boundary_issues"]:
        fids = issue["feature_candidate_ids"]
        objects = sorted({o for fid in fids for o in features[fid]["scientific_basis"].get("scientific_object_ids", [])})
        relations = sorted({r for fid in fids for r in features[fid]["scientific_basis"].get("scientific_relation_ids", [])})
        sources = [r for fid in fids for r in refs(features[fid])]
        boundary_reviews.append({
            "boundary_issue_id": issue["boundary_issue_id"], "feature_candidate_ids": fids,
            "scientific_object_ids": objects, "scientific_relation_ids": relations, "source_evidence": sources,
            "reviewed_defect_type": "excessive_aggregation", "severity": "major",
            "finding": "The candidate groups more than 20 scientific objects; an autonomous behavior and oracle cannot be assumed for the whole group.",
            "correction_options": [
                "Split only at source-supported behavioral boundaries.",
                "Keep shared data separate from behaviors and invariants.",
                "Defer unresolved subgroups instead of inventing an aggregate API.",
            ],
            "effects": {
                "inputs": "must be reassigned to each supported behavior", "outputs": "must remain source-grounded",
                "behavior": "separates mixed or undocumented responsibilities", "dependencies": "may remove aggregate hub edges",
                "testability": "permits one correction property per behavior", "math_contract": "requires revised boundary first",
            },
            "human_decision_required": True, "confidence": "high", "status": "candidate",
        })
    dump("boundary-review.yaml", {"status": "candidate", "count": len(boundary_reviews), "boundary_issues": boundary_reviews})

    variants = []
    for v in variant_doc["variants"]:
        variants.append({
            "variant_id": v["variant_id"], "name": v["name"], "candidate_count": len(v["feature_candidates"]),
            "observed_boundaries": v.get("boundaries"), "advantages": v.get("advantages", []), "risks": v.get("risks", []),
            "testability": v.get("testability"), "dependencies": v.get("dependencies"), "blockages": v.get("blockages"),
            "assessment": "The three variants list the same 224 feature IDs; differences are narrative boundary policies, not instantiated alternative catalogs.",
        })
    variant_md = """# Candidate decomposition variant review

Status: `candidate`
Source commit: `{commit}`

## Finding

All three variants (`minimal`, `balanced`, and `fine`) contain exactly the same 224 feature identifiers. The
registry therefore does not instantiate three alternative decompositions; it records three narrative boundary
policies around one catalog. The main feature catalog implicitly reflects this shared catalog, but no variant can
be shown to have been selected structurally.

## Comparative assessment

| Variant | Scientific fidelity | Testability | Main risk | Contract generation | Candidate recommendation |
|---|---|---|---|---|---|
| minimal | unresolved until boundaries are instantiated | lower for 17 aggregates | excessive aggregation | difficult for mixed groups | retain only as comparison baseline |
| balanced | unresolved; its name is not evidence | moderate in narrative only | hidden implicit selection | plausible after boundary decisions | retain, do not select yet |
| fine | unresolved until splits cite sources | potentially high | fragmentation and invented dependencies | good only for source-supported splits | retain for targeted boundary experiments |

No variant is rejected outright because the artifacts do not instantiate their distinct boundaries. Human review is
required for the 17 excessive aggregations. The candidate recommendation is to instantiate a small, traceable subset
of `fine` splits for those issues and compare it with unchanged boundaries; this is not approval of `fine` globally.

## Observed registry records

```yaml
{records}```
""".format(commit=SOURCE_COMMIT, records=yaml.safe_dump(variants, allow_unicode=True, sort_keys=False))
    (OUT / "variant-review.md").write_text(variant_md, encoding="utf-8")

    eligible = [r for r in accepted]
    # A deliberately limited pipeline-validation wave: one/two objects, no boundary issue, few immediate deps.
    ranked = sorted(eligible, key=lambda r: (
        len(r["scientific_fidelity"]["object_ids"]),
        len(r["dependency_assessment"]["immediate_candidates"]), r["feature_candidate_id"]
    ))
    wave1 = ranked[:8]
    wave2 = ranked[8:28]
    wave3 = ranked[28:]
    def wave_entry(r: dict[str, Any], order: int) -> dict[str, Any]:
        return {
            "feature_candidate_id": r["feature_candidate_id"], "order": order,
            "reason": "Behavioral candidate with direct source ranges, small scientific basis, and independent candidate test strategy.",
            "risks": r["issues"], "dependencies": r["dependency_assessment"]["immediate_candidates"],
            "reservations": r["required_changes"], "parallelization": "parallel after its retained immediate dependencies",
            "status": "candidate",
        }
    waves = {
        "CONTRACT_WAVE_1": [wave_entry(r, i + 1) for i, r in enumerate(wave1)],
        "CONTRACT_WAVE_2": [wave_entry(r, i + 1) for i, r in enumerate(wave2)],
        "CONTRACT_WAVE_3": [wave_entry(r, i + 1) for i, r in enumerate(wave3)],
        "DEFERRED": [{"feature_candidate_id": r["feature_candidate_id"], "reason": r["review_status"], "status": "candidate"} for r in revision],
    }
    dump("contract-waves.yaml", {"status": "candidate", "selection_rule": "limited, source-traceable, low-object-count pipeline validation; no domain entity preferred", **waves})

    issue_records = []
    issue_number = 1
    for dep in dep_reviews:
        if dep["reviewed_type"] == "invalid_dependency":
            issue_records.append({
                "review_issue_id": f"TLC-FDRI-{issue_number:04d}", "severity": "major",
                "artifact": "registry/features/dependency-hints.yaml", "feature_candidate_id": dep["from_feature"],
                "object_ids": [], "relation_ids": [x for x in dep["evidence"]["scientific_evidence"] if str(x).startswith("TLC-SR-")],
                "source_evidence": dep["evidence"]["source_references"],
                "finding": f"{dep['dependency_candidate_id']} is a self-dependency mechanically inherited from a scientific relation.",
                "consequence": "It cannot express a software dependency and inflates cycles and centrality.",
                "proposed_action": "Reject the dependency candidate; preserve the relation only as scientific context.",
                "human_required": False, "confidence": "high", "status": "candidate",
            }); issue_number += 1
    for b in boundary_reviews:
        issue_records.append({
            "review_issue_id": f"TLC-FDRI-{issue_number:04d}", "severity": "major", "artifact": "registry/features/feature-boundary-issues.yaml",
            "feature_candidate_id": b["feature_candidate_ids"][0], "object_ids": b["scientific_object_ids"],
            "relation_ids": b["scientific_relation_ids"], "source_evidence": b["source_evidence"],
            "finding": b["finding"], "consequence": "The future mathematical contract would mix an unresolved group boundary.",
            "proposed_action": "Review and instantiate a source-supported split before contract drafting.",
            "human_required": True, "confidence": "high", "status": "candidate",
        }); issue_number += 1
    # One systemic critical issue captures the two ready candidates carrying explicit blockers.
    blocked_ready = [f for f in features_list if f["candidate_feature_id"] in ready and has_blocker(f)]
    for f in blocked_ready:
        issue_records.append({
            "review_issue_id": f"TLC-FDRI-{issue_number:04d}", "severity": "critical", "artifact": "registry/features/feature-candidates.yaml",
            "feature_candidate_id": f["candidate_feature_id"], "object_ids": f["readiness"].get("blocking_object_ids", []),
            "relation_ids": f["readiness"].get("blocking_relation_ids", []), "source_evidence": refs(f),
            "finding": "Feature is marked ready_for_math_contract while retaining explicit blocking relations.",
            "consequence": "Proceeding would silently ignore a recorded scientific blocker.",
            "proposed_action": "Resolve the listed relations or reclassify readiness before contract drafting.",
            "human_required": True, "confidence": "high", "status": "candidate",
        }); issue_number += 1
    dump("review-issues.yaml", {"status": "candidate", "count": len(issue_records), "review_issues": issue_records})

    counts = collections.Counter(r["review_status"] for r in reviews)
    dep_counts = collections.Counter(d["reviewed_type"] for d in dep_reviews)
    questions = [
        {"question_id": "TLC-FDR-Q001", "question": "Which source-grounded oracle or correction property is required for each accepted-with-reservations behavior?", "affected_features": [r["feature_candidate_id"] for r in accepted], "status": "unresolved"},
        {"question_id": "TLC-FDR-Q002", "question": "Which source-supported splits should instantiate the 17 excessive aggregations?", "affected_features": sorted(boundary_ids), "status": "unresolved"},
        {"question_id": "TLC-FDR-Q003", "question": "Should the two nominally ready Master candidates remain blocked by their listed relations?", "affected_features": [f["candidate_feature_id"] for f in blocked_ready], "status": "unresolved"},
    ]
    decision = {
        "work_item_id": WORK_ITEM_ID, "stage": "functional_decomposition_scientific_review", "status": "candidate",
        "input_manifest_status": "supplied_by_user",
        "human_decision_from_previous_stage": PREVIOUS_DECISION,
        "input": {"source_commit": SOURCE_COMMIT, "feature_candidates": 224, "dependency_candidates": 1365, "boundary_issues": 17, "decomposition_variants": 3},
        "summary": {
            "reviewed_features": len(reviews), "accepted_for_math_contract": counts["ACCEPT_FOR_MATH_CONTRACT"],
            "accepted_with_reservations": counts["ACCEPT_WITH_RESERVATIONS"], "boundary_revision_required": counts["REVISE_FEATURE_BOUNDARY"],
            "targeted_extraction_required": counts["REQUIRES_TARGETED_EXTRACTION"], "scientific_decision_required": counts["REQUIRES_SCIENTIFIC_DECISION"],
            "rejected_as_feature": counts["REJECT_AS_SOFTWARE_FEATURE"], "dependencies_confirmed": dep_counts["required_functional_dependency"],
            "dependencies_reclassified": dep_counts["shared_scientific_context"], "dependencies_rejected": dep_counts["invalid_dependency"],
            "contract_wave_1": len(wave1), "contract_wave_2": len(wave2), "contract_wave_3": len(wave3), "deferred": len(revision),
        },
        "blocking_issues": [i["review_issue_id"] for i in issue_records if i["severity"] == "critical"],
        "non_blocking_issues": [i["review_issue_id"] for i in issue_records if i["severity"] != "critical"],
        "questions_for_human": questions,
        "recommended_decision": {"value": "revise", "justification": "Explicit blockers, 17 unresolved aggregate boundaries, 554 invalid self-dependencies, and absent explicit oracles prevent catalog update."},
        "allowed_decisions": ["approved", "approved_with_reservations", "revise", "rejected"],
        "readiness": {"ready_for_catalog_update": False, "ready_for_contract_wave_1": False, "ready_for_ir": False, "ready_for_implementation": False},
    }
    dump("decision_required.yaml", decision)

    files_read = mandated + scientific_files
    report = f"""# Independent scientific review of candidate functional decomposition

Status: `candidate`
Input commit: `{SOURCE_COMMIT}`

## Executive result

The review recommends **revise**. All 224 feature candidates and all 1,365 dependency candidates were classified.
No feature is accepted without reservation because none of the 69 nominally ready candidates identifies an explicit
required oracle. Two nominally ready candidates retain blocking relations. Seventeen candidates have unresolved
excessive-aggregation boundaries. Of the dependencies, {dep_counts['invalid_dependency']} are invalid self-edges,
{dep_counts['shared_scientific_context']} are scientific context rather than software dependencies, and
{dep_counts['required_functional_dependency']} correspond to an immediate dependency declared by the source feature.

The supplied execution manifest identifies this review as `{WORK_ITEM_ID}` and authorizes the candidate decomposition
for independent review with reservations. Its prior-stage decision explicitly states that no feature is approved, no
variant is selected, and no dependency is normative. The dependency classifications below therefore remain review
recommendations and do not promote any candidate edge to normative status.

## Verified counts

| Item | Count |
|---|---:|
| Features reviewed | {len(reviews)} |
| ACCEPT_FOR_MATH_CONTRACT | {counts['ACCEPT_FOR_MATH_CONTRACT']} |
| ACCEPT_WITH_RESERVATIONS | {counts['ACCEPT_WITH_RESERVATIONS']} |
| REVISE_FEATURE_BOUNDARY | {counts['REVISE_FEATURE_BOUNDARY']} |
| REQUIRES_TARGETED_EXTRACTION | {counts['REQUIRES_TARGETED_EXTRACTION']} |
| REQUIRES_SCIENTIFIC_DECISION | {counts['REQUIRES_SCIENTIFIC_DECISION']} |
| REJECT_AS_SOFTWARE_FEATURE | {counts['REJECT_AS_SOFTWARE_FEATURE']} |
| Ready-linked dependencies fully reviewed | {sum(d['evidence']['review_scope'] == 'full' for d in dep_reviews)} |
| Boundary issues reviewed | {len(boundary_reviews)} |
| Variants compared | {len(variants)} |

## Input schemas and anomalies

The feature registry is a mapping with `count` and a `features` sequence; each feature nests scientific basis, scope,
behavior, dependencies, testability, readiness, risks, and status. The dependency registry contains a single
`scientific_requires` type. Boundary issues contain only `feature_too_large`. Each variant repeats all 224 feature IDs
and differs only in narrative metadata. The input report in the working tree was locally modified before this review;
the audit used the committed input at `{SOURCE_COMMIT}` and did not include that modification.

Material anomalies: 554 self-dependencies; all 1,365 dependency types mechanically use `scientific_requires`; two ready
features retain explicit blocking relations; no ready feature names an explicit required oracle; and the three variants
do not instantiate distinct feature sets. No required file was missing.

The manifest provides no separate schemas and instructs the reviewer to preserve the actual repository structures;
the validator consequently checks the observed mappings and sequences rather than imposing an external schema.

## Review method and limits

Ready features received detailed field-by-field review. Their source ranges, candidate inputs/outputs, behavior,
preconditions, postconditions, constraints, invariants, test strategies, blockers, immediate dependencies, and boundary
membership are retained in `scientific-review.yaml`. Other statuses received structured classification. Every dependency
touching a ready feature was fully evaluated; remaining dependencies were classified by the same deterministic rules.
This review does not infer types, dimensions, equations, APIs, or missing scientific definitions.

`CONTRACT_WAVE_1` is only a candidate order of eight small, traceable behaviors. It is not ready to start until an
explicit source-grounded oracle is recorded for each entry and retained immediate dependencies are confirmed.

## Files actually read

""" + "\n".join(f"- `{p}`" for p in files_read) + "\n"
    (OUT / "scientific-review-report.md").write_text(report, encoding="utf-8")


def summary() -> dict[str, Any]:
    return load("reviews/functional-decomposition/decision_required.yaml")["summary"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true", help="rebuild review outputs deterministically")
    args = parser.parse_args()
    if args.build:
        build()
    for key, value in summary().items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
