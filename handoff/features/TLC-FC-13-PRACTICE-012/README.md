# TLC-FC-13-PRACTICE-012 — Provisionally separated relation candidate representation

## What is this feature?
A deterministic structural representation of the Practice measurability relation candidate `TLC-SO-PRACTICE-061`. Its separate feature boundary is provisional and must remain explicit.

## What must be implemented?
Validate the exact feature identity, required opaque input, relation object, canonical provenance, absence of inferred endpoints, and exact decision `TLC-HR-0100`; construct the immutable representation; preserve the provisional boundary; support deterministic serialization, deserialization, comparison, and trace inspection.

## Valid inputs and required output
`INPUT-PRACTICE-012-1` is required. The output preserves `TLC-SO-PRACTICE-061`, `OUTPUT-PRACTICE-012-1`, the provisional separation status, and exactly `TLC-HR-0100`.

## Mandatory and forbidden behavior
Structural representation remains available. Scientific evaluation returns `scientific_decision_required` with `TLC-HR-0100`. Supplying or inferring relation endpoints, indicator types, metric formulas, scales, thresholds, evaluation procedures, or scientific results is forbidden and endpoint inference is out of scope.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, transport, concurrency, and internal decomposition remain free when the provisional public boundary and observable obligations are preserved.

## Errors and conformance
Invalid identity, missing or non-opaque input, provenance mismatch, missing or replaced decision, inferred endpoints, structural failure, and unsupported operations must produce stable atomic errors. Every test in `acceptance.json` is mandatory.

## Unresolved science
Endpoint identity and indicator semantics remain unresolved. The feature must not be merged with another relation or promoted to executable evaluation without future scientific authority.