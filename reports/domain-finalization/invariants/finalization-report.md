# Invariants domain finalization

## Baseline and scope

The finalization uses `main` commit `c34d40713bf444d38f92f76e1c6239ee596d5a18` and branch `phase4/invariants-domain-finalization-001`.

The authoritative baseline and domain feature matrix confirm exactly ten active features:

1. `TLC-FC-04-INVARIANTS-001`
2. `TLC-FC-04-INVARIANTS-002`
3. `TLC-FC-04-INVARIANTS-003`
4. `TLC-FC-04-INVARIANTS-004`
5. `TLC-FC-04-INVARIANTS-005`
6. `TLC-FC-04-INVARIANTS-006`
7. `TLC-FC-04-INVARIANTS-007`
8. `TLC-FC-04-INVARIANTS-008`
9. `TLC-FC-04-INVARIANTS-009`
10. `TLC-FC-04-INVARIANTS-010`

No population divergence was found. Every feature has one preserved limited engineering contract, one preserved prototype IR, one preserved source test plan, and contract traceability to `maths/04-invariants/invariants.md`.

## Source findings

The historical preparation reports identify 69 candidate scientific objects, 68 candidate relations, 12 unresolved terms, ten catalogue features, nine internal feature edges, and no internal cycle. The source contracts and prototype IR batch report establish ten structurally implementable prototype IRs and no canonical or production scientific readiness.

The twelve unresolved terms are fully mapped. Eleven belong to feature 008 and one belongs to feature 009. They block scientific execution and code-generation claims, but do not block the source-preserving structural behavior required by this phase.

## Finalized feature behavior

| Feature | Public operation | Finalized behavior |
|---|---|---|
| 001 | `build_admissibility_constraint_set` | Builds an immutable ordered set of covered opaque axiom records. |
| 002 | `index_definition_fragments` | Indexes nine definition fragments as documentary, non-executable evidence. |
| 003 | `build_invariant_declaration_catalog` | Builds an immutable declaration and source-relation catalogue without truth evaluation. |
| 004 | `declare_disciple_invariant_scope` | Constructs one scientifically deferred disciple-scope declaration without inventing members or validation rules. |
| 005 | `attach_interpretation_annotations` | Attaches three ordered non-normative annotations without changing invariant truth or status. |
| 006 | `construct_collective_ethics_invariant_expression` | Constructs exactly three source-defined immutable symbolic AST roots without evaluation. |
| 007 | `construct_disintegration_relation` | Constructs one exact immutable source-backed `refers_to` relation record. |
| 008 | `assemble_invariant_state_vocabulary` | Builds the twelve-term state vocabulary and preserves the exact eleven-ID unresolved attachment map. |
| 009 | `construct_cohesion_interval_constraint` | Constructs exactly three source-defined cohesion AST roots and preserves `TLC-UT-INVARIANTS-009`. |
| 010 | `index_state_interpretation_fragments` | Indexes three documentary state annotations as non-operational and rejected source metadata. |

## Patterns

The demonstrated shared patterns are:

- validation of source-covered identities, relations, targets, references, and statuses;
- exact preservation of opaque values;
- immutable result construction with a common preservation envelope;
- explicit propagation of unresolved identifiers and provisional assumptions;
- deterministic identity-preserving ordering;
- explicit failure at the scientific-evaluation boundary;
- source-defined symbolic AST construction for features 006 and 009;
- documentary non-promotion for features 002 and 010 and non-normative annotation behavior for feature 005.

Resemblance, textual duplication, structural duplication, and demonstrated equivalence were kept distinct. No public features were merged. Features 006 and 009 share only an internal AST-construction shape; their templates, evidence, status, unresolved behavior, output types, and scopes remain feature-owned.

## Optimizations and normalizations

The finalization applies only semantics-preserving transformations:

- common traceability and preservation envelopes;
- common validation-before-construction phase order;
- shared structural error families with feature-specific aliases retained;
- common immutable evidence, index, relation, and AST representation shapes;
- explicit classification of documentary, scientific, internal structural, and execution dependencies;
- exact source-order rules when order is semantic or explicitly required;
- testable postcondition and conservation checks;
- explicit external-evaluator outcomes instead of invented scientific computations.

No source equation, threshold, type, dimension, unit, ordering, cardinality, time rule, comparator, evaluator, transition graph, or scientific condition was added or changed.

## Source catalogue statuses

Features 002, 009, and 010 carry historical source metadata `rejected_as_feature`. The current authoritative baseline nevertheless lists all ten identifiers as active. Finalization therefore preserves this historical status as metadata while selecting every baseline-active feature for the Invariants implementation specification. This is not a scientific status change and no active feature is rejected by this work.

## Decisions and remaining blockers

There are no blockers preventing definition of the required observable structural behavior.

The following remain deliberately unresolved or external:

- eleven state-vocabulary scientific meanings in feature 008;
- cohesion domain, ordering, comparator, bounds, metric, score, transition rule, and evaluator in feature 009;
- concrete runtime scientific types and truth evaluators for all features;
- exact member set and validation rule for feature 004;
- future upstream reconciliation with Master, Disciple, Community, and Dynamics.

These are classified as `deferred_to_scientific_review`, `preserved_as_opaque`, `external_evaluator_required`, `parameter_required`, `descriptive_scope`, or `external_reference`. They remain blocking for scientific execution where the source says so, not for this implementation-specification package.

## Produced package

For every active feature, this branch adds:

- `registry/optimized-ir/invariants/<FEATURE_ID>/ir.yaml`;
- `registry/algorithms/invariants/<FEATURE_ID>/algorithm.yaml`;
- `registry/oracles/invariants/<FEATURE_ID>/oracle.yaml`.

The domain package also includes the manifest, finalized status, patterns, complete module specification, implementation tasks, decision classification, this report, and a domain-scoped validator.

## Conservation statement

- All ten active features are retained.
- No source contract is modified or removed.
- No source IR is modified or removed.
- `maths/04-invariants/invariants.md` is not modified.
- No Master, Disciple, Community, Huit Dimensions, or other concurrently finalized domain artifact is modified.
- No global reconciliation registry is regenerated or modified.
- No C++ code is produced.
- No Python binding is produced.
- No reference implementation is produced.

## Completion

Invariants is complete for this phase through the implementation-ready specification package: every active feature has preserved sources, a finalized implementation IR, a directly implementable structural algorithm, an acceptance oracle, module integration, and a future developer task.
