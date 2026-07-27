# TLC-FC-09-VALUES-013 — Value-operator registry

## What is this feature?
A structural registry for four source-declared operator descriptor roles covering professional value, decision weight, transmission systems, and numeric descriptors.

## What must be implemented?
Require exactly four distinct source-declared roles, validate descriptor source bindings, preserve opaque callable descriptors without assigning signatures, return `ValueOperatorRegistry`, and attach complete traceability.

## Valid inputs and required output
Input is a four-entry mapping from `ValueOperatorRole` to `OpaqueOperatorDescriptor`. The output is one immutable registry with exactly four distinct entries.

## Mandatory and forbidden behavior
Exact role population, distinct identities, declared order, opaque round-trip, deterministic construction, and atomic failure are mandatory. Signature assignment, invocation, numeric representation, return semantics, invented comparison, or invented aggregation are forbidden.

## Implementation freedom
Registry representation, lookup structure, language, storage, ownership, allocation, serialization, and concurrency are free. Validation precedes publication; traceability precedes return.

## Errors and conformance
Source errors `missing_operator_role`, `duplicate_operator_role`, and `descriptor_source_mismatch` are preserved through public aliases. Every acceptance test is mandatory.

## Unresolved science
`operator_signatures`, `numeric_representation`, and `return_semantics` remain preserved unresolved. Invocation requires an external provider.
