# TLC-FC-02-COMMUNITY-008 — Community operator specification

## What is this feature?

This package is the final structural handoff for the Community operator feature. It preserves three Community source objects and two upstream symbol references. The Master and Disciple references are documentary only; they do not authorize upstream execution.

## What must be implemented?

Implement deterministic description and validation for `TLC-FC-02-COMMUNITY-008`. Preserve source objects `TLC-SO-COMMUNITY-018`, `TLC-SO-COMMUNITY-019`, and `TLC-SO-COMMUNITY-020` in source order. Preserve `TLC-COMMUNITY-MASTER-001` and `TLC-COMMUNITY-DISCIPLE-001` as `symbol_only_documentary` with `executable: false`. Preserve all 29 unresolved identifiers, transport opaque operator handles unchanged, and reject scientific execution with `COMMUNITY_ERR_UNSUPPORTED_EXECUTION_REQUEST`.

## Inputs and output

The input is a Community specification request containing the exact feature identity, a supported operation, optional opaque values, and optional provenance or dependency records. A successful describe or validate operation returns immutable structural metadata with exact source identities, exact non-executable dependency classifications, complete traceability, preserved unresolved items, unchanged opaque values, and deterministic normalized serialization.

## Mandatory, forbidden, and free behavior

`contract.json` and `acceptance.json` are normative. Promoting either upstream reference to execution, importing Master or Disciple behavior, inferring operator inputs or outputs, inventing scientific types or dimensions, evaluating the operator, mutating upstream artifacts, and returning partial success after failure are forbidden. Programming language, API naming, storage, ownership, allocation, concurrency, error transport, and internal sequencing remain free when observable obligations are unchanged.

## Errors and conformance

Dependency promotion or reclassification must produce `COMMUNITY_ERR_DEPENDENCY_CLASSIFICATION`. Other observable errors cover identity mismatch, missing artifacts, incomplete traceability, unresolved preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution. Conformance requires all eleven oracle-derived acceptance tests to pass.

## Unresolved scientific semantics

Yes. Operator inputs, outputs, and execution semantics, together with all 29 Community reservations, remain preserved and unresolved. The two upstream references are not scientific execution providers in this package.