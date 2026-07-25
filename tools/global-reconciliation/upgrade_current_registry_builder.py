#!/usr/bin/env python3
"""One-time source upgrade for the Phase 4 current registry builder.

The first generated snapshot proved that the repository uses three legitimate
IR layouts: external candidate IRs, external prototype IRs, and substantive
`registry/ir/.../ir.yaml` files.  It also proved that the former 175 count
included nine explicitly non-authoritative `legacy_goose_feature_ids` from the
Capacities preparation.  This upgrade makes the builder inventory authoritative
feature lists and all three IR layouts without changing scientific content.
"""

from __future__ import annotations

import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[2]
BUILDER = ROOT / "tools/global-reconciliation/build_current_global_registry.py"
VALIDATOR = ROOT / "tools/global-reconciliation/validate_current_global_registry.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise RuntimeError(f"upgrade marker not found: {label}")
    return text.replace(old, new, 1)


def upgrade_builder() -> None:
    text = BUILDER.read_text(encoding="utf-8")

    insertion = '''\n\ndef extract_authoritative_feature_ids(data: Any) -> list[str]:
    """Read active feature entries without counting lineage or internal IDs."""
    primary_keys = (
        "features",
        "active_features",
        "feature_catalogue",
        "feature_catalog",
        "catalogue",
        "items",
        "entries",
    )
    id_keys = ("feature_id", "feature_candidate_id", "id")

    def direct_ids(value: Any) -> list[str]:
        found: list[str] = []
        if isinstance(value, str):
            if value.startswith("TLC-FC-"):
                found.append(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.startswith("TLC-FC-"):
                    found.append(item)
                elif isinstance(item, dict):
                    for key in id_keys:
                        candidate = item.get(key)
                        if isinstance(candidate, str) and candidate.startswith("TLC-FC-"):
                            found.append(candidate)
                            break
        elif isinstance(value, dict):
            for item in value.values():
                found.extend(direct_ids(item))
        return found

    if isinstance(data, dict):
        for key in primary_keys:
            if key in data:
                found = direct_ids(data[key])
                if found:
                    return sorted(set(found))

    found: list[str] = []

    def walk(value: Any, parent_key: str = "") -> None:
        lowered = parent_key.lower()
        if any(token in lowered for token in ("legacy", "rejected", "excluded", "deferred", "comparison")):
            return
        if isinstance(value, dict):
            for key, child in value.items():
                if key in id_keys and isinstance(child, str) and child.startswith("TLC-FC-"):
                    found.append(child)
                else:
                    walk(child, str(key))
        elif isinstance(value, list):
            for child in value:
                walk(child, parent_key)

    walk(data)
    return sorted(set(found))


def authoritative_matrix(root: pathlib.Path, domain_registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for domain in domain_registry.get("domains", []):
        slug = str(domain.get("domain_id"))
        source_ref = domain.get("feature_source")
        if not isinstance(source_ref, str):
            raise RuntimeError(f"missing authoritative feature source for {slug}")
        identifiers = extract_authoritative_feature_ids(load(root / source_ref, {}))
        if not identifiers:
            raise RuntimeError(f"no active feature identifiers found for {slug} in {source_ref}")
        rows.extend({"domain": slug, "feature_id": feature_id} for feature_id in identifiers)
    return rows
'''
    text = replace_once(
        text,
        "\n\ndef source_commit(root: pathlib.Path, explicit: str | None) -> str:\n",
        insertion + "\n\ndef source_commit(root: pathlib.Path, explicit: str | None) -> str:\n",
        "authoritative feature extraction",
    )

    old_locator = '''def locate_ir_artifact(root: pathlib.Path, feature_id: str, registry_entry: dict[str, Any]) -> str | None:
    for key in (
        "candidate_ref",
        "canonical_ref",
        "ir_ref",
        "artifact_ref",
        "prototype_ref",
        "declarative_ir_ref",
    ):
        value = registry_entry.get(key)
        if isinstance(value, str) and (root / value).is_file():
            return value.replace("\\\\", "/")
    directory = root / "ir" / feature_id
    if directory.is_dir():
        candidates = sorted(
            path for path in directory.iterdir()
            if path.is_file() and path.suffix.lower() in {".json", ".yaml", ".yml"}
        )
        if candidates:
            return str(candidates[0].relative_to(root)).replace("\\\\", "/")
    return None
'''
    new_locator = '''def locate_ir_artifact(root: pathlib.Path, feature_id: str, registry_entry: dict[str, Any]) -> str | None:
    for key in (
        "candidate_ref",
        "canonical_ref",
        "ir_ref",
        "artifact_ref",
        "prototype_ref",
        "declarative_ir_ref",
    ):
        value = registry_entry.get(key)
        if isinstance(value, str) and (root / value).is_file():
            return value.replace("\\\\", "/")

    directory = root / "ir" / feature_id
    if directory.is_dir():
        candidates = sorted(
            path for path in directory.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".json", ".yaml", ".yml"}
            and "test" not in path.name.lower()
            and "coverage" not in path.name.lower()
            and "manifest" not in path.name.lower()
            and ("ir" in path.name.lower() or "prototype" in path.name.lower())
        )
        if candidates:
            return str(candidates[0].relative_to(root)).replace("\\\\", "/")

    registry_path = root / f"registry/ir/{feature_id}/ir.yaml"
    if registry_path.is_file():
        role = normalized(registry_entry.get("artifact_role")) or ""
        substantive_keys = {"ir_id", "ir_kind", "operations", "nodes", "entrypoint", "control_flow"}
        if "registry_entry" not in role or substantive_keys.intersection(registry_entry):
            return str(registry_path.relative_to(root)).replace("\\\\", "/")
    return None


def locate_test_plan(root: pathlib.Path, feature_id: str) -> str | None:
    direct = (
        root / f"registry/test-plans/{feature_id}/test-plan.yaml",
        root / f"ir/{feature_id}/test-plan.yaml",
        root / f"ir/{feature_id}/test-plan.yml",
    )
    for path in direct:
        if path.is_file():
            return str(path.relative_to(root)).replace("\\\\", "/")
    directory = root / "ir" / feature_id
    if directory.is_dir():
        candidates = sorted(
            path for path in directory.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".yaml", ".yml", ".json"}
            and ("test" in path.name.lower() or "oracle" in path.name.lower())
        )
        if candidates:
            return str(candidates[0].relative_to(root)).replace("\\\\", "/")
    return None
'''
    text = replace_once(text, old_locator, new_locator, "IR and test-plan locators")

    old_inventory = '''def build_feature_inventory(root: pathlib.Path, matrix_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source_row in sorted(matrix_rows, key=lambda row: (row.get("domain", ""), row.get("feature_id", ""))):
        feature_id = str(source_row["feature_id"])
        domain = str(source_row["domain"])
        contract_ref = f"registry/math-contracts/{feature_id}/contract.yaml"
        ir_registry_ref = f"registry/ir/{feature_id}/ir.yaml"
        test_plan_ref = f"registry/test-plans/{feature_id}/test-plan.yaml"
        contract = load(root / contract_ref, {})
        ir_registry = load(root / ir_registry_ref, {})
        if not isinstance(contract, dict):
            contract = {}
        if not isinstance(ir_registry, dict):
            ir_registry = {}
        ir_artifact_ref = locate_ir_artifact(root, feature_id, ir_registry)
        selection_status = first_status(
            ir_registry,
            ("selection_status", "canonical_status", "approval_status", "status"),
        )
        scientific_status = first_status(
            ir_registry,
            ("scientific_status", "validation_status"),
        )
        execution_status = first_status(
            ir_registry,
            ("execution_status", "computational_status", "implementation_status"),
        )
        contract_status = first_status(
            contract,
            ("scientific_status", "contract_status", "validation_status", "status"),
        )
        contract_present = (root / contract_ref).is_file()
        ir_registry_present = (root / ir_registry_ref).is_file()
        ir_artifact_present = ir_artifact_ref is not None
        test_plan_present = (root / test_plan_ref).is_file()
        ir_layer_complete = all(
            (contract_present, ir_registry_present, ir_artifact_present, test_plan_present)
        )
        selected = normalized(selection_status) in SELECTED_STATUSES
        rows.append(
            {
                "domain": domain,
                "feature_id": feature_id,
                "contract_ref": contract_ref if contract_present else None,
                "ir_registry_ref": ir_registry_ref if ir_registry_present else None,
                "ir_artifact_ref": ir_artifact_ref,
                "test_plan_ref": test_plan_ref if test_plan_present else None,
                "contract_present": contract_present,
                "ir_registry_present": ir_registry_present,
                "ir_artifact_present": ir_artifact_present,
                "test_plan_present": test_plan_present,
                "ir_layer_complete": ir_layer_complete,
                "contract_status": contract_status,
                "selection_status": selection_status,
                "scientific_status": scientific_status,
                "execution_status": execution_status,
                "canonical_selection_explicit": selected,
                "implementation_ready_asserted": normalized(execution_status)
                in {"ready_for_code_generation", "implementation_ready", "executable_approved"},
            }
        )
    return rows
'''
    new_inventory = '''def build_feature_inventory(root: pathlib.Path, matrix_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source_row in sorted(matrix_rows, key=lambda row: (row.get("domain", ""), row.get("feature_id", ""))):
        feature_id = str(source_row["feature_id"])
        domain = str(source_row["domain"])
        contract_ref = f"registry/math-contracts/{feature_id}/contract.yaml"
        ir_registry_ref = f"registry/ir/{feature_id}/ir.yaml"
        contract = load(root / contract_ref, {})
        ir_registry = load(root / ir_registry_ref, {})
        if not isinstance(contract, dict):
            contract = {}
        if not isinstance(ir_registry, dict):
            ir_registry = {}
        ir_artifact_ref = locate_ir_artifact(root, feature_id, ir_registry)
        ir_artifact = {}
        if ir_artifact_ref:
            artifact_path = root / ir_artifact_ref
            try:
                if artifact_path.suffix.lower() == ".json":
                    ir_artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
                else:
                    ir_artifact = load(artifact_path, {})
            except Exception:
                ir_artifact = {}
        if not isinstance(ir_artifact, dict):
            ir_artifact = {}
        status_source = {**ir_artifact, **ir_registry}
        selection_status = first_status(
            status_source,
            ("selection_status", "canonical_status", "approval_status", "status", "ir_kind"),
        )
        scientific_status = first_status(
            status_source,
            ("scientific_status", "validation_status", "prototype_classification", "semantic_quality"),
        )
        execution_status = first_status(
            status_source,
            ("execution_status", "computational_status", "implementation_status"),
        )
        contract_status = first_status(
            contract,
            ("scientific_status", "contract_status", "validation_status", "status"),
        )
        contract_present = (root / contract_ref).is_file()
        ir_registry_present = (root / ir_registry_ref).is_file()
        ir_artifact_present = ir_artifact_ref is not None
        test_plan_ref = locate_test_plan(root, feature_id)
        test_plan_present = test_plan_ref is not None
        ir_layer_complete = all((contract_present, ir_artifact_present, test_plan_present))
        selected = normalized(selection_status) in SELECTED_STATUSES
        if ir_registry_present and ir_artifact_ref == ir_registry_ref:
            representation_mode = "substantive_registry_ir"
        elif ir_registry_present:
            representation_mode = "registry_plus_external_ir"
        else:
            representation_mode = "external_ir_without_registry_entry"
        rows.append(
            {
                "domain": domain,
                "feature_id": feature_id,
                "contract_ref": contract_ref if contract_present else None,
                "ir_registry_ref": ir_registry_ref if ir_registry_present else None,
                "ir_artifact_ref": ir_artifact_ref,
                "test_plan_ref": test_plan_ref,
                "contract_present": contract_present,
                "ir_registry_present": ir_registry_present,
                "ir_artifact_present": ir_artifact_present,
                "test_plan_present": test_plan_present,
                "ir_layer_complete": ir_layer_complete,
                "ir_representation_mode": representation_mode,
                "registry_normalization_required": not ir_registry_present,
                "contract_status": contract_status,
                "selection_status": selection_status,
                "scientific_status": scientific_status,
                "execution_status": execution_status,
                "canonical_selection_explicit": selected,
                "implementation_ready_asserted": normalized(execution_status)
                in {"ready_for_code_generation", "implementation_ready", "executable_approved"},
            }
        )
    return rows
'''
    text = replace_once(text, old_inventory, new_inventory, "feature inventory")

    text = replace_once(
        text,
        '    old_matrix = load(registry_dir / "domain-feature-matrix.yaml", {}).get("rows", [])\n    feature_rows = build_feature_inventory(root, old_matrix)\n',
        '    authoritative_rows = authoritative_matrix(root, old_domain_registry)\n    feature_rows = build_feature_inventory(root, authoritative_rows)\n',
        "authoritative matrix",
    )

    text = text.replace(
        '"meaning": "Each active feature has an IR registry entry, an IR artifact, and a structural test plan.",',
        '"meaning": "Each active feature has a mathematical contract, an IR artifact, and a structural test plan; a separate IR registry entry is optional for legacy prototype layouts.",',
    )

    loop_marker = '''        domain["next_phase"] = current.get("next_phase")
    old_domain_registry.update(meta)
'''
    loop_replacement = '''        domain["next_phase"] = current.get("next_phase")
        if isinstance(domain.get("counts"), dict):
            domain["counts"]["features"] = current.get("feature_count", 0)
            domain["counts"]["contract_plans"] = current.get("feature_count", 0) if domain.get("contract_plan_present") else 0
            domain["counts"]["ir_plans"] = current.get("feature_count", 0) if domain.get("ir_plan_present") else 0
    if isinstance(old_domain_registry.get("global_counts"), dict):
        old_domain_registry["global_counts"]["features"] = total_features
        old_domain_registry["global_counts"]["contract_plans"] = sum(
            domain_by_id.get(row.get("domain_id"), {}).get("feature_count", 0)
            for row in old_domain_registry.get("domains", []) if row.get("contract_plan_present")
        )
        old_domain_registry["global_counts"]["ir_plans"] = sum(
            domain_by_id.get(row.get("domain_id"), {}).get("feature_count", 0)
            for row in old_domain_registry.get("domains", []) if row.get("ir_plan_present")
        )
    old_domain_registry.update(meta)
'''
    text = replace_once(text, loop_marker, loop_replacement, "corrected domain counts")

    old_report = '''The legacy aggregate count of 175 is retained as the current active feature inventory because it is reproduced
from the sixteen domain catalogues and matched to the generated feature matrices. Historical lineages, rejected
or deferred candidates, and internal IR node identifiers are not added to this active count.
'''
    new_report = '''The current authoritative active count is **{total_features}**. The previous aggregate of 175 recursively
counted nine identifiers under `legacy_goose_feature_ids` in the Capacities preparation. That source explicitly
marks those identifiers as non-authoritative. They are now preserved as lineage evidence but excluded from the
active feature matrix. Historical, rejected, deferred, and internal IR node identifiers are likewise excluded.
'''
    text = replace_once(text, old_report, new_report, "feature count explanation")

    BUILDER.write_text(text, encoding="utf-8", newline="\n")


def upgrade_validator() -> None:
    text = VALIDATOR.read_text(encoding="utf-8")
    text = text.replace("EXPECTED_FEATURES = 175", "EXPECTED_FEATURES = 166")
    text = text.replace(
        '''    required_flags = (
        "contract_present",
        "ir_registry_present",
        "ir_artifact_present",
        "test_plan_present",
        "ir_layer_complete",
    )
''',
        '''    required_flags = (
        "contract_present",
        "ir_artifact_present",
        "test_plan_present",
        "ir_layer_complete",
    )
''',
    )
    VALIDATOR.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    upgrade_builder()
    upgrade_validator()
    print("current registry builder upgraded for authoritative features and heterogeneous IR layouts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
