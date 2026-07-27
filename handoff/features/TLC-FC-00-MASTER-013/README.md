# TLC-FC-00-MASTER-013 — Master-versus-expert predicate

This package defines the final observable handoff for Master-versus-expert predicate.

## What must be implemented

Implement one structural descriptor operation that accepts only the exact feature, object, relation, and unresolved collections stated in `contract.json`. Preserve their identities and order, emit complete provenance, and expose the stable errors listed by the contract.

## Inputs and output

Valid object references: TLC-SO-MASTER-038. Valid relation references: TLC-SR-MASTER-035. Required unresolved identifiers: TLC-GU-00342, TLC-UT-MASTER-025.

The output is an immutable structural descriptor. No external domain dependency is required.

## Mandatory and forbidden behavior

Exact identity, membership, order, unresolved preservation, opacity, immutability, failure atomicity, and provenance are mandatory. Scientific completion, inferred equations or values, invented runtime types or layouts, external mutation, and successful partial results are forbidden.

## Implementation freedom

Language, public naming, storage, ownership mechanism, allocation, serialization, concurrency policy, error transport, and internal validation decomposition remain free unless they change observable behavior.

## Errors and conformance

Return the stable errors in `contract.json` for their stated conditions with no observable partial result. Conformance requires every test in `acceptance.json` and every preservation obligation to pass. Unresolved scientific semantics are deliberately preserved and must not be converted into executable defaults.
