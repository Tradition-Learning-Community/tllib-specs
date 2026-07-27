# TLC-FC-04-INVARIANTS-006 — Collective ethics invariant expression

This package defines the final structural handoff for Collective ethics invariant expression.

## What must be implemented

Implement `construct_collective_ethics_invariant_expression` as a deterministic, immutable evidence transformation. It validates feature-covered identities and source references, preserves opaque content and historical catalogue status, and returns a `SymbolicCollectiveEthicsInvariant` with complete provenance.

## Valid inputs and required output

The accepted covered evidence identities are: TLC-SO-INVARIANTS-013, TLC-SO-INVARIANTS-057, TLC-SR-INVARIANTS-012, TLC-SR-INVARIANTS-056. The required catalogue status is `deferred_for_targeted_extraction`. Required unresolved identifiers are: none. Required provisional assumptions are: TLC-EA-INVARIANTS-006-001.

The required output is an immutable `SymbolicCollectiveEthicsInvariant`. produces the source-defined integral AST followed by derivative-equals-zero and gradient-equals-zero constraint ASTs with provenance

## Mandatory and forbidden behavior

Identity, source order, provenance, opaque values, status, assumptions, reservations, unresolved mappings, input immutability, deterministic structural equality, and failure atomicity are mandatory. Scientific truth evaluation, status promotion, inferred thresholds or comparators, transition graphs, chronology, causality, symmetry, transitivity, dimensions, units, precision, and numerical methods are forbidden.

## Implementation freedom

Language, public wrapper naming, storage, allocation, ownership mechanism, serialization, concurrency policy, error transport, and internal traversal remain free when observable behavior is unchanged.

## Errors and conformance

The authoritative observable error codes are: MissingRequiredSymbol, MissingCollectiveEthicsEvidence, ScientificEvaluationProhibited, PreservationViolation. Errors publish no partial result. Conformance requires every test in `acceptance.json`, exact preservation of the source envelope, and rejection of scientific evaluation. Scientific truth conditions remain opaque and require future externally sourced evaluation semantics.
