# TLC-FC-13-PRACTICE-004 — Blocked dynamics candidate representation

## What is this feature?
A deterministic structural representation of four blocked Practice dynamics candidates. Structural use remains available, while scientific evaluation is deferred until the exact authoritative decision set is resolved.

## What must be implemented?
Validate the feature identity, four keyed opaque inputs, ordered object population, provenance, and exact decision references; preserve every payload and blocker; construct the immutable representation; support deterministic serialization, deserialization, structural comparison, and trace inspection.

## Valid inputs and required output
Inputs `INPUT-PRACTICE-004-1` through `004-4` are independently required. The output preserves objects `068`, `085`, `086`, and `088` in documentary order, unresolved output references `004-1` through `004-4`, and the twelve authoritative decision references.

## Mandatory and forbidden behavior
Blocked evaluation must not reject structural representation. Scientific evaluation returns `scientific_decision_required` with exactly the declared references; scientific execution returns `external_executor_required`. Equation evaluation, solver choice, inferred runtime types, sequences, durations, progressions, and effects are forbidden.

## Implementation freedom
Language, storage, ownership, allocation, transport, API spelling, concurrency, and internal decomposition are free when observable behavior is preserved.

## Errors and conformance
Missing inputs, invalid carriers, identity or provenance mismatches, altered decision sets, structural failures, unsupported operations, and provider absence must be stable and atomic. Every test in `acceptance.json` is mandatory.

## Unresolved science
The exact decision set is preserved as opaque authority. No scientific evaluation may proceed until a future scientific source resolves it.