#!/usr/bin/env python3
"""Validate the candidate IR for TLC-FC-08-PRINCIPLE-002."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required to validate YAML artifacts") from exc

FEATURE = "TLC-FC-08-PRINCIPLE-002"
COMMIT = "3db96ff560ff110ccd0a0fbf7e30997ac3264aa7"
ROOT = Path(__file__).resolve().parents[3]
IR_DIR = ROOT / "ir" / FEATURE
REPORT_DIR = ROOT / "reports" / "ir" / FEATURE
TOOL_DIR = ROOT / "tools" / "ir" / FEATURE

NODE_KINDS = {
    "Entity", "State", "Input", "Output", "Parameter", "Constant", "Scalar",
    "Tensor", "Vector", "Matrix", "Set", "Graph", "Function", "Operator",
    "Constraint", "Metric", "Invariant", "RandomVariable", "StochasticProcess",
    "DifferentialEquation", "IntegrationStep", "Conditional", "Loop", "Reduction",
    "Projection", "Transformation", "StateUpdate", "OpaqueValue", "OpaqueOperator",
    "Validation", "ErrorCondition",
}
CLASSIFICATIONS = {
    "normative_from_contract", "derived_without_semantic_change", "structural_encoding",
    "engineering_choice_required", "unresolved",
}
DEPENDENCIES = {"data", "control", "state", "constraint", "validation", "temporal", "stochastic", "semantic", "unresolved"}
REQUIRED_VARIANTS = {"semantic", "functional", "dynamic"}
CONTRACT_ELEMENTS = {
    "TLC-SO-PRINCIPLE-087", "SYM-P", "SYM-D", "SYM-t", "SYM-E", "SYM-dPdt",
    "EQ-PRINCIPLE-EVOLUTION-001", "POST-EQUATION-SATISFIED-001", "COMP-E-ARGS-001",
    "oracle_basis", "UNRESOLVED-SYMBOL-SEMANTICS-001", "UNRESOLVED-DOMAIN-001",
    "UNRESOLVED-INITIAL-CONDITION-001", "IMPL-DEC-001", "IMPL-DEC-002",
}
CONTRACT_UNRESOLVED = {
    "UNRESOLVED-SYMBOL-SEMANTICS-001", "UNRESOLVED-DOMAIN-001",
    "UNRESOLVED-INITIAL-CONDITION-001",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def validate_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        data = json.load(stream)
    if data.get("feature_id") != FEATURE:
        fail(f"{path}: wrong feature_id")
    if data.get("status") != "engineering_candidate":
        fail(f"{path}: wrong status")
    provenance = data.get("provenance", {})
    if provenance.get("source_contract_commit") != COMMIT:
        fail(f"{path}: wrong contract commit")
    validation = data.get("validation", {})
    if validation.get("ready_for_code_generation") is not False:
        fail(f"{path}: ready_for_code_generation must be false")
    if validation.get("scientific_validation") != "pending":
        fail(f"{path}: scientific validation must be pending")
    if not data.get("source_traceability"):
        fail(f"{path}: source traceability missing")

    nodes = data.get("nodes", [])
    node_ids = [node.get("node_id") for node in nodes]
    if None in node_ids or len(node_ids) != len(set(node_ids)):
        fail(f"{path}: node_id values must be present and unique")
    ports: dict[str, tuple[str, str]] = {}
    for node in nodes:
        if node.get("node_kind") not in NODE_KINDS:
            fail(f"{path}: invalid node kind {node.get('node_kind')}")
        if node.get("classification") not in CLASSIFICATIONS:
            fail(f"{path}: invalid node classification")
        for collection, direction in (("input_ports", "input"), ("output_ports", "output")):
            for port in node.get(collection, []):
                port_id = port.get("port_id")
                if not port_id or port_id in ports:
                    fail(f"{path}: port_id values must be present and globally unique")
                if port.get("direction") != direction:
                    fail(f"{path}: inconsistent port direction for {port_id}")
                ports[port_id] = (node["node_id"], direction)

    edge_ids: set[str] = set()
    for edge in data.get("edges", []):
        edge_id = edge.get("edge_id")
        if not edge_id or edge_id in edge_ids:
            fail(f"{path}: edge_id values must be present and unique")
        edge_ids.add(edge_id)
        if edge.get("classification") not in CLASSIFICATIONS:
            fail(f"{path}: invalid edge classification")
        if edge.get("dependency_kind") not in DEPENDENCIES:
            fail(f"{path}: invalid dependency kind")
        source = edge.get("source_node")
        target = edge.get("target_node")
        if source not in node_ids or target not in node_ids:
            fail(f"{path}: edge references a missing node")
        source_port = edge.get("source_port")
        target_port = edge.get("target_port")
        if ports.get(source_port) != (source, "output"):
            fail(f"{path}: invalid source port {source_port}")
        if ports.get(target_port) != (target, "input"):
            fail(f"{path}: invalid target port {target_port}")

    if set(data.get("unresolved_properties", [])) != CONTRACT_UNRESOLVED:
        fail(f"{path}: contract unresolved items not exactly propagated")
    text = path.read_text(encoding="utf-8")
    banned = [r"\bpybind11\b", r"\bstd::", r"\bfloat\b", r"\bdouble\b", r"\bNumPy\b", r"Runge.Kutta", r"Euler method"]
    for pattern in banned:
        if re.search(pattern, text, re.IGNORECASE):
            fail(f"{path}: banned target-language or unauthorized numerical term: {pattern}")
    if any(node.get("node_kind") in {"IntegrationStep", "StateUpdate"} for node in nodes):
        fail(f"{path}: unauthorized integration or state-update node")
    return data


def main() -> int:
    expected = {
        IR_DIR / "ir-semantic.candidate.json", IR_DIR / "ir-functional.candidate.json",
        IR_DIR / "ir-dynamic.candidate.json", IR_DIR / "ir-comparison.md",
        IR_DIR / "ir-validation-report.md", IR_DIR / "ir-open-questions.yaml",
        IR_DIR / "ir-coverage.yaml", IR_DIR / "implementation-decisions-required.yaml",
        REPORT_DIR / "ir-report.md", REPORT_DIR / "decision_required.yaml",
        TOOL_DIR / "README.md",
    }
    missing_files = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
    if missing_files:
        fail(f"missing required artifacts: {missing_files}")

    json_files = sorted(IR_DIR.glob("*.json"))
    variants = {validate_json(path)["variant"] for path in json_files}
    if variants != REQUIRED_VARIANTS:
        fail(f"variant set mismatch: {variants}")
    if (IR_DIR / "ir-compute.candidate.json").exists():
        fail("compute variant is not authorized by the contract")

    yaml_files = sorted(IR_DIR.glob("*.yaml")) + [REPORT_DIR / "decision_required.yaml"]
    for path in yaml_files:
        if load_yaml(path) is None:
            fail(f"{path}: empty YAML")

    questions = load_yaml(IR_DIR / "ir-open-questions.yaml")
    question_ids = {item["question_id"] for item in questions.get("questions", [])}
    if question_ids != CONTRACT_UNRESOLVED:
        fail("open questions do not exactly propagate contract unresolved items")
    if any(item.get("status") != "unresolved" for item in questions["questions"]):
        fail("all open questions must remain unresolved")

    coverage = load_yaml(IR_DIR / "ir-coverage.yaml")
    references = "\n".join(item["contract_reference"] for item in coverage.get("contract_elements", []))
    absent = {element for element in CONTRACT_ELEMENTS if element not in references}
    if absent:
        fail(f"contract coverage missing elements: {sorted(absent)}")
    summary = coverage.get("coverage_summary", {})
    if summary.get("missing") != 0:
        fail("coverage summary contains missing elements")
    if summary.get("total_contract_elements") != len(coverage.get("contract_elements", [])):
        fail("coverage summary count is inconsistent")

    decision = load_yaml(REPORT_DIR / "decision_required.yaml")
    if decision.get("feature_id") != FEATURE or decision.get("source_contract_commit") != COMMIT:
        fail("decision report provenance mismatch")
    if decision.get("ready_for_code_generation") is not False:
        fail("decision report must not authorize code generation")

    allowed_roots = {IR_DIR.resolve(), REPORT_DIR.resolve(), TOOL_DIR.resolve()}
    for path in [*json_files, *yaml_files, *expected]:
        resolved = path.resolve()
        if not any(root == resolved or root in resolved.parents for root in allowed_roots):
            fail(f"artifact outside feature scope: {path}")

    print(f"IR VALIDATION PASSED feature={FEATURE} variants={','.join(sorted(variants))} json={len(json_files)} yaml={len(yaml_files)} coverage_missing=0 unresolved={len(question_ids)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"IR VALIDATION FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
