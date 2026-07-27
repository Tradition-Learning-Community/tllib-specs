# Message existential cycle descriptor

## What is this feature?

`TLC-FC-07-MESSAGE-005` assembles the exact 18 source-declared existence, content, property, revelation, transmission, and transformation records into a non-executable Message-cycle descriptor.

## What must be implemented?

Implement `assemble_message_existential_cycle_descriptor`. Validate the authoritative 18-object population, preserve every contextual relation, partition records into four source contexts, expose six cycle-stage references in recorded source order, and preserve `TLC-SO-MESSAGE-059` and `TLC-SO-MESSAGE-071` as distinct Transmission occurrences.

## Valid input

Exactly one record for each identifier listed in `contract.json`, with the authoritative contextual relations, source context, recorded source position, opaque payload, candidate status, provenance, the 17 unresolved identifiers, and reservation `TLC-DUP-MESSAGE-002`.

## Required output

One descriptor containing all 18 distinct identities, four source-context partitions, six ordered stage references, all contextual relations, complete unresolved and reservation metadata, provenance, and no executable transition.

## Mandatory behavior

Exact population, identity distinction, relation preservation, four partitions, six-stage source order, separate Transmission occurrences, content conservation, determinism, metamorphic input permutation, unresolved propagation, and failure atomicity are normative.

## Forbidden behavior

Do not execute transitions, infer timing, causal effects, transformation criteria, sender/receiver roles, encoding, delivery, transport, or scientific truth. Never merge the two Transmission records.

## Left to the implementer

Partition and index structures, internal ordering mechanism, language, storage, ownership, allocation, concurrency policy, and serialization format remain implementation-defined.

## Observable errors

- `IncompleteCycleEvidence`: one or more authoritative records or required references are absent.
- `DuplicateCycleIdentifier`: an authoritative identity occurs more than once.
- `TransmissionOccurrencesMerged`: the distinct `TLC-SO-MESSAGE-059` and `TLC-SO-MESSAGE-071` occurrences are collapsed.

## Conformance

`acceptance.json` verifies the exact population, four partitions, six-stage order, all errors, separate Transmission identities, content and relation preservation, determinism, metamorphic permutation, round-trip preservation, unresolved propagation, and absence of transition or transport execution.

## Unresolved scientific semantics

Transition rules, timing, causal effects, transformation criteria, sender/receiver roles, encoding, and transport remain unresolved or externally provided. The descriptor is structural only.