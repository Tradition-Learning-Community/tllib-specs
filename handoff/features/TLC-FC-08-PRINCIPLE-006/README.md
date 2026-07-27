# TLC-FC-08-PRINCIPLE-006 — Unverifiable principle invariant requirements

## What is this feature?
It records two source-stated invariant requirements: Principle stability/structuring and adaptive fidelity to essential tradition invariants.

## What must be implemented?
Implement `DESCRIBE-PRINCIPLE-INVARIANT-REQUIREMENTS`. Validate exact objects `TLC-SO-PRINCIPLE-002` and `TLC-SO-PRINCIPLE-081`, preserve both requirement statements and provenance, and return an immutable descriptor marked `verifiable = false` and `external_evaluator_required = true`.

## Valid inputs and required output
Input supplies the exact two object references, opaque source-bound evidence, an empty unresolved collection, and provenance. Output contains exactly two requirements, no pass/fail field, and `evaluated = false`.

## Mandatory and forbidden behavior
Exact identity, two-statement population, source order, explicit non-verifiability, opacity, and provenance are mandatory. Any checker, boolean result, inferred predicate, or invented observable state is forbidden.

## Implementer freedom
Descriptor storage, ownership, allocation, serialization, language, and concurrency policy are implementation-defined.

## Errors and conformance
Use the four `PRINCIPLE_*` errors in `contract.json`. `acceptance.json` verifies two statements, `verifiable=false`, absence of a boolean, stable errors, and determinism.

## Unresolved scientific semantics
Essential invariants, observable state, preservation relation, contextual adaptation, and pass/fail predicate are not defined. Scientific verification requires an external provider.
