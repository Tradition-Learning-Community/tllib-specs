# TLC-FC-02-COMMUNITY-006 — Community locally blocked invariant specification

## What is this feature?

This package is the final structural handoff for a Community invariant whose scientific definition is locally blocked. Structural representation, validation, traceability, unresolved propagation, and deterministic error behavior are implementable; invariant evaluation is not.

## What must be implemented?

Implement deterministic description and validation for `TLC-FC-02-COMMUNITY-006`. Preserve source object `TLC-SO-COMMUNITY-036`, all 29 unresolved identifiers, and blocker `COMMUNITY-DECISION-001`. Successful structural results must expose the blocker. A scientific execution request must return `COMMUNITY_ERR_UNRESOLVED_SCIENTIFIC_SEMANTICS`, identify the blocker, and return no partial result.

## Inputs and output

The input is a Community specification request with the exact feature identity, a supported operation, optional opaque invariant and result handles, and optional provenance references. A successful describe or validate operation returns immutable structural metadata with exact identities, complete traceability, unchanged opaque values, visible blocker state, and deterministic normalized serialization.

## Mandatory, forbidden, and free behavior

`contract.json` and `acceptance.json` are normative. Defining the missing invariant, inferring a result, supplying a default, hiding or resolving the blocker, evaluating the invariant, mutating source state, or replacing the authoritative blocking error are forbidden. Programming language, API naming, storage, ownership, allocation, concurrency, error transport, and internal sequencing remain free when observable obligations are unchanged.

## Errors and conformance

Observable errors cover identity mismatch, missing artifacts or blocker references, incomplete traceability, unresolved or blocker preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution modes. Conformance requires every blocker-aware acceptance test to pass.

## Unresolved scientific semantics

Yes. `COMMUNITY-DECISION-001` requires an external authoritative scientific definition before invariant evaluation can exist. The 29 Community reservations also remain preserved and unresolved.