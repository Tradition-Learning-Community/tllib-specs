# Mathematical contract report — TLC-FC-08-PRINCIPLE-002

## Work item and selection

- Work item: `TLC-MATH-CONTRACT-TLC-FC-08-PRINCIPLE-002`
- Wave: `CONTRACT_WAVE_1`; verified position: **3 of 5**
- Input branch and commit: `planning/math-contract-entry` at `7f73fd908ff887e6ab3b7d184ca46f0c8477ad68`
- Output branch: `contract/TLC-FC-08-PRINCIPLE-002`
- Entry status: `READY_FOR_MATH_CONTRACT`

The identifier, position, contractable-feature entry, and authorization status all match. Only this feature is treated.

## Inspected inputs and resolved source

The seven mandatory input artifacts were inspected: `contractable-features.yaml`, `contract-dependencies.yaml`, `oracle-basis.yaml`, `contract-wave-1.yaml`, `feature-candidates.yaml`, `feature-lineage.yaml`, and `decomposition-input-snapshot.yaml`. The referenced candidate object record in `registry/scientific-objects/principle/scientific-objects.candidate.yaml` was inspected to confirm identity and the preserved source statement; no content from another contract branch was read.

Authorized traceability resolves exactly one scientific source passage:

- `maths/08-principle.md`, document *Principes (Principles)*, section “Évolution temporelle et dynamique”, lines 198–200, source commit `68a4d4c728bab655631543b3e1788d4f0da31e8e`.

No referenced file was missing and no provenance inconsistency was found. The feature lineage attaches object `TLC-SO-PRINCIPLE-087` and no scientific relation. The broader scientific registry contains a relation involving the object, but the revised feature does not authorize it as feature lineage; it is therefore not used by this contract.

## Scientific contract

The sole normative expression is preserved exactly:

`dP/dt = E(P,D,t)` (with `E` represented by source notation `\mathcal{E}`).

It is classified as a differential equation. The derivative notation provides evidence of a continuous derivative formulation, but no evolution interval, discretization, initial condition, regularity, determinism, stochastic model, space, shape, dimension, or unit is supplied in the authorized passage.

The symbol table contains five entries: `P`, `D`, `t`, `\mathcal{E}`, and the compound derivative `dP/dt`. `P` is recorded as the equation state, `D` and `t` as inputs to the right-hand side, `\mathcal{E}` as an operator, and `dP/dt` as output. These structural roles are direct readings of the equation; their exact semantic meanings and mathematical types remain unresolved.

Counts: 1 scientific object; 0 scientific relations; 5 symbols; 0 defined spaces or sets; 1 state; 2 inputs; 1 output; 1 equation; 0 source constraints; 0 preconditions; 1 directly derived equality postcondition; 0 invariants; 0 hypotheses; 0 properties.

## Dependencies and oracle basis

The candidate dependency registry states `no_contract_dependency`, and inspection found no justified required contract. Definitions of the equation symbols are nevertheless unresolved and may later become shared definitions or dependencies; the contract does not guess their targets.

The oracle basis consists only of `TLC-SO-PRINCIPLE-087` / the preserved equation. It can support equation-structure conformance, but no independent theorem, invariant, property, example, or expected numeric value is available. The executable oracle is explicitly `not_produced`.

## Derivations, excluded choices, and open questions

Direct derivations without semantic change are limited to identifying equation roles, requiring `\mathcal{E}` to accept the ordered arguments `(P,D,t)` and return something comparable with `dP/dt`, and stating equality satisfaction as the postcondition.

Two implementation decisions are deferred: mathematical-to-IR type mapping and any numerical method. Prohibited assumptions include scalarity, shapes, units, finite representation, time step, integrator, tolerance, precision, and solver.

Three mathematical questions remain open: exact symbol semantics/types; evolution domain and regularity; and initial-condition requirements. They block IR readiness, not independent scientific review.

## Issues and validation assessment

- Critical: 0
- Major: 2 — undefined symbol types/domains; missing evolution and initial conditions
- Minor: 1 — oracle basis is structural only

Exact source text and equation normalization were compared; the normalized form is an exact copy aside from display delimiters. Static checks cover YAML readability, feature/wave selection, scope isolation, identifier uniqueness, object existence, symbol references, source preservation, equivalence status, forbidden implementation vocabulary, and `executable_oracle.status`.

Type, dimensional, shape, uniqueness-of-solution, invariant-preservation, and numerical validations were not executed because the required mathematical definitions or examples are absent. Their status is unresolved rather than inferred.

The candidate is ready for independent scientific review because the source equation, limitations, and questions are explicit and traceable. It is not ready for IR, executable tests, or implementation until the blocking mathematical definitions are resolved or accepted by human review. Recommended human decision: `approved_with_reservations`.
