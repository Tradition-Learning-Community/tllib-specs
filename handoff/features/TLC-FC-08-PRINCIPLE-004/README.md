# TLC-FC-08-PRINCIPLE-004 — Symbolic principle formal tuple

## What is this feature?
It constructs the formal Principle tuple `P = (D_P, F_P, succeeds_under_P)` as one immutable ordered symbolic AST.

## What must be implemented?
Implement `CONSTRUCT-PRINCIPLE-FORMAL-TUPLE`. Validate object `TLC-SO-PRINCIPLE-033`, require exactly three non-empty components, preserve order `D_P`, `F_P`, relation, attach provenance, and freeze the result.

## Valid inputs and required output
Input supplies the exact source object, three opaque components in source order, an empty unresolved set, and provenance. Output is an immutable arity-three `symbolic_principle_tuple` with `evaluated = false`.

## Mandatory and forbidden behavior
Arity, component identity, component order, opacity, provenance, and deterministic structure are mandatory. Component interpretation, domain inference, equality semantics, relation execution, and scientific promotion are forbidden.

## Implementer freedom
Tuple storage, AST representation, ownership, allocation, serialization, language, and concurrency policy are implementation-defined.

## Errors and conformance
Use the four `PRINCIPLE_*` errors in `contract.json`. `acceptance.json` verifies arity, exact order, opaque round-trip, stable errors, non-interpretation, and determinism.

## Unresolved scientific semantics
Component types, tuple meaning beyond order, domains, equality semantics, and relation behavior remain opaque.
