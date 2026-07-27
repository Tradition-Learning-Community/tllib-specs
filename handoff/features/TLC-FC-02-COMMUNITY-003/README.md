# TLC-FC-02-COMMUNITY-003 — Community dynamics specification

## What is this feature?

This package defines the final structural handoff for the Community dynamics feature. It preserves the three authoritative source objects and their provenance but does not execute coupled evolution, stochastic terms, perturbations, or crises.

## What must be implemented?

Implement deterministic description and validation for feature `TLC-FC-02-COMMUNITY-003`. Preserve source objects `TLC-SO-COMMUNITY-029`, `TLC-SO-COMMUNITY-040`, and `TLC-SO-COMMUNITY-044` in source order, preserve all 29 unresolved identifiers exactly, transport opaque values unchanged, and reject scientific execution with `COMMUNITY_ERR_UNSUPPORTED_EXECUTION_REQUEST`.

## Inputs and output

The input is a Community specification request with an exact feature identity, a supported operation, optional opaque values, and optional provenance references. The successful output is immutable structural metadata containing the exact source and unresolved identities, complete traceability, and deterministic normalized serialization.

## Mandatory, forbidden, and free behavior

`contract.json` and `acceptance.json` are normative. No integrator, stochastic process, temporal discretization, noise model, perturbation model, scientific input type, scientific output type, equation execution, or default semantics may be invented. Internal architecture, language, storage, allocation, ownership, concurrency, and error transport remain free when they do not change observable behavior. The upstream total step list is not a required implementation sequence.

## Errors and conformance

Errors must expose the authoritative Community codes for identity mismatch, missing artifacts, incomplete traceability, unresolved preservation failure, opaque-value interpretation, unresolved scientific semantics, and unsupported execution. Conformance requires every oracle-derived acceptance test to pass with no partial result on failure.

## Unresolved scientific semantics

Yes. Scientific inputs, outputs, evolution semantics, perturbation semantics, stochastic behavior, and the 29 Community reservations remain preserved and unresolved.