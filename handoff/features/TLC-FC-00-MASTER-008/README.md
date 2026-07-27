# TLC-FC-00-MASTER-008 — Reserved Master dynamics

This package defines the final observable handoff for Reserved Master dynamics.

## What must be implemented

Implement one conditional opaque-provider operation that accepts only the exact feature, object, relation, and unresolved collections stated in `contract.json`. Preserve their identities and order, emit complete provenance, and expose the stable errors listed by the contract.

## Inputs and output

Valid object references: TLC-SO-MASTER-025, TLC-SO-MASTER-027, TLC-SO-MASTER-028. Valid relation references: TLC-SR-MASTER-025, TLC-SR-MASTER-027, TLC-SR-MASTER-028. Required unresolved identifiers: TLC-GU-00333, TLC-GU-00334, TLC-GU-00335, TLC-UT-MASTER-016, TLC-UT-MASTER-017, TLC-UT-MASTER-018.

The output is an immutable envelope with explicit evaluated or unresolved status; any provider payload remains opaque and unchanged. No external domain dependency is required.

## Mandatory and forbidden behavior

Exact identity, membership, order, unresolved preservation, opacity, immutability, failure atomicity, and provenance are mandatory. Scientific completion, inferred equations or values, invented runtime types or layouts, external mutation, and successful partial results are forbidden.

## Implementation freedom

Language, public naming, storage, ownership mechanism, allocation, serialization, concurrency policy, error transport, and internal validation decomposition remain free unless they change observable behavior.

## Errors and conformance

Return the stable errors in `contract.json` for their stated conditions with no observable partial result. Conformance requires every test in `acceptance.json` and every preservation obligation to pass. Unresolved scientific semantics are deliberately preserved and must not be converted into executable defaults.
