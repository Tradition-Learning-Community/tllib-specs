# Transmission ergodicity hypothesis

## What is this feature?

This feature binds an opaque transmission-operator symbol and an opaque uniform-ergodicity spectral-gap condition into one source-traceable hypothesis record used by the community-stability theorem.

## What must be implemented?

Implement `construct_transmission_ergodicity_hypothesis`. Require both opaque components, require both to cite `maths/06-theorems.md:20`, preserve their identities and payloads unchanged, and return a descriptor explicitly labelled `hypothesis_not_verified`.

## Valid inputs and required output

Valid inputs contain a present operator and condition that refer to the same cited hypothesis. The required output is an immutable `TransmissionErgodicityHypothesis` preserving both components, source reference, and unverified status.

## Mandatory and forbidden behavior

Identical inputs produce the same semantic descriptor. The result must never be labelled verified or proved. Do not compute a spectral gap, test ergodicity, execute the operator, infer stability, or return a theorem truth value.

## Implementation freedom

Validation organization, storage, ownership, allocation, serialization, and concurrency are implementation-defined. Only validation before successful publication, exact preservation, provenance, and status are normative.

## Observable errors

- `MISSING_OPERATOR_SYMBOL`: the operator is absent.
- `MISSING_ERGODICITY_CONDITION`: the condition is absent.
- `SOURCE_REFERENCE_MISMATCH`: either component does not cite the required source or the two references differ.

No successful partial result may be observable on error.

## Conformance and unresolved semantics

Acceptance verifies component presence, common provenance, opacity, unverified status, errors, determinism, and negative scientific capability. The associated theorem proof remains partial and not formalized; this operation constructs a hypothesis and does not verify it.
