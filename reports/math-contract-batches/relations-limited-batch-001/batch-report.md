# Relations limited-contract batch 001

## Authority and scope

This batch is generated from `origin/main` commit `ff800dd1e8e87bb8a89d855d8a45c1ff6bbd8cff`, which merges PR #30. It implements the economic batch `TLC-FIRST-ECONOMIC-001` and contains only `TLC-FC-15-RELATIONS-004` and `TLC-FC-15-RELATIONS-007`.

## Contracts

- `TLC-LC-TLC-FC-15-RELATIONS-004-001` covers three candidate function objects, no covered scientific relation, 31 received and propagated unresolved items, and no strong contractual dependency.
- `TLC-LC-TLC-FC-15-RELATIONS-007-001` covers five candidate relation objects, no covered scientific relation, 12 received and propagated unresolved items, and no strong contractual dependency.

Candidate `refers_to` relations are retained only as contextual traceability. Relevant external domain references remain `documentary_reference_only`. No ambiguous dependency is promoted. The global ambiguous cycle `TLC-GCYCLE-DOMAIN-001` remains unresolved and requires a human decision.

## Explicit limits

The batch does not define complete Relations semantics, global graph properties, universal cardinality, general symmetry or transitivity, complete temporality, numerical methods, execution structures, implementation types, automatic cross-domain compatibility, executable oracles, tests, code, or IR.

No batch validator is committed because the absolute scope requires absence of code. Validation is performed with repository commands and read-only ad hoc checks.

## Validation results

- Thirteen generated YAML files parse successfully; all 42 repository JSON files parse successfully.
- Feature IDs, contract IDs, generated local IDs, exact source references, object coverage, empty covered-relation sets, unresolved counts, dependency classifications, limited-contract markers, and readiness flags pass targeted checks.
- All 31 unresolved items for `TLC-FC-15-RELATIONS-004` and all 12 unresolved items for `TLC-FC-15-RELATIONS-007` are propagated.
- No ambiguous or documentary dependency is promoted; no code, IR path, or `maths/` modification is present.
- Python syntax checks pass for the existing Relations and targeted-review validators. Their execution rejects this downstream contract branch by design because those preparation/review validators prohibit any contract output; they are not batch-contract validators.
- `git diff --check` passes.

## Readiness

- `ready_for_scientific_review`: `true`
- `ready_for_full_contract_extension`: `false`
- `ready_for_ir`: `false`
- `ready_for_implementation_planning`: `false`

The recommended internal disposition is scientific review with reservations.
