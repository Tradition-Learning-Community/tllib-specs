# TLC-FC-02-COMMUNITY-001 — Community admissibility constraint

## What is this feature?

This package is the final implementation handoff for the Community admissibility constraint. It exposes structural description and validation only. The scientific measure, coherence function, actor domain, comparator, and result semantics remain unresolved and opaque.

## What must be implemented?

Accept the exact feature identity and a supported operation, validate complete provenance, preserve source object `TLC-SO-COMMUNITY-008`, preserve the authoritative 29 unresolved identifiers exactly, transport opaque values unchanged, and return deterministic normalized structural metadata. A scientific execution request must be rejected with `COMMUNITY_ERR_UNSUPPORTED_EXECUTION_REQUEST`.

## Inputs and output

The input is a Community specification request containing `feature_id`, `operation`, optional opaque values, and optional supplied provenance references. A successful describe or validate operation returns an immutable structural result containing the exact feature identity, source artifacts, source objects, dependencies, unresolved items, opaque values, traceability, status, and deterministic-serialization marker.

## Mandatory and forbidden behavior

Mandatory behavior is defined in `contract.json` and verified by `acceptance.json`. The supplemental semantic IR must remain non-canonical evidence. Scientific evaluation, inferred scientific types, invented dimensions or equations, default semantics, source mutation, unresolved-item changes, and partial success after failure are forbidden.

## Implementation freedom

Programming language, API spelling, internal decomposition, storage, ownership, allocation, concurrency, and error transport are unrestricted unless they change an observable obligation. The total step order shown by the upstream algorithm is not mandatory; only the partial-order constraints in `contract.json` are normative.

## Errors and conformance

Observable errors include feature mismatch, missing source artifacts, incomplete traceability, unresolved-set preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution. Conformance requires every acceptance test to pass and every forbidden behavior to remain impossible.

## Unresolved scientific semantics

Yes. All 29 Community domain reservations remain `preserved_unresolved`. In addition, the historical semantic variant is preserved without promotion, and its measure, coherence, actor-domain, and result semantics are not executable.