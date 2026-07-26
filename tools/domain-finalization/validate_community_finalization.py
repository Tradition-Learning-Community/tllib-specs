#!/usr/bin/env python3
"""Validate the Community domain finalization package without executing science."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - explicit CI dependency
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
FEATURES = [
    "TLC-FC-02-COMMUNITY-001",
    "TLC-FC-02-COMMUNITY-003",
    "TLC-FC-02-COMMUNITY-004",
    "TLC-FC-02-COMMUNITY-005",
    "TLC-FC-02-COMMUNITY-006",
    "TLC-FC-02-COMMUNITY-007",
    "TLC-FC-02-COMMUNITY-008",
    "TLC-FC-02-COMMUNITY-009",
]
UNRESOLVED = [f"TLC-UT-COMMUNITY-{number:03d}" for number in range(1, 30)]
SOURCE_OBJECTS = {
    "TLC-FC-02-COMMUNITY-001": ["TLC-SO-COMMUNITY-008"],
    "TLC-FC-02-COMMUNITY-003": ["TLC-SO-COMMUNITY-029", "TLC-SO-COMMUNITY-040", "TLC-SO-COMMUNITY-044"],
    "TLC-FC-02-COMMUNITY-004": ["TLC-SO-COMMUNITY-027", "TLC-SO-COMMUNITY-028", "TLC-SO-COMMUNITY-030"],
    "TLC-FC-02-COMMUNITY-005": ["TLC-SO-COMMUNITY-009", "TLC-SO-COMMUNITY-035", "TLC-SO-COMMUNITY-037", "TLC-SO-COMMUNITY-038", "TLC-SO-COMMUNITY-039"],
    "TLC-FC-02-COMMUNITY-006": ["TLC-SO-COMMUNITY-036"],
    "TLC-FC-02-COMMUNITY-007": ["TLC-SO-COMMUNITY-017", "TLC-SO-COMMUNITY-031"],
    "TLC-FC-02-COMMUNITY-008": ["TLC-SO-COMMUNITY-018", "TLC-SO-COMMUNITY-019", "TLC-SO-COMMUNITY-020"],
    "TLC-FC-02-COMMUNITY-009": ["TLC-SO-COMMUNITY-004", "TLC-SO-COMMUNITY-026", "TLC-SO-COMMUNITY-032"],
}
REQUIRED_FINAL_FILES = [
    "registry/domain-finalization/community/manifest.yaml",
    "registry/domain-finalization/community/feature-status.yaml",
    "registry/domain-finalization/community/patterns.yaml",
    "registry/domain-finalization/community/module-specification.yaml",
    "registry/domain-finalization/community/implementation-tasks.yaml",
    "registry/domain-finalization/community/decision-required.yaml",
    "reports/domain-finalization/community/finalization-report.md",
    "tools/domain-finalization/validate_community_finalization.py",
]
ALLOWED_PREFIXES = (
    "registry/domain-finalization/community/",
    "registry/optimized-ir/community/",
    "registry/algorithms/community/",
    "registry/oracles/community/",
    "reports/domain-finalization/community/",
)
TEMP_WORKFLOW = ".github/workflows/community-finalization-validation.yml"


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_yaml(relative: str) -> Any:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing YAML file: {relative}")
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid YAML {relative}: {exc}")


def load_json(relative: str) -> Any:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing JSON file: {relative}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {relative}: {exc}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def recursive_dicts(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from recursive_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from recursive_dicts(child)


def git(*args: str) -> str:
    process = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if process.returncode != 0:
        fail(f"git {' '.join(args)} failed: {process.stderr.strip()}")
    return process.stdout


def validate_population() -> None:
    manifest = load_yaml("registry/domain-finalization/community/manifest.yaml")
    population = manifest["authoritative_population"]
    require(population["feature_ids"] == FEATURES, "manifest population is not exact")
    require(population["count"] == len(FEATURES), "manifest population count mismatch")
    require(manifest["baseline"]["main_head"] == BASE_SHA, "baseline main HEAD mismatch")
    require(manifest["baseline"]["count_divergence"] is False, "unexpected count divergence")
    require(manifest["unresolved_authoritative"]["exact_ids"] == UNRESOLVED, "manifest unresolved set mismatch")

    domain_matrix = load_yaml("registry/global-reconciliation/domain-feature-matrix.yaml")
    matrix_ids = {
        item.get("feature_id")
        for item in recursive_dicts(domain_matrix)
        if item.get("domain") == "community" and item.get("feature_id")
    }
    require(matrix_ids == set(FEATURES), f"global matrix Community population mismatch: {sorted(matrix_ids)}")

    baseline = load_yaml("registry/global-reconciliation/current-baseline.yaml")
    matching_lists = []
    for item in recursive_dicts(baseline):
        if item.get("domain") == "community":
            for key in ("feature_ids", "features", "active_feature_ids"):
                value = item.get(key)
                if isinstance(value, list) and all(isinstance(entry, str) for entry in value):
                    matching_lists.append(value)
    require(any(value == FEATURES for value in matching_lists), "current baseline does not expose the exact Community population")


def validate_source_chain(feature_id: str) -> None:
    contract_path = f"registry/math-contracts/{feature_id}/contract.yaml"
    ir_registry_path = f"registry/ir/{feature_id}/ir.yaml"
    source_ir_path = f"ir/{feature_id}/ir.candidate.json"
    test_plan_path = f"registry/test-plans/{feature_id}/test-plan.yaml"
    contract = load_yaml(contract_path)
    ir_registry = load_yaml(ir_registry_path)
    source_ir = load_json(source_ir_path)
    test_plan = load_yaml(test_plan_path)

    for name, artifact in (("contract", contract), ("IR registry", ir_registry), ("source IR", source_ir), ("test plan", test_plan)):
        require(artifact.get("feature_id") == feature_id, f"{name} feature mismatch for {feature_id}")
    require(contract.get("source_objects") == SOURCE_OBJECTS[feature_id], f"contract source objects mismatch for {feature_id}")
    candidate_objects = [
        element.get("source_object_id")
        for element in source_ir.get("structure", {}).get("elements", [])
        if element.get("kind") == "source_object_reference"
    ]
    require(candidate_objects == SOURCE_OBJECTS[feature_id], f"source IR objects mismatch for {feature_id}")
    contract_unresolved = [entry.get("unresolved_id") for entry in contract.get("unresolved", [])]
    source_ir_unresolved = [entry.get("unresolved_id") for entry in source_ir.get("unresolved", [])]
    require(contract_unresolved == UNRESOLVED, f"contract unresolved mismatch for {feature_id}")
    require(source_ir_unresolved == UNRESOLVED, f"source IR unresolved mismatch for {feature_id}")
    require(ir_registry.get("selection_status") == "active_candidate_not_canonical", f"unexpected source IR status for {feature_id}")
    require(test_plan.get("test_plan_status") == "structural_candidate", f"unexpected source test-plan status for {feature_id}")


def validate_final_triplet(feature_id: str) -> None:
    ir_path = f"registry/optimized-ir/community/{feature_id}/ir.yaml"
    algorithm_path = f"registry/algorithms/community/{feature_id}/algorithm.yaml"
    oracle_path = f"registry/oracles/community/{feature_id}/oracle.yaml"
    ir = load_yaml(ir_path)
    algorithm = load_yaml(algorithm_path)
    oracle = load_yaml(oracle_path)

    require(ir.get("feature_id") == feature_id, f"final IR feature mismatch for {feature_id}")
    require(ir.get("status") == "selected_for_community_implementation_specification", f"wrong final IR status for {feature_id}")
    for key, expected in (
        ("source_ir_preserved", True),
        ("source_contract_preserved", True),
        ("replaces_source_ir", False),
        ("scientific_source_modified", False),
    ):
        require(ir.get(key) is expected, f"{key} mismatch for {feature_id}")
    require(ir.get("source_objects") == SOURCE_OBJECTS[feature_id], f"final IR source objects mismatch for {feature_id}")
    unresolved = ir.get("unresolved_propagated", {})
    require(unresolved.get("count") == 29 and unresolved.get("preservation") == "exact", f"final IR unresolved preservation mismatch for {feature_id}")
    require(ir.get("algorithm_ref") == algorithm_path, f"IR to algorithm link mismatch for {feature_id}")
    require(ir.get("oracle_ref") == oracle_path, f"IR to oracle link mismatch for {feature_id}")
    required_ir_keys = ["inputs", "outputs", "types", "opaque_values", "preconditions", "operations", "order_of_execution", "control_flow", "states", "effects", "postconditions", "invariants", "errors", "determinism", "dependencies", "reservations", "transformations_applied", "obligations_of_preservation", "implementation_fitness"]
    require(all(key in ir for key in required_ir_keys), f"incomplete final IR fields for {feature_id}")
    require(ir["implementation_fitness"].get("implementation_specification_ready") is True, f"implementation package not ready for {feature_id}")
    require(ir["implementation_fitness"].get("scientific_execution_ready") is False, f"scientific execution incorrectly enabled for {feature_id}")

    require(algorithm.get("feature_id") == feature_id, f"algorithm feature mismatch for {feature_id}")
    require(algorithm.get("finalized_ir_ref") == ir_path, f"algorithm IR link mismatch for {feature_id}")
    required_algorithm_keys = ["signature", "inputs", "outputs", "validations", "ordered_steps", "branching", "transitions", "effects", "errors", "postconditions", "invariants", "determinism", "edge_cases", "dependencies", "unresolved_conserved", "pseudocode"]
    require(all(key in algorithm for key in required_algorithm_keys), f"incomplete algorithm fields for {feature_id}")
    require(algorithm["unresolved_conserved"].get("count") == 29, f"algorithm unresolved mismatch for {feature_id}")

    require(oracle.get("feature_id") == feature_id, f"oracle feature mismatch for {feature_id}")
    require(oracle.get("finalized_ir_ref") == ir_path, f"oracle IR link mismatch for {feature_id}")
    require(oracle.get("algorithm_ref") == algorithm_path, f"oracle algorithm link mismatch for {feature_id}")
    require(oracle.get("scientific_values_created") is False, f"oracle invents scientific values for {feature_id}")
    categories = {case.get("category") for case in oracle.get("cases", [])}
    required_categories = {"nominal", "precondition", "source_traceability", "conservation", "unresolved_propagation", "opaque_value_propagation", "determinism", "metamorphic", "non_invention"}
    require(required_categories <= categories, f"oracle coverage incomplete for {feature_id}: {sorted(required_categories - categories)}")
    require("unsupported_execution" in categories or "blocking_execution" in categories, f"missing execution-gate oracle for {feature_id}")
    require(oracle.get("acceptance") == "all_cases_pass", f"oracle acceptance missing for {feature_id}")


def validate_module_documents() -> None:
    feature_status = load_yaml("registry/domain-finalization/community/feature-status.yaml")
    status_ids = [entry["feature_id"] for entry in feature_status["features"]]
    require(status_ids == FEATURES, "feature-status population mismatch")
    require(feature_status["summary"]["rejected"] == 0, "an active feature was rejected")
    require(all(entry["finalization_status"] == "selected_for_community_implementation_specification" for entry in feature_status["features"]), "feature finalization status mismatch")

    module = load_yaml("registry/domain-finalization/community/module-specification.yaml")
    require(module["active_features"] == FEATURES, "module active feature list mismatch")
    require(module["status"] == "selected_for_community_implementation_specification", "module status mismatch")
    require(module["unresolved"]["count"] == 29, "module unresolved count mismatch")
    require(module["internal_dependencies"] == [], "unexpected internal Community dependency")
    external = module["external_dependencies"]
    require({entry["dependency_id"] for entry in external} == {"TLC-COMMUNITY-MASTER-001", "TLC-COMMUNITY-DISCIPLE-001"}, "Community 008 external dependency mismatch")
    require(all(entry["kind"] == "symbol_only_documentary" and entry["executable"] is False for entry in external), "symbol-only dependency promoted")

    patterns = load_yaml("registry/domain-finalization/community/patterns.yaml")
    require(set(patterns["distinctions"]) == {"resemblance", "textual_duplication", "structural_duplication", "demonstrated_equivalence"}, "pattern distinctions incomplete")
    require("merge_features" in patterns["optimizations_not_applied"], "feature merge prohibition missing")

    decisions = load_yaml("registry/domain-finalization/community/decision-required.yaml")
    blocking = [entry for entry in decisions["decisions"] if entry["classification"] == "blocking"]
    require(len(blocking) == 1 and blocking[0]["feature_id"] == "TLC-FC-02-COMMUNITY-006", "real feature-specific blocker classification mismatch")
    require(decisions["implementation_package_blockers"] == [], "implementation package unexpectedly blocked")

    tasks = load_yaml("registry/domain-finalization/community/implementation-tasks.yaml")
    feature_tasks = []
    for workstream in tasks["workstreams"]:
        for task in workstream.get("tasks", []):
            if isinstance(task, dict) and task.get("feature_id"):
                feature_tasks.append(task["feature_id"])
    require(feature_tasks == FEATURES, "per-feature implementation task coverage mismatch")


def validate_changed_paths() -> None:
    changed = [line for line in git("diff", "--name-only", f"{BASE_SHA}...HEAD").splitlines() if line]
    require(changed, "no changed files found")
    for required in REQUIRED_FINAL_FILES:
        require(required in changed, f"required final file not changed: {required}")
    for feature_id in FEATURES:
        for path in (
            f"registry/optimized-ir/community/{feature_id}/ir.yaml",
            f"registry/algorithms/community/{feature_id}/algorithm.yaml",
            f"registry/oracles/community/{feature_id}/oracle.yaml",
        ):
            require(path in changed, f"required feature artifact not changed: {path}")
    for path in changed:
        allowed = path == "tools/domain-finalization/validate_community_finalization.py" or path == TEMP_WORKFLOW or path.startswith(ALLOWED_PREFIXES)
        require(allowed, f"forbidden changed path: {path}")
        lower = path.lower()
        require(not lower.endswith((".cpp", ".cc", ".cxx", ".h", ".hpp", ".pyi")), f"production or binding code added: {path}")
        require("__pycache__" not in lower and not lower.endswith(".status"), f"temporary artifact present: {path}")
    forbidden_prefixes = ("maths/", "registry/global-reconciliation/", "registry/math-contracts/", "registry/ir/", "ir/")
    require(not any(path.startswith(forbidden_prefixes) for path in changed), "source contract, source IR, scientific source or global registry modified")
    require(not any("/master/" in f"/{path.lower()}/" or "/disciple/" in f"/{path.lower()}/" for path in changed), "Master or Disciple artifact modified")
    git("diff", "--check", f"{BASE_SHA}...HEAD")


def main() -> int:
    try:
        validate_population()
        for feature_id in FEATURES:
            validate_source_chain(feature_id)
            validate_final_triplet(feature_id)
        validate_module_documents()
        validate_changed_paths()
    except ValidationError as exc:
        print(f"COMMUNITY FINALIZATION VALIDATION: FAIL\n{exc}", file=sys.stderr)
        return 1
    print("COMMUNITY FINALIZATION VALIDATION: PASS")
    print(f"baseline_main_head={BASE_SHA}")
    print(f"authoritative_features={len(FEATURES)}")
    print("contracts=8 source_irs=8 source_test_plans=8 finalized_irs=8 algorithms=8 oracles=8")
    print("unresolved_preserved=29 rejected_features=0")
    print("scientific_sources_modified=false master_modified=false disciple_modified=false global_registry_modified=false")
    print("production_code_generated=false bindings_generated=false reference_implementation_generated=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
