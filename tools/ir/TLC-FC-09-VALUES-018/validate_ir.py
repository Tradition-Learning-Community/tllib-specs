#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

FEATURE = "TLC-FC-09-VALUES-018"
SOURCE_COMMIT = "7daa8758945e63feb0e64a2865acbb43dfab75dd"
ROOT = Path(__file__).resolve().parents[3]
IR_DIR = ROOT / "ir" / FEATURE
NODE_KINDS = {"Entity", "State", "Input", "Output", "Parameter", "Constant", "Scalar", "Tensor", "Vector", "Matrix", "Set", "Graph", "Function", "Operator", "Constraint", "Metric", "Invariant", "RandomVariable", "StochasticProcess", "DifferentialEquation", "IntegrationStep", "Conditional", "Loop", "Reduction", "Projection", "Transformation", "StateUpdate", "OpaqueValue", "OpaqueOperator", "Validation", "ErrorCondition"}
CLASSIFICATIONS = {"normative_from_contract", "derived_without_semantic_change", "structural_encoding", "engineering_choice_required", "unresolved"}
DEPENDENCIES = {"data", "control", "state", "constraint", "validation", "temporal", "stochastic", "semantic", "unresolved"}
EXPECTED_UNRESOLVED = {"UNRES-M", "UNRES-ENDPOINTS", "UNRES-CATEGORIES", "UNRES-OUTPUT"}
FORBIDDEN = ("pybind11", "std::", "numpy", "float32", "float64", "double", "cuda", "euler", "runge-kutta")
ALLOWED_PREFIXES = (f"ir/{FEATURE}/", f"reports/ir/{FEATURE}/", f"tools/ir/{FEATURE}/")


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def collect_classifications(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"classification", "derivation_classification"}:
                yield item
            yield from collect_classifications(item)
    elif isinstance(value, list):
        for item in value:
            yield from collect_classifications(item)


def changed_paths():
    result = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=ROOT, text=True, capture_output=True, check=False)
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) >= 4]


def main() -> int:
    errors = []
    json_paths = sorted(IR_DIR.glob("ir-*.candidate.json"))
    if {p.name for p in json_paths} != {"ir-semantic.candidate.json", "ir-functional.candidate.json"}:
        errors.append("candidate variant set")
    documents = []
    for path in json_paths:
        try:
            documents.append(json.loads(path.read_text(encoding="utf-8")))
        except Exception as exc:
            errors.append(f"JSON {path.name}: {exc}")

    all_node_ids, all_edge_ids = set(), set()
    for doc in documents:
        if doc.get("feature_id") != FEATURE or doc.get("status") != "engineering_candidate":
            errors.append(f"identity/status {doc.get('ir_id')}")
        if doc.get("provenance", {}).get("source_contract_commit") != SOURCE_COMMIT:
            errors.append(f"source commit {doc.get('ir_id')}")
        validation = doc.get("validation", {})
        if validation.get("ready_for_code_generation") is not False or validation.get("source_contract_ready_for_ir") is not False or validation.get("contains_unresolved") is not True:
            errors.append(f"readiness {doc.get('ir_id')}")
        if set(doc.get("unresolved_properties", [])) != EXPECTED_UNRESOLVED:
            errors.append(f"unresolved propagation {doc.get('ir_id')}")
        nodes = doc.get("nodes", [])
        node_ids = [node.get("node_id") for node in nodes]
        if len(node_ids) != len(set(node_ids)) or None in node_ids:
            errors.append(f"node ids {doc.get('ir_id')}")
        all_node_ids.update(node_ids)
        ports = {}
        for node in nodes:
            if node.get("node_kind") not in NODE_KINDS:
                errors.append(f"node kind {node.get('node_id')}")
            for port in node.get("input_ports", []) + node.get("output_ports", []):
                port_id = port.get("port_id")
                if port_id in ports or port_id is None:
                    errors.append(f"port id {doc.get('ir_id')}:{port_id}")
                ports[port_id] = node.get("node_id")
        edges = doc.get("edges", [])
        edge_ids = [edge.get("edge_id") for edge in edges]
        if len(edge_ids) != len(set(edge_ids)) or None in edge_ids:
            errors.append(f"edge ids {doc.get('ir_id')}")
        all_edge_ids.update(edge_ids)
        node_set = set(node_ids)
        for edge in edges:
            if edge.get("source_node") not in node_set or edge.get("target_node") not in node_set:
                errors.append(f"edge node reference {edge.get('edge_id')}")
            if edge.get("source_port") is not None and ports.get(edge.get("source_port")) != edge.get("source_node"):
                errors.append(f"edge source port {edge.get('edge_id')}")
            if edge.get("target_port") is not None and ports.get(edge.get("target_port")) != edge.get("target_node"):
                errors.append(f"edge target port {edge.get('edge_id')}")
            if edge.get("dependency_kind") not in DEPENDENCIES:
                errors.append(f"dependency kind {edge.get('edge_id')}")
        invalid_classes = {x for x in collect_classifications(doc) if x not in CLASSIFICATIONS}
        if invalid_classes:
            errors.append(f"classifications {doc.get('ir_id')}:{sorted(invalid_classes)}")
        lowered = json.dumps(doc, ensure_ascii=False).lower()
        if any(term in lowered for term in FORBIDDEN):
            errors.append(f"forbidden implementation term {doc.get('ir_id')}")

    questions = load_yaml(IR_DIR / "ir-open-questions.yaml")
    question_ids = {q.get("question_id") for q in questions.get("questions", [])}
    if question_ids != EXPECTED_UNRESOLVED or any(q.get("status") != "unresolved" for q in questions.get("questions", [])):
        errors.append("open-question propagation")
    for question in questions.get("questions", []):
        if not set(question.get("affected_nodes", [])) <= all_node_ids or not set(question.get("affected_edges", [])) <= all_edge_ids:
            errors.append(f"question references {question.get('question_id')}")
    coverage = load_yaml(IR_DIR / "ir-coverage.yaml")
    summary = coverage.get("coverage_summary", {})
    if summary.get("missing") != 0 or len(coverage.get("contract_elements", [])) != summary.get("total_contract_elements") or any(row.get("coverage_status") == "missing" for row in coverage.get("contract_elements", [])):
        errors.append("coverage")
    contract = load_yaml(ROOT / "registry" / "math-contracts" / FEATURE / "contract.yaml")
    if contract.get("feature_id") != FEATURE or contract.get("contract_id") != "TLC-MC-TLC-FC-09-VALUES-018" or set(contract.get("unresolved_items", [])) != EXPECTED_UNRESOLVED:
        errors.append("source contract")
    scope_violations = [path for path in changed_paths() if not path.startswith(ALLOWED_PREFIXES)]
    if scope_violations:
        errors.append(f"scope paths {scope_violations}")
    if errors:
        print("IR VALIDATION FAILED: " + "; ".join(errors))
        return 1
    print(f"IR VALIDATION PASSED feature={FEATURE} variants=2 nodes={len(all_node_ids)} edges={len(all_edge_ids)} coverage_missing=0 unresolved=4")
    return 0


if __name__ == "__main__":
    sys.exit(main())
