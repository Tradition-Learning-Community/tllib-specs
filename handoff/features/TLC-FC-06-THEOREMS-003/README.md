# Explicit theorem equation catalogue

## What is this feature?

This feature builds a source-addressable catalogue of four explicit theorem equations while treating every mathematical expression as opaque.

## What must be implemented?

Implement `catalogue_explicit_theorem_equations`. Accept exactly one complete entry for each of `TLC-SO-THEOREMS-016`, `TLC-SO-THEOREMS-017`, `TLC-SO-THEOREMS-026`, and `TLC-SO-THEOREMS-029`. Each entry needs a source reference, an opaque expression, and one unique role: stability bound, emergence probability, trajectory convergence, or wave speed.

## Valid inputs and output

A valid input has exactly four covered entries and four distinct roles. The output is an immutable catalogue addressable by object identifier and role. Input sequence order does not create a scientific ordering obligation; expressions and source references must remain unchanged.

## Mandatory and forbidden behavior

Preserve all object identities, roles, sources, and expression bytes. Mathematically equivalent-looking expressions must not be parsed, normalized, simplified, merged, solved, or compared. The operation returns no theorem truth value.

## Implementation freedom

Internal catalogue ordering, container type, allocation, ownership, serialization, and concurrency are implementation-defined. Deterministic semantic lookup and exact population are mandatory.

## Observable errors

- `MISSING_EQUATION_ROLE`: an entry lacks a declared role.
- `DUPLICATE_EQUATION_ROLE`: a role occurs more than once.
- `MISSING_SOURCE_REFERENCE`: an entry lacks its source reference.

No successful partial catalogue may be observable on error.

## Conformance and scientific status

Acceptance verifies exact population, four distinct roles, opaque expression preservation, stable errors, determinism, source traceability, and absence of algebraic or scientific evaluation. This package catalogues equations; it does not validate them mathematically.
