# TLC-FC-11-CAPACITIES-007 — Hamiltonian capacity dynamics AST

## What is this feature?

A structural constructor for the single cited Hamiltonian-style capacity expression `TLC-SO-CAPACITIES-098`.

## What must be implemented?

Accept that exact object with an explicit symbol-table entry, complete provenance, and blocker `scientific decision required`. Return an immutable `CapacityHamiltonianAst` whose root may expose opaque kinetic, potential, Phi-coupling, and Psi-coupling child labels only when they are present in the cited source payload.

## Valid inputs and required output

The object sequence has exactly one member. The result preserves its identity, symbols, provenance, blocker, and non-evaluation guard.

## Mandatory and forbidden behavior

Exact identity, explicit symbols, provenance, conditional label preservation, determinism, blocker retention, and atomic failure are mandatory. Hamiltonian evaluation, energy computation, dynamics simulation, inferred child terms, optimization, numerical interpretation, and partial success are forbidden.

## Implementation freedom

Language, data structure, storage, ownership, allocation, serialization, and concurrency are implementation-defined. No unique internal algorithm is prescribed.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `UnexpectedCoveredObject`, `ObjectOrderMismatch`, `MissingSymbolTableEntry`, `MissingSourceReference`, `MissingDecisionBlocker`, and `ScientificEvaluationRequested`. All acceptance tests must pass.

## Unresolved science

Hamiltonian meaning and executable dynamics remain preserved unresolved.
