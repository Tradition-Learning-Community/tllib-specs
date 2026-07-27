# TLC-FC-02-COMMUNITY-004 — Community equation specification

## What is this feature?

This package is the final structural handoff for the Community equation feature. It preserves three authoritative source objects and all provenance needed to identify the source equations, but it does not define or execute their scientific operands, outputs, dimensions, units, or numerical semantics.

## What must be implemented?

Implement deterministic description and validation for `TLC-FC-02-COMMUNITY-004`. Preserve source objects `TLC-SO-COMMUNITY-027`, `TLC-SO-COMMUNITY-028`, and `TLC-SO-COMMUNITY-030` in source order, preserve all 29 unresolved identifiers exactly, transport opaque equation handles unchanged, and reject scientific execution with `COMMUNITY_ERR_UNSUPPORTED_EXECUTION_REQUEST`.

## Inputs and output

The input is a Community specification request carrying the exact feature identity, a supported operation, optional opaque values, and optional provenance references. A successful describe or validate operation returns immutable structural metadata with exact source identities, complete traceability, preserved unresolved items, unchanged opaque values, and deterministic normalized serialization.

## Mandatory, forbidden, and free behavior

`contract.json` and `acceptance.json` are normative. Operand inference, output-type inference, equation evaluation, dimensional assumptions, invented units, numerical methods, default scientific semantics, source mutation, and partial success after failure are forbidden. Programming language, API naming, storage, allocation, ownership, concurrency, and internal validation decomposition remain free when they do not alter observable behavior. The upstream total step list is not a mandatory implementation sequence.

## Errors and conformance

Observable errors cover identity mismatch, missing source artifacts, incomplete traceability, unresolved-set preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution. Conformance requires every oracle-derived acceptance test to pass and no forbidden scientific behavior to occur.

## Unresolved scientific semantics

Yes. Scientific inputs, outputs, equation execution semantics, dimensions, and all 29 Community reservations remain preserved and unresolved.