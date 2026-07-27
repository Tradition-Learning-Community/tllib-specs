# TLC-FC-02-COMMUNITY-009 — Community relation specification

## What is this feature?

This package is the final structural handoff for the Community relation feature. It preserves three authoritative source objects and their provenance but does not define an executable relation domain, codomain, input, output, dimension, or evaluator.

## What must be implemented?

Implement deterministic description and validation for `TLC-FC-02-COMMUNITY-009`. Preserve source objects `TLC-SO-COMMUNITY-004`, `TLC-SO-COMMUNITY-026`, and `TLC-SO-COMMUNITY-032` in source order, preserve all 29 unresolved identifiers exactly, transport opaque relation handles unchanged, and reject scientific execution with `COMMUNITY_ERR_UNSUPPORTED_EXECUTION_REQUEST`.

## Inputs and output

The input is a Community specification request carrying the exact feature identity, a supported operation, optional opaque values, and optional provenance references. A successful describe or validate operation returns immutable structural metadata with exact source identities, complete traceability, preserved unresolved items, unchanged opaque values, and deterministic normalized serialization.

## Mandatory, forbidden, and free behavior

`contract.json` and `acceptance.json` are normative. Domain or codomain inference, input or output inference, dimensional assumptions, invented scientific types or evaluation methods, relation execution, source mutation, default semantics, and partial success after failure are forbidden. Programming language, API naming, storage, allocation, ownership, concurrency, error transport, and internal sequencing remain free when observable obligations are unchanged.

## Errors and conformance

Observable errors cover identity mismatch, missing source artifacts, incomplete traceability, unresolved-set preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution. Conformance requires all oracle-derived acceptance tests to pass.

## Unresolved scientific semantics

Yes. Relation domain, codomain, inputs, outputs, evaluation semantics, and all 29 Community reservations remain preserved and unresolved.