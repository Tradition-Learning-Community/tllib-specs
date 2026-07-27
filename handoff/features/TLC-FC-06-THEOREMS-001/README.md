# Experiential conservation claim

Feature ID: `TLC-FC-06-THEOREMS-001`

## What is this feature?

This feature constructs an unevaluated, source-traceable descriptor for the experiential-information conservation claim. It records an external axiom reference, an opaque experience symbol, and exactly three clause identifiers: bounded energy, controlled variation, and stationary law.

## What must be implemented?

Implement `assemble_experiential_conservation_claim` as a structural validation and construction operation. It must preserve the axiom identity, preserve the experience symbol byte-for-byte, retain exactly the three required clause identifiers, and return no successful partial result after a validation failure.

## Valid inputs

A present opaque axiom reference, a present opaque experience symbol, and a clause collection containing exactly the required three source clauses are valid. Additional or missing clauses are invalid.

## Required output

Return an immutable `UnevaluatedConservationClaim` descriptor containing only the supplied axiom reference, experience symbol, and required clause identifiers, together with traceable status metadata. The result must not contain an evaluated scientific value or theorem truth value.

## Mandatory behavior

Identical structural inputs produce semantically identical outputs. Every accepted identity remains distinct and unchanged. The associated proof remains partial and not formalized; `PROOF-THEOREMS-006` is metadata, not a runtime proof result.

## Forbidden behavior

Do not evaluate energy boundedness, variation control, stationary convergence, an invariant measure, or theorem truth. Do not add units, dimensions, probability laws, tolerances, numeric methods, storage rules, or language-specific types.

## Implementation freedom

Internal data structures, allocation, ownership, serialization, concurrency, and validation architecture are implementation-defined, provided all observable obligations and errors remain conforming.

## Observable errors

- `MISSING_AXIOM_REFERENCE`: the axiom reference is absent.
- `INCOMPLETE_CONSERVATION_CLAUSES`: the clause collection is missing a required clause, contains an extra clause, or otherwise differs from the exact required population.

No successful partial descriptor may be observable on error.

## Conformance

Conformance is verified by `acceptance.json`: exact-component construction, opaque preservation, stable errors, deterministic output, source traceability, and rejection of scientific evaluation must all pass.

## Unresolved scientific semantics

The package does not prove the conservation statement. Scientific proof completion remains external; structural implementation is ready.
