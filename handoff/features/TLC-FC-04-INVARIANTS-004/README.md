# TLC-FC-04-INVARIANTS-004 — Disciple invariant scope declaration

This package defines the final structural handoff for Disciple invariant scope declaration.

## What must be implemented

Implement `declare_disciple_invariant_scope` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `ScopedInvariantDeclaration` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-007, TLC-SR-INVARIANTS-006. The required catalogue status is `deferred_for_scientific_decision`. Required unresolved identifiers are: none. Required provisional assumptions are: TLC-EA-INVARIANTS-004-001.

The required output is an immutable `ScopedInvariantDeclaration`. returns one declaration scoped to the disciple evidence record and marked scientifically deferred

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: WrongScopeObject, MissingRootReference, StatusPromotionProhibited, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Scientific truth conditions remain opaque and require future externally sourced evaluation semantics.
