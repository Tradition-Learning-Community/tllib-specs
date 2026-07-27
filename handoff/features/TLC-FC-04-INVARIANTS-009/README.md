# TLC-FC-04-INVARIANTS-009 — Cohesion interval symbolic constraint

This package defines the final structural handoff for Cohesion interval symbolic constraint.

## What must be implemented

Implement `construct_cohesion_interval_constraint` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `SymbolicCohesionIntervalConstraint` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-065, TLC-SR-INVARIANTS-064. The required catalogue status is `rejected_as_feature`. Required unresolved identifiers are: TLC-UT-INVARIANTS-009. Required provisional assumptions are: TLC-EA-INVARIANTS-009-001.

The required output is an immutable `SymbolicCohesionIntervalConstraint`. produces interval membership, below-bound fragmentation annotation, and above-bound centralization-and-rigidity annotation ASTs with TLC-UT-INVARIANTS-009 preserved

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: MissingIntervalSymbol, MissingCohesionReservation, MissingCohesionEvidence, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Unresolved scientific identifiers remain attached to their affected evidence and must never be resolved implicitly.
