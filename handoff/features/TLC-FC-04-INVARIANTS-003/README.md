# TLC-FC-04-INVARIANTS-003 — Invariant declaration catalog

This package defines the final structural handoff for Invariant declaration catalog.

## What must be implemented

Implement `build_invariant_declaration_catalog` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `InvariantDeclarationCatalog` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-002, TLC-SO-INVARIANTS-003, TLC-SO-INVARIANTS-004, TLC-SO-INVARIANTS-005, TLC-SO-INVARIANTS-006, TLC-SO-INVARIANTS-008, TLC-SO-INVARIANTS-009, TLC-SO-INVARIANTS-011, TLC-SO-INVARIANTS-012, TLC-SO-INVARIANTS-014, TLC-SO-INVARIANTS-015, TLC-SO-INVARIANTS-016, TLC-SO-INVARIANTS-018, TLC-SO-INVARIANTS-019, TLC-SO-INVARIANTS-020, TLC-SO-INVARIANTS-023, TLC-SO-INVARIANTS-024, TLC-SO-INVARIANTS-025, TLC-SO-INVARIANTS-028, TLC-SO-INVARIANTS-029, TLC-SO-INVARIANTS-030, TLC-SO-INVARIANTS-034, TLC-SO-INVARIANTS-036, TLC-SO-INVARIANTS-037, TLC-SO-INVARIANTS-038, TLC-SO-INVARIANTS-042, TLC-SO-INVARIANTS-043, TLC-SO-INVARIANTS-047, TLC-SO-INVARIANTS-048, TLC-SO-INVARIANTS-055, TLC-SO-INVARIANTS-056, TLC-SO-INVARIANTS-060, TLC-SO-INVARIANTS-064, TLC-SR-INVARIANTS-001, TLC-SR-INVARIANTS-002, TLC-SR-INVARIANTS-003, TLC-SR-INVARIANTS-004, TLC-SR-INVARIANTS-005, TLC-SR-INVARIANTS-007, TLC-SR-INVARIANTS-008, TLC-SR-INVARIANTS-010, TLC-SR-INVARIANTS-011, TLC-SR-INVARIANTS-013, TLC-SR-INVARIANTS-014, TLC-SR-INVARIANTS-015, TLC-SR-INVARIANTS-017, TLC-SR-INVARIANTS-018, TLC-SR-INVARIANTS-019, TLC-SR-INVARIANTS-022, TLC-SR-INVARIANTS-023, TLC-SR-INVARIANTS-024, TLC-SR-INVARIANTS-027, TLC-SR-INVARIANTS-028, TLC-SR-INVARIANTS-029, TLC-SR-INVARIANTS-033, TLC-SR-INVARIANTS-035, TLC-SR-INVARIANTS-036, TLC-SR-INVARIANTS-037, TLC-SR-INVARIANTS-041, TLC-SR-INVARIANTS-042, TLC-SR-INVARIANTS-046, TLC-SR-INVARIANTS-047, TLC-SR-INVARIANTS-054, TLC-SR-INVARIANTS-055, TLC-SR-INVARIANTS-059, TLC-SR-INVARIANTS-063. The required catalogue status is `deferred_for_scientific_decision`. Required unresolved identifiers are: none. Required provisional assumptions are: TLC-EA-INVARIANTS-003-001.

The required output is an immutable `InvariantDeclarationCatalog`. returns a catalogue preserving declaration IDs, object types, source scopes, and linked evidence relations

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: UnknownDeclarationId, DanglingEvidenceRelation, MissingSourceReference, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Scientific truth conditions remain opaque and require future externally sourced evaluation semantics.
