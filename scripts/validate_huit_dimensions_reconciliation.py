#!/usr/bin/env python3
"""Validate reconciliation against current origin/main without scientific adjudication."""
from pathlib import Path
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/huit-dimensions"
REP = ROOT / "reports/domain-progress/huit-dimensions"
BASELINE = "d8e616c71173495b9a014d4a5909df9f30e2a7ae"
ALLOWED = (
    "registry/domain-progress/huit-dimensions/",
    "reports/domain-progress/huit-dimensions/",
    "scripts/validate_huit_dimensions_preparation.py",
    "scripts/validate_huit_dimensions_reconciliation.py",
)


def read_yaml(name):
    with (REG / name).open(encoding="utf-8-sig") as stream:
        return yaml.safe_load(stream)


def git(*args):
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8"
    ).splitlines()


errors = []
yaml_files = list(REG.glob("*.yaml"))
report_files = list(REP.glob("*.md"))
for path in yaml_files:
    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
        json.dumps(document, ensure_ascii=False)
        if document.get("baseline_commit") != BASELINE:
            errors.append(f"stale baseline: {path.name}")
    except Exception as exc:
        errors.append(f"invalid YAML/JSON model {path.name}: {exc}")
for path in report_files:
    if not path.read_text(encoding="utf-8-sig").strip():
        errors.append(f"empty report: {path.name}")

source = read_yaml("source-inventory.yaml")
coverage = read_yaml("scientific-coverage.yaml")["coverage"]
inventory = read_yaml("feature-inventory.yaml")
functional = read_yaml("functional-coverage.yaml")
contract_plan = read_yaml("contract-production-plan.yaml")
ir_plan = read_yaml("ir-production-plan.yaml")
unresolved = read_yaml("unresolved-status.yaml")
dependencies = read_yaml("feature-dependencies.yaml")
status = read_yaml("preparation-status.yaml")
community = read_yaml("community-dependencies.yaml")
reconciliation = read_yaml("reconciliation-report.yaml")

expected = {
    "objects": 118,
    "relations": 117,
    "unresolved_terms": 68,
    "duplicate_candidates": 9,
}
for key, value in expected.items():
    if source["scientific_registries"][key] != value:
        errors.append(f"source inventory mismatch: {key}")
    if coverage[key]["accounted_for"] != value or not coverage[key]["complete"]:
        errors.append(f"scientific coverage mismatch: {key}")
if inventory["active_feature_count"] != 11:
    errors.append("feature inventory must contain 11 revised features")
feature_ids = {item["feature_id"] for item in inventory["features"]}
if len(feature_ids) != 11:
    errors.append("feature IDs must be unique")
if {item["feature_id"] for item in functional["features"]} != feature_ids:
    errors.append("functional coverage differs from feature inventory")
if {item["feature_id"] for item in contract_plan["plans"]} != feature_ids:
    errors.append("contract plans do not cover all features")
if set(ir_plan["feature_sequence"]) != feature_ids:
    errors.append("IR plan does not cover all features")
if unresolved["source_unresolved_count"] != 68 or "none are silently closed" not in unresolved["policy"]:
    errors.append("all 68 unresolved records must be preserved")
if dependencies["edges"] or dependencies["cycles"]:
    errors.append("unsubstantiated internal dependencies present")
if reconciliation["recovered_files"] != 43:
    errors.append("recovered file count mismatch")
if reconciliation["deleted_files"] or reconciliation["abandoned_files"]:
    errors.append("recovered files were deleted or abandoned")
if community.get("upstream_authority_status") != "canonical_complete_to_ir_with_reservations":
    errors.append("Community handoff authority is stale")
for key in (
    "ready_for_full_contract_generation",
    "ready_for_ir_generation",
    "ready_for_implementation_planning",
    "ready_for_code_generation",
):
    if status[key] is not False:
        errors.append(f"{key} must remain false")

changed = set(git("diff", "--name-only", "origin/main...HEAD"))
changed.update(git("diff", "--name-only"))
changed.update(git("ls-files", "--others", "--exclude-standard"))
outside = [
    path for path in changed
    if path and not any(path == prefix or path.startswith(prefix) for prefix in ALLOWED)
]
if outside:
    errors.append(f"out-of-scope paths: {outside}")
if any(path.startswith("registry/math-contracts/TLC-FC-03-") for path in changed):
    errors.append("final contract created")
if any(path.startswith("ir/TLC-FC-03-") for path in changed):
    errors.append("final IR created")
text = "\n".join(
    path.read_text(encoding="utf-8-sig").lower()
    for path in [*REG.glob("*"), *REP.glob("*")]
    if path.is_file()
)
if any(token in text for token in ("#include <", "pybind11", "bindings python")):
    errors.append("implementation artifact detected")

if errors:
    print("Huit Dimensions reconciliation validation: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Huit Dimensions reconciliation validation: PASSED")
print(f"- YAML registries: {len(yaml_files)}; Markdown reports: {len(report_files)}")
print("- scientific coverage: 118 objects, 117 relations, 68 unresolved, 9 duplicates")
print("- functional coverage: 11 features, 11 contract plans, 11 IR plans")
print("- recovered: 43; deleted: 0; abandoned: 0")
