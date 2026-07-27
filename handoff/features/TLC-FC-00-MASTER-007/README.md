# TLC-FC-00-MASTER-007 — Admissible Master dynamics

This package defines the final observable handoff for Admissible Master dynamics.

## What must be implemented

Implement one conditional opaque-provider operation that accepts only the exact feature, object, relation, and unresolved collections stated in `contract.json`. Preserve their identities and order, emit complete provenance, and expose the stable errors listed by the contract.

## Inputs and output

Valid object references: TLC-SO-MASTER-026, TLC-SO-MASTER-036. Valid relation references: TLC-SR-MASTER-026, TLC-SR-MASTER-033. Required unresolved identifiers: none.

The output is an immutable envelope with explicit evaluated or unresolved status; any provider payload remains opaque and unchanged. No external domain dependency is required.

## Mandatory and forbidden behavior

Exact identity, membership, order, unresolved preservation, opacity, immutability, failure atomicity, and provenance are mandatory. Scientific completion, inferred equations or values, invented runtime types or layouts, external mutation, and successful partial results are forbidden.

## Implementation freedom

Language, public naming, storage, ownership mechanism, allocation, serialization, concurrency policy, error transport, and internal validation decomposition remain free unless they change observable behavior.

## Errors and conformance

Return the stable errors in `contract.json` for their stated conditions with no observable partial result. Conformance requires every test in `acceptance.json` and every preservation obligation to pass. Scientific canonicalization remains outside this package.
