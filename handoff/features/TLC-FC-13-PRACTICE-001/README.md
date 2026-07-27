# TLC-FC-13-PRACTICE-001 — Constraint candidate representation

## What is this feature?
A deterministic structural representation of the cited Practice constraint candidate concerning environmental influences, resource availability, and social context. It does not evaluate a constraint predicate.

## What must be implemented?
Validate the exact feature identity, required opaque input, covered object reference, and provenance; construct an immutable declarative representation; preserve the opaque payload and reservations; support deterministic serialization, deserialization, structural comparison, and source-trace inspection.

## Valid inputs and required output
The required input is `INPUT-PRACTICE-001-1`, carried as an opaque candidate scientific value under candidate status. The output is a traceable `constraint_candidate` representation for `TLC-SO-PRACTICE-045`, with the unresolved output slot `OUTPUT-PRACTICE-001-1` preserved.

## Mandatory and forbidden behavior
Identity, provenance, documentary order, opacity, deterministic canonical serialization, and failure atomicity are mandatory. Inferring a predicate, type, unit, threshold, numerical method, temporal rule, practice effect, or scientific result is forbidden.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, concurrency policy, and internal decomposition remain implementation choices. Only the observable preservation and validation obligations are normative.

## Errors and conformance
Missing or malformed inputs, invalid identity, missing or mismatched provenance, structural failure, unsupported operations, and absent external scientific providers must be observable through the stable errors in `contract.json`. Every test in `acceptance.json` is mandatory.

## Unresolved science
Scientific execution requires an external executor and scientific evaluation requires an external evaluator. No exact scientific result is defined by this package.