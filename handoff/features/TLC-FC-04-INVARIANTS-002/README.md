# TLC-FC-04-INVARIANTS-002 — Documentary definition evidence index

This package defines the final structural handoff for Documentary definition evidence index.

## What must be implemented

Implement `index_definition_fragments` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `DefinitionEvidenceIndex` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-017, TLC-SO-INVARIANTS-022, TLC-SO-INVARIANTS-027, TLC-SO-INVARIANTS-035, TLC-SO-INVARIANTS-040, TLC-SO-INVARIANTS-045, TLC-SO-INVARIANTS-053, TLC-SO-INVARIANTS-058, TLC-SO-INVARIANTS-062, TLC-SR-INVARIANTS-016, TLC-SR-INVARIANTS-021, TLC-SR-INVARIANTS-026, TLC-SR-INVARIANTS-034, TLC-SR-INVARIANTS-039, TLC-SR-INVARIANTS-044, TLC-SR-INVARIANTS-052, TLC-SR-INVARIANTS-057, TLC-SR-INVARIANTS-061. The required catalogue status is `rejected_as_feature`. Required unresolved identifiers are: none. Required provisional assumptions are: TLC-EA-INVARIANTS-002-001.

The required output is an immutable `DefinitionEvidenceIndex`. returns an index keyed by definition object ID with every entry documentary and non-executable

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: DuplicateDefinitionId, InvalidCoveredIdentifier, MissingSourceReference, FeatureStatusPromotion, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Scientific truth conditions remain opaque and require future externally sourced evaluation semantics.
