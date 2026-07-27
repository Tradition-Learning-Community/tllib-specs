# TLC-FC-08-PRINCIPLE-002 — Symbolic principle evolution equation

## What is this feature?
It constructs the unevaluated symbolic equation `dP/dt = E(P,D,t)` as one immutable equality AST.

## What must be implemented?
Implement `CONSTRUCT-PRINCIPLE-EVOLUTION-EQUATION`. Validate the exact feature and object IDs, build the derivative on the left, apply the evolution operator to `P`, `D`, and `t` in that order on the right, attach provenance and unresolved identifiers, and freeze the result.

## Valid inputs and required output
Valid input provides opaque equation symbols, exact object `TLC-SO-PRINCIPLE-087`, the three authoritative unresolved IDs, and source provenance. Output is one immutable `symbolic_principle_evolution_equation` with `evaluated = false`.

## Mandatory and forbidden behavior
Equation shape, argument order, object identity, unresolved propagation, opacity, and determinism are mandatory. Solving, simulation, discretization, domain inference, initial-condition invention, or solver selection is forbidden.

## Implementer freedom
AST storage, ownership, allocation, serialization, language, and threading are not prescribed.

## Errors and conformance
Expose the four `PRINCIPLE_*` errors defined in `contract.json`. `acceptance.json` verifies exact shape, P-D-t order, unresolved round-trip, non-solving behavior, stable errors, and determinism.

## Unresolved scientific semantics
Symbol semantics, domain, initial conditions, derivative existence, codomain, solver, discretization, and operator implementation remain unresolved. An external scientific provider is required for any execution beyond structural construction.
