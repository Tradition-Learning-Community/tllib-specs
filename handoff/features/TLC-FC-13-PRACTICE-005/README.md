# TLC-FC-13-PRACTICE-005 — Equation candidate representation

## What is this feature?
A deterministic structural package for four independent Practice equation candidates. It preserves the cited transformations as unevaluated source statements.

## What must be implemented?
Validate the exact feature identity, four keyed opaque inputs, ordered object population, and canonical provenance; construct an immutable representation; preserve all payloads and reservations; support deterministic serialization, deserialization, structural comparison, and trace inspection.

## Valid inputs and required output
Inputs `INPUT-PRACTICE-005-1` through `005-4` are independently required. The output preserves objects `069`, `087`, `089`, and `090` in documentary order and the unresolved output identities `005-1` through `005-4`.

## Mandatory and forbidden behavior
Exact identity, cardinality, ordering, opacity, traceability, deterministic canonical serialization, and atomic failure are mandatory. Equation evaluation, method selection, habit-loop inference, repetition rules, stop rules, guaranteed effects, thresholds, units, types, durations, and progressions are forbidden.

## Implementation freedom
Language, storage, ownership, allocation, transport, API spelling, concurrency, and internal decomposition remain free when the observable contract is preserved.

## Errors and conformance
Invalid identity, missing or non-opaque inputs, missing or mismatched provenance, structural errors, unsupported operations, and absent external providers must be observable without partial success. Every test in `acceptance.json` is mandatory.

## Unresolved science
Execution and evaluation require external providers. No exact transformed value, habit semantics, or guaranteed effect is authorized.