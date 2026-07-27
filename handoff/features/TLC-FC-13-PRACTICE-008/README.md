# TLC-FC-13-PRACTICE-008 — Blocked metric candidate representation

## What is this feature?
A deterministic structural representation of the blocked quantitative-measures candidate `TLC-SO-PRACTICE-022`. The package preserves the source statement without computing frequency, accuracy, or efficiency.

## What must be implemented?
Validate the exact feature identity, required opaque input, source object, provenance, and exact three-reference scientific decision set; construct an immutable representation; preserve the payload and decisions; support deterministic serialization, deserialization, comparison, and trace inspection.

## Valid inputs and required output
`INPUT-PRACTICE-008-1` is required. The output preserves `TLC-SO-PRACTICE-022`, `OUTPUT-PRACTICE-008-1`, and decisions `TLC-SO-PRACTICE-022`, `TLC-SR-PRACTICE-021`, and `TLC-HR-0101`.

## Mandatory and forbidden behavior
Structural representation remains available. Scientific evaluation returns `scientific_decision_required` with exactly the three decisions; execution returns `external_executor_required`. A session unit, observation window, duration, denominator meaning, resource arithmetic, numeric validation, threshold, progression, or effect must not be inferred.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, transport, concurrency, and internal decomposition remain free when observable obligations are preserved.

## Errors and conformance
Invalid identity, absent or non-opaque input, missing or mismatched provenance, altered decisions, structural errors, and unsupported operations must be stable and atomic. Every test in `acceptance.json` is mandatory.

## Unresolved science
The exact decision set remains unresolved. No quantitative metric value is authorized until future scientific review.