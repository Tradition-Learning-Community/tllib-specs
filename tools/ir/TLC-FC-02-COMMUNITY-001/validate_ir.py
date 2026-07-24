#!/usr/bin/env python3
"""Structural validator for the candidate IR of TLC-FC-02-COMMUNITY-001."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required to validate IR artifacts") from exc

FEATURE = "TLC-FC-02-COMMUNITY-001"
SOURCE_COMMIT = "2e0858acc21bd97fe6c59db50b2598fb73971e52"
ROOT = Path(__file__).resolve().parents[3]
IR_DIR = ROOT / "ir" / FEATURE
REPORT_DIR = ROOT / "reports" / "ir" / FEATURE
CONTRACT_DIR = ROOT / "registry" / "math-contracts" / FEATURE
ALLOWED_NODE_KINDS = {
    "Entity", "State", "Input", "Output", "Parameter", "Constant", "Scalar",
    "Tensor", "Vector", "Matrix", "Set", "Graph", "Function", "Operator",
    "Constraint", "Metric", "Invariant", "RandomVariable", "StochasticProcess",
    "DifferentialEquation", "IntegrationStep", "Conditional", "Loop", "Reduction",
    "Projection", "Transformation", "StateUpdate", "OpaqueValue", "OpaqueOperator",
    "Validation", "ErrorCondition",
}
ALLOWED_CLASSIFICATIONS = {
    "normative_from_contract", "derived_without_semantic_change", "structural_encoding",
    "engineering_choice_required", "unresolved",
}
EXPECTED_UNRESOLVED = {
    "UNRES-MEASURE", "UNRES-COHERENCE", "UNRES-ACTOR-DOMAIN", "UNRES-OUTPUT"
}
EXPECTED_CONSTRAINTS = {
    "CON-C1-SUBSET", "CON-C1-MEASURE", "CON-C1-MEMBERSHIP", "CON-C1-COHERENCE",
    "PRE-INPUTS-CANDIDATE", "POST-TRACEABLE", "INV-OBJECT-DISTINCT",
}
REQUIRED_YAML = [
    IR_DIR / "ir-open-questions.yaml", IR_DIR / "ir-coverage.yaml",
    IR_DIR / "implementation-decisions-required.yaml", REPORT_DIR / "decision_required.yaml",
]
FORBIDDEN = re.compile(
    r"\b(?:pybind11|numpy|Eigen|std::|float|double|int32|int64|Runge.Kutta|Euler(?:\s+step)?|"
    r"Python\s+type|C\+\+\s+type|CUDA|OpenCL)\b", re.I
)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def main() -> int:
    errors: list[str] = []
    json_paths = sorted(IR_DIR.glob("*.json"))
    require([path.name for path in json_paths] == ["ir-semantic.candidate.json"],
            "exactly the justified semantic candidate JSON must be present", errors)
    documents = []
    for path in json_paths:
        try:
            with path.open(encoding="utf-8") as stream:
                documents.append((path, json.load(stream)))
        except Exception as exc:
            errors.append(f"invalid JSON {path}: {exc}")

    yaml_docs = {}
    for path in REQUIRED_YAML:
        try:
            yaml_docs[path.name] = load_yaml(path)
        except Exception as exc:
            errors.append(f"invalid YAML {path}: {exc}")

    for path, doc in documents:
        require(doc.get("feature_id") == FEATURE, f"wrong feature_id in {path}", errors)
        require(doc.get("status") == "engineering_candidate", f"wrong status in {path}", errors)
        provenance = doc.get("provenance", {})
        require(provenance.get("source_contract_commit") == SOURCE_COMMIT,
                f"wrong source contract commit in {path}", errors)
        require(bool(doc.get("source_traceability")), f"missing traceability in {path}", errors)
        validation = doc.get("validation", {})
        require(validation.get("scientific_validation") == "pending", "scientific status changed", errors)
        require(validation.get("source_contract_ready_for_ir") is False, "source readiness changed", errors)
        require(validation.get("contains_unresolved") is True, "unresolved flag missing", errors)
        require(validation.get("ready_for_code_generation") is False, "code generation enabled", errors)

        nodes = doc.get("nodes", [])
        node_ids = [node.get("node_id") for node in nodes]
        require(len(node_ids) == len(set(node_ids)), "duplicate node_id", errors)
        ports = {}
        for node in nodes:
            require(node.get("node_kind") in ALLOWED_NODE_KINDS,
                    f"invalid node kind {node.get('node_kind')}", errors)
            require(node.get("classification") in ALLOWED_CLASSIFICATIONS,
                    f"invalid node classification on {node.get('node_id')}", errors)
            local_ports = []
            for direction in ("input_ports", "output_ports"):
                for port in node.get(direction, []):
                    port_id = port.get("port_id")
                    require(port_id not in ports and port_id not in local_ports,
                            f"duplicate port_id {port_id}", errors)
                    local_ports.append(port_id)
                    ports[port_id] = (node.get("node_id"), direction)

        edge_ids = []
        for edge in doc.get("edges", []):
            edge_ids.append(edge.get("edge_id"))
            require(edge.get("source_node") in node_ids, f"unknown edge source {edge}", errors)
            require(edge.get("target_node") in node_ids, f"unknown edge target {edge}", errors)
            require(edge.get("classification") in ALLOWED_CLASSIFICATIONS,
                    f"invalid edge classification {edge.get('edge_id')}", errors)
            source_port, target_port = edge.get("source_port"), edge.get("target_port")
            if source_port is not None:
                require(ports.get(source_port) == (edge.get("source_node"), "output_ports"),
                        f"incoherent source port {source_port}", errors)
            if target_port is not None:
                require(ports.get(target_port) == (edge.get("target_node"), "input_ports"),
                        f"incoherent target port {target_port}", errors)
        require(len(edge_ids) == len(set(edge_ids)), "duplicate edge_id", errors)
        represented_constraints = {item.get("constraint_id") for item in doc.get("contract_constraints", [])}
        require(represented_constraints == EXPECTED_CONSTRAINTS,
                f"contract constraint coverage differs: {represented_constraints}", errors)
        for item in doc.get("contract_constraints", []):
            require(item.get("classification") in ALLOWED_CLASSIFICATIONS,
                    f"invalid constraint classification {item.get('constraint_id')}", errors)
            require(set(item.get("applies_to_nodes", [])) <= set(node_ids),
                    f"constraint references unknown node {item.get('constraint_id')}", errors)
        unresolved = {item.get("unresolved_id") for item in doc.get("unresolved_properties", [])}
        require(unresolved == EXPECTED_UNRESOLVED, f"IR unresolved mismatch: {unresolved}", errors)

    questions = yaml_docs.get("ir-open-questions.yaml", {}) or {}
    question_ids = {item.get("question_id") for item in questions.get("questions", [])}
    require(question_ids == EXPECTED_UNRESOLVED, f"open questions mismatch: {question_ids}", errors)
    coverage = yaml_docs.get("ir-coverage.yaml", {}) or {}
    summary = coverage.get("coverage_summary", {})
    require(summary.get("missing") == 0, "coverage has missing elements", errors)
    require(summary.get("total_contract_elements") == len(coverage.get("contract_elements", [])),
            "coverage summary total mismatch", errors)
    require(all(item.get("coverage_status") != "missing" for item in coverage.get("contract_elements", [])),
            "coverage entry is missing", errors)
    decision = yaml_docs.get("decision_required.yaml", {}) or {}
    require(set(decision.get("unresolved_propagated", [])) == EXPECTED_UNRESOLVED,
            "decision report does not propagate every unresolved", errors)
    require(decision.get("ready_for_code_generation") is False, "decision report enables code generation", errors)

    source_open = load_yaml(CONTRACT_DIR / "open-math-questions.yaml")
    source_unresolved = {item.get("question_id") for item in source_open.get("questions", [])}
    require(source_unresolved == EXPECTED_UNRESOLVED, "source unresolved set changed", errors)

    scope_roots = [IR_DIR, REPORT_DIR, Path(__file__).resolve().parent]
    for scope_root in scope_roots:
        for path in scope_root.iterdir():
            if path.is_file() and path.resolve() != Path(__file__).resolve():
                text = path.read_text(encoding="utf-8")
                require(not FORBIDDEN.search(text), f"forbidden implementation term in {path}", errors)
    for base in (ROOT / "ir", ROOT / "reports" / "ir", ROOT / "tools" / "ir"):
        if base.exists():
            others = [p.name for p in base.iterdir() if p.is_dir() and p.name != FEATURE]
            require(not others, f"other feature IR directories present under {base}: {others}", errors)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED: semantic IR, references, coverage, unresolved propagation, and exclusions are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
