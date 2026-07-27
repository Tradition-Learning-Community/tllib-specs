# TLC-FC-13-PRACTICE-010 — Blocked operator candidate representation

## What is this feature?
A deterministic structural representation of the aggregate Practice operator source object `TLC-SO-PRACTICE-018`. The aggregate identity is preserved and must not be silently split into executable operators.

## What must be implemented?
Validate the exact feature identity, required opaque input, aggregate object, canonical provenance, and exact three-reference scientific decision set; preserve the aggregate payload and decisions; construct the immutable representation; support deterministic serialization, deserialization, comparison, and trace inspection.

## Valid inputs and required output
`INPUT-PRACTICE-010-1` is required. The output preserves `TLC-SO-PRACTICE-018`, `OUTPUT-PRACTICE-010-1`, and decisions `TLC-SO-PRACTICE-018`, `TLC-SR-PRACTICE-017`, and `TLC-HR-0108`.

## Mandatory and forbidden behavior
Structural representation remains available. Invocation or scientific execution returns `external_executor_required`; evaluation returns `scientific_decision_required` with exactly the three decisions. Splitting the aggregate, inferring runtime types, implementing or composing internal operators, or calculating outputs is forbidden.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, transport, concurrency, and internal decomposition remain free, except that the public aggregate identity must remain singular.

## Errors and conformance
Invalid identity, missing or non-opaque input, provenance mismatch, altered decisions, structural failure, invocation, evaluation, and unsupported operations must produce stable atomic errors. Every test in `acceptance.json` is mandatory.

## Unresolved science
The aggregate scientific behavior remains deferred. The package authorizes no internal operator selection or invocation.