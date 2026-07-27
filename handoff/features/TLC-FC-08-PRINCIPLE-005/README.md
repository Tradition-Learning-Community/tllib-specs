# TLC-FC-08-PRINCIPLE-005 — Principle invariant specification

## What is this feature?
It constructs an invariant specification with six source-backed records: four learning characteristics, invariant formal essence `F_P`, and a documentary reference to the Principle evolution equation.

## What must be implemented?
Implement `CONSTRUCT-PRINCIPLE-INVARIANT-SPECIFICATION`. Validate exact source objects `026, 028, 035`, construct six records, preserve source order and provenance, and retain `TLC-FC-08-PRINCIPLE-002` only as a non-executable documentary reference.

## Valid inputs and required output
Input supplies exact source references, opaque evidence symbols, the documentary feature reference, an empty unresolved set, and provenance. Output is an immutable six-node `principle_invariant_specification` with no truth value and `evaluated = false`.

## Mandatory and forbidden behavior
Six-node population, source bindings, documentary-only dependency, opacity, provenance, and determinism are mandatory. Measurement, pass/fail checking, invariant evaluation, and execution of the equation reference are forbidden.

## Implementer freedom
Descriptor storage, AST representation, ownership, allocation, serialization, language, and threading are implementation-defined.

## Errors and conformance
Use the four `PRINCIPLE_*` errors in `contract.json`. `acceptance.json` verifies six-node shape, no boolean result, documentary-only dependency, stable errors, and determinism.

## Unresolved scientific semantics
Measurement methods, essential invariant content, verification predicates, and the preservation relation remain unspecified and external.
