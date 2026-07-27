# TLC-FC-00-MASTER-004 — Reserved Master constraints

This package defines the final observable handoff for Reserved Master constraints.

## What must be implemented

Implement one conditional opaque-provider operation that accepts only the exact feature, object, relation, and unresolved collections stated in `contract.json`. Preserve their identities and order, emit complete provenance, and expose the stable errors listed by the contract.

## Inputs and output

Valid object references: TLC-SO-MASTER-004, TLC-SO-MASTER-006, TLC-SO-MASTER-017, TLC-SO-MASTER-018, TLC-SO-MASTER-019, TLC-SO-MASTER-020, TLC-SO-MASTER-021, TLC-SO-MASTER-034. Valid relation references: TLC-SR-MASTER-003, TLC-SR-MASTER-005, TLC-SR-MASTER-016, TLC-SR-MASTER-017, TLC-SR-MASTER-018, TLC-SR-MASTER-019, TLC-SR-MASTER-020, TLC-SR-MASTER-031, TLC-SR-MASTER-036, TLC-SR-MASTER-037. Required unresolved identifiers: TLC-GU-00319, TLC-GU-00321, TLC-GU-00328, TLC-GU-00329, TLC-GU-00330, TLC-GU-00332, TLC-GU-00339, TLC-RELISS-MASTER-003, TLC-UT-MASTER-002, TLC-UT-MASTER-004, TLC-UT-MASTER-011, TLC-UT-MASTER-012, TLC-UT-MASTER-013, TLC-UT-MASTER-015, TLC-UT-MASTER-022.

The output is an immutable envelope with explicit evaluated or unresolved status; any provider payload remains opaque and unchanged. The disciple domain is required read-only only when evaluated mode is requested.

## Mandatory and forbidden behavior

Exact identity, membership, order, unresolved preservation, opacity, immutability, failure atomicity, and provenance are mandatory. Scientific completion, inferred equations or values, invented runtime types or layouts, external mutation, and successful partial results are forbidden.

## Implementation freedom

Language, public naming, storage, ownership mechanism, allocation, serialization, concurrency policy, error transport, and internal validation decomposition remain free unless they change observable behavior.

## Errors and conformance

Return the stable errors in `contract.json` for their stated conditions with no observable partial result. Conformance requires every test in `acceptance.json` and every preservation obligation to pass. Unresolved scientific semantics are deliberately preserved and must not be converted into executable defaults.
