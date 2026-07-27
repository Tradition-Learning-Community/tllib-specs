# TLC-FC-03-HUIT-DIMENSIONS-DE-TL-002 — Message convergence constraint

## What is this feature?

A pure structural operation that records the source Principle–Message convergence declaration without performing convergence.

## What must be implemented?

Accept one `convergence_declaration`, the exact phase labels `germination`, `crystallisation`, and `stabilisation`, plus opaque Gamma and limit tokens. Preserve the equation identity, source trace, nine unresolved identifiers, and provisional assumption.

## Inputs, output, and mandatory behavior

The declaration must identify `TLC-SO-HUIT-DIMENSIONS-DE-TL-011`. The output is an immutable `MessageConvergenceConstraint` containing the declaration, the three named phase labels, opaque operator tokens, complete provenance, and unresolved convergence and feature-boundary status. Identical inputs must produce structurally identical outputs.

## Forbidden behavior

Do not iterate, evaluate a limit, decide convergence, infer temporal order, resolve feature identity, mutate inputs, drop phase labels, or add numeric semantics.

## Implementation freedom

Language, API spelling, storage, ownership, allocation, serialization, concurrency, and internal decomposition are free. Validation and preservation must precede successful publication, but no total algorithm is prescribed.

## Errors, conformance, and unresolved science

Use the schema-compatible aliases in `contract.json`, preserving the exact source identifiers in their conditions and acceptance tests. No partial result is observable on failure. Conformance requires all `acceptance.json` tests. Scientific types, signatures, units, ordering, aggregation, numerics, oracle semantics, boundary, and identity remain unresolved.
