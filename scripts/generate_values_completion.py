from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "f2b4dc5b04d88f9fc39b455aa8a8b463691ae4aa"
PREP = ROOT / "registry" / "domain-progress" / "values"

coverage = yaml.safe_load((PREP / "functional-coverage.yaml").read_text(encoding="utf-8"))["features"]
objects = yaml.safe_load((PREP / "scientific-inventory.yaml").read_text(encoding="utf-8"))["objects"]
relations = yaml.safe_load((PREP / "relation-inventory.yaml").read_text(encoding="utf-8"))["relations"]
object_by_id = {x["provisional_object_id"]: x for x in objects}
feature_by_id = {x["feature_id"]: x for x in coverage}

specs = {
    "001": {
        "purpose": "Compile the cited axiomatic-foundation statements into a source-addressable constraint AST.",
        "responsibility": "Reject unknown statements and preserve each accepted axiom or hypothesis as an unevaluated constraint node.",
        "entrypoint": "compile_axiomatic_foundation_constraint_ast",
        "inputs": ["statements: Sequence[AxiomaticStatement]", "provenance: SourceProvenance"],
        "output": "constraint_ast: AxiomaticConstraintAst",
        "errors": ["empty_statement_set", "unknown_source_identifier", "duplicate_statement_identifier"],
        "unresolved": ["axiom_scientific_status", "constraint_truth_semantics"],
    },
    "003": {
        "purpose": "Assemble the four admissible short-term, contextual-adaptation, and group-impact equations into a dynamics AST.",
        "responsibility": "Bind cited equation expressions to their source objects while preserving their declared order and dynamic role.",
        "entrypoint": "assemble_admissible_value_dynamics_ast",
        "inputs": ["equations: Sequence[SymbolicDynamicsEquation]", "symbols: SymbolTable"],
        "output": "dynamics_ast: AdmissibleValueDynamicsAst",
        "errors": ["missing_equation_source", "unbound_symbol", "duplicate_equation_role"],
        "unresolved": ["state_domains", "initial_conditions", "solver_and_discretization"],
    },
    "004": {
        "purpose": "Assemble the deferred consolidation, motivation, and collective-feedback equations without resolving their scientific status.",
        "responsibility": "Create three role-labelled dynamics nodes and retain each local blocker on the corresponding node.",
        "entrypoint": "assemble_deferred_value_dynamics_ast",
        "inputs": ["consolidation: SymbolicEquation", "motivation: SymbolicEquation", "collective_feedback: SymbolicEquation"],
        "output": "dynamics_ast: DeferredValueDynamicsAst",
        "errors": ["missing_required_role", "source_role_mismatch", "unknown_source_identifier"],
        "unresolved": ["consolidation_semantics", "motivation_semantics", "collective_feedback_semantics"],
    },
    "005": {
        "purpose": "Compile the provisionally separated axiomatic-dynamics equation into an unevaluated expression node.",
        "responsibility": "Parse and source-bind exactly one symbolic equation while retaining its provisional separation.",
        "entrypoint": "compile_axiomatic_dynamics_expression",
        "inputs": ["expression: SymbolicExpression", "source_object_id: ScientificObjectId"],
        "output": "node: AxiomaticDynamicsExpressionNode",
        "errors": ["empty_expression", "unexpected_source_object", "expression_parse_error"],
        "unresolved": ["axiomatic_dynamics_classification", "evaluation_semantics"],
    },
    "006": {
        "purpose": "Assemble the decision-influence and collective-understanding equations as two named symbolic transformations.",
        "responsibility": "Produce a transformation AST with distinct decision and collective-intelligence branches.",
        "entrypoint": "assemble_value_transformation_ast",
        "inputs": ["decision_equation: SymbolicEquation", "collective_equation: SymbolicEquation"],
        "output": "transformation_ast: ValueTransformationAst",
        "errors": ["missing_transformation_branch", "branch_source_mismatch", "unbound_symbol"],
        "unresolved": ["input_output_domains", "evaluation_algorithm"],
    },
    "007": {
        "purpose": "Compile the cited value-validity-domain set expression into a membership-query AST.",
        "responsibility": "Represent the tuple components and named membership predicates without deciding the opaque carrier sets.",
        "entrypoint": "compile_validity_domain_membership_ast",
        "inputs": ["domain_expression: SymbolicSetExpression", "tuple_symbols: Sequence[SymbolId]"],
        "output": "membership_ast: ValidityDomainMembershipAst",
        "errors": ["missing_tuple_component", "unknown_membership_predicate", "expression_parse_error"],
        "unresolved": ["carrier_set_definitions", "membership_evaluation_policy"],
    },
    "008": {
        "purpose": "Compile the fundamental-principle component as a preservation invariant descriptor.",
        "responsibility": "Create a predicate descriptor that compares opaque before/after principle references symbolically.",
        "entrypoint": "compile_fundamental_principle_invariant",
        "inputs": ["before: OpaquePrincipleRef", "after: OpaquePrincipleRef", "source_claim: SymbolicInvariant"],
        "output": "invariant: FundamentalPrincipleInvariant",
        "errors": ["missing_principle_reference", "source_claim_mismatch"],
        "unresolved": ["principle_equality_semantics", "permitted_transformation_scope"],
    },
    "009": {
        "purpose": "Compile the partial-invariance claim into a perturbation-guarded symbolic predicate.",
        "responsibility": "Bind an opaque perturbation, radius symbol, and relative-order claim without evaluating norms or order.",
        "entrypoint": "compile_partial_invariance_predicate",
        "inputs": ["perturbation: OpaquePerturbation", "radius: SymbolicBound", "order_claim: SymbolicOrderClaim"],
        "output": "predicate: PartialInvariancePredicate",
        "errors": ["missing_radius_symbol", "missing_order_claim", "source_claim_mismatch"],
        "unresolved": ["norm_semantics", "relative_order_semantics", "radius_domain"],
    },
    "010": {
        "purpose": "Assemble the five cited essential properties as distinct, unevaluated predicate descriptors.",
        "responsibility": "Produce an ordered property set covering invariance, hierarchy, motivation, context, and integration.",
        "entrypoint": "assemble_essential_property_predicates",
        "inputs": ["property_claims: Mapping[EssentialPropertyKind, SymbolicClaim]"],
        "output": "predicates: EssentialPropertyPredicateSet",
        "errors": ["missing_property_kind", "duplicate_property_kind", "unknown_property_kind"],
        "unresolved": ["property_evaluation_semantics", "cross_property_consistency"],
    },
    "011": {
        "purpose": "Declare the cited quantitative measures as provenance-bearing metric specifications.",
        "responsibility": "Validate unique metric identifiers and retain every formula, scale, and interpretation as opaque metadata.",
        "entrypoint": "declare_quantitative_measure_catalog",
        "inputs": ["measure_declarations: Sequence[OpaqueMeasureDeclaration]"],
        "output": "catalog: QuantitativeMeasureCatalog",
        "errors": ["duplicate_measure_identifier", "missing_measure_provenance", "unknown_source_identifier"],
        "unresolved": ["metric_formulas", "scales_and_units", "comparison_semantics"],
    },
    "012": {
        "purpose": "Declare the cited value spaces and structures as a typed symbolic structure descriptor.",
        "responsibility": "Index each named space or structure and preserve declared containment or association edges.",
        "entrypoint": "declare_value_space_structure",
        "inputs": ["spaces: Sequence[OpaqueSpaceDeclaration]", "edges: Sequence[SymbolicStructureEdge]"],
        "output": "structure: ValueSpaceStructure",
        "errors": ["duplicate_space_identifier", "edge_endpoint_missing", "unknown_structure_edge"],
        "unresolved": ["space_dimensions", "topology_and_metric", "edge_semantics"],
    },
    "013": {
        "purpose": "Bind professional-value, decision-weight, transmission-system, and numeric descriptors into an operator registry.",
        "responsibility": "Create four distinct callable-descriptor entries without assigning signatures or evaluating them.",
        "entrypoint": "bind_value_function_operator_descriptors",
        "inputs": ["descriptors: Mapping[ValueOperatorRole, OpaqueOperatorDescriptor]"],
        "output": "registry: ValueOperatorRegistry",
        "errors": ["missing_operator_role", "duplicate_operator_role", "descriptor_source_mismatch"],
        "unresolved": ["operator_signatures", "numeric_representation", "return_semantics"],
    },
    "014": {
        "purpose": "Compose memory/storage and integration descriptors into an ordered, unevaluated operator pipeline.",
        "responsibility": "Require the memory stage before the integration stage and preserve both opaque payload contracts.",
        "entrypoint": "compose_memory_integration_operator_descriptors",
        "inputs": ["memory_stage: OpaqueOperatorDescriptor", "integration_stage: OpaqueOperatorDescriptor"],
        "output": "pipeline: MemoryIntegrationOperatorPipeline",
        "errors": ["missing_memory_stage", "missing_integration_stage", "invalid_stage_order"],
        "unresolved": ["memory_model", "integration_semantics", "stage_signatures"],
    },
    "018": {
        "purpose": "Validate the structural shape and closed entry range of the systemic-coherence matrix.",
        "responsibility": "Check square shape and entries in the sourced closed interval while leaving endpoint and category semantics opaque.",
        "entrypoint": "validate_systemic_coherence_matrix_structure",
        "inputs": ["matrix: Matrix[OpaqueScalar]", "declared_order: PositiveInteger"],
        "output": "result: CoherenceMatrixValidationResult",
        "errors": ["declared_order_mismatch", "non_square_matrix", "entry_outside_closed_interval"],
        "unresolved": ["UNRES-M", "UNRES-ENDPOINTS", "UNRES-CATEGORIES", "UNRES-OUTPUT"],
        "revises_pilot": True,
    },
}

def dump_yaml(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110), encoding="utf-8")

def relation_ids_for(object_ids):
    return [r["provisional_relation_id"] for r in relations if r.get("source_object_id") in object_ids]

all_unresolved = set()
assumption_ids = []

for suffix, spec in specs.items():
    fid = f"TLC-FC-09-VALUES-{suffix}"
    cov = feature_by_id[fid]
    obj_ids = cov["source_objects"]
    rel_ids = relation_ids_for(obj_ids)
    cid = f"TLC-MC-{fid}"
    iid = f"TLC-IR-{fid}"
    tid = f"TLC-TP-{fid}"
    aid = f"TLC-EA-{fid}-001"
    assumption_ids.append(aid)
    all_unresolved.update(spec["unresolved"])
    source_refs = []
    for oid in obj_ids:
        ref = object_by_id[oid]["source_reference"]
        source_refs.append({
            "path": ref["source_path"],
            "lines": f'{ref["start_line"]}-{ref["end_line"]}',
            "object_id": oid,
            "source_commit": ref["source_commit"],
        })
    assumption = {
        "assumption_id": aid,
        "feature_id": fid,
        "undefined_property": "runtime carrier for symbolic or scientifically opaque values",
        "technical_need": "The implementation needs a lossless carrier to validate structure and provenance.",
        "minimal_choice": "immutable tagged opaque value or symbolic AST node",
        "alternatives_left_open": ["domain-specific value class", "external symbolic engine", "future canonical type"],
        "impact": "Only the specified structural operation is executable; scientific evaluation remains unavailable.",
        "reversibility": "Replace the carrier adapter while preserving IDs, AST shape, and provenance.",
        "status": "provisional_engineering_assumption",
    }
    readiness = {
        "ready_for_limited_engineering_contract": True,
        "ready_for_prototype_ir": True,
        "ready_for_reference_python": True,
        "ready_for_cpp_prototype": True,
        "ready_for_canonical_ir": False,
        "ready_for_production_implementation": False,
    }
    contract = {
        "contract_id": cid,
        "feature_id": fid,
        "contract_kind": "limited_engineering_contract_with_reservations",
        "status": "limited_engineering_contract_with_reservations",
        "scientific_authority": {"authority": "origin/main", "source_commit": SOURCE_COMMIT,
                                   "complete_scientific_contract": False},
        "source_references": source_refs,
        "covered_objects": obj_ids,
        "covered_relations": rel_ids,
        "contextual_relations": [],
        "functional_purpose": spec["purpose"],
        "primary_responsibility": spec["responsibility"],
        "inputs": spec["inputs"],
        "outputs": [spec["output"]],
        "types": {
            "opaque": ["OpaqueScalar", "OpaqueScientificValue", "ScientificObjectId"],
            "parameterized": ["Sequence[T]", "Mapping[K,V]", "Optional[T]"],
            "symbolic": ["SymbolicExpression", "SymbolicClaim", "SourceProvenance"],
        },
        "preconditions": [
            "Every referenced scientific object and relation identifier exists in the Values preparation.",
            "Every required operation-specific input is present and retains source provenance.",
        ],
        "postconditions": [
            f"The {spec['output'].split(':')[0]} is produced by {spec['entrypoint']} without scientific evaluation.",
            "All input source identifiers, unresolved items, and provisional assumptions remain traceable.",
        ],
        "explicitly_sourced_invariants": [
            {"statement": "Provisionally separated scientific objects remain distinct.",
             "source": "registry/domain-progress/values/functional-coverage.yaml"}
        ],
        "errors": spec["errors"],
        "undefined_behaviors": spec["unresolved"],
        "propagated_unresolved": spec["unresolved"],
        "provisional_engineering_assumptions": [assumption],
        "scientific_reservations": [
            "No missing formula, type, unit, scale, order, threshold, aggregation, or scientific algorithm is inferred.",
            "Candidate and deferred scientific status remain unchanged.",
        ],
        "confirmed_dependencies": [],
        "traceability": {
            "source_commit": SOURCE_COMMIT,
            "preparation_feature": fid,
            "revises_contract": "TLC-MC-TLC-FC-09-VALUES-018 candidate contract" if spec.get("revises_pilot") else None,
        },
        "validation_criteria": [
            "operation-specific inputs and output are present",
            "all source identifiers resolve",
            "unresolved and assumption propagation matches the IR",
            "no scientific evaluation or promotion is introduced",
        ],
        "readiness": readiness,
    }
    dump_yaml(ROOT / "registry" / "math-contracts" / fid / "contract.yaml", contract)

    ir = {
        "ir_id": iid,
        "feature_id": fid,
        "contract_id": cid,
        "ir_kind": "prototype_ir_with_reservations",
        "classification": "substantive_and_implementable",
        "entrypoint": spec["entrypoint"],
        "primary_operation": spec["responsibility"],
        "inputs": spec["inputs"],
        "outputs": [spec["output"]],
        "opaque_types": ["OpaqueScalar", "OpaqueScientificValue", "ScientificObjectId"],
        "parameterized_types": ["Sequence[T]", "Mapping[K,V]", "Optional[T]"],
        "symbolic_types": ["SymbolicExpression", "SymbolicClaim", "SourceProvenance"],
        "operations": [
            {"operation_id": f"OP-VALUES-{suffix}-VALIDATE-INPUTS", "kind": "validate_operation_inputs",
             "observable_effect": "named errors identify missing, duplicate, mismatched, or unknown inputs"},
            {"operation_id": f"OP-VALUES-{suffix}-PRIMARY", "kind": spec["entrypoint"],
             "observable_effect": spec["output"]},
            {"operation_id": f"OP-VALUES-{suffix}-ATTACH-TRACE", "kind": "attach_source_traceability",
             "observable_effect": "result retains feature, object, relation, unresolved, and assumption IDs"},
        ],
        "operation_sequence": [
            f"OP-VALUES-{suffix}-VALIDATE-INPUTS",
            f"OP-VALUES-{suffix}-PRIMARY",
            f"OP-VALUES-{suffix}-ATTACH-TRACE",
        ],
        "preconditions": contract["preconditions"],
        "postconditions": contract["postconditions"],
        "invariants": contract["explicitly_sourced_invariants"],
        "errors": spec["errors"],
        "undefined_behaviors": spec["unresolved"],
        "propagated_unresolved": spec["unresolved"],
        "propagated_provisional_assumptions": [aid],
        "traceability": {
            "source_commit": SOURCE_COMMIT,
            "contract": f"registry/math-contracts/{fid}/contract.yaml",
            "source_objects": obj_ids,
            "source_relations": rel_ids,
            "replaces_historical_irs": [
                "ir-functional.candidate.json", "ir-semantic.candidate.json"
            ] if spec.get("revises_pilot") else [],
        },
        "determinism_status": "deterministic_for_structural_construction_and_validation",
        "testability_status": "operation_specific_structural_tests_defined",
        "implementation_constraints": [
            "Implement exactly the named construction or validation operation.",
            "Preserve symbolic payloads and source order unless the contract explicitly states otherwise.",
            "Do not evaluate formulas or invent scientific semantics.",
        ],
        "active_or_historical_status": "active_prototype",
        "blocks_all_prototype_progress": False,
        "readiness": readiness,
    }
    dump_yaml(ROOT / "registry" / "ir" / fid / "ir.yaml", ir)

    output_name = spec["output"].split(":")[0]
    test_plan = {
        "test_plan_id": tid,
        "feature_id": fid,
        "contract_id": cid,
        "ir_id": iid,
        "entrypoint": spec["entrypoint"],
        "primary_operation": spec["responsibility"],
        "inputs_under_test": spec["inputs"],
        "expected_output_or_effect": spec["output"],
        "cases": [
            {"case_id": f"VALUES-{suffix}-NOMINAL", "kind": "nominal",
             "assertion": f"{spec['entrypoint']} produces {spec['output']} from valid source-addressable inputs."},
            {"case_id": f"VALUES-{suffix}-TYPE-SHAPE", "kind": "type_or_shape",
             "assertion": "Operation-specific required input roles and container shapes are validated before construction."},
            {"case_id": f"VALUES-{suffix}-OBSERVABLE", "kind": "observable_result",
             "assertion": f"The {output_name} exposes the operation-specific structure described by the contract."},
            {"case_id": f"VALUES-{suffix}-POST", "kind": "postcondition",
             "assertion": contract["postconditions"][0]},
            {"case_id": f"VALUES-{suffix}-PRECONDITION", "kind": "invalid_precondition",
             "assertion": f"An invalid required input returns one of: {', '.join(spec['errors'])}."},
            {"case_id": f"VALUES-{suffix}-OPAQUE", "kind": "opaque_value",
             "assertion": "Opaque payloads survive construction unchanged and are never scientifically evaluated."},
            {"case_id": f"VALUES-{suffix}-PROVENANCE", "kind": "provenance",
             "assertion": f"Output retains feature {fid} and all covered object and relation identifiers."},
            {"case_id": f"VALUES-{suffix}-UNRESOLVED", "kind": "unresolved_propagation",
             "assertion": f"Output retains unresolved items: {', '.join(spec['unresolved'])}."},
            {"case_id": f"VALUES-{suffix}-ASSUMPTION", "kind": "assumption_propagation",
             "assertion": f"Output retains provisional assumption {aid}."},
            {"case_id": f"VALUES-{suffix}-NO-INVENTION", "kind": "scientific_non_evaluation",
             "assertion": "No absent formula, scale, ordering, threshold, aggregation, or scientific result is computed."},
            {"case_id": f"VALUES-{suffix}-CONFORMANCE", "kind": "contract_ir_conformance",
             "assertion": "Entrypoint, inputs, output, errors, unresolved, assumption, classification, and readiness match."},
            {"case_id": f"VALUES-{suffix}-INTEGRATION", "kind": "minimal_integration",
             "assertion": "Contract loader -> IR entrypoint -> provenance serializer preserves operation-specific structure."},
        ],
        "forbidden_expected_results": ["invented numeric oracle", "scientific approval", "canonical semantics"],
        "readiness": "planned",
    }
    dump_yaml(ROOT / "registry" / "test-plans" / fid / "test-plan.yaml", test_plan)

active = {
    "feature_id": "TLC-FC-09-VALUES-018",
    "active_ir_id": "TLC-IR-TLC-FC-09-VALUES-018",
    "active_artifact": "registry/ir/TLC-FC-09-VALUES-018/ir.yaml",
    "historical_artifacts": [
        {"path": "ir/TLC-FC-09-VALUES-018/ir-functional.candidate.json", "status": "historical_comparison_only"},
        {"path": "ir/TLC-FC-09-VALUES-018/ir-semantic.candidate.json", "status": "historical_comparison_only"},
    ],
    "ambiguity_resolved": True,
    "scientific_validation": "still_required_for_canonical_release",
}
dump_yaml(ROOT / "ir" / "TLC-FC-09-VALUES-018" / "active-ir.yaml", active)

manifest = {
    "domain_index": "09",
    "domain_id": "values",
    "domain_name": "Values",
    "source_commit": SOURCE_COMMIT,
    "total_features": 14,
    "contracts_reused": 0,
    "contracts_created": 13,
    "contracts_revised": 1,
    "canonical_irs_preserved": 0,
    "pilot_irs_revised": 1,
    "prototype_irs_created": 14,
    "feature_without_ir": [],
    "classification_A_count": 14,
    "classification_B_count": 0,
    "classification_C_count": 0,
    "classification_D_count": 0,
    "classification_E_count": 0,
    "unresolved_propagated": sorted(all_unresolved),
    "provisional_assumptions": assumption_ids,
    "test_plans_created_or_revised": 14,
    "ready_for_reference_python_count": 14,
    "ready_for_cpp_prototype_count": 14,
    "ready_for_canonical_ir_count": 0,
    "remaining_blockers": [
        "scientific validation of deferred and candidate claims",
        "canonical scientific types, domains, units, scales, orders, and operator semantics",
        "production algorithms and numerical policies",
    ],
    "scientific_reservations_preserved": True,
}
dump_yaml(ROOT / "registry" / "ir-batches" / "values-domain-completion-001" / "manifest.yaml", manifest)
dump_yaml(ROOT / "registry" / "math-contract-batches" / "values-domain-completion-001" / "manifest.yaml", manifest)

report = f"""# Values substantive prototype completion

Authority: `origin/main` at `{SOURCE_COMMIT}`.

Fourteen prepared features have operation-specific limited engineering contracts, active prototype IRs,
and functional test plans. Each IR is class A for its explicitly bounded software operation: AST construction,
descriptor validation/indexing, symbolic predicate assembly, or sourced structural validation. This readiness
does not authorize scientific evaluation, canonical IR, or production implementation.

The historical Values-018 functional and semantic candidates remain comparison-only. The active designation
now points uniquely to `registry/ir/TLC-FC-09-VALUES-018/ir.yaml`.

Scientific reservations remain intact. No formula, unit, scale, total order, threshold, aggregation rule,
distribution, numerical precision, solver, or scientific algorithm was invented.
"""
for rel in [
    "reports/ir-batches/values-domain-completion-001/completion-report.md",
    "reports/math-contract-batches/values-domain-completion-001/batch-report.md",
]:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
