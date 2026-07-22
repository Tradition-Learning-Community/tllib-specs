#!/usr/bin/env python3
"""Strict validation for the Invariants preparation-only deliverable."""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
BASELINE = "448e01170e123472f3c82b60fff076242ec4a093"
PREFIX = "TLC-FC-04-INVARIANTS-"
REG = ROOT / "registry/domain-progress/invariants"
REP = ROOT / "reports/domain-progress/invariants"
errors: list[str] = []


def read_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"YAML parse failure: {path.relative_to(ROOT)}: {exc}")
        return {}


required_yaml = [
    "source-inventory.yaml", "scientific-coverage.yaml", "feature-inventory.yaml", "functional-coverage.yaml",
    "invariant-semantics.yaml", "concept-separation.yaml", "master-dependencies.yaml", "disciple-dependencies.yaml",
    "community-dependencies.yaml", "huit-dimensions-dependencies.yaml", "dynamics-dependencies.yaml",
    "theorems-dependencies.yaml", "external-domain-dependencies.yaml", "upstream-symbol-mapping.yaml",
    "feature-dependencies.yaml", "feature-classification.yaml", "production-order.yaml",
    "contract-production-plan.yaml", "ir-production-plan.yaml", "unresolved-status.yaml",
    "historical-artifact-assessment.yaml", "production-gates.yaml", "feature-status.yaml",
    "future-reconciliation.yaml", "global-manifest-update-proposal.yaml", "preparation-status.yaml",
]
required_reports = [
    "source-inventory-report.md", "scientific-coverage-report.md", "feature-inventory-report.md",
    "functional-coverage-report.md", "invariant-semantics-report.md", "concept-separation-report.md",
    "master-dependency-report.md", "disciple-dependency-report.md", "community-dependency-report.md",
    "huit-dimensions-dependency-report.md", "dynamics-dependency-report.md", "theorems-dependency-report.md",
    "external-domain-dependency-report.md", "upstream-symbol-reconciliation-report.md",
    "feature-dependency-report.md", "feature-classification-report.md", "production-order-report.md",
    "contract-production-plan-report.md", "ir-production-plan-report.md", "unresolved-report.md",
    "historical-artifact-assessment.md", "domain-preparation-report.md",
]

for name in required_yaml:
    path = REG / name
    if not path.exists():
        errors.append(f"Missing required registry: {path.relative_to(ROOT)}")
    else:
        read_yaml(path)
for name in required_reports:
    if not (REP / name).exists():
        errors.append(f"Missing required report: {(REP / name).relative_to(ROOT)}")
for path in REG.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON parse failure: {path.relative_to(ROOT)}: {exc}")

objects = read_yaml(ROOT / "registry/scientific-objects/invariants/scientific-objects.candidate.yaml")["objects"]
relations = read_yaml(ROOT / "registry/scientific-objects/invariants/scientific-relations.candidate.yaml")["relations"]
unresolved = read_yaml(ROOT / "registry/scientific-objects/invariants/unresolved-terms.yaml")["unresolved_terms"]
catalogue = read_yaml(ROOT / "registry/features/feature-candidates.yaml")["features"]
expected_features = sorted(x["candidate_feature_id"] for x in catalogue if x["candidate_feature_id"].startswith(PREFIX))

if len(expected_features) != len(set(expected_features)):
    errors.append("Duplicate Invariants feature IDs in canonical catalogue")
object_ids = [x["provisional_object_id"] for x in objects]
relation_ids = [x["provisional_relation_id"] for x in relations]
unresolved_ids = [x["unresolved_id"] for x in unresolved]
for label, values in (("object", object_ids), ("relation", relation_ids), ("unresolved", unresolved_ids)):
    if len(values) != len(set(values)):
        errors.append(f"Duplicate Invariants {label} IDs")
if any(x["source_object_id"] not in object_ids or x["target_object_id"] not in object_ids for x in relations):
    errors.append("Relation references an absent Invariants object")

inventory = read_yaml(REG / "source-inventory.yaml")
expected_counts = (len(objects), len(relations), len(unresolved), len(expected_features))
actual_counts = (inventory["objects"]["found"], inventory["relations"]["found"], inventory["unresolved"]["found"],
    read_yaml(REG / "feature-inventory.yaml")["catalogue_features"])
if actual_counts != expected_counts:
    errors.append(f"Inventory count mismatch: expected {expected_counts}, got {actual_counts}")

scientific = read_yaml(REG / "scientific-coverage.yaml")
if len(scientific["objects"]) != len(objects) or len(scientific["relations"]) != len(relations):
    errors.append("Scientific object/relation coverage is incomplete")
functional = read_yaml(REG / "functional-coverage.yaml")
if len(functional["objects"]) != len(objects) or len(functional["relations"]) != len(relations) or len(functional["unresolved"]) != len(unresolved):
    errors.append("Functional coverage matrix is incomplete")

feature_inventory = read_yaml(REG / "feature-inventory.yaml")["features"]
feature_status = read_yaml(REG / "feature-status.yaml")["features"]
classifications = read_yaml(REG / "feature-classification.yaml")["features"]
contract_plans = read_yaml(REG / "contract-production-plan.yaml")
ir_plans = read_yaml(REG / "ir-production-plan.yaml")
for label, values in (
    ("feature inventory", [x["feature_id"] for x in feature_inventory]),
    ("feature status", [x["feature_id"] for x in feature_status]),
    ("classification", [x["feature_id"] for x in classifications]),
    ("contract plan", [x["feature_id"] for x in contract_plans["plans"]]),
    ("IR plan", [x["feature_id"] for x in ir_plans["plans"]]),
):
    if sorted(values) != expected_features:
        errors.append(f"Incomplete {label} coverage")
if contract_plans["contracts_produced"] != 0 or ir_plans["irs_produced"] != 0:
    errors.append("Preparation incorrectly claims produced contracts or IRs")

semantics = read_yaml(REG / "invariant-semantics.yaml")
expected_invariants = sum(x["object_type"] == "Invariant" for x in objects)
if len(semantics["invariants"]) != expected_invariants:
    errors.append("Invariant semantics does not cover every extracted Invariant object")
separation = read_yaml(REG / "concept-separation.yaml")
required_terms = {"invariant", "constraint", "axiom", "hypothesis", "theorem", "validation_rule"}
if not required_terms.issubset({x["source_term"] for x in separation["terms"]}):
    errors.append("Concept-separation matrix is incomplete")

for name in ("master", "disciple", "community", "huit-dimensions", "dynamics", "theorems"):
    path = REG / f"{name}-dependencies.yaml"
    if not path.exists():
        errors.append(f"Missing {name} dependency analysis")
external = read_yaml(REG / "external-domain-dependencies.yaml")
if len(external["domains"]) != 9:
    errors.append("Other-domain dependency audit must cover nine domains")
graph = read_yaml(REG / "feature-dependencies.yaml")
for edge in graph["edges"]:
    if edge["from_feature_id"] not in expected_features or edge["to_feature_id"] not in expected_features:
        errors.append("Internal dependency edge references an unknown feature")

unresolved_status = read_yaml(REG / "unresolved-status.yaml")["unresolved"]
if sorted(x["unresolved_id"] for x in unresolved_status) != sorted(unresolved_ids):
    errors.append("Unresolved status coverage is incomplete")
gates = read_yaml(REG / "production-gates.yaml")
if gates["ready_for_ir_generation"] or gates["ready_for_implementation_planning"] or gates["ready_for_code_generation"]:
    errors.append("Forbidden readiness gate is true")
preparation = read_yaml(REG / "preparation-status.yaml")
if preparation["preparation_status"] not in {"preparation_complete", "preparation_complete_with_reservations"}:
    errors.append("Preparation status is not complete")
history = read_yaml(REG / "historical-artifact-assessment.yaml")
if history["contracts_found"] or history["irs_found"]:
    errors.append("Historical contract/IR claim conflicts with canonical repository")

if list((ROOT / "registry/math-contracts").glob("TLC-FC-04-INVARIANTS-*")):
    errors.append("An Invariants contract directory was created")
if list((ROOT / "ir").glob("TLC-FC-04-INVARIANTS-*")):
    errors.append("An Invariants IR directory was created")

diff = subprocess.run(["git", "diff", "--name-only", BASELINE], cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()
allowed_prefixes = ("registry/domain-progress/invariants/", "reports/domain-progress/invariants/")
allowed_files = {"scripts/validate_invariants_preparation.py"}
for path in diff:
    normalized = path.replace("\\", "/")
    if not normalized.startswith(allowed_prefixes) and normalized not in allowed_files:
        errors.append(f"Out-of-scope modified file: {normalized}")
    if normalized.startswith(("registry/math-contracts/", "ir/", "cpp/", "bindings/")):
        errors.append(f"Forbidden production path modified: {normalized}")
for domain in ("master", "disciple", "community", "huit-dimensions", "dynamics", "theorems"):
    if any(f"domain-progress/{domain}/" in p.replace("\\", "/") for p in diff):
        errors.append(f"Forbidden {domain} domain modification")

try:
    py_compile.compile(str(Path(__file__)), doraise=True)
except Exception as exc:
    errors.append(f"Validator compilation failed: {exc}")

if errors:
    print("Invariants preparation validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(
    f"Invariants preparation validation: PASS "
    f"({len(objects)} objects, {len(relations)} relations, {len(unresolved)} unresolved, {len(expected_features)} features)"
)
