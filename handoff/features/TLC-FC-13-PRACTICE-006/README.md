# TLC-FC-13-PRACTICE-006 — Blocked equation candidate representation

## What is this feature?
A deterministic structural package for two blocked Practice equation candidates concerning validity domains and collective coordination. Structural representation is ready; scientific evaluation remains deferred.

## What must be implemented?
Validate the exact feature identity, two keyed opaque inputs, ordered objects, canonical provenance, and exact six-reference decision set; preserve payloads and blockers; construct the immutable representation; support deterministic serialization, deserialization, comparison, and trace inspection.

## Valid inputs and required output
Inputs `INPUT-PRACTICE-006-1` and `006-2` are required. The output preserves objects `062` and `091`, output identities `006-1` and `006-2`, and decisions `SO-062`, `SO-091`, `SR-061`, `SR-090`, `HR-0048`, and `HR-0051` under their full TLC identifiers.

## Mandatory and forbidden behavior
Structural representation remains available while evaluation returns `scientific_decision_required`. Scientific execution returns `external_executor_required`. Threshold values, adequacy predicates, collective coordination algorithms, runtime types, sequences, durations, progressions, or effects must not be inferred.

## Implementation freedom
Language, storage, ownership, allocation, transport, API spelling, concurrency, and internal architecture remain free when observable obligations are preserved.

## Errors and conformance
Identity, input, provenance, decision-set, structural, provider, and unsupported-operation failures must be stable and atomic. Every test in `acceptance.json` is mandatory.

## Unresolved science
The exact six-reference decision set must remain unresolved and visible. No validity predicate or coordination procedure is authorized.