#!/usr/bin/env python3
"""Validate the Huit Dimensions preparation package without generating contracts or IR."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/huit-dimensions"
REP = ROOT / "reports/domain-progress/huit-dimensions"

REQUIRED_REGISTRIES = {
    "source-inventory.yaml", "scientific-coverage.yaml", "feature-inventory.yaml",
    "functional-coverage.yaml", "dimension-semantics.yaml", "master-dependencies.yaml",
    "disciple-dependencies.yaml", "community-dependencies.yaml", "invariants-dependencies.yaml",
    "dynamics-dependencies.yaml", "external-domain-dependencies.yaml", "feature-dependencies.yaml",
    "feature-classification.yaml", "production-order.yaml", "contract-production-plan.yaml",
    "ir-production-plan.yaml", "unresolved-status.yaml", "historical-artifact-assessment.yaml",
    "production-gates.yaml", "feature-status.yaml", "global-manifest-update-proposal.yaml",
    "preparation-status.yaml", "future-reconciliation.yaml",
}
REQUIRED_REPORTS = {
    "source-inventory-report.md", "scientific-coverage-report.md", "feature-inventory-report.md",
    "functional-coverage-report.md", "master-dependency-report.md", "disciple-dependency-report.md",
    "community-dependency-report.md", "invariants-dependency-report.md", "dynamics-dependency-report.md",
    "external-domain-dependency-report.md", "feature-dependency-report.md",
    "feature-classification-report.md", "production-order-report.md", "contract-production-plan.md",
    "ir-production-plan.md", "unresolved-report.md", "historical-artifact-assessment.md",
    "domain-preparation-report.md", "future-reconciliation-report.md",
}

def read_yaml(path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)

errors = []
for name in sorted(REQUIRED_REGISTRIES):
    path = REG / name
    if not path.is_file(): errors.append(f"missing registry: {name}")
    else:
        try: read_yaml(path)
        except Exception as exc: errors.append(f"invalid YAML {name}: {exc}")
for name in sorted(REQUIRED_REPORTS):
    path = REP / name
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"missing or empty report: {name}")

if not errors:
    source = read_yaml(REG / "source-inventory.yaml")
    coverage = read_yaml(REG / "scientific-coverage.yaml")["coverage"]
    inventory = read_yaml(REG / "feature-inventory.yaml")
    dependencies = read_yaml(REG / "feature-dependencies.yaml")
    semantics = read_yaml(REG / "dimension-semantics.yaml")
    status = read_yaml(REG / "preparation-status.yaml")
    expected = {"objects": 118, "relations": 117, "unresolved_terms": 68, "duplicate_candidates": 9}
    for key, value in expected.items():
        actual = source["scientific_registries"][key]
        if actual != value: errors.append(f"{key}: expected {value}, got {actual}")
        if coverage[key]["accounted_for"] != value or not coverage[key]["complete"]:
            errors.append(f"incomplete coverage for {key}")
    if inventory["active_feature_count"] != 11: errors.append("active revised feature count must be 11")
    if len({f["feature_id"] for f in inventory["features"]}) != 11: errors.append("feature IDs are not unique")
    if dependencies["edges"] or dependencies["cycles"]: errors.append("unsubstantiated dependency or cycle present")
    if semantics["entities"]["count"] != 8: errors.append("dimension cardinality must remain exactly eight")
    if semantics["vector_space_interpretation_supported"] is not False: errors.append("unsupported vector-space inference")
    required_false = ["ready_for_full_contract_generation", "ready_for_ir_generation",
                      "ready_for_implementation_planning", "ready_for_code_generation"]
    for key in required_false:
        if status[key] is not False: errors.append(f"{key} must be false")
    if status["ready_for_contract_generation_now"] is not True: errors.append("limited contract subset must be marked ready")
    if len(status["independent_ready_feature_ids"]) != 5: errors.append("independent ready subset must contain five features")
    if len(status["reconciliation_required_feature_ids"]) != 6: errors.append("reconciliation subset must contain six features")
    if status["next_task"] != "reconcile_huit_dimensions_after_required_upstream_domains":
        errors.append("unexpected next task")

if errors:
    print("Huit Dimensions preparation validation: FAILED")
    for error in errors: print(f"- {error}")
    sys.exit(1)
print("Huit Dimensions preparation validation: PASSED")
print("- 23 required YAML registries are present and parseable")
print("- 19 required Markdown reports are present")
print("- scientific coverage: 118 objects, 117 relations, 68 unresolved terms, 9 duplicate candidates")
print("- revised feature scope: 11 active; 5 limited-ready; 6 reconciliation-required")
