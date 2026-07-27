# TLC-FC-00-MASTER-016 — Master composite state

This package defines the final observable handoff for Master composite state.

## What must be implemented

Implement one structural descriptor operation that accepts only the exact feature, object, relation, and unresolved collections stated in `contract.json`. Preserve their identities and order, emit complete provenance, and expose the stable errors listed by the contract.

## Inputs and output

Valid object references: TLC-SO-MASTER-001, TLC-SO-MASTER-009, TLC-SO-MASTER-012, TLC-SO-MASTER-015, TLC-SO-MASTER-035, TLC-SO-MASTER-037. Valid relation references: TLC-SR-MASTER-001, TLC-SR-MASTER-002, TLC-SR-MASTER-003, TLC-SR-MASTER-004, TLC-SR-MASTER-005, TLC-SR-MASTER-006, TLC-SR-MASTER-007, TLC-SR-MASTER-008, TLC-SR-MASTER-011, TLC-SR-MASTER-012, TLC-SR-MASTER-013, TLC-SR-MASTER-014, TLC-SR-MASTER-015, TLC-SR-MASTER-016, TLC-SR-MASTER-017, TLC-SR-MASTER-019, TLC-SR-MASTER-021, TLC-SR-MASTER-022, TLC-SR-MASTER-023, TLC-SR-MASTER-025, TLC-SR-MASTER-030, TLC-SR-MASTER-032, TLC-SR-MASTER-033, TLC-SR-MASTER-034, TLC-SR-MASTER-035. Required unresolved identifiers: TLC-GU-00321, TLC-GU-00322, TLC-GU-00323, TLC-GU-00327, TLC-GU-00340, TLC-GU-00341, TLC-GU-00343, TLC-UT-MASTER-004, TLC-UT-MASTER-005, TLC-UT-MASTER-006, TLC-UT-MASTER-010, TLC-UT-MASTER-023, TLC-UT-MASTER-024, TLC-UT-MASTER-026.

The output is an immutable structural descriptor. The disciple domain is an optional read-only symbol reference.

## Mandatory and forbidden behavior

Exact identity, membership, order, unresolved preservation, opacity, immutability, failure atomicity, and provenance are mandatory. Scientific completion, inferred equations or values, invented runtime types or layouts, external mutation, and successful partial results are forbidden.

## Implementation freedom

Language, public naming, storage, ownership mechanism, allocation, serialization, concurrency policy, error transport, and internal validation decomposition remain free unless they change observable behavior.

## Errors and conformance

Return the stable errors in `contract.json` for their stated conditions with no observable partial result. Conformance requires every test in `acceptance.json` and every preservation obligation to pass. Unresolved scientific semantics are deliberately preserved and must not be converted into executable defaults.
