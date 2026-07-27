# Theorem dynamics equation registry

## What is this feature?

This feature registers three source-defined theorem dynamics equations as distinct, unevaluated records keyed by scientific object identifier.

## What must be implemented?

Implement `register_theorem_dynamics_equations`. Validate the exact covered object population `TLC-SO-THEOREMS-027`, `TLC-SO-THEOREMS-028`, and `TLC-SO-THEOREMS-030`; require one opaque equation and one prepared role for each; preserve every equation-role pair unchanged; and return a three-entry registry.

## Valid inputs and required output

Valid inputs are two complete mappings over the exact covered object set. Roles must be the prepared trajectory, identity-wave, or receptivity roles. The output is an immutable registry addressable by exact object identifier. Mapping iteration order is not a scientific ordering requirement.

## Mandatory and forbidden behavior

Objects, equations, and roles remain distinct even when opaque payload bytes are identical. Identical inputs produce the same semantic registry. Do not evaluate derivatives, trajectories, waves, receptivity, convergence, or theorem truth. The external Dynamics dependency is retained only as a reference.

## Implementation freedom

Container type, key ordering, ownership, allocation, serialization, and concurrency are not prescribed. An uncovered identifier must never be silently included; upstream artifacts do not assign a distinct stable error code for that otherwise complete population mismatch.

## Observable errors

- `DUPLICATE_SCIENTIFIC_OBJECT`: a covered identifier occurs more than once.
- `MISSING_DYNAMICS_EQUATION`: a covered object has no equation.
- `UNKNOWN_DYNAMICS_ROLE`: a covered object lacks a prepared role or supplies an unsupported role.

No partial successful registry may be observable on error.

## Conformance and scientific status

`acceptance.json` verifies exact population, pairing, opacity, errors, deterministic output, and absence of scientific evaluation. This is a structural registry, not a dynamics solver or proof operation.
