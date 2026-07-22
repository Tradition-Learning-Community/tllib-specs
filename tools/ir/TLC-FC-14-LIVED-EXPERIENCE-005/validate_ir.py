#!/usr/bin/env python3
"""Structural validator for TLC-FC-14-LIVED-EXPERIENCE-005 candidate IR."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml


FEATURE = "TLC-FC-14-LIVED-EXPERIENCE-005"
CONTRACT = "TLC-MC-TLC-FC-14-LIVED-EXPERIENCE-005"
SOURCE_COMMIT = "1ff27ea31bae784a64ac3eee534404ce2ce322fa"
EXPECTED_VARIANTS = {"semantic", "functional"}
EXPECTED_UNRESOLVED = {
    "UNRES-SYNERGY",
    "UNRES-N",
    "UNRES-EXPERIENCE-TYPE",
    "UNRES-SIGMA",
}
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
FORBIDDEN_IR_TERMS = {
    "c++", "pybind11", "float", "double", "numpy", "torch", "solver",
    "euler", "runge-kutta", "gpu", "cpu backend",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    root = Path(__file__).resolve().parents[3]
    ir_dir = root / "ir" / FEATURE
    contract_dir = root / "registry" / "math-contracts" / FEATURE
    report_dir = root / "reports" / "ir" / FEATURE
    errors: list[str] = []

    json_paths = sorted(ir_dir.glob("ir-*.candidate.json"))
    if {p.stem.split(".")[0].removeprefix("ir-") for p in json_paths} != EXPECTED_VARIANTS:
        fail(errors, "expected exactly semantic and functional candidate JSON variants")

    documents = []
    global_nodes: set[tuple[str, str]] = set()
    global_ports: set[tuple[str, str]] = set()
    total_edges = 0
    for path in json_paths:
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(errors, f"invalid JSON {path}: {exc}")
            continue
        documents.append(doc)
        variant = doc.get("variant")
        if doc.get("feature_id") != FEATURE:
            fail(errors, f"wrong feature_id in {path}")
        if doc.get("status") != "engineering_candidate":
            fail(errors, f"wrong status in {path}")
        provenance = doc.get("provenance", {})
        if provenance.get("source_contract_commit") != SOURCE_COMMIT:
            fail(errors, f"wrong source contract commit in {path}")
        if provenance.get("source_contract_id") != CONTRACT:
            fail(errors, f"wrong source contract id in {path}")
        validation = doc.get("validation", {})
        if validation.get("ready_for_code_generation") is not False:
            fail(errors, f"ready_for_code_generation must be false in {path}")
        if validation.get("source_contract_ready_for_ir") is not False:
            fail(errors, f"source_contract_ready_for_ir must be false in {path}")
        if validation.get("progression_mode") != "candidate_with_preserved_reservations":
            fail(errors, f"wrong progression mode in {path}")
        if not doc.get("source_traceability"):
            fail(errors, f"missing traceability in {path}")

        nodes = doc.get("nodes", [])
        node_ids = [node.get("node_id") for node in nodes]
        if len(node_ids) != len(set(node_ids)):
            fail(errors, f"duplicate node_id in {path}")
        node_map = {node["node_id"]: node for node in nodes if node.get("node_id")}
        ports: dict[str, tuple[str, str]] = {}
        for node in nodes:
            node_id = node.get("node_id")
            global_nodes.add((variant, node_id))
            if node.get("node_kind") not in ALLOWED_NODE_KINDS:
                fail(errors, f"invalid node_kind {node.get('node_kind')} in {path}")
            if node.get("classification") not in ALLOWED_CLASSIFICATIONS:
                fail(errors, f"invalid node classification in {node_id}")
            if not node.get("source_contract_reference"):
                fail(errors, f"missing contract traceability in {node_id}")
            for direction, key in (("input", "input_ports"), ("output", "output_ports")):
                for port in node.get(key, []):
                    port_id = port.get("port_id")
                    if port_id in ports:
                        fail(errors, f"duplicate port_id {port_id} in {path}")
                    ports[port_id] = (node_id, direction)
                    global_ports.add((variant, port_id))

        edge_ids: set[str] = set()
        for edge in doc.get("edges", []):
            total_edges += 1
            edge_id = edge.get("edge_id")
            if edge_id in edge_ids:
                fail(errors, f"duplicate edge_id {edge_id} in {path}")
            edge_ids.add(edge_id)
            source = edge.get("source_node")
            target = edge.get("target_node")
            if source not in node_map or target not in node_map:
                fail(errors, f"edge {edge_id} references missing node")
            source_port = edge.get("source_port")
            target_port = edge.get("target_port")
            if source_port is not None and ports.get(source_port) != (source, "output"):
                fail(errors, f"edge {edge_id} has invalid source port")
            if target_port is not None and ports.get(target_port) != (target, "input"):
                fail(errors, f"edge {edge_id} has invalid target port")
            if edge.get("classification") not in ALLOWED_CLASSIFICATIONS:
                fail(errors, f"invalid edge classification in {edge_id}")

        unresolved = {item.get("unresolved_id") for item in doc.get("unresolved_properties", [])}
        if unresolved != EXPECTED_UNRESOLVED:
            fail(errors, f"unresolved propagation mismatch in {path}: {sorted(unresolved)}")
        for item in doc.get("unresolved_properties", []):
            for node_id in item.get("affected_nodes", []):
                if node_id not in node_map:
                    fail(errors, f"unresolved {item.get('unresolved_id')} references missing node {node_id}")
            for edge_id in item.get("affected_edges", []):
                if edge_id not in edge_ids:
                    fail(errors, f"unresolved {item.get('unresolved_id')} references missing edge {edge_id}")

        lower = path.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN_IR_TERMS:
            if term in lower:
                fail(errors, f"forbidden target or numerical term {term!r} in {path}")

    yaml_paths = [
        ir_dir / "ir-open-questions.yaml",
        ir_dir / "ir-coverage.yaml",
        ir_dir / "implementation-decisions-required.yaml",
        report_dir / "decision_required.yaml",
    ]
    for path in yaml_paths:
        try:
            data = load_yaml(path)
        except Exception as exc:
            fail(errors, f"invalid YAML {path}: {exc}")
            continue
        if data.get("feature_id") != FEATURE:
            fail(errors, f"wrong feature_id in {path}")
        if data.get("source_contract_commit") != SOURCE_COMMIT:
            fail(errors, f"wrong source contract commit in {path}")

    coverage = load_yaml(ir_dir / "ir-coverage.yaml")
    summary = coverage.get("coverage_summary", {})
    rows = coverage.get("contract_elements", [])
    if summary.get("total_contract_elements") != len(rows):
        fail(errors, "coverage total does not match rows")
    if summary.get("missing") != 0:
        fail(errors, "coverage contains missing elements")
    if sum(summary.get(key, 0) for key in ("fully_represented", "represented_as_opaque", "unresolved", "omitted_with_justification", "missing")) != len(rows):
        fail(errors, "coverage summary counts do not add up")
    required_refs = {
        "TLC-SO-LIVED-EXPERIENCE-065",
        "SYM-ELL-SET", "SYM-ELL-COL",
        "SYM-ELL-I", "SYM-N", "SYM-I",
        "SYM-SIGMA", "SYM-SYNERGY",
        "EQ-COLLECTIVE-MEMORY", "UNRES-N",
        "UNRES-EXPERIENCE-TYPE", "UNRES-SIGMA", "POST-TRACEABLE",
        "UNRES-SYNERGY", "UNRES-N",
        "UNRES-EXPERIENCE-TYPE", "IMPL-COLLECTION",
        "IMPL-TYPE-MAPPING", "COV-EQUATION", "dependencies", "oracle_basis",
    }
    coverage_refs = {row.get("contract_reference") for row in rows}
    if coverage_refs != required_refs:
        fail(errors, f"contract coverage reference mismatch: {sorted(required_refs - coverage_refs)}")

    contract = load_yaml(contract_dir / "contract.yaml")
    if contract.get("feature_id") != FEATURE or contract.get("contract_id") != CONTRACT:
        fail(errors, "source contract mismatch")
    if set(contract.get("unresolved_items", [])) != EXPECTED_UNRESOLVED:
        fail(errors, "source contract unresolved set changed")

    try:
        changed = subprocess.run(
            ["git", "diff", "--name-only", SOURCE_COMMIT], cwd=root,
            check=True, capture_output=True, text=True,
        ).stdout.splitlines()
        allowed_prefixes = (f"ir/{FEATURE}/", f"reports/ir/{FEATURE}/", f"tools/ir/{FEATURE}/")
        foreign = [path for path in changed if not path.startswith(allowed_prefixes)]
        if foreign:
            fail(errors, f"out-of-scope changed paths: {foreign}")
    except Exception as exc:
        fail(errors, f"unable to verify git scope: {exc}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED")
    print(f"feature={FEATURE} variants={','.join(sorted(EXPECTED_VARIANTS))}")
    print(f"json_files={len(json_paths)} yaml_files={len(yaml_paths)} nodes={len(global_nodes)} ports={len(global_ports)} edges={total_edges}")
    print(f"unresolved={len(EXPECTED_UNRESOLVED)} coverage={len(rows)} missing=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
