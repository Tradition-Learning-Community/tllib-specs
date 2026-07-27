# TLC-FC-10-VIRTUES-006 — Virtue equation-form registration

## What is this feature?

A declarative structural registrar for supplied equation forms, free symbols, opaque operators, and duplicate-candidate links.

## What must be implemented?

Implement `REGISTER-VIRTUE-EQUATION-FORMS`: validate the exact feature identity and all five required source references, preserve notation and collection order, retain candidate links without merging their endpoints, and emit a deterministic descriptor.

## Valid inputs and required output

The input artifact contains source-supplied forms, symbols, operators, candidate links, and opaque context. Success returns these structures unchanged; failure returns a named error and no accepted descriptor.

## Mandatory and forbidden behavior

Object identity, notation, operator opacity, source order, and candidate-link cardinality are mandatory. Equation solving, formula completion, symbol normalization, ranking, scientific-equivalence assertions, and candidate merging are forbidden.

## Implementation freedom

Internal data structures and traversal order are free, except that validation and complete preservation must occur before the result is exposed. No language, solver, serialization, layout, or allocation model is prescribed.

## Errors and conformance

The source errors are preserved through public schema-compatible aliases. Conformance requires all acceptance tests, including the rule that duplicate-candidate never means identity or equivalence.

## Unresolved science

Operator meaning, basis semantics, equation-solving semantics, and scientific equivalence remain outside this registration package.