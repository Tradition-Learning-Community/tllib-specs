# Message forms and process states catalogue

## What is this feature?

`TLC-FC-07-MESSAGE-004` builds a provenance-preserving catalogue of the exact 45 source-declared Message forms, validity conditions, discourse modes, understanding stages, crystallisation stages, and application examples.

## What must be implemented?

Implement `index_message_forms_and_process_states`. Validate the authoritative 45-identifier population, reject missing, duplicate, and unknown identifiers, group records by recorded source section/subsection, preserve recorded source order within each context, and expose immutable lookup indexes by object identifier and source context.

## Valid input

Exactly one record for each object identifier listed in `contract.json`, with its authoritative source reference, recorded source position, opaque candidate payload, candidate status, provenance, and the complete preserved unresolved set.

## Required output

One catalogue with complete 45-object coverage, an identifier index, a source-context index, source-ordered records within every context, preserved unresolved metadata, and no inferred hierarchy between contexts.

## Mandatory behavior

Exact population, uniqueness, retrievability, source-context grouping, recorded order within context, identity and content preservation, candidate status, unresolved propagation, determinism, and failure atomicity are normative. Permuting input records while preserving their recorded source positions must not change the canonical semantic catalogue.

## Forbidden behavior

Do not infer scientific classification, hierarchy, medium semantics, temporal transitions, application validity, protocol, transport, execution, or truth. Do not merge records, promote candidate status, or use incidental input order as scientific order.

## Left to the implementer

Index data structures, grouping implementation, sorting strategy, language, storage, ownership, allocation, concurrency policy, and serialization format remain implementation-defined.

## Observable errors

- `MissingMessageStateRecord`: one or more authoritative records are absent.
- `DuplicateMessageStateIdentifier`: an authoritative identifier occurs more than once.
- `UnknownMessageStateIdentifier`: an identifier outside the exact authoritative set is supplied.

## Conformance

`acceptance.json` verifies 45-object coverage, both indexes, all three errors, content and identity conservation, source-context order, metamorphic input permutation, determinism, round-trip preservation, unresolved propagation, and absence of inferred hierarchy or transitions.

## Unresolved scientific semantics

The 42 unresolved identifiers listed in `contract.json` remain visible. Scientific classification, hierarchy, medium semantics, transitions, and application validity are not supplied by this package.