from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []


def load(relative: str):
    path = ROOT / relative
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"unreadable YAML {relative}: {exc}")
        return {}


def require(condition: bool, message: str):
    if not condition:
        ERRORS.append(message)


def main() -> int:
    snapshot = load("registry/functional-decomposition/decomposition-input-snapshot.yaml")
    object_doc = load("reports/functional-decomposition-input/object-status.yaml")
    relation_doc = load("reports/functional-decomposition-input/relation-status.yaml")
    catalog = load("registry/features/feature-candidates.yaml")
    variants = load("registry/features/feature-decomposition-variants.yaml")
    boundaries = load("registry/features/feature-boundary-issues.yaml")
    dependency_doc = load("registry/features/dependency-hints.yaml")
    priority = load("reports/functional-decomposition/prioritization.yaml")
    decision = load("reports/functional-decomposition/decision_required.yaml")

    objects = object_doc.get("objects", [])
    relations = relation_doc.get("relations", [])
    features = catalog.get("features", [])
    dependencies = dependency_doc.get("dependencies", [])
    object_by_id = {o["object_id"]: o for o in objects}
    relation_by_id = {r["relation_id"]: r for r in relations}
    feature_by_id = {f["candidate_feature_id"]: f for f in features}
    require(len(object_by_id) == len(objects), "duplicate object identifiers in input")
    require(len(relation_by_id) == len(relations), "duplicate relation identifiers in input")
    require(len(feature_by_id) == len(features), "feature identifiers are not unique")
    require(len({d["dependency_candidate_id"] for d in dependencies}) == len(dependencies), "dependency identifiers are not unique")
    require(len(objects) == snapshot["summary"]["total_objects"] == object_doc.get("count"), "object input counts disagree")
    require(len(relations) == snapshot["summary"]["total_relations"] == relation_doc.get("count"), "relation input counts disagree")

    mandatory = {"what_to_build", "why_it_exists", "candidate_inputs", "candidate_outputs", "expected_behavior", "correctness_evidence"}
    referenced_objects = []
    referenced_relations = []
    for feature in features:
        fid = feature["candidate_feature_id"]
        basis = feature.get("scientific_basis", {})
        oids = basis.get("scientific_object_ids", [])
        rids = basis.get("scientific_relation_ids", [])
        referenced_objects.extend(oids)
        referenced_relations.extend(rids)
        require(feature.get("status") == "candidate", f"{fid}: status must be candidate")
        require(feature.get("status") != "approved", f"{fid}: approved status is forbidden")
        require(bool(oids), f"{fid}: must cite at least one scientific object")
        require(set(oids) <= object_by_id.keys(), f"{fid}: cites unknown objects")
        require(set(rids) <= relation_by_id.keys(), f"{fid}: cites unknown relations")
        question = feature.get("construction_question", {})
        require(mandatory <= question.keys() and all(question.get(k) not in (None, "", []) for k in mandatory), f"{fid}: mandatory construction questions incomplete")
        readiness = feature.get("readiness", {})
        blocked_used = {oid for oid in oids if object_by_id[oid]["status"] == "blocked_locally"}
        require(blocked_used <= set(readiness.get("blocking_object_ids", [])), f"{fid}: silent dependency on blocked object")
        provisional = [oid for oid in oids if object_by_id[oid]["status"] == "provisionally_separated"]
        if provisional:
            require(readiness.get("status") == "requires_targeted_scientific_review", f"{fid}: provisional objects require targeted review")
            require(len(provisional) == len(set(provisional)), f"{fid}: provisional object identifiers merged or duplicated")
        if readiness.get("status") == "ready_for_math_contract":
            require(not blocked_used, f"{fid}: blocked object cannot be ready")
            require(bool(question.get("candidate_inputs")) and bool(question.get("candidate_outputs")), f"{fid}: ready feature lacks candidate inputs/outputs")
            require(bool(feature.get("testability", {}).get("candidate_test_strategies")), f"{fid}: ready feature lacks test strategy")
        if readiness.get("status") != "ready_for_math_contract":
            has_reason = any(readiness.get(k) for k in ("blocking_object_ids", "blocking_relation_ids", "blocking_decision_ids", "blocking_terms")) or bool(feature.get("unresolved_questions")) or readiness.get("status") == "requires_targeted_extraction"
            require(has_reason, f"{fid}: non-ready feature does not cite a blocker or unresolved question")

    dep_relation_ids = []
    for dep in dependencies:
        require(dep.get("from_feature") in feature_by_id, f"{dep.get('dependency_candidate_id')}: unknown from_feature")
        require(dep.get("to_feature") in feature_by_id, f"{dep.get('dependency_candidate_id')}: unknown to_feature")
        evidence = dep.get("scientific_evidence", [])
        if evidence and evidence[0] in relation_by_id:
            dep_relation_ids.append(evidence[0])
        else:
            ERRORS.append(f"{dep.get('dependency_candidate_id')}: missing relation evidence")
    require(set(referenced_objects) == set(object_by_id), "not all snapshot objects are traceably assigned to a feature")
    require(set(dep_relation_ids) == set(relation_by_id), "not all snapshot relations are represented by dependencies")
    require(len(dep_relation_ids) == len(relations), "relations are not represented one-for-one")
    for variant in variants.get("variants", []):
        require(set(variant.get("feature_candidates", [])) <= feature_by_id.keys(), f"{variant.get('variant_id')}: unknown feature")
    for issue in boundaries.get("boundary_issues", []):
        require(set(issue.get("feature_candidate_ids", [])) <= feature_by_id.keys(), f"{issue.get('boundary_issue_id')}: unknown feature")
    for group, ids in priority.get("groups", {}).items():
        require(set(ids) <= feature_by_id.keys(), f"prioritization group {group}: unknown feature")

    actual = Counter(f["readiness"]["status"] for f in features)
    summary = decision.get("summary", {})
    require(catalog.get("count") == len(features) == summary.get("feature_candidates"), "feature report counts disagree")
    require(variants.get("count") == len(variants.get("variants", [])) == summary.get("decomposition_variants"), "variant report counts disagree")
    require(boundaries.get("count") == len(boundaries.get("boundary_issues", [])) == summary.get("boundary_issues"), "boundary report counts disagree")
    require(dependency_doc.get("count") == len(dependencies) == summary.get("dependency_candidates"), "dependency report counts disagree")
    for status, count in actual.items():
        require(summary.get(status) == count, f"readiness count disagrees for {status}")

    if ERRORS:
        print(f"FAILED: {len(ERRORS)} validation error(s)")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"OK: {len(features)} candidate features; {len(dependencies)} dependencies; all YAML registries consistent")
    print(f"Objects covered: {len(object_by_id)}; relations covered: {len(relation_by_id)}")
    print("Readiness: " + ", ".join(f"{k}={v}" for k, v in sorted(actual.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
