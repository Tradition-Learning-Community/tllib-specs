# CNS operator claim registry

## What is this feature?

This feature registers two distinct families of CNS source claims: one transformation-signature claim and per-dimension removal-effect claims.

## What must be implemented?

Implement `register_cns_operator_claims`. Require the transformation claim to cite `maths/06-theorems/theorems.md:54-55`, require every removal-effect claim to cite `maths/06-theorems/theorems.md:66-67`, preserve all opaque payloads, prevent a claim from occupying both families, and return an immutable two-family claim set with scientific status `blocked_local`.

## Valid inputs and required output

A valid input contains one transformation claim and a dimension-keyed mapping of sourced removal claims. The output keeps the transformation family and removal family separately addressable, even when payload bytes are identical.

## Mandatory and forbidden behavior

Preserve source identities, family identity, payloads, blocked-local status, and the partial/not-formalized proof reference `PROOF-THEOREMS-003`. Do not execute a removal effect or assert completeness, necessity, sufficiency, equivalence, or theorem truth.

## Implementation freedom

Internal mapping type, ordering, storage, ownership, allocation, serialization, and concurrency are implementation-defined. Claim-family separation and provenance are normative.

## Observable errors

- `MISSING_TRANSFORMATION_CLAIM`: the transformation claim is absent or lacks its required source.
- `MISSING_REMOVAL_CLAIM_SOURCE`: a removal claim lacks the required source reference.
- `CLAIM_FAMILY_COLLISION`: a claim is assigned to both families or stored in the wrong family.

No successful partial claim set may be observable on error.

## Conformance and unresolved semantics

Acceptance verifies source ranges, family separation, opacity, blocked-local status, errors, determinism, and absence of CNS assertions. Structural registration is ready, but the scientific CNS proof remains partial and is not verified here.
