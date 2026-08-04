# Principles role descriptor

## What is this feature?

This feature constructs the isolated Principles dimension-role descriptor from the source statement while preserving its classification and rational-coherence semantics as opaque.

## What must be implemented?

Implement `construct_principles_role_descriptor`. Require the exact label `Principles`, exact source ordinal `2`, exact source `maths/06-theorems/theorems.md:82`, and unresolved identifier `TLC-UT-THEOREMS-006`. Preserve the supplied opaque role payload and rational-coherence label unchanged.

## Valid inputs and required output

A valid input is an opaque Principles role carrying the required source and unresolved identifier plus source ordinal 2. The output is an immutable `PrinciplesRoleDescriptor` containing the exact label, ordinal, payload, source, and unresolved identifier.

## Mandatory and forbidden behavior

Reject semantically similar but non-exact labels rather than normalizing them. Preserve `PROOF-THEOREMS-003` as partial, not formalized metadata. Do not define or evaluate rational coherence, resolve the Principles classification, infer sufficiency, or prove the CNS theorem.

## Implementation freedom

Validation architecture, storage, ownership, allocation, serialization, and concurrency are implementation-defined. Exact label, ordinal, source, unresolved attachment, opacity, errors, and deterministic output are normative.

## Observable errors

- `WRONG_DIMENSION_LABEL`: the role label is not exactly `Principles`.
- `WRONG_SOURCE_ORDINAL`: the ordinal is not 2 or the role does not cite the required source position.
- `MISSING_PRINCIPLES_UNRESOLVED`: `TLC-UT-THEOREMS-006` is absent.

No successful partial descriptor may be observable on error.

## Conformance and unresolved scientific semantics

Acceptance verifies exact constants, opaque preservation, stable errors, determinism, and absence of scientific definition or sufficiency assertion. `TLC-UT-THEOREMS-006` remains `preserved_unresolved`; structural implementation is ready.
