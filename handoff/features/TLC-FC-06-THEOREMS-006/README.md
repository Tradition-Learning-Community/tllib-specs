# Theorem declaration index

## What is this feature?

This feature indexes six prepared theorem declarations by exact scientific object identifier and supports exact lookup without proving, disproving, or completing any declaration.

## What must be implemented?

Implement index construction for exactly `TLC-SO-THEOREMS-002`, `003`, `004`, `008`, `009`, and `010`, plus lookup by exact identifier. Every declaration must have its registered source and a proof status. Preserve declaration payload, hypotheses, conclusion, source metadata, quantifier status, and proof status unchanged.

## Valid inputs and required outputs

A valid construction input contains each covered declaration exactly once and a proof-status mapping for every covered identifier. The index has six entries. Exact lookup returns unchanged declaration metadata. A declaration with an absent proof remains indexable and queryable.

The proof-status map is mandatory: objects 002, 003, 004, 008, and 010 are `partial`; object 009 is `absent`; no status is complete. `RESULT-THEOREMS-002` and `RESULT-THEOREMS-003` retain one explicit quantifier each; other indexed result quantifiers remain unspecified.

## Mandatory and forbidden behavior

Do not promote proof status, validate proof correctness, synthesize missing hypotheses or conclusions, fall back to a similar theorem, or return true, false, proved, or disproved. Identical construction and lookup inputs produce identical semantic results.

## Implementation freedom

Index storage, key order, ownership, allocation, serialization, and concurrency are implementation-defined. Exact population, exact lookup, metadata preservation, and errors are normative.

## Observable errors

- `DUPLICATE_THEOREM_ID`: a covered identifier occurs more than once.
- `MISSING_PROOF_STATUS`: a covered declaration has no proof status.
- `UNKNOWN_THEOREM_ID`: construction or lookup uses an uncovered identifier, or a declaration source does not match its registered theorem source.

No successful partial index may be observable on construction error.

## Conformance and unresolved semantics

Acceptance verifies exact population, exact proof map, quantifier preservation, lookup, opacity, stable errors, determinism, and absence of truth values. Five proofs are partial and one is absent; this does not block structural indexing.
