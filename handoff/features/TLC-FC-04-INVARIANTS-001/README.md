# TLC-FC-04-INVARIANTS-001 — Admissibility constraint set

This package defines the final structural handoff for Admissibility constraint set.

## What must be implemented

Implement `build_admissibility_constraint_set` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `ConstraintSet` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-010, TLC-SO-INVARIANTS-032, TLC-SO-INVARIANTS-033, TLC-SO-INVARIANTS-046, TLC-SR-INVARIANTS-009, TLC-SR-INVARIANTS-031, TLC-SR-INVARIANTS-032, TLC-SR-INVARIANTS-045. The required catalogue status is `retained_with_reservations`. Required unresolved identifiers are: none. Required provisional assumptions are: TLC-EA-INVARIANTS-001-001.

The required output is an immutable `ConstraintSet`. returns exactly one entry per supplied covered axiom ID with source order and references retained

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: DuplicateAxiomId, UnknownAxiomId, MissingSourceReference, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Scientific truth conditions remain opaque and require future externally sourced evaluation semantics.
