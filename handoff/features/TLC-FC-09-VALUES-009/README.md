# TLC-FC-09-VALUES-009 — Partial-invariance predicate

## What is this feature?
A structural compiler for the sourced perturbation-guarded partial-invariance claim.

## What must be implemented?
Validate an opaque perturbation, a radius symbol, and a sourced relative-order claim; bind them into `PartialInvariancePredicate`; preserve every opaque value and source identity; and attach traceability.

## Valid inputs and required output
Inputs are `perturbation: OpaquePerturbation`, `radius: SymbolicBound`, and `order_claim: SymbolicOrderClaim`. The output is one immutable unevaluated predicate.

## Mandatory and forbidden behavior
Presence and source validation, exact claim preservation, deterministic construction, and atomic failure are mandatory. Norm evaluation, radius-domain inference, relative-order decision, or perturbation magnitude calculation are forbidden.

## Implementation freedom
Predicate representation, language, storage, ownership, allocation, serialization, and concurrency are free. Validation precedes construction; traceability precedes return.

## Errors and conformance
Source errors `missing_radius_symbol`, `missing_order_claim`, and `source_claim_mismatch` are preserved through public aliases. All acceptance tests are mandatory.

## Unresolved science
`norm_semantics`, `relative_order_semantics`, and `radius_domain` remain preserved unresolved. Scientific evaluation is external.
