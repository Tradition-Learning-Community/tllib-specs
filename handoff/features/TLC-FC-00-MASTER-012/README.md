# TLC-FC-00-MASTER-012 — Master operators

This package defines the final observable handoff for Master operators.

## What must be implemented

Implement one conditional opaque-provider operation that accepts only the exact feature, object, relation, and unresolved collections stated in `contract.json`. Preserve their identities and order, emit complete provenance, and expose the stable errors listed by the contract.

## Inputs and output

Valid object references: TLC-SO-MASTER-013, TLC-SO-MASTER-014, TLC-SO-MASTER-029. Valid relation references: TLC-SR-MASTER-012, TLC-SR-MASTER-013, TLC-SR-MASTER-028. Required unresolved identifiers: TLC-GU-00321, TLC-GU-00325, TLC-GU-00326, TLC-GU-00328, TLC-GU-00336, TLC-UT-MASTER-004, TLC-UT-MASTER-008, TLC-UT-MASTER-009, TLC-UT-MASTER-011, TLC-UT-MASTER-019.

The output is an immutable envelope with explicit evaluated or unresolved status; any provider payload remains opaque and unchanged. The community domain is required read-only only when evaluated mode is requested.

## Mandatory and forbidden behavior

Exact identity, membership, order, unresolved preservation, opacity, immutability, failure atomicity, and provenance are mandatory. Scientific completion, inferred equations or values, invented runtime types or layouts, external mutation, and successful partial results are forbidden.

## Implementation freedom

Language, public naming, storage, ownership mechanism, allocation, serialization, concurrency policy, error transport, and internal validation decomposition remain free unless they change observable behavior.

## Errors and conformance

Return the stable errors in `contract.json` for their stated conditions with no observable partial result. Conformance requires every test in `acceptance.json` and every preservation obligation to pass. Unresolved scientific semantics are deliberately preserved and must not be converted into executable defaults.
