# TLC-FC-09-VALUES-008 — Fundamental-principle invariant descriptor

## What is this feature?
A structural compiler for the sourced preservation-invariant claim relating opaque before and after principle references.

## What must be implemented?
Validate both principle references and the matching source claim, construct `FundamentalPrincipleInvariant`, preserve the symbolic comparison descriptor and provenance, and attach unresolved semantics without evaluating equality.

## Valid inputs and required output
Inputs are `before: OpaquePrincipleRef`, `after: OpaquePrincipleRef`, and `source_claim: SymbolicInvariant`. The output is one immutable invariant descriptor.

## Mandatory and forbidden behavior
Source-claim binding, exact reference preservation, deterministic structure, declared symbolic comparison, and atomic failure are mandatory. Defining equality, deciding whether the invariant holds, or expanding the permitted transformation scope are forbidden.

## Implementation freedom
Internal predicate representation, language, storage, ownership, allocation, serialization, and concurrency are free. Validation precedes construction; traceability precedes return.

## Errors and conformance
Source errors `missing_principle_reference` and `source_claim_mismatch` are preserved through public aliases. All acceptance tests are mandatory.

## Unresolved science
`principle_equality_semantics` and `permitted_transformation_scope` remain preserved unresolved. The descriptor is structural only.
