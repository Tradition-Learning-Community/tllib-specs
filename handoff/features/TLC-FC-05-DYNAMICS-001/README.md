# TLC-FC-05-DYNAMICS-001 — Constraint admissible

## What is this feature?

This feature packages the four source-defined Community viability constraints as distinct, traceable, unevaluated predicate records.

## What must be implemented?

Implement `EVALUATE-VIABILITY-PREDICATES-SYMBOLICALLY`. It accepts an opaque Community state and source-addressable opaque viability bounds, validates identifiers and carrier shapes, and returns one `UnevaluatedPredicateSet` containing exactly four distinct predicates.

## Inputs and output

Valid inputs are `community_state: OpaqueCommunityState` and `bounds: ViabilityBounds[OpaqueScalar]`. The output preserves predicate identity, source order, inclusive comparator notation, opaque payloads, provenance, unresolved items, and reservations.

## Mandatory and forbidden behavior

Validation must complete before a successful result is exposed. No numerical comparison, predicate truth value, aggregate viability Boolean, collapse transition, terminal state, solver, or scientific default may be produced. Failure must expose no partial predicate set.

## Implementation freedom

Language, public spelling, storage, ownership mechanism, allocation, serialization format, concurrency policy, and internal decomposition are implementation-defined when observable behavior is unchanged.

## Errors and conformance

The observable errors are `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` under the conditions in `contract.json`. Conformance requires every test in `acceptance.json` to pass. Viability truth, time semantics, operator definitions, norm semantics, memory notation, and final scientific output semantics remain unresolved.