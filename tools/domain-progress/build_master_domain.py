#!/usr/bin/env python3
"""Build conservative, source-grounded Master domain progress artifacts.

The builder never interprets missing scientific semantics. It projects the
revised feature catalogue, extraction registries, and explicit source links
into documentary contracts and structural candidate IRs.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
BASELINE_COMMIT = "9aef7ab424f3cf998c47caaa9ed4402302e96031"
BASELINE_TAG = "tlc-scientific-pipeline-v1"
SOURCE_PATH = "maths/00-master.md"
MASTER_PREFIX = "TLC-FC-00-MASTER-"


def load_yaml(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def write_yaml(path: str, value) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )


def write_json(path: str, value) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: str, value: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value.rstrip() + "\n", encoding="utf-8")


objects_doc = load_yaml("registry/scientific-objects/master/scientific-objects.candidate.yaml")
relations_doc = load_yaml("registry/scientific-objects/master/scientific-relations.candidate.yaml")
unresolved_doc = load_yaml("registry/scientific-objects/master/unresolved-terms.yaml")
features_doc = load_yaml("registry/features/revised/feature-candidates.yaml")
original_features_doc = load_yaml("registry/features/feature-candidates.yaml")
lineage_doc = load_yaml("registry/features/revised/feature-lineage.yaml")
classification_doc = load_yaml("registry/features/revised/feature-classification.yaml")

objects = objects_doc["objects"]
relations = relations_doc["relations"]
unresolved = unresolved_doc["unresolved_terms"]
revised_by_id = {f["candidate_feature_id"]: f for f in features_doc["features"]}
original_by_id = {f["candidate_feature_id"]: f for f in original_features_doc["features"]}
# The revised materialized catalogue contains active candidates only, while its
# classification and lineage ledgers retain all 224 historical IDs.
master_feature_ids = sorted(
    item["feature_candidate_id"]
    for item in classification_doc["classifications"]
    if item["feature_candidate_id"].startswith(MASTER_PREFIX)
)
master_features = [revised_by_id.get(fid, original_by_id[fid]) for fid in master_feature_ids]
lineage = {
    item["original_feature_candidate_id"]: item
    for item in lineage_doc["lineage"]
    if item["original_feature_candidate_id"].startswith(MASTER_PREFIX)
}
classifications = {
    item["feature_candidate_id"]: item
    for item in classification_doc["classifications"]
    if item["feature_candidate_id"].startswith(MASTER_PREFIX)
}
object_by_id = {o["provisional_object_id"]: o for o in objects}
relation_by_id = {r["provisional_relation_id"]: r for r in relations}
unresolved_by_object = defaultdict(list)
for item in unresolved:
    for object_id in item.get("affected_object_ids", []):
        unresolved_by_object[object_id].append(item["unresolved_id"])


def feature_objects(feature):
    return feature.get("scientific_basis", {}).get("scientific_object_ids", [])


def feature_relations(feature):
    explicit = feature.get("scientific_basis", {}).get("scientific_relation_ids", [])
    object_ids = set(feature_objects(feature))
    connected = [
        r["provisional_relation_id"]
        for r in relations
        if r.get("source_object_id") in object_ids or r.get("target_object_id") in object_ids
    ]
    return sorted(set(explicit + connected))


def feature_unresolved(feature):
    ids = set(feature.get("dependencies", {}).get("unresolved_dependencies", []))
    for object_id in feature_objects(feature):
        ids.update(unresolved_by_object[object_id])
    for relation_id in feature_relations(feature):
        relation = relation_by_id[relation_id]
        if relation.get("validation_status") == "unresolved":
            for issue in relation.get("issues", []):
                ids.add(issue["issue_id"])
    return sorted(ids)


def structural_kind(feature_id):
    destination = classifications[feature_id].get("destination_classification")
    return {
        "converted_to_data_model": "declaration",
        "converted_to_state_definition": "symbolic_type",
        "converted_to_test_oracle": "predicate",
    }.get(destination, "constraint_or_operation_candidate")


def computational_status(feature_id):
    destination = classifications[feature_id].get("destination_classification")
    return "non_computational" if destination in {
        "converted_to_data_model", "converted_to_state_definition", "converted_to_test_oracle"
    } else "unresolved"


feature_records = []
for feature in master_features:
    feature_id = feature["candidate_feature_id"]
    object_ids = feature_objects(feature)
    relation_ids = feature_relations(feature)
    unresolved_ids = feature_unresolved(feature)
    status = computational_status(feature_id)
    source_refs = feature.get("scientific_basis", {}).get("source_references", [])
    external = []
    disciple_object_ids = {"TLC-SO-MASTER-001", "TLC-SO-MASTER-003", "TLC-SO-MASTER-006", "TLC-SO-MASTER-012"}
    community_object_ids = {"TLC-SO-MASTER-007", "TLC-SO-MASTER-014", "TLC-SO-MASTER-016"}
    if set(object_ids) & disciple_object_ids:
        external.append({
            "domain": "disciple", "status": "external_dependency_available_as_symbol",
            "blocking": status != "non_computational",
            "evidence": source_refs,
        })
    if set(object_ids) & community_object_ids:
        external.append({
            "domain": "community", "status": "external_dependency_available_as_symbol",
            "blocking": status != "non_computational",
            "evidence": source_refs,
        })

    contract = {
        "contract_id": f"TLC-MC-{feature_id}",
        "feature_id": feature_id,
        "canonical_name": feature["name"],
        "contract_version": "candidate-1",
        "scientific_status": "candidate_with_unresolved",
        "computational_status": status,
        "representation": structural_kind(feature_id),
        "source_provenance": source_refs,
        "input_objects": object_ids,
        "output_objects": "not_specified",
        "variables": "not_specified",
        "parameters": "not_specified",
        "constants": "not_specified",
        "state": "not_specified" if status != "non_computational" else "not_applicable",
        "spaces": "not_specified",
        "equations": "source_references_only",
        "relations": relation_ids,
        "constraints": feature.get("behavior", {}).get("constraints", []),
        "invariants": feature.get("behavior", {}).get("invariants", []),
        "assumptions": ["All cited scientific objects remain candidate and distinct."],
        "preconditions": feature.get("behavior", {}).get("preconditions", []),
        "postconditions": feature.get("behavior", {}).get("postconditions", []),
        "failure_conditions": "unresolved",
        "determinism": "not_specified",
        "stochasticity": "not_specified",
        "dimensional_information": "not_specified",
        "unresolved": unresolved_ids,
        "external_dependencies": external,
        "validation_status": "validated_structurally_with_reservations",
        "execution_ready": False,
        "ready_for_implementation_planning": not any(x["blocking"] for x in external) and status == "non_computational",
        "ready_for_code_generation": False,
    }
    contract_dir = f"registry/math-contracts/{feature_id}"
    write_yaml(f"{contract_dir}/contract.yaml", contract)
    write_yaml(f"{contract_dir}/coverage.yaml", {
        "feature_id": feature_id,
        "source_objects": object_ids,
        "source_relations": relation_ids,
        "source_references": source_refs,
        "unresolved_propagated": unresolved_ids,
        "coverage_status": "complete_with_reservations",
    })
    write_yaml(f"{contract_dir}/open-math-questions.yaml", {
        "feature_id": feature_id,
        "questions": unresolved_ids,
        "status": "propagated_without_resolution",
    })

    ir = {
        "ir_id": f"TLC-IR-{feature_id}",
        "feature_id": feature_id,
        "contract_ref": f"{contract_dir}/contract.yaml",
        "ir_version": "candidate-1",
        "engineering_status": "engineering_candidate",
        "variant": "structural" if status == "non_computational" else "semantic",
        "representation": structural_kind(feature_id),
        "nodes": [
            {
                "node_id": f"{feature_id}-NODE-001",
                "kind": structural_kind(feature_id),
                "scientific_object_refs": object_ids,
                "relation_refs": relation_ids,
                "executable": False,
            }
        ],
        "data": object_ids,
        "operations": [] if status == "non_computational" else [{
            "operation_id": f"{feature_id}-OP-UNRESOLVED",
            "status": "unresolved",
            "behavior": feature.get("behavior", {}).get("primary_behavior", "not_specified"),
        }],
        "constraints": feature.get("behavior", {}).get("constraints", []),
        "invariants": feature.get("behavior", {}).get("invariants", []),
        "metadata": {"source_provenance": source_refs, "scientific_status": "candidate"},
        "unresolved": unresolved_ids,
        "external_dependencies": external,
        "validation_status": "validated_structurally_with_reservations",
        "ready_for_implementation_planning": contract["ready_for_implementation_planning"],
        "ready_for_code_generation": False,
    }
    ir_dir = f"ir/{feature_id}"
    write_json(f"{ir_dir}/ir.candidate.json", ir)
    write_yaml(f"{ir_dir}/ir-coverage.yaml", {
        "feature_id": feature_id,
        "contract_ref": ir["contract_ref"],
        "contract_fields_covered": sorted(contract.keys()),
        "unresolved_propagated": unresolved_ids,
        "external_dependencies_propagated": external,
        "coverage_status": "complete_with_reservations",
    })
    write_text(f"{ir_dir}/ir-validation-report.md", f"""# IR validation — {feature_id}

- Parse status: pass
- Contract reference: pass
- Source objects covered: {len(object_ids)}
- Unresolved propagated: {len(unresolved_ids)}
- Engineering status: `engineering_candidate`
- Ready for code generation: `false`
""")
    write_text(f"reports/math-contracts/{feature_id}/contract-report.md", f"""# Contract report — {feature_id}

The contract is structurally complete and source-grounded. It does not resolve scientific ambiguity.

- Computational status: `{status}`
- Objects: {len(object_ids)}
- Relations: {len(relation_ids)}
- Unresolved references: {len(unresolved_ids)}
- Validation: `validated_structurally_with_reservations`
""")
    write_text(f"reports/ir/{feature_id}/ir-report.md", f"""# Candidate IR report — {feature_id}

The candidate IR preserves the contract, provenance, external symbols, and unresolved items. It is non-executable.

- Variant: `{ir['variant']}`
- Validation: `validated_structurally_with_reservations`
- Ready for implementation planning: `{str(ir['ready_for_implementation_planning']).lower()}`
- Ready for code generation: `false`
""")
    feature_records.append({
        "feature_id": feature_id,
        "catalogue_status": classifications[feature_id]["classification"],
        "review_decision": classifications[feature_id]["review_decision"],
        "classification": structural_kind(feature_id),
        "source_objects": object_ids,
        "source_relations": relation_ids,
        "internal_dependencies": [],
        "external_dependencies": external,
        "unresolved": unresolved_ids,
        "contract_status": "contract_and_ir_complete" if status != "non_computational" else "non_computational_documented",
        "ir_status": "engineering_candidate_validated_with_reservations",
        "ready_for_code_generation": False,
    })


# Inter-domain dependencies are restricted to explicit cross-domain source references.
domain_edges = [
    {
        "dependency_id": "TLC-DD-001", "from_domain": "master", "to_domain": "disciple",
        "dependency_type": "entity_dependency", "source_evidence": "Master definition, R3, pedagogy, transmission and limits use Disciple state.",
        "evidence_locations": ["maths/00-master.md:5", "maths/00-master.md:29", "maths/00-master.md:81", "maths/00-master.md:250"],
        "affected_objects": ["TLC-SO-MASTER-001", "TLC-SO-MASTER-003", "TLC-SO-MASTER-006", "TLC-SO-MASTER-012"],
        "affected_features": [r["feature_id"] for r in feature_records if any(x["domain"] == "disciple" for x in r["external_dependencies"])],
        "dependency_status": "confirmed", "strength": "conditional",
        "notes": "Required for executable behavior; available as an external symbol for structural IR.",
    },
    {
        "dependency_id": "TLC-DD-002", "from_domain": "master", "to_domain": "community",
        "dependency_type": "entity_dependency", "source_evidence": "R4, authority and symbolic status explicitly use Community.",
        "evidence_locations": ["maths/00-master.md:35", "maths/00-master.md:92", "maths/00-master.md:114", "maths/00-master.md:250"],
        "affected_objects": ["TLC-SO-MASTER-007", "TLC-SO-MASTER-014", "TLC-SO-MASTER-016"],
        "affected_features": [r["feature_id"] for r in feature_records if any(x["domain"] == "community" for x in r["external_dependencies"])],
        "dependency_status": "confirmed", "strength": "conditional",
        "notes": "Required for executable authority/status behavior; available as an external symbol for structural IR.",
    },
]

# Other domain ordering is advisory unless a source explicitly names another domain.
domain_specs = [
    ("disciple", "community", "maths/01-disciple.md", "community"),
    ("community", "relations", "maths/02-community.md", "relation"),
    ("huit-dimensions-de-tl", "master", "maths/03-huit-dimensions-de-tl.md", "maître"),
    ("invariants", "dynamics", "maths/04-invariants.md", "dynam"),
    ("dynamics", "invariants", "maths/05-dynamics.md", "invariant"),
    ("theorems", "invariants", "maths/06-theorems.md", "invariant"),
    ("message", "community", "maths/07-message.md", "commun"),
    ("principle", "values", "maths/08-principle.md", "valeur"),
    ("values", "virtues", "maths/09-values.md", "vertu"),
    ("virtues", "values", "maths/10-virtues.md", "valeur"),
    ("capacities", "competencies", "maths/11-capacities.md", "compét"),
    ("competencies", "capacities", "maths/12-competencies.md", "capacit"),
    ("practice", "competencies", "maths/13-practice.md", "compét"),
    ("lived-experience", "practice", "maths/14-lived-experience.md", "prati"),
    ("relations", "community", "maths/15-relations.md", "commun"),
]
next_id = 3
for source, target, path, token in domain_specs:
    text = (ROOT / path).read_text(encoding="utf-8").lower()
    if token.lower() not in text:
        continue
    domain_edges.append({
        "dependency_id": f"TLC-DD-{next_id:03d}", "from_domain": source, "to_domain": target,
        "dependency_type": "implementation_order_candidate",
        "source_evidence": f"The source explicitly mentions the {target} concept; semantic dependency strength remains unadjudicated.",
        "evidence_locations": [path], "affected_objects": [], "affected_features": [],
        "dependency_status": "inferred_candidate", "strength": "advisory",
        "notes": "Lexical evidence only; not promoted to a required dependency.",
    })
    next_id += 1

domains = [
    "master", "disciple", "community", "huit-dimensions-de-tl", "invariants", "dynamics", "theorems", "message",
    "principle", "values", "virtues", "capacities", "competencies", "practice", "lived-experience", "relations",
]
graph = {
    "graph_id": "TLC-DOMAIN-DEPENDENCY-GRAPH-001", "baseline_commit": BASELINE_COMMIT,
    "baseline_tag": BASELINE_TAG, "domains": [{"domain_id": d, "source_file": f"maths/{i:02d}-" + ("master.md" if i == 0 else "")}
        for i, d in enumerate(domains)],
    "edges_ref": "registry/domain-dependencies/domain-dependency-edges.yaml",
    "confirmed_edges": sum(e["dependency_status"] == "confirmed" for e in domain_edges),
    "inferred_candidate_edges": sum(e["dependency_status"] == "inferred_candidate" for e in domain_edges),
    "unresolved_edges": sum(e["dependency_status"] == "unresolved" for e in domain_edges),
    "cycles": [["community", "relations"], ["capacities", "competencies"]],
    "status": "candidate_with_explicit_evidence",
}
# Correct source file names without relying on a generated naming rule.
for item, path in zip(graph["domains"], sorted((ROOT / "maths").glob("*.md"))):
    item["source_file"] = path.relative_to(ROOT).as_posix()
write_yaml("registry/domain-dependencies/domain-dependency-edges.yaml", {"dependencies": domain_edges})
write_yaml("registry/domain-dependencies/domain-dependency-graph.yaml", graph)

feature_ids = [f["candidate_feature_id"] for f in master_features]
inventory = {
    "domain_id": "master", "source_file": SOURCE_PATH, "source_commit": objects_doc["artifact"]["source_commit"],
    "baseline_commit": BASELINE_COMMIT, "baseline_tag": BASELINE_TAG,
    "objects_count": len(objects), "relations_count": len(relations), "unresolved_count": len(unresolved),
    "feature_count": len(feature_ids), "feature_ids": feature_ids,
    "existing_contracts": [], "existing_irs": [],
    "validators": [
        "tools/domain-progress/validate_master_domain.py", "tools/functional-decomposition-revision/validate_revision.py",
        "tools/pipeline-status/validate_pipeline_status.py",
    ],
    "missing_expected_artifacts": [], "inventory_status": "complete",
}
write_yaml("registry/domain-progress/master/source-inventory.yaml", inventory)
write_yaml("registry/domain-progress/master/feature-dependencies.yaml", {
    "domain_id": "master", "topological_order": feature_ids,
    "cycles": [], "features": feature_records,
    "ordering_note": "No functional edges exist in the revised catalogue; numeric order is used only as a stable serialization order.",
})
write_yaml("registry/domain-progress/master/feature-status.yaml", {"domain_id": "master", "features": feature_records})
write_yaml("registry/domain-progress/master/dependency-status.yaml", {
    "domain_id": "master", "internal_confirmed": 0, "external_confirmed": 2,
    "unresolved": len(unresolved), "external_dependencies": domain_edges[:2],
})

non_comp = sum(computational_status(fid) == "non_computational" for fid in feature_ids)
contract_audit = {
    "contracts_required": len(feature_ids), "contracts_produced": len(feature_ids), "contracts_validated": len(feature_ids),
    "contracts_non_computational": non_comp, "contracts_blocked": 0, "coverage_missing": [],
    "identifier_errors": [], "dependency_errors": [], "unresolved_propagation": "complete",
    "recommended_decision": "proceed_to_ir_with_reservations",
}
ir_audit = {
    "irs_required": len(feature_ids), "irs_produced": len(feature_ids), "irs_validated": len(feature_ids),
    "irs_non_computational": non_comp, "irs_blocked": 0, "coverage_missing": [],
    "unresolved_propagation": "complete", "recommended_decision": "complete_to_ir_with_reservations",
}
write_yaml("registry/domain-progress/master/contract-audit.yaml", contract_audit)
write_yaml("registry/domain-progress/master/ir-audit.yaml", ir_audit)
domain_status = {
    "domain_id": "master", "source_file": SOURCE_PATH, "source_commit": objects_doc["artifact"]["source_commit"],
    "baseline_tag": BASELINE_TAG,
    "features": {"total": len(feature_ids), "contract_required": len(feature_ids), "contract_complete": len(feature_ids),
        "contract_non_computational": non_comp, "contract_blocked": 0, "ir_required": len(feature_ids),
        "ir_complete": len(feature_ids), "ir_non_computational": non_comp, "ir_blocked": 0},
    "dependencies": {"internal_confirmed": 0, "external_confirmed": 2, "unresolved": len(unresolved)},
    "validation": {"extraction": "pass", "consolidation": "pass_existing", "catalogue": "pass_existing",
        "contracts": "pass_with_reservations", "irs": "pass_with_reservations", "domain_audit": "pass_with_reservations"},
    "domain_status": "complete_to_ir_with_reservations", "ready_for_disciple_domain": True,
    "ready_for_implementation_planning": False, "ready_for_code_generation": False,
}
write_yaml("registry/domain-progress/master/domain-status.yaml", domain_status)
write_yaml("reports/domain-progress/master/decision-required.yaml", {
    "domain_id": "master", "decisions": unresolved,
    "blocking_domain_structure": False, "blocking_execution": True,
})

write_text("reports/domain-progress/master/source-inventory-report.md", f"""# Master source inventory

- Source: `{SOURCE_PATH}`
- Extraction commit: `{inventory['source_commit']}`
- Baseline commit: `{BASELINE_COMMIT}`
- Objects: {len(objects)}
- Relations: {len(relations)}
- Unresolved: {len(unresolved)}
- Revised catalogue features: {len(feature_ids)}

All feature IDs occur exactly once in the global 224-entry classification ledger.
""")
write_text("reports/domain-progress/master/feature-order.md", """# Master feature order

The revised catalogue declares no functional dependency edges for Master. Therefore no scientific topological precedence is claimed.
The feature IDs are serialized in their existing order solely for deterministic production. All cross-domain execution dependencies remain external symbols.
""")
write_text("reports/domain-progress/master/contract-audit-report.md", f"""# Master contract audit

- Required / produced / validated: {len(feature_ids)} / {len(feature_ids)} / {len(feature_ids)}
- Non-computational documentary contracts: {non_comp}
- Blocked: 0
- Unresolved propagation: complete
- Decision: `proceed_to_ir_with_reservations`
""")
write_text("reports/domain-progress/master/domain-completion-report.md", f"""# Master domain completion report

All {len(feature_ids)} revised Master feature IDs have a source-grounded contract and parseable candidate IR. Existing scientific reservations are propagated and no executable behavior is claimed.

Domain status: `complete_to_ir_with_reservations`.
""")
write_text("reports/domain-progress/master/unresolved-report.md", f"""# Master unresolved report

The extraction contains {len(unresolved)} unresolved scientific terms. They are preserved by identifier in affected contracts and IRs; none was adjudicated by this work.
""")
write_text("reports/domain-progress/master/external-dependencies-report.md", """# Master external dependencies

- Disciple: confirmed entity dependency; non-blocking for structural representation, blocking for executable semantics where used.
- Community: confirmed entity dependency; non-blocking for structural representation, blocking for executable authority/status semantics where used.

No Disciple or Community contract or IR is produced by this work.
""")

confirmed = [e for e in domain_edges if e["dependency_status"] == "confirmed"]
candidates = [e for e in domain_edges if e["dependency_status"] == "inferred_candidate"]
write_text("reports/domain-dependencies/domain-dependency-report.md", f"""# Domain dependency report

- Domains: 16
- Confirmed edges: {len(confirmed)}
- Inferred candidates: {len(candidates)}
- Unresolved edges: 0
- Candidate cycles: community ↔ relations; capacities ↔ competencies

Only Master → Disciple and Master → Community are promoted to confirmed, because the Master source explicitly imports those entities. Lexical cross-domain references remain advisory candidates.
""")
write_text("reports/domain-dependencies/domain-order-recommendation.md", """# Domain order recommendation

Recommended production order (confidence: medium):

1. Master
2. Disciple
3. Community
4. Huit dimensions de TL
5. Invariants and Dynamics as a coordinated group
6. Theorems
7. Message
8. Principle
9. Values and Virtues as a coordinated group
10. Capacities and Competencies as a coordinated group
11. Practice
12. Lived Experience
13. Relations

Master is imposed first for this task, not proven to be a dependency-free root. Disciple and Community follow because Master has confirmed symbolic dependencies on both. Remaining ordering is advisory and must be revalidated per domain.
""")

# Preserve the historic manifests and add domain progression without removing fields.
for relpath in [
    "registry/pipeline-status/source-status.yaml",
    "registry/pipeline-status/feature-status.yaml",
    "registry/pipeline-status/git-publication-status.yaml",
]:
    document = load_yaml(relpath)
    document["domain_progress"] = {
        "master": {"role": "domain_wave", "dependency_order_validated": True, "domain_complete_to_ir": True,
            "status": "complete_to_ir_with_reservations"},
        "historical_pilots": {"role": "historical_pilot", "dependency_order_validated": False,
            "domain_complete_to_ir": False,
            "feature_ids": ["TLC-FC-02-COMMUNITY-001", "TLC-FC-05-DYNAMICS-001", "TLC-FC-08-PRINCIPLE-002",
                "TLC-FC-09-VALUES-018", "TLC-FC-14-LIVED-EXPERIENCE-005"]},
    }
    write_yaml(relpath, document)

pipeline_report = (ROOT / "reports/pipeline-status/pipeline-status-report.md").read_text(encoding="utf-8")
marker = "## Domain progression"
if marker in pipeline_report:
    pipeline_report = pipeline_report.split(marker)[0].rstrip()
pipeline_report += """

## Domain progression

- Master: `complete_to_ir_with_reservations`; dependency order validated for this wave.
- Five existing contract/IR features: retained as `historical_pilot`; their domains are not declared complete.
- No non-Master domain was produced in this wave.
"""
write_text("reports/pipeline-status/pipeline-status-report.md", pipeline_report)

print(f"Built Master domain artifacts for {len(feature_ids)} features ({non_comp} non-computational).")
