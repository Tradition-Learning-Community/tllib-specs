# TLC-FC-02-COMMUNITY-005 — Community invariant specification

## What is this feature?

This package is the final structural handoff for the admissible Community invariants. It identifies and preserves five authoritative source objects but does not define executable invariant operands, thresholds, comparators, results, or evaluation semantics.

## What must be implemented?

Implement deterministic description and validation for `TLC-FC-02-COMMUNITY-005`. Preserve source objects `TLC-SO-COMMUNITY-009`, `TLC-SO-COMMUNITY-035`, `TLC-SO-COMMUNITY-037`, `TLC-SO-COMMUNITY-038`, and `TLC-SO-COMMUNITY-039` in source order, preserve all 29 unresolved identifiers exactly, transport opaque invariant handles unchanged, and reject scientific execution with `COMMUNITY_ERR_UNSUPPORTED_EXECUTION_REQUEST`.

## Inputs and output

The input is a Community specification request with the exact feature identity, a supported operation, optional opaque values, and optional provenance references. A successful describe or validate operation returns immutable structural metadata containing exact source identities, complete traceability, preserved unresolved items, unchanged opaque values, and deterministic normalized serialization.

## Mandatory, forbidden, and free behavior

`contract.json` and `acceptance.json` are normative. Invariant evaluation, threshold or comparator selection, operand or result-type inference, dimensional assumptions, invented numerical methods, default semantics, source mutation, and partial success after failure are forbidden. Programming language, API naming, storage, allocation, ownership, concurrency, and internal decomposition remain free when observable obligations are unchanged. The upstream total step list is not a required implementation sequence.

## Errors and conformance

Observable errors cover identity mismatch, missing source artifacts, incomplete traceability, unresolved-set preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution. Conformance requires all oracle-derived acceptance tests to pass and all forbidden behavior to remain absent.

## Unresolved scientific semantics

Yes. Scientific inputs, outputs, invariant evaluation semantics, and all 29 Community reservations remain preserved and unresolved.