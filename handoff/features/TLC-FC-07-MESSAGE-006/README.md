# Message entity profile

## What is this feature?

`TLC-FC-07-MESSAGE-006` declares the root Message entity as a non-executable structural profile. It links three distinct evidence roles—`entity`, `essential_properties`, and `transmissibility`—through two exact source relations.

## What must be implemented?

Implement `declare_message_entity_profile`. Validate exact objects `TLC-SO-MESSAGE-001`, `TLC-SO-MESSAGE-004`, and `TLC-SO-MESSAGE-030`; validate exact relations `TLC-SR-MESSAGE-003` and `TLC-SR-MESSAGE-029` and their endpoints; reject protocol fields; and return the three-role profile.

## Valid input

The three distinct object records, the two exact relation records with authoritative endpoints, unchanged source references, opaque candidate payloads, candidate status, provenance, unresolved identifiers `TLC-UT-MESSAGE-001` and `TLC-UT-MESSAGE-021`, and reservation `TLC-DUP-MESSAGE-001`.

## Required output

One root profile preserving three separate role references, both relation identities, all opaque evidence and provenance, unresolved and reservation metadata, and explicit absence of encoding, transport, execution, sender, recipient, or channel fields.

## Mandatory behavior

Exact identity, relation endpoint validity, role separation, content and provenance preservation, candidate status, unresolved propagation, deterministic structural equality, prohibited-field rejection, and failure atomicity are normative.

## Forbidden behavior

Do not define property classifications, transmission mechanics, audience, medium, encoding, transport, delivery, execution, sender, recipient, or channel behavior. Do not merge roles, objects, or relations.

## Left to the implementer

Language, internal representation, ownership, storage, allocation, concurrency policy, relation-validation decomposition, and serialization format remain implementation-defined.

## Observable errors

- `IncompleteMessageDeclaration`: a required object, relation, or source reference is absent or duplicated.
- `RelationEndpointMismatch`: a required relation does not connect its authoritative evidence endpoints.
- `ForbiddenProtocolField`: protocol, encoding, transport, execution, sender, recipient, or channel data is supplied or produced.

## Conformance

`acceptance.json` verifies nominal role and relation structure, all three errors, identity and content conservation, role separation, determinism, round-trip preservation, unresolved propagation, and absence of protocol or transport fields.

## Unresolved scientific semantics

Property classifications, transmission mechanics, audience, medium, encoding, transport, and execution remain unresolved or external. This profile provides the documentary root used by the other Message packages, not an execution service.