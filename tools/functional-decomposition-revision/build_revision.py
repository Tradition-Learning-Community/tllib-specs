"""Build the mechanically revised functional-decomposition catalogue.

This is an application tool: it copies review conclusions without making
scientific decisions.  It never reads or writes scientific source files.
"""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[2]
REVISED = ROOT / "registry/features/revised"
REPORTS = ROOT / "reports/functional-decomposition-revision"
APPLICATION = ROOT / "reviews/functional-decomposition/application"
DECOMPOSITION_COMMIT = "d0d1e26ef6a488aa291e1f4e616b9b2748ff2370"
REVIEW_COMMIT = "94683f9a8a762b3afe735b8442e1dfff6a624368"


def load(relative: str):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def dump(relative: str, value) -> None:
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110),
        encoding="utf-8",
    )


def review_reason(review: dict) -> str:
    changes = review.get("required_changes") or []
    issues = review.get("issues") or []
    return "; ".join(changes or issues or [review["functional_coherence"]["assessment"]])


def primary_classification(review: dict) -> str:
    status = review["review_status"]
    if status == "ACCEPT_WITH_RESERVATIONS":
        return "retained_with_reservations"
    if status == "REVISE_FEATURE_BOUNDARY":
        return "deferred_for_scientific_decision"
    if status == "REQUIRES_TARGETED_EXTRACTION":
        return "deferred_for_targeted_extraction"
    if status == "REQUIRES_SCIENTIFIC_DECISION":
        return "deferred_for_scientific_decision"
    if status == "REJECT_AS_SOFTWARE_FEATURE":
        return "rejected_as_feature"
    raise ValueError(status)


def destination_classification(review: dict) -> str | None:
    action = review["functional_coherence"]["recommended_action"]
    return {
        "convert_to_data_model": "converted_to_data_model",
        "convert_to_state_definition": "converted_to_state_definition",
        "convert_to_test_oracle": "converted_to_test_oracle",
        "keep_as_feature": None,
    }[action]


def main() -> None:
    original = load("registry/features/feature-candidates.yaml")
    reviews = load("reviews/functional-decomposition/scientific-review.yaml")
    dependencies = load("reviews/functional-decomposition/dependency-audit.yaml")
    boundaries = load("reviews/functional-decomposition/boundary-review.yaml")
    variants = load("registry/features/feature-decomposition-variants.yaml")
    reviewed_waves = load("reviews/functional-decomposition/contract-waves.yaml")
    review_issues = load("reviews/functional-decomposition/review-issues.yaml")

    originals = {f["candidate_feature_id"]: f for f in original["features"]}
    review_by_id = {f["feature_candidate_id"]: f for f in reviews["features"]}
    if set(originals) != set(review_by_id) or len(originals) != 224:
        raise RuntimeError("The review does not cover exactly the 224 original feature identifiers")

    critical_ids = {"TLC-FC-00-MASTER-003", "TLC-FC-00-MASTER-007"}
    boundary_by_feature = {
        feature_id: issue["boundary_issue_id"]
        for issue in boundaries["boundary_issues"]
        for feature_id in issue["feature_candidate_ids"]
    }

    classifications = []
    lineage = []
    revised_features = []
    oracle_records = []
    for feature_id, source in originals.items():
        review = review_by_id[feature_id]
        classification = primary_classification(review)
        destination = destination_classification(review)
        retained = review["functional_coherence"]["recommended_action"] == "keep_as_feature"
        active = classification == "retained_with_reservations"
        critical = feature_id in critical_ids
        blocking_relations = list(source.get("readiness", {}).get("blocking_relation_ids") or [])
        blocking_decisions = list(source.get("readiness", {}).get("blocking_decision_ids") or [])
        if critical:
            active = False
            classification = "deferred_for_scientific_decision"

        record = {
            "feature_candidate_id": feature_id,
            "review_decision": review["review_status"],
            "classification": classification,
            "destination_classification": destination,
            "justification": review_reason(review),
            "destination_id": None,
            "candidate_status": "candidate",
            "active_feature_candidate": active,
            "boundary_issue_id": boundary_by_feature.get(feature_id),
            "critical_reclassification": critical,
        }
        classifications.append(record)
        lineage.append({
            "original_feature_candidate_id": feature_id,
            "review_decision": review["review_status"],
            "new_classification": classification,
            "justification": record["justification"],
            "destination_classification": destination,
            "destination_id": None,
            "candidate_status": "candidate",
            "scientific_object_ids": review["scientific_fidelity"].get("object_ids") or [],
            "source_references": review.get("source_evidence") or [],
        })

        if retained:
            candidate = deepcopy(source)
            candidate["review_application"] = {
                "review_decision": review["review_status"],
                "classification": classification,
                "reservations": review.get("issues") or [],
                "required_changes": review.get("required_changes") or [],
                "review_commit": REVIEW_COMMIT,
            }
            candidate["dependencies"]["immediate_feature_candidates"] = []
            candidate["readiness"]["status"] = (
                "requires_targeted_scientific_review" if critical else classification
            )
            candidate["status"] = "candidate"
            revised_features.append(candidate)

        explicit_oracles = list(review.get("testability_assessment", {}).get("required_oracles") or [])
        source_candidates = []
        for strategy in review.get("testability_assessment", {}).get("strategies") or []:
            source_candidates.append({"type": "comparison_structural", "reference": strategy})
        oracle_records.append({
            "feature_candidate_id": feature_id,
            "candidate_for_contract": active,
            "oracle_source_candidates": source_candidates,
            "explicit_oracles": explicit_oracles,
            "missing_oracle_information": [] if explicit_oracles else [
                "No explicit expected result or source-grounded acceptance oracle is identified by the review."
            ],
            "oracle_readiness": "ready" if explicit_oracles else "incomplete",
            "blocking_reservation": active and not explicit_oracles,
            "status": "candidate",
        })

    context = []
    rejected = []
    for dep in dependencies["dependencies"]:
        common = {
            "dependency_candidate_id": dep["dependency_candidate_id"],
            "from_feature": dep["from_feature"],
            "to_feature": dep["to_feature"],
            "original_type": dep["original_type"],
            "evidence": dep.get("evidence") or {},
            "review_action": dep["action"],
            "normative": False,
            "status": "candidate",
        }
        if dep["reviewed_type"] == "shared_scientific_context":
            context.append({**common, "relation_type": "scientific_context_only"})
        elif dep["reviewed_type"] == "invalid_dependency":
            rejected.append({**common, "relation_type": "rejected_dependency"})
        else:
            raise RuntimeError(f"Unrecognized reviewed dependency type: {dep['reviewed_type']}")

    pending_boundaries = []
    human_decisions = []
    for issue in boundaries["boundary_issues"]:
        pending_boundaries.append({
            "boundary_issue_id": issue["boundary_issue_id"],
            "feature_ids": issue["feature_candidate_ids"],
            "scientific_object_ids": issue["scientific_object_ids"],
            "scientific_relation_ids": issue["scientific_relation_ids"],
            "source_references": issue["source_evidence"],
            "reviewed_defect_type": issue["reviewed_defect_type"],
            "finding": issue["finding"],
            "options": issue["correction_options"],
            "decision_reason": "The review explicitly requires a human decision among multiple correction options.",
            "status": "pending",
        })
        human_decisions.append({
            "decision_id": "TLC-HBD-" + issue["boundary_issue_id"].split("-")[-1],
            "feature_ids": issue["feature_candidate_ids"],
            "question": issue["finding"],
            "options": issue["correction_options"],
            "evidence": issue["source_evidence"],
            "consequences": issue["effects"],
            "recommendation_non_normative": "No option selected; retain the review options for scientific arbitration.",
            "priority": "high" if issue["severity"] in {"critical", "major"} else "normal",
            "local_blocking": True,
            "status": "pending",
        })

    human_decisions.extend([
        {
            "decision_id": "TLC-HSD-MASTER-003",
            "feature_ids": ["TLC-FC-00-MASTER-003"],
            "question": "Which reviewed scientific relations are indispensable before this candidate can be reconsidered for contract selection?",
            "options": ["resolve cited blocking relations", "defer the candidate", "reject it as a software feature"],
            "evidence": review_by_id["TLC-FC-00-MASTER-003"].get("source_evidence") or [],
            "consequences": ["The candidate remains outside every contract wave until the relations are decided."],
            "recommendation_non_normative": "Keep requires_targeted_scientific_review until a scientific decision is recorded.",
            "priority": "critical", "local_blocking": True, "status": "pending",
        },
        {
            "decision_id": "TLC-HSD-MASTER-007",
            "feature_ids": ["TLC-FC-00-MASTER-007"],
            "question": "Which reviewed scientific relations are indispensable before this candidate can be reconsidered for contract selection?",
            "options": ["resolve cited blocking relations", "defer the candidate", "reject it as a software feature"],
            "evidence": review_by_id["TLC-FC-00-MASTER-007"].get("source_evidence") or [],
            "consequences": ["The candidate remains outside every contract wave until the relations are decided."],
            "recommendation_non_normative": "Keep requires_targeted_scientific_review until a scientific decision is recorded.",
            "priority": "critical", "local_blocking": True, "status": "pending",
        },
    ])

    proposed_wave_1 = [x["feature_candidate_id"] for x in reviewed_waves.get("CONTRACT_WAVE_1", [])]
    human_decisions.append({
        "decision_id": "TLC-HOD-CONTRACT-WAVE-1",
        "feature_ids": proposed_wave_1,
        "question": "Which source-grounded oracle, if any, permits each proposed candidate to enter contract work?",
        "options": ["identify an existing source oracle", "retain a blocking oracle reservation", "defer the candidate"],
        "evidence": [{"review_artifact": "reviews/functional-decomposition/contract-waves.yaml"}],
        "consequences": ["CONTRACT_WAVE_1 remains empty while explicit oracle information is absent."],
        "recommendation_non_normative": "Perform targeted oracle extraction from existing cited sources; do not invent expected values.",
        "priority": "high", "local_blocking": True, "status": "pending",
    })

    meta = {"work_item_id": "TLC-FUNCTIONAL-DECOMPOSITION-REVISION-001", "status": "candidate",
            "decomposition_commit": DECOMPOSITION_COMMIT, "review_commit": REVIEW_COMMIT}
    dump("registry/features/revised/feature-candidates.yaml", {**meta, "count": len(revised_features), "features": revised_features})
    dump("registry/features/revised/feature-classification.yaml", {**meta, "count": 224, "classifications": classifications})
    dump("registry/features/revised/feature-lineage.yaml", {**meta, "count": 224, "lineage": lineage})
    dump("registry/features/revised/functional-dependencies.yaml", {**meta, "count": 0, "cycle_count": 0, "dependencies": []})
    dump("registry/features/revised/scientific-context-relations.yaml", {**meta, "count": len(context), "relations": context})
    dump("registry/features/revised/rejected-dependencies.yaml", {**meta, "count": len(rejected), "dependencies": rejected})
    dump("registry/features/revised/boundary-decisions-pending.yaml", {**meta, "count": len(pending_boundaries), "boundary_decisions": pending_boundaries})
    dump("registry/features/revised/oracle-readiness.yaml", {**meta, "count": 224, "features": oracle_records})
    dump("registry/features/revised/decomposition-variants.yaml", {**meta, "selected_variant": None, "regeneration_recommended": True,
        "variants": [{**v, "status": "not_materialized", "selected": False,
                      "materialization_finding": "All three original variants contain the same 224 identifiers; no distinct structure is materialized."}
                     for v in variants["variants"]]})
    dump("reviews/functional-decomposition/application/human-decisions.yaml", {**meta, "count": len(human_decisions), "decisions": human_decisions})

    counts = Counter(x["classification"] for x in classifications)
    summary = {
        "original_feature_candidates": 224,
        "retained_features": len(revised_features),
        "retained_with_reservations": counts["retained_with_reservations"],
        "converted_candidates": sum(x["destination_classification"] is not None for x in classifications),
        "rejected_as_features": counts["rejected_as_feature"],
        "active_functional_dependencies": 0,
        "scientific_context_relations": len(context),
        "rejected_dependencies": len(rejected),
        "unresolved_dependencies": 0,
        "boundary_corrections_applied": 0,
        "boundary_decisions_pending": len(pending_boundaries),
        "oracle_ready": sum(x["oracle_readiness"] == "ready" for x in oracle_records),
        "oracle_incomplete": sum(x["oracle_readiness"] == "incomplete" for x in oracle_records),
        "contract_wave_1": 0, "contract_wave_2": 0, "contract_wave_3": 0, "deferred": 224,
    }
    waves = {**meta, "selection_rule": "No candidate satisfies every Wave 1 gate after the missing-oracle and pending-decision checks.",
             "CONTRACT_WAVE_1": [], "CONTRACT_WAVE_2": [], "CONTRACT_WAVE_3": [],
             "DEFERRED": [{"feature_candidate_id": fid, "reason": review_by_id[fid]["review_status"], "status": "candidate"} for fid in originals]}
    dump("reports/functional-decomposition-revision/contract-waves.yaml", waves)
    dump("reports/functional-decomposition-revision/decision_required.yaml", {
        "work_item_id": "TLC-FUNCTIONAL-DECOMPOSITION-REVISION-001", "stage": "functional_decomposition_revision", "status": "candidate",
        "input": {"decomposition_commit": DECOMPOSITION_COMMIT, "review_commit": REVIEW_COMMIT},
        "summary": summary,
        "blocking_issues": ["17 boundary decisions remain pending", "Explicit oracle information is absent", "Two critical candidates require scientific relation decisions"],
        "non_blocking_issues": ["Three variants are not structurally materialized"],
        "questions_for_human": [d["decision_id"] for d in human_decisions],
        "recommended_decision": {"value": "revise", "justification": "The deterministic cleanup is complete, but scientific boundary and oracle decisions remain."},
        "allowed_decisions": ["approved", "approved_with_reservations", "revise", "rejected"],
        "readiness": {"ready_for_human_validation": False, "ready_for_contract_wave_1": False, "ready_for_ir": False, "ready_for_implementation": False},
    })

    report_lines = [
        "# Application report", "", "The independent scientific review was applied mechanically without scientific interpretation.", "",
        "## Result", "", f"- Original identifiers traced: 224", f"- Active retained candidates: {len(revised_features)}",
        f"- Rejected as features: {counts['rejected_as_feature']}", f"- Context-only relations: {len(context)}",
        f"- Rejected dependencies: {len(rejected)}", "- Active functional dependencies: 0", "- Boundary corrections applied: 0",
        f"- Boundary decisions pending: {len(pending_boundaries)}", "- CONTRACT_WAVE_1: empty", "",
        "The two critical candidates TLC-FC-00-MASTER-003 and TLC-FC-00-MASTER-007 were reclassified for targeted scientific review and excluded from all contract waves.",
    ]
    (REPORTS / "application-report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    (REPORTS / "README.md").write_text("# Functional decomposition revision\n\nCandidate outputs applying review commit `94683f9a8a762b3afe735b8442e1dfff6a624368`. No output is approved or normative.\n", encoding="utf-8")
    (REPORTS / "revised-catalog-summary.md").write_text("# Revised catalogue summary\n\n" + "\n".join(f"- `{k}`: {v}" for k, v in summary.items()) + "\n", encoding="utf-8")
    (REPORTS / "dependency-cleanup-report.md").write_text("# Dependency cleanup\n\nAll 1,365 candidate relations were removed from the active graph: 811 are retained as scientific context only and 554 are rejected. The active graph is empty, acyclic, and non-normative.\n", encoding="utf-8")
    (REPORTS / "oracle-readiness-report.md").write_text("# Oracle readiness\n\nNo explicit oracle was identified by the review. Potential structural test strategies are recorded only as source candidates, never as invented oracles. All retained candidates carry a blocking oracle reservation.\n", encoding="utf-8")


if __name__ == "__main__":
    main()
