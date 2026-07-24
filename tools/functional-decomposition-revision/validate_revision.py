"""Validate the mechanically revised functional-decomposition catalogue."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import yaml


ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []


def load(relative: str):
    try:
        return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"unreadable YAML {relative}: {exc}")
        return {}


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> int:
    original = load("registry/features/feature-candidates.yaml")
    classes = load("registry/features/revised/feature-classification.yaml")
    lineage = load("registry/features/revised/feature-lineage.yaml")
    features = load("registry/features/revised/feature-candidates.yaml")
    active = load("registry/features/revised/functional-dependencies.yaml")
    context = load("registry/features/revised/scientific-context-relations.yaml")
    rejected = load("registry/features/revised/rejected-dependencies.yaml")
    boundaries = load("registry/features/revised/boundary-decisions-pending.yaml")
    oracles = load("registry/features/revised/oracle-readiness.yaml")
    variants = load("registry/features/revised/decomposition-variants.yaml")
    waves = load("reports/functional-decomposition-revision/contract-waves.yaml")
    humans = load("reviews/functional-decomposition/application/human-decisions.yaml")

    original_ids = {x["candidate_feature_id"] for x in original.get("features", [])}
    class_items = classes.get("classifications", [])
    lineage_items = lineage.get("lineage", [])
    require(len(original_ids) == 224, "original catalogue does not contain 224 unique identifiers")
    require({x["feature_candidate_id"] for x in class_items} == original_ids, "classification loses original identifiers")
    require({x["original_feature_candidate_id"] for x in lineage_items} == original_ids, "lineage loses original identifiers")
    require(len(class_items) == len(lineage_items) == 224, "classification or lineage is not one-to-one")
    require(all(x.get("justification") for x in class_items), "a transformation lacks review justification")
    require(all(x.get("candidate_status") == "candidate" for x in class_items), "a feature is not candidate")
    require(not any(x.get("candidate_status") == "approved" for x in class_items), "an approved feature exists")

    by_id = {x["feature_candidate_id"]: x for x in class_items}
    for critical in ("TLC-FC-00-MASTER-003", "TLC-FC-00-MASTER-007"):
        require(by_id.get(critical, {}).get("classification") == "deferred_for_scientific_decision", f"{critical} not reclassified")
        require(not by_id.get(critical, {}).get("active_feature_candidate", True), f"{critical} remains active")
        require(all(x.get("feature_candidate_id") != critical for wave in ("CONTRACT_WAVE_1", "CONTRACT_WAVE_2", "CONTRACT_WAVE_3") for x in waves.get(wave, [])), f"{critical} remains in a contract wave")

    active_items = active.get("dependencies", [])
    require(active.get("count") == len(active_items) == 0, "active dependency graph should be empty after review")
    require(not any(x.get("from_feature") == x.get("to_feature") for x in active_items), "active self-dependency exists")
    require(context.get("count") == len(context.get("relations", [])) == 811, "context relation count is not 811")
    require(rejected.get("count") == len(rejected.get("dependencies", [])) == 554, "rejected dependency count is not 554")
    active_ids = {x.get("dependency_candidate_id") for x in active_items}
    require(active_ids.isdisjoint(x["dependency_candidate_id"] for x in context.get("relations", [])), "context relation remains active")
    require(active_ids.isdisjoint(x["dependency_candidate_id"] for x in rejected.get("dependencies", [])), "rejected dependency remains active")
    require(boundaries.get("count") == len(boundaries.get("boundary_decisions", [])) == 17, "pending boundary count is not 17")
    require(all(x.get("status") == "pending" for x in boundaries.get("boundary_decisions", [])), "a pending boundary was applied")
    require(len(oracles.get("features", [])) == 224, "oracle register does not cover 224 features")
    require(all(x.get("oracle_readiness") in {"ready", "incomplete"} for x in oracles.get("features", [])), "invalid oracle readiness")
    require(variants.get("selected_variant") is None, "a variant was selected")
    require(all(x.get("status") == "not_materialized" and not x.get("selected") for x in variants.get("variants", [])), "a non-materialized variant is presented as selected")
    require(all(x.get("status") == "pending" for x in humans.get("decisions", [])), "a scientific pending decision was applied")

    wave1 = waves.get("CONTRACT_WAVE_1", [])
    oracle_by_id = {x["feature_candidate_id"]: x for x in oracles.get("features", [])}
    for item in wave1:
        fid = item["feature_candidate_id"]
        require(by_id[fid]["active_feature_candidate"], f"Wave 1 feature {fid} is inactive")
        require(not by_id[fid].get("boundary_issue_id"), f"Wave 1 feature {fid} has unstable boundary")
        require(oracle_by_id[fid]["oracle_readiness"] == "ready" or not oracle_by_id[fid]["blocking_reservation"], f"Wave 1 feature {fid} has blocking oracle reserve")

    changed = set()
    for command in (["git", "diff", "--cached", "--name-only"], ["git", "diff", "--name-only"]):
        changed.update(subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False).stdout.splitlines())
    forbidden = ("maths/", "algorithms/", "registry/scientific-objects/", "registry/features/feature-candidates.yaml", "registry/features/feature-decomposition-variants.yaml", "registry/features/feature-boundary-issues.yaml", "registry/features/dependency-hints.yaml", "reviews/functional-decomposition/")
    # The application subdirectory is the only allowed addition below reviews/functional-decomposition.
    for path in changed:
        normalized = path.replace("\\", "/")
        if normalized.startswith("reviews/functional-decomposition/application/"):
            continue
        require(not any(normalized == p or normalized.startswith(p) for p in forbidden), f"forbidden source changed: {normalized}")

    if ERRORS:
        print("REVISION VALIDATION FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print("REVISION VALIDATION PASSED")
    print("224 identifiers traced; 0 active dependencies; 811 context relations; 554 rejected dependencies; 17 pending boundaries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
