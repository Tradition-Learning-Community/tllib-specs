#!/usr/bin/env python3
"""Validate the Relations phase-4 finalization package without changing sources."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception as exc:  # pragma: no cover - environment guard
    print(f"PyYAML unavailable: {exc}")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
BASE_COMMIT = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
EXPECTED_FEATURES = [
    "TLC-FC-15-RELATIONS-002",
    "TLC-FC-15-RELATIONS-003",
    "TLC-FC-15-RELATIONS-004",
    "TLC-FC-15-RELATIONS-007",
    "TLC-FC-15-RELATIONS-008",
]
EXPECTED_PARTICIPANTS = {
    "TLC-FC-15-RELATIONS-002": [
        "TLC-SO-RELATIONS-047",
        "TLC-SO-RELATIONS-048",
        "TLC-SO-RELATIONS-064",
        "TLC-SO-RELATIONS-077",
        "TLC-SO-RELATIONS-088",
        "TLC-SO-RELATIONS-100",
    ],
    "TLC-FC-15-RELATIONS-003": ["TLC-SO-RELATIONS-008"],
    "TLC-FC-15-RELATIONS-004": [
        "TLC-SO-RELATIONS-004",
        "TLC-SO-RELATIONS-017",
        "TLC-SO-RELATIONS-023",
    ],
    "TLC-FC-15-RELATIONS-007": [
        "TLC-SO-RELATIONS-002",
        "TLC-SO-RELATIONS-009",
        "TLC-SO-RELATIONS-015",
        "TLC-SO-RELATIONS-021",
        "TLC-SO-RELATIONS-027",
    ],
    "TLC-FC-15-RELATIONS-008": [
        "TLC-SO-RELATIONS-014",
        "TLC-SO-RELATIONS-020",
    ],
}
EXPECTED_SCOPE = {
    "TLC-FC-15-RELATIONS-002": "relations_002_source_equation_bundle",
    "TLC-FC-15-RELATIONS-003": "relations_003_master_message_tuple_record",
    "TLC-FC-15-RELATIONS-004": "relations_004_three_function_blocks",
    "TLC-FC-15-RELATIONS-007": "relations_007_five_named_relation_objects",
    "TLC-FC-15-RELATIONS-008": "relations_008_virtue_value_tuple_records",
}
EXPECTED_CONTEXT = {
    "TLC-FC-15-RELATIONS-002": "master_message_virtue_value_capacity_competence_formalizations",
    "TLC-FC-15-RELATIONS-003": "master_message_formalization",
    "TLC-FC-15-RELATIONS-004": "master_message_value_capacity_essential_functions",
    "TLC-FC-15-RELATIONS-007": "master_message_virtue_value_capacity_competence_relation_names",
    "TLC-FC-15-RELATIONS-008": "master_virtue_and_master_value_formalizations",
}
EXPECTED_UNRESOLVED = {
    "TLC-FC-15-RELATIONS-002": 5,
    "TLC-FC-15-RELATIONS-003": 5,
    "TLC-FC-15-RELATIONS-004": 31,
    "TLC-FC-15-RELATIONS-007": 12,
    "TLC-FC-15-RELATIONS-008": 5,
}
EXPECTED_STATUS = "selected_for_relations_implementation_specification"
RAW_SOURCE_IR_STATUS = "canonical_declarative_ir_non_executable"
PRESERVATION_FLAGS = {
    "source_ir_preserved": True,
    "source_contract_preserved": True,
    "replaces_source_ir": False,
    "scientific_source_modified": False,
    "relation_invented": False,
    "direction_invented": False,
    "property_invented": False,
    "causality_invented": False,
}
ALLOWED_CHANGED_PREFIXES = (
    "registry/domain-finalization/relations/",
    "registry/optimized-ir/relations/",
    "registry/algorithms/relations/",
    "registry/oracles/relations/",
    "reports/domain-finalization/relations/",
)
ALLOWED_CHANGED_EXACT = {
    "tools/domain-finalization/validate_relations_finalization.py",
    ".github/workflows/validate-relations-finalization-temp.yml",
}

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_yaml(path: Path) -> Any:
    if not path.is_file():
        fail(f"missing required YAML: {rel(path)}")
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        fail(f"invalid YAML {rel(path)}: {exc}")
        return {}


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing required file: {rel(path)}")


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def changed_paths() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"{BASE_COMMIT}...HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception as exc:
        fail(f"unable to inspect changed paths: {exc}")
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def feature_dirs(base: Path) -> list[str]:
    if not base.is_dir():
        fail(f"missing feature directory: {rel(base)}")
        return []
    return sorted(path.name for path in base.iterdir() if path.is_dir())


def unresolved_count(data: dict[str, Any]) -> int | None:
    node = data.get("unresolved_propagated", {})
    if "count" in node:
        return node.get("count")
    if "propagated_count" in node:
        return node.get("propagated_count")
    return None


def verify_authoritative_population() -> None:
    baseline = load_yaml(ROOT / "registry/global-reconciliation/current-baseline.yaml")
    domains = [row for row in baseline.get("domains", []) if row.get("domain_id") == "relations"]
    if len(domains) != 1:
        fail(f"baseline must contain exactly one Relations domain row, got {len(domains)}")
    elif domains[0].get("feature_count") != 5:
        fail(f"baseline Relations feature_count must be 5, got {domains[0].get('feature_count')}")

    matrix = load_yaml(ROOT / "registry/global-reconciliation/domain-feature-matrix.yaml")
    matrix_ids = [row.get("feature_id") for row in matrix.get("rows", []) if row.get("domain") == "relations"]
    if matrix_ids != EXPECTED_FEATURES:
        fail(f"authoritative Relations population mismatch: {matrix_ids}")
    for row in [row for row in matrix.get("rows", []) if row.get("domain") == "relations"]:
        if not all(row.get(key) is True for key in ("contract_present", "ir_registry_present", "ir_artifact_present", "test_plan_present", "ir_layer_complete")):
            fail(f"incomplete authoritative source coverage for {row.get('feature_id')}")
        if row.get("selection_status") != RAW_SOURCE_IR_STATUS:
            fail(f"raw source IR status changed in matrix for {row.get('feature_id')}")


def verify_domain_artifacts() -> tuple[dict[str, Any], dict[str, Any]]:
    required = [
        ROOT / "registry/domain-finalization/relations/manifest.yaml",
        ROOT / "registry/domain-finalization/relations/feature-status.yaml",
        ROOT / "registry/domain-finalization/relations/patterns.yaml",
        ROOT / "registry/domain-finalization/relations/module-specification.yaml",
        ROOT / "registry/domain-finalization/relations/implementation-tasks.yaml",
        ROOT / "registry/domain-finalization/relations/decision-required.yaml",
        ROOT / "reports/domain-finalization/relations/finalization-report.md",
    ]
    for path in required:
        require_file(path)

    manifest = load_yaml(required[0])
    feature_status = load_yaml(required[1])
    patterns = load_yaml(required[2])
    module = load_yaml(required[3])
    tasks = load_yaml(required[4])
    decisions = load_yaml(required[5])

    if manifest.get("population") != EXPECTED_FEATURES:
        fail("manifest population is not the exact authoritative population")
    if manifest.get("baseline", {}).get("authoritative_feature_count") != 5:
        fail("manifest authoritative_feature_count is not 5")
    if manifest.get("base_commit") != BASE_COMMIT:
        fail("manifest base_commit does not match the main HEAD used")
    if feature_status.get("authoritative_feature_count") != 5:
        fail("feature-status authoritative_feature_count is not 5")
    if feature_status.get("summary", {}).get("rejected") != 0:
        fail("feature-status reports a rejected feature")
    if feature_status.get("summary", {}).get("declarative_non_executable_accepted") != 5:
        fail("all five declarative non-executable IRs must be accepted")
    if decisions.get("blocking") != []:
        fail("decision-required contains a blocker for this structural phase")
    if decisions.get("closure", {}).get("real_blockers_for_this_phase") != 0:
        fail("decision-required real blocker count is not zero")
    if patterns.get("pattern_policy", {}).get("scientific_equivalence_requires_source_proof") is not True:
        fail("patterns policy does not protect scientific equivalence")
    if module.get("active_features") != EXPECTED_FEATURES:
        fail("module active feature list mismatch")
    if module.get("implementation_readiness", {}).get("package_ready_for_structural_implementation") is not True:
        fail("module structural implementation readiness is not asserted")
    if module.get("implementation_readiness", {}).get("package_ready_for_semantic_relation_evaluation") is not False:
        fail("module incorrectly asserts semantic relation evaluation readiness")
    if tasks.get("status") != "ready_for_future_developer_assignment":
        fail("implementation task package is not ready for assignment")

    feature_rows = feature_status.get("features", [])
    row_ids = [row.get("feature_id") for row in feature_rows]
    if row_ids != EXPECTED_FEATURES:
        fail(f"feature-status population mismatch: {row_ids}")
    for row in feature_rows:
        fid = row.get("feature_id")
        if fid not in EXPECTED_FEATURES:
            continue
        if row.get("expected_participants") != EXPECTED_PARTICIPANTS[fid]:
            fail(f"feature-status participant mismatch for {fid}")
        if row.get("scope_id") != EXPECTED_SCOPE[fid]:
            fail(f"feature-status scope mismatch for {fid}")
        if row.get("context_id") != EXPECTED_CONTEXT[fid]:
            fail(f"feature-status context mismatch for {fid}")
        if row.get("unresolved_count") != EXPECTED_UNRESOLVED[fid]:
            fail(f"feature-status unresolved count mismatch for {fid}")
        if row.get("source_ir_status_raw") != RAW_SOURCE_IR_STATUS:
            fail(f"feature-status raw source IR status mismatch for {fid}")
        if row.get("accepted_despite_non_executable") is not True or row.get("rejected") is not False:
            fail(f"feature {fid} is not explicitly accepted without rejection")

    return manifest, feature_status


def verify_source_preservation(manifest: dict[str, Any]) -> None:
    scientific = manifest.get("source_authority", {}).get("scientific_source", {})
    science_path = ROOT / scientific.get("path", "")
    if not science_path.is_file():
        fail("scientific source is missing")
    elif git_blob_sha(science_path) != scientific.get("blob_sha"):
        fail("scientific source blob identity changed")
    if scientific.get("modified") is not False:
        fail("manifest does not mark the scientific source unchanged")

    source_artifacts = manifest.get("source_artifacts", {})
    if list(source_artifacts) != EXPECTED_FEATURES:
        fail("manifest source_artifacts population mismatch")
    for fid in EXPECTED_FEATURES:
        row = source_artifacts.get(fid, {})
        checks = (
            ("contract", "contract_blob_sha"),
            ("source_ir", "source_ir_blob_sha"),
            ("test_plan", "test_plan_blob_sha"),
        )
        for path_key, sha_key in checks:
            value = row.get(path_key)
            path = ROOT / value if value else ROOT / "__missing__"
            if not path.is_file():
                fail(f"missing preserved source artifact for {fid}: {value}")
                continue
            if git_blob_sha(path) != row.get(sha_key):
                fail(f"preserved source artifact blob changed for {fid}: {value}")
            data = load_yaml(path)
            if data.get("feature_id") != fid:
                fail(f"source artifact feature identity mismatch for {fid}: {value}")


def verify_feature_chain(fid: str, feature_status_rows: dict[str, dict[str, Any]]) -> None:
    contract_path = ROOT / f"registry/math-contracts/{fid}/contract.yaml"
    source_ir_path = ROOT / f"registry/ir/{fid}/ir.yaml"
    test_plan_path = ROOT / f"registry/test-plans/{fid}/test-plan.yaml"
    final_ir_path = ROOT / f"registry/optimized-ir/relations/{fid}/ir.yaml"
    algorithm_path = ROOT / f"registry/algorithms/relations/{fid}/algorithm.yaml"
    oracle_path = ROOT / f"registry/oracles/relations/{fid}/oracle.yaml"

    contract = load_yaml(contract_path)
    source_ir = load_yaml(source_ir_path)
    test_plan = load_yaml(test_plan_path)
    final_ir = load_yaml(final_ir_path)
    algorithm = load_yaml(algorithm_path)
    oracle = load_yaml(oracle_path)

    for label, data in (
        ("contract", contract),
        ("source IR", source_ir),
        ("test plan", test_plan),
        ("finalized IR", final_ir),
        ("algorithm", algorithm),
        ("oracle", oracle),
    ):
        if data.get("feature_id") != fid:
            fail(f"{label} feature identity mismatch for {fid}")

    if source_ir.get("ir_kind") != RAW_SOURCE_IR_STATUS:
        fail(f"source IR raw status mismatch for {fid}")
    if final_ir.get("source_ir_raw_status") != RAW_SOURCE_IR_STATUS:
        fail(f"finalized IR does not preserve raw source IR status for {fid}")
    if final_ir.get("source_ir_nature") != "declarative":
        fail(f"finalized IR source nature is not declarative for {fid}")
    if final_ir.get("status") != EXPECTED_STATUS or algorithm.get("status") != EXPECTED_STATUS or oracle.get("status") != EXPECTED_STATUS:
        fail(f"finalized chain status mismatch for {fid}")
    for key, value in PRESERVATION_FLAGS.items():
        if final_ir.get(key) is not value:
            fail(f"finalized IR preservation flag {key} mismatch for {fid}")
    if final_ir.get("accepted_despite_non_executable") is not True:
        fail(f"declarative non-executable source IR not explicitly accepted for {fid}")

    expected_contract = f"registry/math-contracts/{fid}/contract.yaml"
    expected_source_ir = f"registry/ir/{fid}/ir.yaml"
    expected_test_plan = f"registry/test-plans/{fid}/test-plan.yaml"
    expected_final_ir = f"registry/optimized-ir/relations/{fid}/ir.yaml"
    expected_algorithm = f"registry/algorithms/relations/{fid}/algorithm.yaml"
    expected_oracle = f"registry/oracles/relations/{fid}/oracle.yaml"

    if source_ir.get("contract_path") != expected_contract:
        fail(f"source IR contract reference mismatch for {fid}")
    if test_plan.get("contract_path") != expected_contract or test_plan.get("ir_path") != expected_source_ir:
        fail(f"source test-plan references mismatch for {fid}")
    if final_ir.get("source_contract") != expected_contract or final_ir.get("source_ir") != expected_source_ir or final_ir.get("source_test_plan") != expected_test_plan:
        fail(f"finalized IR source traceability mismatch for {fid}")
    if final_ir.get("links", {}).get("algorithm") != expected_algorithm or final_ir.get("links", {}).get("oracle") != expected_oracle:
        fail(f"finalized IR output links mismatch for {fid}")
    if algorithm.get("source_ir") != expected_final_ir:
        fail(f"algorithm finalized-IR reference mismatch for {fid}")
    if oracle.get("source_ir") != expected_final_ir or oracle.get("algorithm") != expected_algorithm or oracle.get("source_test_plan") != expected_test_plan:
        fail(f"oracle traceability mismatch for {fid}")

    row = feature_status_rows[fid]
    participants = final_ir.get("participants", {}).get("expected_ids")
    if participants != EXPECTED_PARTICIPANTS[fid] or participants != algorithm.get("expected_participants") or participants != oracle.get("expected_participants") or participants != row.get("expected_participants"):
        fail(f"participant conservation mismatch across IR/algorithm/oracle for {fid}")
    scope = final_ir.get("scope", {}).get("scope_id")
    context = final_ir.get("context", {}).get("context_id")
    if scope != EXPECTED_SCOPE[fid] or scope != algorithm.get("scope_id") or scope != oracle.get("scope_id"):
        fail(f"scope conservation mismatch for {fid}")
    if context != EXPECTED_CONTEXT[fid] or context != algorithm.get("context_id") or context != oracle.get("context_id"):
        fail(f"context conservation mismatch for {fid}")

    if final_ir.get("source") is not None or final_ir.get("target") is not None:
        fail(f"source or target was invented for {fid}")
    if final_ir.get("direction", {}).get("status") != "not_materialized":
        fail(f"direction was materialized for {fid}")
    if final_ir.get("arity", {}).get("status") != "not_materialized":
        fail(f"arity was materialized for {fid}")
    if final_ir.get("properties", {}).get("explicitly_defined") != []:
        fail(f"relation property was invented for {fid}")
    for operation_name in ("composition", "inversion", "projection"):
        if final_ir.get(operation_name, {}).get("declared") is not False:
            fail(f"{operation_name} was invented for {fid}")
    if final_ir.get("creation", {}).get("declared") is not False:
        fail(f"scientific relation creation was invented for {fid}")
    if final_ir.get("dependencies", {}).get("execution") != []:
        fail(f"execution dependency was invented for {fid}")

    count = unresolved_count(final_ir)
    if count != EXPECTED_UNRESOLVED[fid]:
        fail(f"finalized IR unresolved count mismatch for {fid}: {count}")
    if row.get("unresolved_count") != count or oracle.get("expected_unresolved_count") != count:
        fail(f"unresolved conservation mismatch across status/IR/oracle for {fid}")

    source_equations = contract.get("source_equations_preserved")
    if source_equations is not None and final_ir.get("opaque_values", {}).get("source_equations") != source_equations:
        fail(f"source equation text changed for {fid}")

    if fid == "TLC-FC-15-RELATIONS-004":
        unresolved = load_yaml(ROOT / "registry/math-contracts/TLC-FC-15-RELATIONS-004/unresolved.yaml")
        if unresolved.get("received_count") != 31 or unresolved.get("propagated_count") != 31:
            fail("Relations-004 source unresolved counts are not 31/31")
        if oracle.get("expected_candidate_result_count") != 3:
            fail("Relations-004 candidate-result count is not 3")
        duplicate_rows = [item for item in unresolved.get("contract_reservations", []) if item.get("value") == "TLC-DUP-RELATIONS-002"]
        if len(duplicate_rows) != 1 or duplicate_rows[0].get("status") != "unresolved":
            fail("Relations-004 duplicate reservation is not preserved")
    if fid == "TLC-FC-15-RELATIONS-007":
        unresolved = load_yaml(ROOT / "registry/math-contracts/TLC-FC-15-RELATIONS-007/unresolved.yaml")
        if unresolved.get("received_count") != 12 or unresolved.get("propagated_count") != 12:
            fail("Relations-007 source unresolved counts are not 12/12")
        if oracle.get("expected_candidate_result_count") != 5:
            fail("Relations-007 candidate-result count is not 5")
        if final_ir.get("source") is not None or final_ir.get("target") is not None:
            fail("Relations-007 endpoint identity was inferred")
    if fid == "TLC-FC-15-RELATIONS-008" and oracle.get("expected_tuple_text_count") != 2:
        fail("Relations-008 tuple text count is not 2")


def verify_feature_directory_populations() -> None:
    bases = [
        ROOT / "registry/optimized-ir/relations",
        ROOT / "registry/algorithms/relations",
        ROOT / "registry/oracles/relations",
    ]
    expected = sorted(EXPECTED_FEATURES)
    for base in bases:
        actual = feature_dirs(base)
        if actual != expected:
            fail(f"feature directory population mismatch at {rel(base)}: {actual}")
        for fid in EXPECTED_FEATURES:
            expected_name = "ir.yaml" if "optimized-ir" in base.parts else "algorithm.yaml" if "algorithms" in base.parts else "oracle.yaml"
            require_file(base / fid / expected_name)


def verify_changed_path_confinement() -> None:
    paths = changed_paths()
    if not paths:
        fail("no changed paths detected from the declared base commit")
        return
    for path in paths:
        allowed = path in ALLOWED_CHANGED_EXACT or any(path.startswith(prefix) for prefix in ALLOWED_CHANGED_PREFIXES)
        if not allowed:
            fail(f"changed path outside Relations finalization scope: {path}")
        if path.startswith("maths/"):
            fail(f"scientific source modified: {path}")
        if path.startswith("registry/global-reconciliation/"):
            fail(f"global registry modified or regenerated: {path}")
        lowered = path.lower()
        if lowered.endswith((".cc", ".cpp", ".cxx", ".h", ".hpp", ".hh")):
            fail(f"C++ artifact present: {path}")
        if lowered.endswith(".py") and path != "tools/domain-finalization/validate_relations_finalization.py":
            fail(f"unexpected Python implementation artifact present: {path}")
        if "binding" in lowered or "reference-implementation" in lowered or "reference_implementation" in lowered:
            fail(f"binding or reference implementation artifact present: {path}")
        if any(token in lowered for token in ("__pycache__", ".status", ".log", ".cache")):
            fail(f"temporary diagnostic or cache artifact present: {path}")

    changed_yaml = [ROOT / path for path in paths if path.endswith((".yaml", ".yml"))]
    for path in changed_yaml:
        load_yaml(path)


def main() -> int:
    verify_authoritative_population()
    manifest, feature_status = verify_domain_artifacts()
    verify_source_preservation(manifest)
    verify_feature_directory_populations()
    status_rows = {row.get("feature_id"): row for row in feature_status.get("features", [])}
    for fid in EXPECTED_FEATURES:
        if fid not in status_rows:
            fail(f"feature-status row missing for {fid}")
            continue
        verify_feature_chain(fid, status_rows)
    verify_changed_path_confinement()

    if ERRORS:
        print("Relations finalization validation failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"Authoritative population: {len(EXPECTED_FEATURES)} Relations features")
    print("Contracts, source IRs and source test plans: preserved")
    print("Finalized IR -> algorithm -> oracle chains: complete")
    print("Declarative non-executable IRs accepted: 5")
    print("Changed paths: confined to Relations finalization, report and validator")
    print("Scientific sources, global registry and other domains: unchanged")
    print("Relations finalization validation passed for 5 authoritative features.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
