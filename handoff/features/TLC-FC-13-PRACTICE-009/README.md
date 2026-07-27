# TLC-FC-13-PRACTICE-009 — Operator candidate representation

## What is this feature?
A deterministic structural package for one performance-function candidate and three Practice operator candidates. Their source signatures remain independent, ordered, and unevaluated.

## What must be implemented?
Validate the exact feature identity, four keyed opaque inputs, ordered object population, and canonical provenance; preserve signatures, payloads, and reservations; construct the immutable representation; support deterministic serialization, deserialization, comparison, and trace inspection.

## Valid inputs and required output
Inputs `INPUT-PRACTICE-009-1` through `009-4` are required. The output preserves objects `024`, `074`, `075`, and `076` in documentary order and output identities `009-1` through `009-4`.

## Mandatory and forbidden behavior
Exact identity, order, opacity, traceability, deterministic canonical serialization, and atomic failure are mandatory. Operator invocation, composition, body inference, threshold selection, runtime type promotion, exact output calculation, progression, or effect is forbidden.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, transport, concurrency, and internal decomposition remain free when observable obligations are preserved.

## Errors and conformance
Invalid identity, missing or non-opaque inputs, provenance mismatch, structural failure, invocation, evaluation, and unsupported operations must produce stable errors without partial success. Every test in `acceptance.json` is mandatory.

## Unresolved science
Invocation and scientific execution require an external executor; evaluation requires an external evaluator. No operator output is calculated.