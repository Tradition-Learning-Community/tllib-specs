from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/values"
REP = ROOT / "reports/domain-progress/values"
EXPECTED_YAML = {
    "concept-separation.yaml", "contract-production-plan.yaml", "external-domain-dependencies.yaml",
    "feature-classification.yaml", "functional-coverage.yaml", "historical-artifact-assessment.yaml",
    "internal-dependencies.yaml", "ir-production-plan.yaml", "preparation-manifest.yaml",
    "production-readiness.yaml", "relation-inventory.yaml", "scientific-inventory.yaml",
    "source-inventory.yaml", "unresolved-status.yaml", "value-semantics.yaml", "value-structure.yaml",
}
EXPECTED_REPORTS = {
    "concept-separation-report.md", "contract-production-plan-report.md", "domain-preparation-report.md",
    "external-domain-dependencies-report.md", "feature-classification-report.md", "functional-coverage-report.md",
    "historical-artifact-assessment.md", "internal-dependencies-report.md", "ir-production-plan-report.md",
    "production-readiness-report.md", "relation-inventory-report.md", "scientific-inventory-report.md",
    "source-inventory-report.md", "unresolved-report.md", "value-semantics-report.md", "value-structure-report.md",
}
ALLOWED = (
    "registry/domain-progress/values/", "reports/domain-progress/values/",
    "scripts/prepare_values_domain.py", "scripts/validate_values_preparation.py",
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8").strip()


def ids(items: list[dict], key: str, label: str, errors: list[str]) -> set[str]:
    values = [x.get(key) for x in items]
    if None in values or len(values) != len(set(values)):
        errors.append(f"{label}: missing or duplicate identifiers")
    return set(values)


def main() -> int:
    errors: list[str] = []
    yaml_names = {p.name for p in REG.glob("*.yaml")}
    report_names = {p.name for p in REP.glob("*.md")}
    if yaml_names != EXPECTED_YAML:
        errors.append(f"YAML set mismatch: {sorted(yaml_names ^ EXPECTED_YAML)}")
    if report_names != EXPECTED_REPORTS:
        errors.append(f"report set mismatch: {sorted(report_names ^ EXPECTED_REPORTS)}")
    docs = {}
    for path in REG.glob("*.yaml"):
        try:
            docs[path.name] = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
            json.dumps(docs[path.name], ensure_ascii=False)
        except Exception as exc:
            errors.append(f"parse {path}: {exc}")

    canonical_objects = yaml.safe_load((ROOT / "registry/scientific-objects/values/scientific-objects.candidate.yaml").read_text(encoding="utf-8-sig"))["objects"]
    canonical_relations = yaml.safe_load((ROOT / "registry/scientific-objects/values/scientific-relations.candidate.yaml").read_text(encoding="utf-8-sig"))["relations"]
    canonical_unresolved = yaml.safe_load((ROOT / "registry/scientific-objects/values/unresolved-terms.yaml").read_text(encoding="utf-8-sig"))["unresolved_terms"]
    catalogue = yaml.safe_load((ROOT / "registry/features/revised/feature-candidates.yaml").read_text(encoding="utf-8-sig"))["features"]
    canonical_features = [x for x in catalogue if x["candidate_feature_id"].startswith("TLC-FC-09-VALUES-")]
    expected_object_ids = {x["provisional_object_id"] for x in canonical_objects}
    expected_relation_ids = {x["provisional_relation_id"] for x in canonical_relations}
    expected_unresolved_ids = {x["unresolved_id"] for x in canonical_unresolved}
    expected_feature_ids = {x["candidate_feature_id"] for x in canonical_features}

    source = docs.get("source-inventory.yaml", {})
    counts = source.get("counts", {})
    if counts != {"objects": 103, "relations": 102, "unresolved": 68, "duplicate_candidates": 1, "catalogue_features": 14}:
        errors.append(f"source counts: {counts}")
    obj_rows = docs.get("scientific-inventory.yaml", {}).get("objects", [])
    if ids(obj_rows, "provisional_object_id", "objects", errors) != expected_object_ids:
        errors.append("object coverage")
    rel_rows = docs.get("relation-inventory.yaml", {}).get("relations", [])
    if ids(rel_rows, "provisional_relation_id", "relations", errors) != expected_relation_ids:
        errors.append("relation coverage")
    unr_rows = docs.get("unresolved-status.yaml", {}).get("unresolved", [])
    if ids(unr_rows, "unresolved_id", "unresolved", errors) != expected_unresolved_ids:
        errors.append("unresolved coverage")
    if any(x.get("status") != "unresolved" for x in unr_rows):
        errors.append("unresolved adjudicated")

    features = docs.get("functional-coverage.yaml", {}).get("features", [])
    if ids(features, "feature_id", "features", errors) != expected_feature_ids:
        errors.append("feature coverage")
    fsum = docs.get("functional-coverage.yaml", {}).get("summary", {})
    if any(fsum.get(k) != v for k, v in {"catalogue_features": 14, "inventoried_features": 14, "missing_features": 0, "orphan_features": 0}.items()):
        errors.append("feature summary")
    classes = docs.get("feature-classification.yaml", {}).get("features", [])
    if ids(classes, "feature_id", "classifications", errors) != expected_feature_ids:
        errors.append("classification coverage")
    allowed_classes = {"value_declaration_contract", "value_structure_contract", "value_set_contract", "value_relation_contract",
        "value_classification_contract", "value_comparison_contract", "value_ordering_contract", "value_aggregation_contract",
        "value_validation_contract", "value_context_contract", "value_state_contract", "value_principle_contract",
        "value_virtue_contract", "structural_contract", "relational_contract", "constraint_contract", "validation_contract",
        "computational_contract", "non_computational_contract", "not_yet_determinable"}
    if any(x.get("classification") not in allowed_classes for x in classes):
        errors.append("invalid feature classification")

    contract_plans = docs.get("contract-production-plan.yaml", {}).get("plans", [])
    ir_plans = docs.get("ir-production-plan.yaml", {}).get("plans", [])
    if ids(contract_plans, "feature_id", "contract plans", errors) != expected_feature_ids or len(contract_plans) != 14:
        errors.append("contract plan coverage")
    if ids(ir_plans, "feature_id", "IR plans", errors) != expected_feature_ids or len(ir_plans) != 14:
        errors.append("IR plan coverage")
    if any(x.get("candidate_operation_kind") != "not_yet_determinable" or x.get("candidate_types") or x.get("candidate_shapes") or x.get("candidate_dimensions") for x in ir_plans):
        errors.append("invented IR execution semantics")

    structure = docs.get("value-structure.yaml", {})
    if structure.get("not_authorized_as_global_fact", {}).get("total_order") != "not_explicit":
        errors.append("invented total order")
    semantics = docs.get("value-semantics.yaml", {})
    if semantics.get("formal_representation", {}).get("kind") != "10-tuple":
        errors.append("Value tuple missing")
    separation = docs.get("concept-separation.yaml", {}).get("pairs", [])
    if len(separation) != 21:
        errors.append("concept separation coverage")
    external = docs.get("external-domain-dependencies.yaml", {}).get("domains", [])
    expected_domains = {"master", "disciple", "community", "huit_dimensions", "invariants", "dynamics", "theorems",
        "message", "principle", "virtues", "capacities", "competencies", "practice", "lived_experience", "relations"}
    if {x.get("domain") for x in external} != expected_domains:
        errors.append("external domain coverage")
    graph = docs.get("internal-dependencies.yaml", {})
    if set(graph.get("nodes", [])) != expected_feature_ids or graph.get("confirmed_edges") or graph.get("cycles"):
        errors.append("internal dependency graph")
    hist = docs.get("historical-artifact-assessment.yaml", {})
    if hist.get("summary", {}).get("modified") != 0 or hist.get("summary", {}).get("promoted") != 0:
        errors.append("historical artifact mutation")
    readiness = docs.get("production-readiness.yaml", {})
    if any(readiness.get(k) is not False for k in ("ready_for_complete_contract", "ready_for_ir", "ready_for_mechanical_validation", "ready_for_implementation", "ready_for_code_generation")):
        errors.append("readiness overclaim")
    manifest = docs.get("preparation-manifest.yaml", {})
    if manifest.get("preparation_status") != "preparation_complete_with_reservations":
        errors.append("preparation status")
    if manifest.get("non_invention", {}).get("contracts_created") != 0 or manifest.get("non_invention", {}).get("irs_created") != 0:
        errors.append("final artifacts claimed")

    changed = set(filter(None, git("diff", "--name-only", "origin/main...HEAD").splitlines()))
    changed |= set(filter(None, git("diff", "--name-only").splitlines()))
    changed |= set(filter(None, git("ls-files", "--others", "--exclude-standard").splitlines()))
    outside = [p for p in changed if not any(p == prefix or p.startswith(prefix) for prefix in ALLOWED)]
    if outside:
        errors.append(f"out-of-scope paths: {outside}")
    if any(p.startswith("registry/math-contracts/TLC-FC-09-VALUES-") for p in changed):
        errors.append("final Values contract modified")
    if any(p.startswith("ir/TLC-FC-09-VALUES-") for p in changed):
        errors.append("final Values IR modified")
    generated = "\n".join(p.read_text(encoding="utf-8-sig") for p in [*REG.glob("*"), *REP.glob("*")] if p.is_file()).lower()
    if any(term in generated for term in ("#include <", "pybind11", "binding python")):
        errors.append("implementation artifact")

    if errors:
        print("VALUES PREPARATION VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALUES PREPARATION VALIDATION PASSED")
    print("objects=103 relations=102 unresolved=68 duplicate_candidates=1 features=14")
    print("contract_plans=14 ir_plans=14 yaml=16 reports=16 contracts_created=0 irs_created=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
