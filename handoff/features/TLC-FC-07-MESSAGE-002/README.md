# Message preexistence claim

## What is this feature?

`TLC-FC-07-MESSAGE-002` registers the source-declared Message preexistence statement as an unevaluated structural claim. It does not decide whether the statement is true.

## What must be implemented?

Implement `register_message_preexistence_claim`. Validate exact evidence identity `TLC-SO-MESSAGE-013` and its unchanged source range, preserve the opaque statement and provenance, and return a claim whose `verification_status` is exactly `unavailable_without_oracle`.

## Valid input

One candidate evidence record for `TLC-SO-MESSAGE-013`, with its source reference, opaque payload, candidate status, provenance, and no request for oracle evaluation.

## Required output

One `UnevaluatedPreexistenceClaim` preserving the evidence and exposing candidate status, `verification_status=unavailable_without_oracle`, absence of a truth value, and absence of an executable oracle.

## Mandatory behavior

Identity, source range, content, opacity, provenance, candidate status, and unavailable-oracle status are normative. Identical evidence produces structurally equal claims. Failures expose no partial claim.

## Forbidden behavior

Do not define or infer an ontology, time model, existence predicate, truth value, scientific oracle, encoding, transport, execution behavior, or protocol.

## Left to the implementer

Internal representation, language, ownership, storage, allocation, serialization format, and validation decomposition are implementation-defined.

## Observable errors

- `MissingPreexistenceEvidence`: the required identity or source range is absent or changed.
- `OracleEvaluationRequested`: a caller requests scientific evaluation or a truth value.

## Conformance

`acceptance.json` verifies registration, both errors, preservation, metadata, determinism, round-trip preservation, and the mandatory absence of truth evaluation.

## Unresolved scientific semantics

Ontology, time model, existence predicate, and scientific oracle require an external scientific provider. The structural registration remains implementable without them.