#!/usr/bin/env python3
"""Validate preparation-only artifacts for the 15-relations domain."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry" / "domain-progress" / "relations"
REP = ROOT / "reports" / "domain-progress" / "relations"
FEATURE_PREFIX = "TLC-FC-15-RELATIONS-"
BASE_COMMIT = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
EXPECTED_YAML = {
    "source-inventory.yaml",
    "scientific-audit.yaml",
    "pattern-analysis.yaml",
    "feature-inventory.yaml",
    "feature-classification.yaml",
    "feature-dependencies.yaml",
    "feature-readiness.yaml",
    "contract-production-plan.yaml",
    "ir-production-plan.yaml",
    "domain-status.yaml",
}


def load(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
    ).strip()


def main() -> int:
    require(
        git("merge-base", "--is-ancestor", "origin/main", "HEAD") == "",
        "origin/main is not an ancestor of HEAD",
    )
    require(
        {path.name for path in REG.glob("*.yaml")} == EXPECTED_YAML,
        "unexpected or missing preparation YAML",
    )
    docs = {name: load(REG / name) for name in EXPECTED_YAML}
    decision = load(REP / "decision-required.yaml")
    require((REP / "preparation-report.md").is_file(), "preparation report missing")
    for name, doc in {**docs, "decision-required.yaml": decision}.items():
        require(doc["domain_id"] == "relations", f"{name}: wrong domain")
        require(doc["working_base_commit"] == BASE_COMMIT, f"{name}: wrong base")
        require(
            doc["scope"] == "preparation_only_no_contract_or_ir",
            f"{name}: wrong scope",
        )

    objects_doc = load(
        ROOT
        / "registry/scientific-objects/relations/scientific-objects.candidate.yaml"
    )
    relations_doc = load(
        ROOT
        / "registry/scientific-objects/relations/scientific-relations.candidate.yaml"
    )
    unresolved_doc = load(
        ROOT / "registry/scientific-objects/relations/unresolved-terms.yaml"
    )
    duplicates_doc = load(
        ROOT / "registry/scientific-objects/relations/duplicate-candidates.yaml"
    )
    objects = objects_doc["objects"]
    relations = relations_doc["relations"]
    unresolved = unresolved_doc["unresolved_terms"]
    duplicates = duplicates_doc["duplicate_candidates"]
    object_ids = [item["provisional_object_id"] for item in objects]
    relation_ids = [item["provisional_relation_id"] for item in relations]
    unresolved_ids = [item["unresolved_id"] for item in unresolved]
    require(len(object_ids) == len(set(object_ids)) == 100, "object IDs/count invalid")
    require(len(relation_ids) == len(set(relation_ids)) == 99, "relation IDs/count invalid")
    require(
        len(unresolved_ids) == len(set(unresolved_ids)) == 61,
        "unresolved IDs/count invalid",
    )
    require(len(duplicates) == 12, "duplicate count invalid")
    require(
        all(item["status"] == "unresolved" for item in unresolved),
        "an unresolved item was resolved",
    )
    require(
        all(item["automatic_merge"] is False for item in duplicates),
        "automatic duplicate merge detected",
    )

    source_line_count = len((ROOT / "maths/15-relations.md").read_text(encoding="utf-8").splitlines())
    for item in [*objects, *relations]:
        ref = item["source_reference"]
        require(ref["source_path"] == "maths/15-relations.md", "wrong source path")
        require(
            1 <= ref["start_line"] <= ref["end_line"] <= source_line_count,
            f"invalid source range in {item}",
        )
    object_set = set(object_ids)
    for relation in relations:
        require(relation["source_object_id"] in object_set, "missing relation source")
        require(relation["target_object_id"] in object_set, "missing relation target")
        require(relation["relation_type"] in {"refers_to", "depends_on"}, "relation type drift")

    inventory = docs["feature-inventory.yaml"]
    feature_rows = inventory["features"]
    feature_ids = [item["feature_id"] for item in feature_rows]
    require(len(feature_ids) == len(set(feature_ids)) == 5, "feature IDs/count invalid")
    require(all(item.startswith(FEATURE_PREFIX) for item in feature_ids), "foreign feature")
    require(not inventory["orphan_features"], "orphan feature detected")
    require(
        all(item["source_objects"] or item["source_relations"] for item in feature_rows),
        "feature without source basis",
    )
    coverage = inventory["object_coverage"]
    require(coverage["objects_total"] == 100, "object coverage total invalid")
    require(
        coverage["mapped_to_active_features"]
        + coverage["not_promoted_by_revised_catalogue"]
        == 100,
        "object coverage incomplete",
    )
    require(len(coverage["rows"]) == 100, "object coverage rows missing")
    require(
        {item["object_id"] for item in coverage["rows"]} == object_set,
        "object coverage IDs mismatch",
    )

    for name in [
        "feature-classification.yaml",
        "feature-readiness.yaml",
        "contract-production-plan.yaml",
        "ir-production-plan.yaml",
    ]:
        key = "features" if "feature-" in name else "plans"
        rows = docs[name][key]
        require(
            {item["feature_id"] for item in rows} == set(feature_ids),
            f"{name}: feature coverage mismatch",
        )
    require(
        docs["contract-production-plan.yaml"]["plans_total"] == 5,
        "contract plan count invalid",
    )
    require(docs["ir-production-plan.yaml"]["plans_total"] == 5, "IR plan count invalid")
    require(
        docs["ir-production-plan.yaml"]["ready_for_ir_generation"] is False,
        "IR generation prematurely authorized",
    )

    dependencies = docs["feature-dependencies.yaml"]
    require(not dependencies["intra_domain"]["edges"], "invented intra-domain edge")
    extracted = dependencies["extraction_dependency_edges"]
    require(len(extracted) == 6, "extraction dependency count invalid")
    require(all(item["direction_preserved"] for item in extracted), "direction changed")
    require(
        all(item["semantic_scope"] == "extraction_dependency_only" for item in extracted),
        "relation semantics invented",
    )
    require(
        set(dependencies["non_merged_domains"])
        == {"11-capacities", "12-competencies", "13-practice"},
        "non-merged dependency set invalid",
    )
    require(
        dependencies["no_dependency_detected"] == ["14-lived-experience"],
        "lived-experience dependency invented",
    )

    status = docs["domain-status.yaml"]
    require(status["contracts_generated"] == 0, "contract generated")
    require(status["irs_generated"] == 0, "IR generated")
    require(status["cpp_generated"] is False, "C++ generated")
    require(status["python_bindings_generated"] is False, "binding generated")
    require(status["ready_for_full_contract_generation"] is False, "full contracts authorized")
    require(status["ready_for_ir_generation"] is False, "IR authorized")
    require(status["ready_for_implementation_planning"] is False, "implementation authorized")
    require(status["ready_for_code_generation"] is False, "code generation authorized")

    forbidden_paths = [
        path
        for root in ["registry/math-contracts", "ir"]
        for path in (ROOT / root).glob(f"**/*{FEATURE_PREFIX}*")
    ]
    require(not forbidden_paths, f"final contract or IR detected: {forbidden_paths}")

    changed = git("diff", "--name-only", "origin/main...HEAD").splitlines()
    allowed_prefixes = (
        "registry/domain-progress/relations/",
        "reports/domain-progress/relations/",
        "scripts/build_relations_preparation.py",
        "scripts/validate_relations_preparation.py",
    )
    require(
        all(path.startswith(allowed_prefixes) for path in changed),
        f"out-of-scope files changed: {changed}",
    )

    for path in ROOT.rglob("*.json"):
        if "relations" in path.parts and (
            "domain-progress" in path.parts or "reports" in path.parts
        ):
            json.loads(path.read_text(encoding="utf-8"))

    print(
        "RELATIONS PREPARATION VALIDATION PASSED "
        "objects=100 relations=99 unresolved=61 duplicates=12 "
        "features=5 contract_plans=5 ir_plans=5"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"RELATIONS PREPARATION VALIDATION FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
