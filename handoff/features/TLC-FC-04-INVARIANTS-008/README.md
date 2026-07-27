# TLC-FC-04-INVARIANTS-008 — Invariant state vocabulary

This package defines the final structural handoff for Invariant state vocabulary.

## What must be implemented

Implement `assemble_invariant_state_vocabulary` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `InvariantStateVocabulary` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-001, TLC-SO-INVARIANTS-041, TLC-SO-INVARIANTS-050, TLC-SO-INVARIANTS-051, TLC-SO-INVARIANTS-052, TLC-SO-INVARIANTS-054, TLC-SO-INVARIANTS-059, TLC-SO-INVARIANTS-061, TLC-SO-INVARIANTS-063, TLC-SO-INVARIANTS-066, TLC-SO-INVARIANTS-067, TLC-SO-INVARIANTS-069, TLC-SR-INVARIANTS-001, TLC-SR-INVARIANTS-002, TLC-SR-INVARIANTS-003, TLC-SR-INVARIANTS-004, TLC-SR-INVARIANTS-005, TLC-SR-INVARIANTS-006, TLC-SR-INVARIANTS-007, TLC-SR-INVARIANTS-008, TLC-SR-INVARIANTS-009, TLC-SR-INVARIANTS-010, TLC-SR-INVARIANTS-011, TLC-SR-INVARIANTS-012, TLC-SR-INVARIANTS-013, TLC-SR-INVARIANTS-014, TLC-SR-INVARIANTS-015, TLC-SR-INVARIANTS-016, TLC-SR-INVARIANTS-017, TLC-SR-INVARIANTS-018, TLC-SR-INVARIANTS-019, TLC-SR-INVARIANTS-020, TLC-SR-INVARIANTS-021, TLC-SR-INVARIANTS-022, TLC-SR-INVARIANTS-023, TLC-SR-INVARIANTS-024, TLC-SR-INVARIANTS-025, TLC-SR-INVARIANTS-026, TLC-SR-INVARIANTS-027, TLC-SR-INVARIANTS-028, TLC-SR-INVARIANTS-029, TLC-SR-INVARIANTS-030, TLC-SR-INVARIANTS-031, TLC-SR-INVARIANTS-032, TLC-SR-INVARIANTS-033, TLC-SR-INVARIANTS-034, TLC-SR-INVARIANTS-035, TLC-SR-INVARIANTS-036, TLC-SR-INVARIANTS-037, TLC-SR-INVARIANTS-038, TLC-SR-INVARIANTS-039, TLC-SR-INVARIANTS-040, TLC-SR-INVARIANTS-041, TLC-SR-INVARIANTS-042, TLC-SR-INVARIANTS-043, TLC-SR-INVARIANTS-044, TLC-SR-INVARIANTS-045, TLC-SR-INVARIANTS-046, TLC-SR-INVARIANTS-047, TLC-SR-INVARIANTS-048, TLC-SR-INVARIANTS-049, TLC-SR-INVARIANTS-050, TLC-SR-INVARIANTS-051, TLC-SR-INVARIANTS-052, TLC-SR-INVARIANTS-053, TLC-SR-INVARIANTS-054, TLC-SR-INVARIANTS-055, TLC-SR-INVARIANTS-056, TLC-SR-INVARIANTS-057, TLC-SR-INVARIANTS-058, TLC-SR-INVARIANTS-059, TLC-SR-INVARIANTS-060, TLC-SR-INVARIANTS-061, TLC-SR-INVARIANTS-062, TLC-SR-INVARIANTS-063, TLC-SR-INVARIANTS-064, TLC-SR-INVARIANTS-065, TLC-SR-INVARIANTS-066, TLC-SR-INVARIANTS-067, TLC-SR-INVARIANTS-068. The required catalogue status is `deferred_for_targeted_extraction`. Required unresolved identifiers are: TLC-UT-INVARIANTS-001, TLC-UT-INVARIANTS-002, TLC-UT-INVARIANTS-003, TLC-UT-INVARIANTS-004, TLC-UT-INVARIANTS-005, TLC-UT-INVARIANTS-006, TLC-UT-INVARIANTS-007, TLC-UT-INVARIANTS-008, TLC-UT-INVARIANTS-010, TLC-UT-INVARIANTS-011, TLC-UT-INVARIANTS-012. Required provisional assumptions are: TLC-EA-INVARIANTS-008-001.

The required output is an immutable `InvariantStateVocabulary`. returns a vocabulary keyed by state-term IDs with unresolved IDs attached to affected terms

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: UnknownStateTermId, DuplicateIdentifier, UnresolvedMappingLoss, MissingSourceReference, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Unresolved scientific identifiers remain attached to their affected evidence and must never be resolved implicitly.
