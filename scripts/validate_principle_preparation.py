from __future__ import annotations

from pathlib import Path
import ast
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/principle"
REP = ROOT / "reports/domain-progress/principle"
SCI = ROOT / "registry/scientific-objects/principle"
PREFIX = "TLC-FC-08-PRINCIPLE-"
BASELINE = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"

REQUIRED_YAML = {
    "source-inventory.yaml", "scientific-inventory.yaml", "relation-inventory.yaml",
    "principle-semantics.yaml", "concept-separation.yaml", "functional-coverage.yaml",
    "feature-classification.yaml", "external-domain-dependencies.yaml", "internal-dependencies.yaml",
    "unresolved-analysis.yaml", "historical-artifact-assessment.yaml", "contract-production-plan.yaml",
    "ir-production-plan.yaml", "production-readiness.yaml", "preparation-manifest.yaml",
}
REQUIRED_REPORTS = {f"{n:02d}-{slug}.md" for n, slug in enumerate([
    "source-inventory", "scientific-inventory", "relation-inventory", "principle-semantics",
    "concept-separation", "functional-coverage", "feature-classification", "external-dependencies",
    "internal-dependencies", "unresolved-analysis", "historical-artifacts", "production-order",
    "contract-production-plan", "ir-production-plan", "production-readiness", "preparation-manifest",
    "final-report"], 1)}
errors: list[str] = []


def load(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")
        return {}


actual_yaml = {p.name for p in REG.glob("*.yaml")}
actual_reports = {p.name for p in REP.glob("*.md")}
errors += [f"missing registry: {x}" for x in sorted(REQUIRED_YAML - actual_yaml)]
errors += [f"missing report: {x}" for x in sorted(REQUIRED_REPORTS - actual_reports)]
docs = {p.name: load(p) for p in REG.glob("*.yaml")}

source_objects = load(SCI / "scientific-objects.candidate.yaml").get("objects", [])
source_relations = load(SCI / "scientific-relations.candidate.yaml").get("relations", [])
source_unresolved = load(SCI / "unresolved-terms.yaml").get("unresolved_terms", [])
source_duplicates = load(SCI / "duplicate-candidates.yaml").get("duplicate_candidates", [])
catalogue = load(ROOT / "registry/features/revised/feature-candidates.yaml").get("features", [])
expected_features = {f["candidate_feature_id"] for f in catalogue if f["candidate_feature_id"].startswith(PREFIX)}
expected_objects = {x["provisional_object_id"] for x in source_objects}
expected_relations = {x["provisional_relation_id"] for x in source_relations}
expected_unresolved = {x["unresolved_id"] for x in source_unresolved}

if (len(source_objects), len(source_relations), len(source_unresolved), len(source_duplicates), len(expected_features)) != (103, 102, 54, 3, 10):
    errors.append("canonical Principle counts differ from 103 objects / 102 relations / 54 unresolved / 3 duplicates / 10 features")

inventory_objects = {x["provisional_object_id"] for x in docs.get("scientific-inventory.yaml", {}).get("objects", [])}
inventory_relations = {x["provisional_relation_id"] for x in docs.get("relation-inventory.yaml", {}).get("relations", [])}
inventory_unresolved = {x["unresolved_id"] for x in docs.get("unresolved-analysis.yaml", {}).get("items", [])}
if inventory_objects != expected_objects:
    errors.append("object inventory coverage mismatch")
if inventory_relations != expected_relations:
    errors.append("relation inventory coverage mismatch")
if inventory_unresolved != expected_unresolved:
    errors.append("unresolved coverage mismatch")

all_ids = list(inventory_objects) + list(inventory_relations) + list(inventory_unresolved)
if len(all_ids) != len(set(all_ids)):
    errors.append("duplicate preparation identifier")
for rel in docs.get("relation-inventory.yaml", {}).get("relations", []):
    if rel.get("source_object") not in expected_objects or rel.get("target_object") not in expected_objects:
        errors.append(f"invalid relation object reference: {rel.get('provisional_relation_id')}")

for name in ["functional-coverage.yaml", "feature-classification.yaml", "contract-production-plan.yaml",
             "ir-production-plan.yaml", "production-readiness.yaml"]:
    actual = {x["feature_id"] for x in docs.get(name, {}).get("features", [])}
    if actual != expected_features:
        errors.append(f"{name} feature coverage mismatch")

contracts = docs.get("contract-production-plan.yaml", {})
irs = docs.get("ir-production-plan.yaml", {})
if contracts.get("planned_contracts") != len(expected_features) or contracts.get("catalogue_features") != len(expected_features):
    errors.append("planned_contracts must equal catalogue features")
if irs.get("planned_irs") != len(expected_features) or irs.get("catalogue_features") != len(expected_features):
    errors.append("planned_irs must equal catalogue features")
if contracts.get("contracts_created") != 0 or irs.get("irs_created") != 0:
    errors.append("preparation claims a definitive contract or IR")

semantics = docs.get("principle-semantics.yaml", {})
for key in ["formulation", "scope", "application_domain", "computational_character", "mechanical_validation"]:
    if key not in semantics:
        errors.append(f"missing Principle semantic dimension: {key}")
separations = docs.get("concept-separation.yaml", {}).get("separations", [])
if len(separations) != 17 or any(x.get("classification") not in {
    "explicit_equivalence", "explicit_non_equivalence", "distinct_by_source_type", "provisional_distinction",
    "candidate_relation", "unresolved", "not_applicable"} for x in separations):
    errors.append("concept separation must cover 17 requested pairs with authorized classifications")

external = docs.get("external-domain-dependencies.yaml", {}).get("dependencies", [])
expected_domains = {"master", "disciple", "community", "huit_dimensions", "invariants", "dynamics", "theorems",
                    "message", "values", "virtues", "capacities", "competencies", "practice", "lived_experience", "relations"}
if {x.get("domain") for x in external} != expected_domains:
    errors.append("external dependency domain coverage mismatch")
if docs.get("external-domain-dependencies.yaml", {}).get("parallel_authority_used") is not False:
    errors.append("parallel branch authority guard missing")

graph = docs.get("internal-dependencies.yaml", {})
if set(graph.get("nodes", [])) != expected_features:
    errors.append("internal graph node coverage mismatch")
edges = graph.get("confirmed_edges", []) + graph.get("candidate_edges", []) + graph.get("unresolved_edges", [])
for edge in edges:
    if edge.get("source") not in expected_features or edge.get("target") not in expected_features:
        errors.append("internal graph edge references unknown feature")
if graph.get("cycles"):
    errors.append("unexpected asserted feature cycle")

pilot = docs.get("historical-artifact-assessment.yaml", {})
if pilot.get("modified_by_preparation") is not False or pilot.get("classification") != "comparison_only":
    errors.append("historical Principle pilot must remain unmodified and comparison-only")

manifest = docs.get("preparation-manifest.yaml", {})
for field in ["contracts_created", "irs_created", "cpp_created", "python_bindings_created"]:
    if manifest.get(field) != 0:
        errors.append(f"manifest guard failed: {field}")
if manifest.get("working_base_commit") != BASELINE:
    errors.append("preparation baseline mismatch")

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
for path in [ROOT / "scripts/validate_principle_preparation.py"]:
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except Exception as exc:
        errors.append(f"invalid Python {path.name}: {exc}")

diff = subprocess.run(["git", "diff", "--name-only", "origin/main...HEAD"], cwd=ROOT, text=True, capture_output=True)
# During pre-commit validation include working-tree paths as well.
status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, text=True, capture_output=True)
paths = {line[3:].strip().replace("\\", "/") for line in status.stdout.splitlines() if len(line) >= 4}
paths.update(x.strip().replace("\\", "/") for x in diff.stdout.splitlines() if x.strip())
allowed = lambda p: (p.startswith("registry/domain-progress/principle/") or
                     p.startswith("reports/domain-progress/principle/") or
                     p == "scripts/validate_principle_preparation.py")
bad_paths = sorted(p for p in paths if p and not allowed(p) and p != "scripts/_generate_principle_preparation.py")
if bad_paths:
    errors.append(f"out-of-scope files: {bad_paths}")

if errors:
    print("PRINCIPLE PREPARATION VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PRINCIPLE PREPARATION VALIDATION PASSED")
print(f"baseline={BASELINE} features={len(expected_features)} objects={len(expected_objects)} "
      f"relations={len(expected_relations)} unresolved={len(expected_unresolved)} duplicates={len(source_duplicates)}")
print(f"registry_yaml={len(actual_yaml)} reports={len(actual_reports)} cycles=0 contracts_created=0 irs_created=0")
print("historical_pilot_modified=false parallel_authority_used=false other_domains_modified=false")
