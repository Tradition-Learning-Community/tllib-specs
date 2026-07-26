#!/usr/bin/env python3
"""Validate the Community finalization package without executing science."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
FEATURES = [
    "TLC-FC-02-COMMUNITY-001", "TLC-FC-02-COMMUNITY-003",
    "TLC-FC-02-COMMUNITY-004", "TLC-FC-02-COMMUNITY-005",
    "TLC-FC-02-COMMUNITY-006", "TLC-FC-02-COMMUNITY-007",
    "TLC-FC-02-COMMUNITY-008", "TLC-FC-02-COMMUNITY-009",
]
UNRESOLVED = [f"TLC-UT-COMMUNITY-{n:03d}" for n in range(1, 30)]
OBJECTS = {
    FEATURES[0]: ["TLC-SO-COMMUNITY-008"],
    FEATURES[1]: ["TLC-SO-COMMUNITY-029", "TLC-SO-COMMUNITY-040", "TLC-SO-COMMUNITY-044"],
    FEATURES[2]: ["TLC-SO-COMMUNITY-027", "TLC-SO-COMMUNITY-028", "TLC-SO-COMMUNITY-030"],
    FEATURES[3]: ["TLC-SO-COMMUNITY-009", "TLC-SO-COMMUNITY-035", "TLC-SO-COMMUNITY-037", "TLC-SO-COMMUNITY-038", "TLC-SO-COMMUNITY-039"],
    FEATURES[4]: ["TLC-SO-COMMUNITY-036"],
    FEATURES[5]: ["TLC-SO-COMMUNITY-017", "TLC-SO-COMMUNITY-031"],
    FEATURES[6]: ["TLC-SO-COMMUNITY-018", "TLC-SO-COMMUNITY-019", "TLC-SO-COMMUNITY-020"],
    FEATURES[7]: ["TLC-SO-COMMUNITY-004", "TLC-SO-COMMUNITY-026", "TLC-SO-COMMUNITY-032"],
}
FINAL_ROOT_FILES = [
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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_yaml(path: str) -> Any:
    target = ROOT / path
    require(target.is_file(), f"missing YAML file: {path}")
    try:
        return yaml.safe_load(target.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationError(f"invalid YAML {path}: {exc}") from exc


def load_json(path: str) -> Any:
    target = ROOT / path
    require(target.is_file(), f"missing JSON file: {path}")
    try:
        return json.loads(target.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationError(f"invalid JSON {path}: {exc}") from exc


def walk_dicts(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_dicts(child)


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=False)
    require(result.returncode == 0, f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def validate_population() -> None:
    manifest = load_yaml(FINAL_ROOT_FILES[0])
    population = manifest["authoritative_population"]
    require(population["feature_ids"] == FEATURES, "manifest population is not exact")
    require(population["count"] == 8, "manifest feature count mismatch")
    require(manifest["baseline"]["main_head"] == BASE_SHA, "baseline main HEAD mismatch")
    require(manifest["baseline"]["count_divergence"] is False, "unexpected count divergence")
    require(manifest["unresolved_authoritative"]["exact_ids"] == UNRESOLVED, "manifest unresolved set mismatch")

    matrix = load_yaml("registry/global-reconciliation/domain-feature-matrix.yaml")
    matrix_ids = {
        row["feature_id"] for row in walk_dicts(matrix)
        if row.get("domain") == "community" and row.get("feature_id")
    }
    require(matrix_ids == set(FEATURES), f"domain-feature matrix mismatch: {sorted(matrix_ids)}")

    baseline = load_yaml("registry/global-reconciliation/current-baseline.yaml")
    community_rows = [row for row in baseline.get("domains", []) if row.get("domain_id") == "community"]
    require(len(community_rows) == 1, "current baseline Community row missing or duplicated")
    row = community_rows[0]
    for key in ("feature_count", "contracts_present", "ir_registry_entries_present", "ir_artifacts_present", "test_plans_present", "ir_layer_complete_features"):
        require(row.get(key) == 8, f"current baseline Community {key} mismatch")
    require(row.get("ir_layer_complete") is True, "current baseline Community IR layer is incomplete")


def validate_source(feature: str) -> None:
    contract_path = f"registry/math-contracts/{feature}/contract.yaml"
    registry_path = f"registry/ir/{feature}/ir.yaml"
    candidate_path = f"ir/{feature}/ir.candidate.json"
    test_path = f"registry/test-plans/{feature}/test-plan.yaml"
    contract = load_yaml(contract_path)
    registry = load_yaml(registry_path)
    candidate = load_json(candidate_path)
    test_plan = load_yaml(test_path)
    for label, artifact in (("contract", contract), ("registry IR", registry), ("candidate IR", candidate), ("test plan", test_plan)):
        require(artifact.get("feature_id") == feature, f"{label} identity mismatch for {feature}")
    require(contract.get("source_objects") == OBJECTS[feature], f"contract object mismatch for {feature}")
    candidate_objects = [e.get("source_object_id") for e in candidate.get("structure", {}).get("elements", []) if e.get("kind") == "source_object_reference"]
    require(candidate_objects == OBJECTS[feature], f"candidate IR object mismatch for {feature}")
    require([e.get("unresolved_id") for e in contract.get("unresolved", [])] == UNRESOLVED, f"contract unresolved mismatch for {feature}")
    require([e.get("unresolved_id") for e in candidate.get("unresolved", [])] == UNRESOLVED, f"candidate IR unresolved mismatch for {feature}")
    require(registry.get("selection_status") == "active_candidate_not_canonical", f"source IR status mismatch for {feature}")
    require(test_plan.get("test_plan_status") == "structural_candidate", f"source test-plan status mismatch for {feature}")


def validate_triplet(feature: str) -> None:
    ir_path = f"registry/optimized-ir/community/{feature}/ir.yaml"
    algorithm_path = f"registry/algorithms/community/{feature}/algorithm.yaml"
    oracle_path = f"registry/oracles/community/{feature}/oracle.yaml"
    ir, algorithm, oracle = load_yaml(ir_path), load_yaml(algorithm_path), load_yaml(oracle_path)

    require(ir.get("feature_id") == feature, f"final IR identity mismatch for {feature}")
    require(ir.get("status") == "selected_for_community_implementation_specification", f"final IR status mismatch for {feature}")
    for key, expected in (("source_ir_preserved", True), ("source_contract_preserved", True), ("replaces_source_ir", False), ("scientific_source_modified", False)):
        require(ir.get(key) is expected, f"{key} mismatch for {feature}")
    require(ir.get("source_objects") == OBJECTS[feature], f"final IR object mismatch for {feature}")
    required_ir = {"inputs", "outputs", "types", "opaque_values", "preconditions", "operations", "order_of_execution", "control_flow", "states", "effects", "postconditions", "invariants", "errors", "determinism", "dependencies", "unresolved_propagated", "reservations", "transformations_applied", "obligations_of_preservation", "implementation_fitness"}
    require(required_ir <= set(ir), f"incomplete final IR for {feature}: {sorted(required_ir - set(ir))}")
    unresolved = ir["unresolved_propagated"]
    require(unresolved.get("count") == 29 and unresolved.get("preservation") == "exact", f"final IR unresolved mismatch for {feature}")
    require(ir.get("algorithm_ref") == algorithm_path and ir.get("oracle_ref") == oracle_path, f"final IR links mismatch for {feature}")
    fitness = ir["implementation_fitness"]
    require(fitness.get("implementation_specification_ready") is True, f"implementation specification not ready for {feature}")
    require(fitness.get("scientific_execution_ready") is False, f"scientific execution incorrectly enabled for {feature}")

    require(algorithm.get("feature_id") == feature and algorithm.get("finalized_ir_ref") == ir_path, f"algorithm traceability mismatch for {feature}")
    required_algorithm = {"signature", "inputs", "outputs", "validations", "ordered_steps", "branching", "transitions", "effects", "errors", "postconditions", "invariants", "determinism", "edge_cases", "dependencies", "unresolved_conserved", "pseudocode"}
    require(required_algorithm <= set(algorithm), f"incomplete algorithm for {feature}: {sorted(required_algorithm - set(algorithm))}")
    require(algorithm["unresolved_conserved"].get("count") == 29, f"algorithm unresolved mismatch for {feature}")

    require(oracle.get("feature_id") == feature, f"oracle identity mismatch for {feature}")
    require(oracle.get("finalized_ir_ref") == ir_path and oracle.get("algorithm_ref") == algorithm_path, f"oracle traceability mismatch for {feature}")
    require(oracle.get("scientific_values_created") is False, f"oracle invents scientific values for {feature}")
    categories = {case.get("category") for case in oracle.get("cases", [])}
    required_categories = {"nominal", "precondition", "source_traceability", "conservation", "unresolved_propagation", "opaque_value_propagation", "determinism", "metamorphic", "non_invention"}
    require(required_categories <= categories, f"oracle coverage incomplete for {feature}: {sorted(required_categories - categories)}")
    require(bool({"unsupported_execution", "blocking_execution"} & categories), f"execution-gate oracle missing for {feature}")
    require(oracle.get("acceptance") == "all_cases_pass", f"oracle acceptance mismatch for {feature}")


def validate_module() -> None:
    status = load_yaml("registry/domain-finalization/community/feature-status.yaml")
    require([f["feature_id"] for f in status["features"]] == FEATURES, "feature-status population mismatch")
    require(status["summary"]["rejected"] == 0, "active feature rejection detected")
    require(all(f["finalization_status"] == "selected_for_community_implementation_specification" for f in status["features"]), "feature-status selection mismatch")

    module = load_yaml("registry/domain-finalization/community/module-specification.yaml")
    require(module["active_features"] == FEATURES, "module population mismatch")
    require(module["status"] == "selected_for_community_implementation_specification", "module status mismatch")
    require(module["unresolved"]["count"] == 29, "module unresolved count mismatch")
    require(module["internal_dependencies"] == [], "unexpected internal dependency")
    external = module["external_dependencies"]
    require({d["dependency_id"] for d in external} == {"TLC-COMMUNITY-MASTER-001", "TLC-COMMUNITY-DISCIPLE-001"}, "external dependency set mismatch")
    require(all(d["kind"] == "symbol_only_documentary" and d["executable"] is False for d in external), "symbol-only dependency promoted")

    patterns = load_yaml("registry/domain-finalization/community/patterns.yaml")
    require(set(patterns["distinctions"]) == {"resemblance", "textual_duplication", "structural_duplication", "demonstrated_equivalence"}, "pattern distinctions incomplete")
    require("merge_features" in patterns["optimizations_not_applied"], "feature-merge prohibition missing")

    decisions = load_yaml("registry/domain-finalization/community/decision-required.yaml")
    blocking = [d for d in decisions["decisions"] if d["classification"] == "blocking"]
    require(len(blocking) == 1 and blocking[0]["feature_id"] == FEATURES[4], "blocking decision classification mismatch")
    require(decisions["implementation_package_blockers"] == [], "implementation package unexpectedly blocked")

    tasks = load_yaml("registry/domain-finalization/community/implementation-tasks.yaml")
    task_features = [task["feature_id"] for stream in tasks["workstreams"] for task in stream.get("tasks", []) if isinstance(task, dict) and task.get("feature_id")]
    require(task_features == FEATURES, "per-feature implementation task coverage mismatch")


def validate_paths() -> None:
    changed = [p for p in git("diff", "--name-only", f"{BASE_SHA}...HEAD").splitlines() if p]
    require(changed, "no changed files")
    required = list(FINAL_ROOT_FILES)
    for feature in FEATURES:
        required += [
            f"registry/optimized-ir/community/{feature}/ir.yaml",
            f"registry/algorithms/community/{feature}/algorithm.yaml",
            f"registry/oracles/community/{feature}/oracle.yaml",
        ]
    for path in required:
        require(path in changed, f"required artifact absent from diff: {path}")
    for path in changed:
        allowed = path == "tools/domain-finalization/validate_community_finalization.py" or path == TEMP_WORKFLOW or path.startswith(ALLOWED_PREFIXES)
        require(allowed, f"forbidden changed path: {path}")
        lower = path.lower()
        require(not lower.endswith((".cpp", ".cc", ".cxx", ".h", ".hpp", ".pyi")), f"production or binding code added: {path}")
        require("__pycache__" not in lower and not lower.endswith((".status", ".log")), f"temporary diagnostic artifact present: {path}")
    protected = ("maths/", "registry/global-reconciliation/", "registry/math-contracts/", "registry/ir/", "ir/")
    require(not any(p.startswith(protected) for p in changed), "scientific source, source contract, source IR or global registry modified")
    require(not any("/master/" in f"/{p.lower()}/" or "/disciple/" in f"/{p.lower()}/" for p in changed), "Master or Disciple artifact modified")
    git("diff", "--check", f"{BASE_SHA}...HEAD")


def main() -> int:
    try:
        validate_population()
        for feature in FEATURES:
            validate_source(feature)
            validate_triplet(feature)
        validate_module()
        validate_paths()
    except ValidationError as exc:
        print(f"COMMUNITY FINALIZATION VALIDATION: FAIL\n{exc}", file=sys.stderr)
        return 1
    print("COMMUNITY FINALIZATION VALIDATION: PASS")
    print(f"baseline_main_head={BASE_SHA}")
    print("authoritative_features=8 contracts=8 source_irs=8 source_test_plans=8")
    print("finalized_irs=8 algorithms=8 oracles=8 unresolved_preserved=29 rejected_features=0")
    print("scientific_sources_modified=false master_modified=false disciple_modified=false global_registry_modified=false")
    print("production_code_generated=false bindings_generated=false reference_implementation_generated=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
