#!/usr/bin/env python3
"""Strict structural validator for the Dynamics domain preparation."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml


DOMAIN = "dynamics"
BASELINE = "ffbcbb66e6fa3fe809d9b94e47ef9c8bf8d19ddb"
FEATURE_PREFIX = "TLC-FC-05-DYNAMICS-"
OBJECT_PREFIX = "TLC-SO-DYNAMICS-"
RELATION_PREFIX = "TLC-SR-DYNAMICS-"
UNRESOLVED_PREFIX = "TLC-UT-DYNAMICS-"
EXPECTED_FEATURE_COUNT = 7
EXPECTED_OBJECT_COUNT = 26
EXPECTED_RELATION_COUNT = 25
EXPECTED_UNRESOLVED_COUNT = 12
EXPECTED_DUPLICATE_COUNT = 9

REGISTRY_FILES = {
    "source-inventory.yaml", "scientific-coverage.yaml", "feature-inventory.yaml",
    "functional-coverage.yaml", "dynamic-semantics.yaml", "concept-separation.yaml",
    "master-dependencies.yaml", "disciple-dependencies.yaml", "community-dependencies.yaml",
    "huit-dimensions-dependencies.yaml", "invariants-dependencies.yaml",
    "theorems-dependencies.yaml", "external-domain-dependencies.yaml",
    "upstream-symbol-mapping.yaml", "feature-dependencies.yaml",
    "historical-pilot-assessment.yaml", "feature-classification.yaml",
    "production-order.yaml", "contract-production-plan.yaml", "ir-production-plan.yaml",
    "unresolved-status.yaml", "production-gates.yaml", "feature-status.yaml",
    "future-reconciliation.yaml", "global-manifest-update-proposal.yaml",
    "preparation-status.yaml",
}

REPORT_FILES = {
    "source-inventory-report.md", "scientific-coverage-report.md",
    "feature-inventory-report.md", "functional-coverage-report.md",
    "dynamic-semantics-report.md", "concept-separation-report.md",
    "master-dependency-report.md", "disciple-dependency-report.md",
    "community-dependency-report.md", "huit-dimensions-dependency-report.md",
    "invariants-dependency-report.md", "theorems-dependency-report.md",
    "external-domain-dependency-report.md", "upstream-symbol-reconciliation-report.md",
    "feature-dependency-report.md", "historical-pilot-assessment.md",
    "feature-classification-report.md", "production-order-report.md",
    "contract-production-plan-report.md", "ir-production-plan-report.md",
    "unresolved-report.md", "domain-preparation-report.md",
}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    ).stdout.strip()


def flatten(values):
    result = []
    for value in values:
        if isinstance(value, list):
            result.extend(value)
        else:
            result.append(value)
    return result


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    registry_dir = root / "registry" / "domain-progress" / DOMAIN
    report_dir = root / "reports" / "domain-progress" / DOMAIN
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(git(root, "merge-base", "--is-ancestor", BASELINE, "HEAD") == "", "HEAD is not descended from canonical baseline")
    require((root / "maths" / "05-dynamics.md").is_file(), "Dynamics source missing")
    require(REGISTRY_FILES == {p.name for p in registry_dir.glob("*.yaml")}, "Dynamics registry file set mismatch")
    require(REPORT_FILES == {p.name for p in report_dir.glob("*.md")}, "Dynamics report file set mismatch")

    parsed_yaml = {}
    for path in sorted(registry_dir.glob("*.yaml")):
        try:
            parsed_yaml[path.name] = load_yaml(path)
        except Exception as exc:
            errors.append(f"invalid YAML {path}: {exc}")
    for path in sorted(root.rglob("*.json")):
        if "domain-progress/dynamics" in path.as_posix():
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid JSON {path}: {exc}")

    source_objects = load_yaml(root / "registry/scientific-objects/dynamics/scientific-objects.candidate.yaml")["objects"]
    source_relations = load_yaml(root / "registry/scientific-objects/dynamics/scientific-relations.candidate.yaml")["relations"]
    source_unresolved = load_yaml(root / "registry/scientific-objects/dynamics/unresolved-terms.yaml")["unresolved_terms"]
    source_duplicates = load_yaml(root / "registry/scientific-objects/dynamics/duplicate-candidates.yaml")["duplicate_candidates"]
    catalogue = load_yaml(root / "registry/features/feature-candidates.yaml")
    catalogue_features = catalogue["features"]
    dynamics_features = [item for item in catalogue_features if item["candidate_feature_id"].startswith(FEATURE_PREFIX)]

    object_ids = {item["provisional_object_id"] for item in source_objects}
    relation_ids = {item["provisional_relation_id"] for item in source_relations}
    unresolved_ids = {item["unresolved_id"] for item in source_unresolved}
    feature_ids = {item["candidate_feature_id"] for item in dynamics_features}
    require(len(source_objects) == EXPECTED_OBJECT_COUNT == len(object_ids), "object count or uniqueness mismatch")
    require(len(source_relations) == EXPECTED_RELATION_COUNT == len(relation_ids), "relation count or uniqueness mismatch")
    require(len(source_unresolved) == EXPECTED_UNRESOLVED_COUNT == len(unresolved_ids), "unresolved count or uniqueness mismatch")
    require(len(source_duplicates) == EXPECTED_DUPLICATE_COUNT, "duplicate candidate count mismatch")
    require(len(catalogue_features) == 224, "canonical catalogue is not the 224-feature catalogue")
    require(len(dynamics_features) == EXPECTED_FEATURE_COUNT == len(feature_ids), "Dynamics feature count mismatch")
    require(all(re.fullmatch(r"TLC-SO-DYNAMICS-\d{3}", value) for value in object_ids), "invalid object identifier")
    require(all(re.fullmatch(r"TLC-SR-DYNAMICS-\d{3}", value) for value in relation_ids), "invalid relation identifier")
    require(all(re.fullmatch(r"TLC-UT-DYNAMICS-\d{3}", value) for value in unresolved_ids), "invalid unresolved identifier")
    require(all(re.fullmatch(r"TLC-FC-05-DYNAMICS-\d{3}", value) for value in feature_ids), "invalid feature identifier")

    inventory = parsed_yaml.get("source-inventory.yaml", {})
    require(set(inventory.get("objects", {}).get("ids", [])) == object_ids, "source inventory object mismatch")
    require(set(inventory.get("relations", {}).get("ids", [])) == relation_ids, "source inventory relation mismatch")
    require(set(inventory.get("unresolved", {}).get("ids", [])) == unresolved_ids, "source inventory unresolved mismatch")

    feature_inventory = parsed_yaml.get("feature-inventory.yaml", {})
    inventoried_ids = {item.get("feature_id") for item in feature_inventory.get("features", [])}
    require(inventoried_ids == feature_ids, "feature inventory does not match catalogue")
    require(feature_inventory.get("summary", {}).get("missing_features") == 0, "missing features reported")
    require(feature_inventory.get("summary", {}).get("orphan_features") == 0, "orphan features reported")

    scientific = parsed_yaml.get("scientific-coverage.yaml", {})
    covered_objects = set(flatten([item.get("object_ids", []) for item in scientific.get("objects", [])]))
    covered_relations = set(flatten([item.get("relation_ids", []) for item in scientific.get("relations", [])]))
    covered_unresolved = set(flatten([item.get("unresolved_ids", []) for item in scientific.get("unresolved", [])]))
    require(covered_objects == object_ids, "scientific object coverage mismatch")
    require(covered_relations == relation_ids, "scientific relation coverage mismatch")
    require(covered_unresolved == unresolved_ids, "scientific unresolved coverage mismatch")

    functional = parsed_yaml.get("functional-coverage.yaml", {})
    mapped_objects = set(flatten([item.get("object_ids", []) for item in functional.get("object_mappings", [])]))
    mapped_relations = set(flatten([item.get("relation_ids", []) for item in functional.get("relation_mappings", [])]))
    mapped_unresolved = set(flatten([item.get("unresolved_ids", []) for item in functional.get("unresolved_mappings", [])]))
    require(mapped_objects == object_ids, "functional object coverage mismatch")
    require(mapped_relations == relation_ids, "functional relation coverage mismatch")
    require(mapped_unresolved == unresolved_ids, "functional unresolved coverage mismatch")

    unresolved_status = parsed_yaml.get("unresolved-status.yaml", {})
    status_ids = {item.get("unresolved_id") for item in unresolved_status.get("unresolved", [])}
    require(status_ids == unresolved_ids, "unresolved status coverage mismatch")
    require(all(item.get("human_decision_required") is True for item in unresolved_status.get("unresolved", [])), "unresolved human decision flag missing")

    for filename in ("feature-classification.yaml", "feature-status.yaml", "contract-production-plan.yaml", "ir-production-plan.yaml"):
        data = parsed_yaml.get(filename, {})
        ids = {item.get("feature_id") for item in data.get("features", [])}
        require(ids == feature_ids, f"feature coverage mismatch in {filename}")

    semantics = parsed_yaml.get("dynamic-semantics.yaml", {})
    require(bool(semantics.get("elements")), "dynamic semantics analysis missing")
    require(semantics.get("summary", {}).get("differential_equations") == 6, "differential equation analysis mismatch")
    require(semantics.get("summary", {}).get("stochastic_equations") == 3, "stochastic equation analysis mismatch")
    concepts = parsed_yaml.get("concept-separation.yaml", {})
    required_terms = {"état", "variable", "paramètre", "transition", "relation", "évolution", "dynamique", "processus", "fonction", "opérateur", "équation", "contrainte", "invariant", "règle_de_validation", "événement", "séquence"}
    require({item.get("source_term") for item in concepts.get("terms", [])} == required_terms, "concept separation coverage mismatch")

    dependency_files = {
        "master-dependencies.yaml", "disciple-dependencies.yaml", "community-dependencies.yaml",
        "huit-dimensions-dependencies.yaml", "invariants-dependencies.yaml",
        "theorems-dependencies.yaml", "external-domain-dependencies.yaml",
        "upstream-symbol-mapping.yaml", "feature-dependencies.yaml",
    }
    require(dependency_files <= parsed_yaml.keys(), "dependency analysis incomplete")
    graph = parsed_yaml.get("feature-dependencies.yaml", {})
    for edge in graph.get("edges", []):
        require(edge.get("from_feature_id") in feature_ids and edge.get("to_feature_id") in feature_ids, f"graph edge outside catalogue: {edge}")
    require(graph.get("summary", {}).get("cycles") == [], "unclassified cycle present")

    pilot = parsed_yaml.get("historical-pilot-assessment.yaml", {})
    require(pilot.get("feature_id") == "TLC-FC-05-DYNAMICS-001", "historical pilot feature mismatch")
    require(pilot.get("modified") is False and pilot.get("promoted") is False, "historical pilot must not be modified or promoted")
    gates = parsed_yaml.get("production-gates.yaml", {})
    require(gates.get("ready_for_ir_generation") is False, "ready_for_ir_generation must remain false")
    require(gates.get("ready_for_implementation_planning") is False, "implementation planning must remain false")
    require(gates.get("ready_for_code_generation") is False, "code generation must remain false")

    status_lines = git(root, "status", "--porcelain", "--untracked-files=all").splitlines()
    changed_paths = {line.strip().split(maxsplit=1)[-1].replace("\\", "/") for line in status_lines if line.strip()}
    committed_paths = set(git(root, "diff", "--name-only", "origin/main...HEAD").splitlines())
    all_paths = {path for path in changed_paths | committed_paths if path}
    allowed = lambda path: (
        path.startswith("registry/domain-progress/dynamics/")
        or path.startswith("reports/domain-progress/dynamics/")
        or path == "scripts/validate_dynamics_preparation.py"
    )
    require(all(allowed(path) for path in all_paths), f"out-of-scope paths: {sorted(path for path in all_paths if not allowed(path))}")
    forbidden_prefixes = (
        "registry/math-contracts/TLC-FC-05-DYNAMICS-", "ir/TLC-FC-05-DYNAMICS-",
        "registry/domain-progress/master/", "registry/domain-progress/disciple/",
        "registry/domain-progress/community/", "registry/domain-progress/huit-dimensions/",
        "registry/domain-progress/invariants/", "reports/domain-progress/master/",
        "reports/domain-progress/disciple/", "reports/domain-progress/community/",
        "reports/domain-progress/huit-dimensions/", "reports/domain-progress/invariants/",
    )
    require(not any(path.startswith(forbidden_prefixes) for path in all_paths), "forbidden domain, contract, IR, or pilot modification")
    require(not any(path.endswith((".cpp", ".cc", ".cxx", ".hpp", ".h")) for path in all_paths), "C++ file created")
    for path_text in all_paths:
        path = root / path_text
        if path.is_file() and path != Path(__file__).resolve():
            text = path.read_text(encoding="utf-8", errors="replace").lower()
            require("pybind11" not in text, f"Python binding reference in {path_text}")

    if errors:
        print("DYNAMICS PREPARATION VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DYNAMICS PREPARATION VALIDATION PASSED")
    print(f"baseline={BASELINE} catalogue=224 features={len(feature_ids)}")
    print(f"objects={len(object_ids)} relations={len(relation_ids)} unresolved={len(unresolved_ids)} duplicates={len(source_duplicates)}")
    print(f"registry_yaml={len(REGISTRY_FILES)} reports={len(REPORT_FILES)} cycles=0 missing=0")
    print("contracts_created=0 irs_created=0 pilot_modified=false other_domains_modified=false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
