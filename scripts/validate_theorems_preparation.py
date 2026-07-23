#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FEATURE_IDS = {f"TLC-FC-06-THEOREMS-{i:03d}" for i in range(1, 10)}
OBJECT_IDS = {f"TLC-SO-THEOREMS-{i:03d}" for i in range(1, 31)}
RELATION_IDS = {f"TLC-SR-THEOREMS-{i:03d}" for i in range(1, 30)}
UNRESOLVED_IDS = {f"TLC-UT-THEOREMS-{i:03d}" for i in range(1, 13)}
REG = ROOT / "registry/domain-progress/theorems"
REP = ROOT / "reports/domain-progress/theorems"

EXPECTED_YAML = {
    "community-dependencies.yaml", "concept-separation.yaml", "contract-production-plan.yaml",
    "disciple-dependencies.yaml", "dynamics-dependencies.yaml", "external-domain-dependencies.yaml",
    "feature-classification.yaml", "feature-dependencies.yaml", "feature-inventory.yaml",
    "feature-status.yaml", "functional-coverage.yaml", "future-reconciliation.yaml",
    "global-manifest-update-proposal.yaml", "historical-artifact-assessment.yaml",
    "huit-dimensions-dependencies.yaml", "invariants-dependencies.yaml", "ir-production-plan.yaml",
    "master-dependencies.yaml", "message-principle-dependencies.yaml", "preparation-status.yaml",
    "production-gates.yaml", "production-order.yaml", "proof-dependency-graph.yaml",
    "proof-inventory.yaml", "result-semantics.yaml", "scientific-coverage.yaml",
    "source-inventory.yaml", "unresolved-status.yaml", "upstream-symbol-mapping.yaml",
}
EXPECTED_REPORTS = {
    "community-dependency-report.md", "concept-separation-report.md",
    "contract-production-plan-report.md", "disciple-dependency-report.md",
    "domain-preparation-report.md", "dynamics-dependency-report.md",
    "external-domain-dependency-report.md", "feature-classification-report.md",
    "feature-dependency-report.md", "feature-inventory-report.md",
    "functional-coverage-report.md", "historical-artifact-assessment.md",
    "huit-dimensions-dependency-report.md", "invariants-dependency-report.md",
    "ir-production-plan-report.md", "master-dependency-report.md",
    "message-principle-dependency-report.md", "production-order-report.md",
    "proof-dependency-graph-report.md", "proof-inventory-report.md",
    "result-semantics-report.md", "scientific-coverage-report.md",
    "source-inventory-report.md", "unresolved-report.md",
    "upstream-symbol-reconciliation-report.md",
}
CONTRACT_GATES = {
    "no_external_gate", "master_symbols_available", "disciple_symbols_available",
    "community_symbols_required", "huit_dimensions_symbols_required", "invariants_symbols_required",
    "invariants_contract_required", "dynamics_symbols_required", "dynamics_contract_required",
    "message_symbols_required", "principle_symbols_required", "proof_source_required",
    "multiple_domains_required", "unresolved_but_contract_plannable",
    "local_scientific_decision_required", "missing_source_evidence", "not_yet_assessable",
}
IR_GATES = {
    "contract_validated", "master_symbol_available", "disciple_symbol_available",
    "community_symbol_available", "huit_dimensions_symbol_available", "invariants_contract_available",
    "invariants_ir_available", "dynamics_contract_available", "dynamics_ir_available",
    "proof_source_available", "multiple_dependencies_available",
    "local_scientific_decision_required", "not_yet_assessable",
}
PREPARATION_CLASSES = {
    "theorem_declaration_contract", "proposition_declaration_contract", "lemma_declaration_contract",
    "proof_structure_contract", "proof_validation_contract", "implication_contract",
    "equivalence_contract", "invariant_theorem_contract", "dynamic_property_theorem_contract",
    "structural_contract", "relational_contract", "validation_contract",
    "non_computational_contract", "not_yet_determinable",
}
ALLOWED_PREFIXES = (
    "registry/domain-progress/theorems/", "reports/domain-progress/theorems/",
    "scripts/prepare_theorems_domain.py", "scripts/validate_theorems_preparation.py",
)


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def unique(items, key: str, label: str, errors: list[str]) -> set:
    values = [x.get(key) for x in items]
    if None in values or len(values) != len(set(values)):
        errors.append(f"{label} identifiers are missing or duplicated")
    return set(values)


def changed_paths() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) >= 4]


def main() -> int:
    errors: list[str] = []
    yaml_names = {p.name for p in REG.glob("*.yaml")}
    if yaml_names != EXPECTED_YAML:
        errors.append(f"YAML artifact set mismatch missing={sorted(EXPECTED_YAML-yaml_names)} extra={sorted(yaml_names-EXPECTED_YAML)}")
    report_names = {p.name for p in REP.glob("*.md")}
    if report_names != EXPECTED_REPORTS:
        errors.append(f"report set mismatch missing={sorted(EXPECTED_REPORTS-report_names)} extra={sorted(report_names-EXPECTED_REPORTS)}")
    docs = {}
    for path in REG.glob("*.yaml"):
        try:
            docs[path.name] = load(path)
        except Exception as exc:
            errors.append(f"YAML parse {path.name}: {exc}")
    json_files = list(REG.glob("*.json")) + list(REP.glob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            errors.append(f"JSON parse {path}: {exc}")

    canonical_objects = load(ROOT / "registry/scientific-objects/theorems/scientific-objects.candidate.yaml")["objects"]
    canonical_relations = load(ROOT / "registry/scientific-objects/theorems/scientific-relations.candidate.yaml")["relations"]
    canonical_unresolved = load(ROOT / "registry/scientific-objects/theorems/unresolved-terms.yaml")["unresolved_terms"]
    if {x["provisional_object_id"] for x in canonical_objects} != OBJECT_IDS:
        errors.append("canonical object identifiers")
    if {x["provisional_relation_id"] for x in canonical_relations} != RELATION_IDS:
        errors.append("canonical relation identifiers")
    if {x["unresolved_id"] for x in canonical_unresolved} != UNRESOLVED_IDS:
        errors.append("canonical unresolved identifiers")

    inv = docs.get("source-inventory.yaml", {})
    if inv.get("objects", {}).get("found") != 30 or inv.get("relations", {}).get("found") != 29 or inv.get("unresolved", {}).get("found") != 12:
        errors.append("source inventory counts")
    logical = inv.get("logical_elements", {})
    if logical.get("theorems") != 7 or logical.get("propositions") != 0 or logical.get("lemmas") != 0 or logical.get("corollaries") != 0:
        errors.append("logical element counts")
    if logical.get("complete_proofs") != 0 or logical.get("partial_proofs") != 6 or logical.get("missing_proofs") != 1:
        errors.append("proof counts")

    sci = docs.get("scientific-coverage.yaml", {})
    sci_elements = sci.get("elements", [])
    covered_objects = {x.get("element_id") for x in sci_elements if x.get("element_kind") == "scientific_object"}
    covered_relations = {x.get("element_id") for x in sci_elements if x.get("element_kind") == "scientific_relation"}
    if covered_objects != OBJECT_IDS or covered_relations != RELATION_IDS:
        errors.append("scientific coverage")

    features = docs.get("feature-inventory.yaml", {}).get("features", [])
    if unique(features, "feature_id", "feature inventory", errors) != FEATURE_IDS:
        errors.append("feature inventory coverage")
    feature_summary = docs.get("feature-inventory.yaml", {}).get("summary", {})
    if any(feature_summary.get(k) != v for k, v in {"catalogue_features": 9, "inventoried_features": 9, "missing_features": 0, "orphan_features": 0}.items()):
        errors.append("feature inventory summary")
    catalogue = (ROOT / "reports/functional-decomposition/feature-catalog.md").read_text(encoding="utf-8-sig")
    catalogue_ids = set(re.findall(r"TLC-FC-06-THEOREMS-\d{3}", catalogue))
    if catalogue_ids != FEATURE_IDS:
        errors.append("catalogue membership")

    functional = docs.get("functional-coverage.yaml", {}).get("mappings", [])
    functional_ids = {x.get("source_element_id") for x in functional}
    if not OBJECT_IDS <= functional_ids or not RELATION_IDS <= functional_ids or not UNRESOLVED_IDS <= functional_ids:
        errors.append("functional coverage")

    results = docs.get("result-semantics.yaml", {}).get("results", [])
    if len(results) != 7 or unique(results, "result_id", "result semantics", errors) != {f"RESULT-THEOREMS-{i:03d}" for i in range(1, 8)}:
        errors.append("result semantics coverage")
    if any(x.get("result_kind") != "theorem" for x in results):
        errors.append("result kind separation")
    if any(x.get("execution_status") != "structurally_representable_not_executable" for x in results):
        errors.append("result execution claims")

    proof_doc = docs.get("proof-inventory.yaml", {})
    proofs = proof_doc.get("proofs", [])
    if len(proofs) != 6 or unique(proofs, "proof_id", "proof inventory", errors) != {f"PROOF-THEOREMS-{i:03d}" for i in range(1, 7)}:
        errors.append("proof inventory coverage")
    if any(x.get("proof_completeness") != "partial" or x.get("proof_kind") != "not_specified" or x.get("mechanical_check_possible") is not False for x in proofs):
        errors.append("proof non-invention")
    if len(proof_doc.get("missing_proofs", [])) != 1:
        errors.append("missing proof preservation")

    concepts = docs.get("concept-separation.yaml", {}).get("concepts", [])
    required_concepts = {"theorem", "proposition", "lemma", "corollary", "axiom", "hypothesis", "assumption", "definition", "invariant", "constraint", "empirical_claim", "example", "proof", "algorithm", "validation_rule"}
    if {x.get("source_term") for x in concepts} != required_concepts:
        errors.append("concept separation")

    for name in ["master-dependencies.yaml", "disciple-dependencies.yaml", "community-dependencies.yaml", "huit-dimensions-dependencies.yaml", "invariants-dependencies.yaml", "dynamics-dependencies.yaml", "message-principle-dependencies.yaml", "external-domain-dependencies.yaml"]:
        if name not in docs:
            errors.append(f"dependency artifact {name}")

    graph = docs.get("feature-dependencies.yaml", {})
    if graph.get("edges") != [] or graph.get("summary", {}).get("cycles") != []:
        errors.append("internal dependency graph review preservation")
    proof_graph = docs.get("proof-dependency-graph.yaml", {})
    if len(proof_graph.get("nodes", [])) != 13 or len(proof_graph.get("edges", [])) != 6 or proof_graph.get("summary", {}).get("cycles") != 0:
        errors.append("proof dependency graph")

    feature_classes = docs.get("feature-classification.yaml", {}).get("features", [])
    if unique(feature_classes, "feature_id", "feature classification", errors) != FEATURE_IDS:
        errors.append("classification coverage")
    if any(x.get("primary_classification") not in PREPARATION_CLASSES for x in feature_classes):
        errors.append("classification vocabulary")

    contract_plans = docs.get("contract-production-plan.yaml", {}).get("features", [])
    ir_plans = docs.get("ir-production-plan.yaml", {}).get("features", [])
    status_rows = docs.get("feature-status.yaml", {}).get("features", [])
    if unique(contract_plans, "feature_id", "contract plan", errors) != FEATURE_IDS:
        errors.append("contract plan coverage")
    if unique(ir_plans, "feature_id", "IR plan", errors) != FEATURE_IDS:
        errors.append("IR plan coverage")
    if unique(status_rows, "feature_id", "feature status", errors) != FEATURE_IDS:
        errors.append("feature status coverage")
    if any(x.get("contract_generation_gate") not in CONTRACT_GATES or x.get("code_generation_readiness_expected") is not False for x in contract_plans):
        errors.append("contract plan gates/readiness")
    if any(x.get("ir_generation_gate") not in IR_GATES or x.get("code_generation_readiness_expected") is not False for x in ir_plans):
        errors.append("IR plan gates/readiness")

    unresolved_rows = docs.get("unresolved-status.yaml", {}).get("unresolved", [])
    if unique(unresolved_rows, "unresolved_id", "unresolved status", errors) != UNRESOLVED_IDS:
        errors.append("unresolved coverage")
    if any(x.get("propagation_strategy") != "preserve_unresolved" or x.get("human_decision_required") is not True for x in unresolved_rows):
        errors.append("unresolved preservation")

    historical = docs.get("historical-artifact-assessment.yaml", {})
    if historical.get("historical_artifact_status") != "no_historical_artifact" or historical.get("modified") is not False or historical.get("promoted") is not False:
        errors.append("historical artifact assessment")
    gates = docs.get("production-gates.yaml", {})
    if gates.get("ready_for_ir_generation") is not False or gates.get("ready_for_proof_mechanical_verification") is not False or gates.get("ready_for_implementation_planning") is not False or gates.get("ready_for_code_generation") is not False:
        errors.append("production gate readiness")
    preparation = docs.get("preparation-status.yaml", {})
    if preparation.get("preparation_status") != "preparation_complete_with_reservations" or preparation.get("contracts_produced") != 0 or preparation.get("irs_produced") != 0 or preparation.get("proofs_invented") != 0:
        errors.append("preparation status")

    changed = changed_paths()
    out_of_scope = [p for p in changed if not any(p == prefix or p.startswith(prefix) for prefix in ALLOWED_PREFIXES)]
    if out_of_scope:
        errors.append(f"out-of-scope paths: {out_of_scope}")
    if any(p.startswith("registry/math-contracts/TLC-FC-06-THEOREMS-") for p in changed):
        errors.append("Theorems contract created")
    if any(p.startswith("ir/TLC-FC-06-THEOREMS-") for p in changed):
        errors.append("Theorems IR created")
    generated_text = "\n".join(p.read_text(encoding="utf-8-sig") for p in list(REG.glob("*")) + list(REP.glob("*")) if p.is_file()).lower()
    if any(term in generated_text for term in ("#include <", "pybind11", "bindings python")):
        errors.append("implementation artifact detected")

    if errors:
        print("THEOREMS PREPARATION VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("THEOREMS PREPARATION VALIDATION PASSED")
    print("objects=30 relations=29 unresolved=12 features=9 results=7 proofs=6 missing_proofs=1")
    print(f"yaml={len(EXPECTED_YAML)} reports={len(EXPECTED_REPORTS)} contracts_created=0 irs_created=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
