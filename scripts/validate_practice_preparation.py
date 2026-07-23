#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/practice"
REP = ROOT / "reports/domain-progress/practice"
BASELINE = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
EXPECTED_YAML = {
    "concept-boundaries.yaml",
    "contract-production-plan.yaml",
    "decision-required.yaml",
    "dependency-matrix.yaml",
    "external-domain-dependencies.yaml",
    "feature-classification.yaml",
    "functional-coverage.yaml",
    "historical-artifact-assessment.yaml",
    "internal-dependencies.yaml",
    "ir-production-plan.yaml",
    "pattern-analysis.yaml",
    "preparation-manifest.yaml",
    "production-readiness.yaml",
    "relation-inventory.yaml",
    "scientific-inventory.yaml",
    "source-inventory.yaml",
    "unresolved-status.yaml",
}
EXPECTED_REPORTS = {
    "concept-boundaries-report.md",
    "contract-production-plan-report.md",
    "decision-required-report.md",
    "dependency-matrix-report.md",
    "domain-preparation-report.md",
    "external-domain-dependencies-report.md",
    "feature-classification-report.md",
    "functional-coverage-report.md",
    "historical-artifact-assessment.md",
    "internal-dependencies-report.md",
    "ir-production-plan-report.md",
    "pattern-analysis-report.md",
    "production-readiness-report.md",
    "relation-inventory-report.md",
    "scientific-inventory-report.md",
    "source-inventory-report.md",
    "unresolved-report.md",
}
ALLOWED = (
    "registry/domain-progress/practice/",
    "reports/domain-progress/practice/",
    "scripts/prepare_practice_domain.py",
    "scripts/validate_practice_preparation.py",
)


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def git(*args: str) -> list[str]:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8"
    ).splitlines()


def unique(items: list[dict], key: str, label: str, errors: list[str]) -> set[str]:
    values = [item.get(key) for item in items]
    if None in values or len(values) != len(set(values)):
        errors.append(f"{label}: missing or duplicate identifiers")
    return set(values)


errors: list[str] = []
yaml_names = {path.name for path in REG.glob("*.yaml")}
report_names = {path.name for path in REP.glob("*.md")}
if yaml_names != EXPECTED_YAML:
    errors.append(f"YAML set mismatch: {sorted(yaml_names ^ EXPECTED_YAML)}")
if report_names != EXPECTED_REPORTS:
    errors.append(f"report set mismatch: {sorted(report_names ^ EXPECTED_REPORTS)}")

docs = {}
for path in REG.glob("*.yaml"):
    try:
        docs[path.name] = load(path)
        json.dumps(docs[path.name], ensure_ascii=False)
        if docs[path.name].get("baseline_commit") != BASELINE:
            errors.append(f"stale baseline: {path.name}")
    except Exception as exc:
        errors.append(f"invalid YAML/JSON model {path.name}: {exc}")
for path in REP.glob("*.md"):
    if not path.read_text(encoding="utf-8-sig").strip():
        errors.append(f"empty report: {path.name}")

base = ROOT / "registry/scientific-objects/practice"
canonical_objects = load(base / "scientific-objects.candidate.yaml")["objects"]
canonical_relations = load(base / "scientific-relations.candidate.yaml")["relations"]
canonical_unresolved = load(base / "unresolved-terms.yaml")["unresolved_terms"]
canonical_duplicates = load(base / "duplicate-candidates.yaml")["duplicate_candidates"]
catalogue = load(ROOT / "registry/features/revised/feature-candidates.yaml")["features"]
canonical_features = [
    item for item in catalogue
    if item["candidate_feature_id"].startswith("TLC-FC-13-PRACTICE-")
]
object_ids = {item["provisional_object_id"] for item in canonical_objects}
relation_ids = {item["provisional_relation_id"] for item in canonical_relations}
unresolved_ids = {item["unresolved_id"] for item in canonical_unresolved}
feature_ids = {item["candidate_feature_id"] for item in canonical_features}

source = docs.get("source-inventory.yaml", {})
expected_counts = {
    "objects": 93,
    "relations": 92,
    "unresolved": 60,
    "duplicate_candidates": 0,
    "revised_features": 10,
}
if source.get("counts") != expected_counts:
    errors.append(f"source counts mismatch: {source.get('counts')}")
if not (ROOT / "maths/13-practice.md").is_file():
    errors.append("canonical source missing")

objects = docs.get("scientific-inventory.yaml", {}).get("objects", [])
if unique(objects, "provisional_object_id", "objects", errors) != object_ids:
    errors.append("object coverage mismatch")
if any(not item.get("source_reference") for item in objects):
    errors.append("object source trace missing")
relations = docs.get("relation-inventory.yaml", {}).get("relations", [])
if unique(relations, "provisional_relation_id", "relations", errors) != relation_ids:
    errors.append("relation coverage mismatch")
if any(
    item.get("source_object_id") not in object_ids
    or item.get("target_object_id") not in object_ids
    or not item.get("source_reference")
    for item in relations
):
    errors.append("invalid relation reference")
unresolved = docs.get("unresolved-status.yaml", {}).get("unresolved", [])
if unique(unresolved, "unresolved_id", "unresolved", errors) != unresolved_ids:
    errors.append("unresolved coverage mismatch")
if any(item.get("status") != "unresolved" for item in unresolved):
    errors.append("unresolved item adjudicated")
if len(canonical_duplicates) != 0:
    errors.append("unexpected canonical duplicate count")

features = docs.get("functional-coverage.yaml", {}).get("features", [])
if unique(features, "feature_id", "features", errors) != feature_ids:
    errors.append("feature coverage mismatch")
summary = docs.get("functional-coverage.yaml", {}).get("summary", {})
if any(summary.get(key) != value for key, value in {
    "catalogue_features": 10,
    "inventoried_features": 10,
    "missing_features": 0,
    "orphan_features": 0,
}.items()):
    errors.append("functional coverage summary mismatch")
for feature in features:
    if not feature.get("source_objects"):
        errors.append(f"orphan feature: {feature.get('feature_id')}")
    if not set(feature.get("source_objects", [])).issubset(object_ids):
        errors.append(f"invalid feature object reference: {feature.get('feature_id')}")
    if not set(feature.get("source_relations", [])).issubset(relation_ids):
        errors.append(f"invalid feature relation reference: {feature.get('feature_id')}")
gap_ids = {
    item["object_id"]
    for item in docs.get("functional-coverage.yaml", {}).get("catalogue_gap_candidates", [])
}
feature_object_ids = {object_id for feature in features for object_id in feature["source_objects"]}
if feature_object_ids | gap_ids != object_ids or feature_object_ids & gap_ids:
    errors.append("objects are not completely partitioned between feature coverage and gap candidates")

classifications = docs.get("feature-classification.yaml", {}).get("features", [])
if unique(classifications, "feature_id", "classifications", errors) != feature_ids:
    errors.append("classification coverage mismatch")
contract_plans = docs.get("contract-production-plan.yaml", {}).get("plans", [])
ir_plans = docs.get("ir-production-plan.yaml", {}).get("plans", [])
if unique(contract_plans, "feature_id", "contract plans", errors) != feature_ids:
    errors.append("contract plan coverage mismatch")
if unique(ir_plans, "feature_id", "IR plans", errors) != feature_ids:
    errors.append("IR plan coverage mismatch")
if any(
    item.get("candidate_operation_kind") != "not_yet_determinable"
    or item.get("candidate_types")
    or item.get("candidate_shapes")
    or item.get("candidate_dimensions")
    or item.get("candidate_state_effects")
    for item in ir_plans
):
    errors.append("invented IR semantics")

patterns = docs.get("pattern-analysis.yaml", {})
if patterns.get("formal_patterns") != 0 or patterns.get("candidate_mentions") != 2:
    errors.append("pattern analysis mismatch")
if any(item.get("formal_structure") != "not_specified" for item in patterns.get("patterns", [])):
    errors.append("pattern formalization invented")
internal = docs.get("internal-dependencies.yaml", {})
if set(internal.get("nodes", [])) != feature_ids:
    errors.append("dependency graph node mismatch")
if internal.get("confirmed_edges") or internal.get("cycles"):
    errors.append("unsupported internal dependency")
matrix = docs.get("dependency-matrix.yaml", {}).get("matrix", [])
if len(matrix) != 10 or any(len(row) != 10 or any(value != 0 for value in row) for row in matrix):
    errors.append("dependency matrix mismatch")

external = docs.get("external-domain-dependencies.yaml", {}).get("dependencies", [])
by_domain = {item["domain"]: item for item in external}
for domain in ("capacities", "competencies", "lived_experience"):
    if by_domain.get(domain, {}).get("authority_status") != "external_non_reconciled":
        errors.append(f"{domain} must remain external_non_reconciled")
    if by_domain.get(domain, {}).get("confirmed_feature_edges"):
        errors.append(f"{domain} has unsupported confirmed feature edge")

readiness = docs.get("production-readiness.yaml", {})
for key in (
    "ready_for_full_contract_generation",
    "ready_for_ir_generation",
    "ready_for_implementation_planning",
    "ready_for_code_generation",
):
    if readiness.get(key) is not False:
        errors.append(f"{key} must remain false")
manifest = docs.get("preparation-manifest.yaml", {})
if manifest.get("preparation_status") != "preparation_complete_with_reservations":
    errors.append("preparation status mismatch")
if any(manifest.get("non_invention", {}).get(key) != 0 for key in (
    "contracts_created", "irs_created", "optimizations_created", "implementations_created"
)):
    errors.append("forbidden output claimed")

changed = set(git("diff", "--name-only", "origin/main...HEAD"))
changed.update(git("diff", "--name-only"))
changed.update(git("ls-files", "--others", "--exclude-standard"))
outside = [
    path for path in changed
    if path and not any(path == prefix or path.startswith(prefix) for prefix in ALLOWED)
]
if outside:
    errors.append(f"out-of-scope paths: {outside}")
if any(path.startswith("registry/math-contracts/TLC-FC-13-") for path in changed):
    errors.append("final Practice contract created")
if any(path.startswith("ir/TLC-FC-13-") for path in changed):
    errors.append("final Practice IR created")
generated_text = "\n".join(
    path.read_text(encoding="utf-8-sig").lower()
    for path in [*REG.glob("*"), *REP.glob("*")]
    if path.is_file()
)
if any(token in generated_text for token in ("#include <", "pybind11", "bindings python")):
    errors.append("implementation artifact detected")

if errors:
    print("Practice preparation validation: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Practice preparation validation: PASSED")
print("- objects=93 relations=92 unresolved=60 duplicate_candidates=0")
print("- features=10 contract_plans=10 ir_plans=10")
print("- YAML=17 reports=17 formal_patterns=0")
print("- final_contracts=0 final_irs=0 optimization=0 implementation=0")
