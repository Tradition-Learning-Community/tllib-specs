# TLC-FC-13-PRACTICE-007 — Metric candidate representation

## What is this feature?
A deterministic structural representation of two Practice metric candidates. It preserves the source references and opaque values without defining or computing a metric.

## What must be implemented?
Validate the exact feature identity, two keyed opaque inputs, ordered object population, and canonical provenance; construct an immutable representation; preserve opaque results supplied by an external evaluator; support deterministic serialization, deserialization, structural comparison, and trace inspection.

## Valid inputs and required output
Inputs `INPUT-PRACTICE-007-1` and `007-2` are required. The output preserves objects `TLC-SO-PRACTICE-021` and `TLC-SO-PRACTICE-034` in documentary order and the unresolved output identities `OUTPUT-PRACTICE-007-1` and `007-2`.

## Mandatory and forbidden behavior
Exact identity, order, opacity, provenance, deterministic canonical serialization, and atomic failure are mandatory. Defining a metric formula, scale, unit, threshold, observation window, cognitive-load computation, numerical result, progression, or effect is forbidden.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, transport, concurrency, and internal decomposition remain free when observable obligations are preserved.

## Errors and conformance
Invalid identity, missing or non-opaque inputs, missing or mismatched provenance, structural errors, unsupported operations, and absent external providers must be observable without partial success. Every test in `acceptance.json` is mandatory.

## Unresolved science
Metric evaluation requires an external evaluator and execution requires an external executor. The package asserts no exact metric value.