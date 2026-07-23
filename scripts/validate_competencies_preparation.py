from __future__ import annotations

from pathlib import Path
import ast
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/competencies"
REP = ROOT / "reports/domain-progress/competencies"
SCI = ROOT / "registry/scientific-objects/competencies"
PREFIX = "TLC-FC-12-COMPETENCIES-"
BASELINE = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
REQUIRED_YAML = {"source-inventory.yaml", "scientific-inventory.yaml", "relation-inventory.yaml",
    "pattern-analysis.yaml", "feature-catalogue.yaml", "feature-classification.yaml", "external-dependencies.yaml",
    "internal-dependencies.yaml", "unresolved-analysis.yaml", "contract-production-plan.yaml",
    "ir-production-plan.yaml", "production-readiness.yaml", "decision-required.yaml", "coverage-manifest.yaml",
    "preparation-report.yaml"}
REQUIRED_REPORTS = {f"{i:02d}-{name}.md" for i, name in enumerate([
    "source-and-scientific-inventory", "relation-audit", "pattern-analysis", "feature-catalogue",
    "feature-classification", "external-dependencies", "internal-dependencies", "unresolved-analysis",
    "contract-production-plan", "ir-production-plan", "production-readiness", "decision-required",
    "coverage-report", "preparation-report"], 1)}
errors: list[str] = []


def load(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")
        return {}


actual_yaml = {p.name for p in REG.glob("*.yaml")}
actual_reports = {p.name for p in REP.glob("*.md")}
errors += [f"missing YAML: {x}" for x in sorted(REQUIRED_YAML - actual_yaml)]
errors += [f"missing report: {x}" for x in sorted(REQUIRED_REPORTS - actual_reports)]
docs = {p.name: load(p) for p in REG.glob("*.yaml")}

source_objects = load(SCI / "scientific-objects.candidate.yaml").get("objects", [])
source_relations = load(SCI / "scientific-relations.candidate.yaml").get("relations", [])
source_unresolved = load(SCI / "unresolved-terms.yaml").get("unresolved_terms", [])
source_duplicates = load(SCI / "duplicate-candidates.yaml").get("duplicate_candidates", [])
catalogue = load(ROOT / "registry/features/revised/feature-candidates.yaml").get("features", [])
expected_features = {x["candidate_feature_id"] for x in catalogue if x["candidate_feature_id"].startswith(PREFIX)}
expected_objects = {x["provisional_object_id"] for x in source_objects}
expected_relations = {x["provisional_relation_id"] for x in source_relations}
expected_unresolved = {x["unresolved_id"] for x in source_unresolved}

if (len(expected_objects), len(expected_relations), len(expected_unresolved), len(source_duplicates), len(expected_features)) != (114, 113, 67, 3, 13):
    errors.append("canonical count mismatch: expected 114/113/67/3/13")

inventory_objects = docs.get("scientific-inventory.yaml", {}).get("objects", [])
if {x.get("provisional_object_id") for x in inventory_objects} != expected_objects:
    errors.append("object inventory coverage mismatch")
if any(x.get("coverage_kind") not in {"direct_scientific_basis", "context_only_not_functionalized"} for x in inventory_objects):
    errors.append("an object is not accounted in feature coverage")
source_line_count = len((ROOT / "maths/12-competencies.md").read_text(encoding="utf-8").splitlines())
for item in inventory_objects:
    ref = item.get("source_reference") or {}
    start, end = ref.get("start_line"), ref.get("end_line")
    if ref.get("source_path") != "maths/12-competencies.md" or not isinstance(start, int) or not isinstance(end, int) or not (1 <= start <= end <= source_line_count):
        errors.append(f"invalid object source range: {item.get('provisional_object_id')}")
inventory_relations = docs.get("relation-inventory.yaml", {}).get("relations", [])
if {x.get("provisional_relation_id") for x in inventory_relations} != expected_relations:
    errors.append("relation inventory coverage mismatch")
for rel in inventory_relations:
    if rel.get("source_object_id") not in expected_objects or rel.get("target_object_id") not in expected_objects:
        errors.append(f"invalid relation reference: {rel.get('provisional_relation_id')}")
    ref = rel.get("source_reference") or {}
    start, end = ref.get("start_line"), ref.get("end_line")
    if ref.get("source_path") != "maths/12-competencies.md" or not isinstance(start, int) or not isinstance(end, int) or not (1 <= start <= end <= source_line_count):
        errors.append(f"invalid relation source range: {rel.get('provisional_relation_id')}")
inventory_unresolved = docs.get("unresolved-analysis.yaml", {}).get("items", [])
if {x.get("unresolved_id") for x in inventory_unresolved} != expected_unresolved:
    errors.append("unresolved coverage mismatch")
if any(x.get("status") != "unresolved" for x in inventory_unresolved):
    errors.append("an unresolved item was silently resolved")

all_ids = list(expected_objects) + list(expected_relations) + list(expected_unresolved)
if len(all_ids) != len(set(all_ids)):
    errors.append("identifier uniqueness failure")

for name in ["feature-catalogue.yaml", "feature-classification.yaml", "contract-production-plan.yaml",
             "ir-production-plan.yaml", "production-readiness.yaml"]:
    actual = {x.get("feature_id") for x in docs.get(name, {}).get("features", [])}
    if actual != expected_features:
        errors.append(f"{name} feature coverage mismatch")
if docs.get("feature-catalogue.yaml", {}).get("orphan_features"):
    errors.append("orphan feature detected")
contracts = docs.get("contract-production-plan.yaml", {})
irs = docs.get("ir-production-plan.yaml", {})
if contracts.get("planned_contracts") != len(expected_features) or contracts.get("catalogue_features") != len(expected_features):
    errors.append("contract plans do not cover catalogue")
if irs.get("planned_irs") != len(expected_features) or irs.get("catalogue_features") != len(expected_features):
    errors.append("IR plans do not cover catalogue")
if contracts.get("contracts_created") != 0 or irs.get("irs_created") != 0:
    errors.append("final contract or IR claimed")

external = {x.get("domain"): x for x in docs.get("external-dependencies.yaml", {}).get("dependencies", [])}
capacity = external.get("capacities", {})
if capacity.get("status") != "external_unreconciled" or capacity.get("future_reconciliation_required") is not True:
    errors.append("Capacities must remain external_unreconciled")
if docs.get("external-dependencies.yaml", {}).get("parallel_authority_used") is not False:
    errors.append("parallel authority guard missing")
if len(docs.get("pattern-analysis.yaml", {}).get("patterns", [])) < 5:
    errors.append("pattern analysis incomplete")
if not docs.get("decision-required.yaml", {}).get("questions"):
    errors.append("decision-required questions missing")

graph = docs.get("internal-dependencies.yaml", {})
if set(graph.get("nodes", [])) != expected_features:
    errors.append("dependency graph node mismatch")
if graph.get("cycles"):
    errors.append("unexpected asserted cycle")

manifest = docs.get("coverage-manifest.yaml", {})
if manifest.get("objects", {}).get("accounted") != len(expected_objects):
    errors.append("object accounting incomplete")
if manifest.get("relations", {}).get("accounted") != len(expected_relations):
    errors.append("relation accounting incomplete")
if manifest.get("unresolved", {}).get("accounted") != len(expected_unresolved):
    errors.append("unresolved accounting incomplete")
for key in ["final_contracts_created", "final_irs_created", "cpp_created", "bindings_created"]:
    if manifest.get(key) != 0:
        errors.append(f"forbidden output claimed: {key}")

for path in REG.glob("*.yaml"):
    load(path)
for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
try:
    ast.parse((ROOT / "scripts/validate_competencies_preparation.py").read_text(encoding="utf-8"))
except Exception as exc:
    errors.append(f"invalid validator Python: {exc}")

status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, text=True, capture_output=True)
diff = subprocess.run(["git", "diff", "--name-only", "origin/main...HEAD"], cwd=ROOT, text=True, capture_output=True)
paths = {line[3:].strip().replace("\\", "/") for line in status.stdout.splitlines() if len(line) >= 4}
paths.update(x.strip().replace("\\", "/") for x in diff.stdout.splitlines() if x.strip())
allowed = lambda p: (p.startswith("registry/domain-progress/competencies/") or
                     p.startswith("reports/domain-progress/competencies/") or
                     p == "scripts/validate_competencies_preparation.py")
bad = sorted(p for p in paths if p and not allowed(p) and p != "scripts/_generate_competencies_preparation.py")
if bad:
    errors.append(f"out-of-scope paths: {bad}")

if errors:
    print("COMPETENCIES PREPARATION VALIDATION FAILED")
    print("\n".join(f"- {x}" for x in errors))
    sys.exit(1)
print("COMPETENCIES PREPARATION VALIDATION PASSED")
print(f"baseline={BASELINE} objects={len(expected_objects)} relations={len(expected_relations)} "
      f"unresolved={len(expected_unresolved)} duplicates={len(source_duplicates)} features={len(expected_features)}")
print(f"yaml={len(actual_yaml)} reports={len(actual_reports)} contract_plans={len(expected_features)} "
      f"ir_plans={len(expected_features)} orphans=0 cycles=0")
print("capacities=external_unreconciled contracts_created=0 irs_created=0 other_domains_modified=false")
