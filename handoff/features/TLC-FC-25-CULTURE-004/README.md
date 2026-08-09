# TLC-FC-25-CULTURE-004 — Context weight evolution delegation for cultural factors

## Purpose

Apply the Culture chapter's statement that cultural weights follow the general Context weight law without copying that law into an autonomous Culture implementation.

## Execution

`conditionally_executable`. The caller must supply a provider attesting conformance to `TLC-FC-24-CONTEXT-004` plus all inputs required by that Context feature. Culture forwards those opaque values and returns the delegated result with Context provenance.

## Forbidden behavior

No autonomous cultural ODE, solver, coefficient default, or reimplementation of the Context RHS is permitted.
