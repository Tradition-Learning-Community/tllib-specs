#!/usr/bin/env python3
"""Validate Master domain coverage, traceability, parseability, and policy."""

from __future__ import annotations

import json
import py_compile
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
PREFIX = "TLC-FC-00-MASTER-"
errors: list[str] = []


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"YAML parse failed: {path.relative_to(ROOT)}: {exc}")
        return None


for path in ROOT.rglob("*.yaml"):
    if any(part == ".git" for part in path.parts):
        continue
    load_yaml(path)
for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON parse failed: {path.relative_to(ROOT)}: {exc}")
for path in ROOT.rglob("*.py"):
    try:
        py_compile.compile(str(path), doraise=True)
    except Exception as exc:
        errors.append(f"Python compile failed: {path.relative_to(ROOT)}: {exc}")

classification = load_yaml(ROOT / "registry/features/revised/feature-classification.yaml")
expected = sorted(
    item["feature_candidate_id"]
    for item in classification["classifications"]
    if item["feature_candidate_id"].startswith(PREFIX)
)
if len(expected) != len(set(expected)):
    errors.append("Duplicate Master feature IDs in revised classification ledger")

status = load_yaml(ROOT / "registry/domain-progress/master/feature-status.yaml")
actual = sorted(item["feature_id"] for item in status["features"])
if actual != expected:
    errors.append(f"Feature coverage mismatch: expected {len(expected)}, got {len(actual)}")

known_objects = {
    item["provisional_object_id"]
    for item in load_yaml(ROOT / "registry/scientific-objects/master/scientific-objects.candidate.yaml")["objects"]
}
known_relations = {
    item["provisional_relation_id"]
    for item in load_yaml(ROOT / "registry/scientific-objects/master/scientific-relations.candidate.yaml")["relations"]
}
known_unresolved = {
    item["unresolved_id"]
    for item in load_yaml(ROOT / "registry/scientific-objects/master/unresolved-terms.yaml")["unresolved_terms"]
}

for feature_id in expected:
    contract_path = ROOT / f"registry/math-contracts/{feature_id}/contract.yaml"
    ir_path = ROOT / f"ir/{feature_id}/ir.candidate.json"
    coverage_path = ROOT / f"ir/{feature_id}/ir-coverage.yaml"
    for path in [contract_path, ir_path, coverage_path]:
        if not path.exists():
            errors.append(f"Missing artifact: {path.relative_to(ROOT)}")
    if not contract_path.exists() or not ir_path.exists():
        continue
    contract = load_yaml(contract_path)
    ir = json.loads(ir_path.read_text(encoding="utf-8"))
    if contract["feature_id"] != feature_id or ir["feature_id"] != feature_id:
        errors.append(f"Identifier mismatch: {feature_id}")
    if ir["contract_ref"] != contract_path.relative_to(ROOT).as_posix():
        errors.append(f"Contract reference mismatch: {feature_id}")
    if not set(contract["input_objects"]).issubset(known_objects):
        errors.append(f"Unknown scientific object reference: {feature_id}")
    if not set(contract["relations"]).issubset(known_relations):
        errors.append(f"Unknown scientific relation reference: {feature_id}")
    extracted_unresolved = {x for x in contract["unresolved"] if x.startswith("TLC-UT-")}
    if not extracted_unresolved.issubset(known_unresolved):
        errors.append(f"Unknown extraction unresolved reference: {feature_id}")
    if sorted(contract["unresolved"]) != sorted(ir["unresolved"]):
        errors.append(f"Unresolved propagation mismatch: {feature_id}")
    if contract["ready_for_code_generation"] or ir["ready_for_code_generation"]:
        errors.append(f"Code generation incorrectly enabled: {feature_id}")

domain = load_yaml(ROOT / "registry/domain-progress/master/domain-status.yaml")
if domain["features"]["total"] != len(expected):
    errors.append("Domain feature total does not match revised classification ledger")
if domain["features"]["contract_complete"] != len(expected):
    errors.append("Contract audit incomplete")
if domain["features"]["ir_complete"] != len(expected):
    errors.append("IR audit incomplete")
if domain["ready_for_code_generation"]:
    errors.append("Domain code generation must remain false")

edges = load_yaml(ROOT / "registry/domain-dependencies/domain-dependency-edges.yaml")["dependencies"]
allowed_statuses = {"confirmed", "inferred_candidate", "unresolved"}
if any(edge["dependency_status"] not in allowed_statuses for edge in edges):
    errors.append("Invalid dependency status")
if any(edge["from_domain"] != "master" and edge["dependency_status"] == "confirmed" for edge in edges):
    errors.append("Non-Master lexical dependency was incorrectly confirmed")

if errors:
    print("Master domain validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"Master domain validation: PASS ({len(expected)} features, {len(edges)} dependency edges)")
