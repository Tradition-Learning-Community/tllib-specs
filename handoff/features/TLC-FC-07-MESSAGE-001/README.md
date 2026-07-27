# Message quadruplet AST

## What is this feature?

`TLC-FC-07-MESSAGE-001` constructs a structural, immutable AST for the source-declared Message quadruplet. The four symbolic slots are `contenu`, `symbolique`, `structure_procedurale`, and `contexte` in source order. The operation preserves the three required evidence identities and the formal expression without interpreting them.

## What must be implemented?

Implement the observable operation `construct_message_quadruplet_ast`. It validates the exact evidence set, verifies that the opaque formal expression exposes exactly four source-named slots, and returns one traceable AST root.

## Valid input

The input must contain exactly `TLC-SO-MESSAGE-002`, `TLC-SO-MESSAGE-003`, and `TLC-SO-MESSAGE-025`, their source references, the unchanged formal expression, candidate status, provenance, and reservation `TLC-DUP-MESSAGE-001`.

## Required output

A successful result contains one Message tuple root, exactly four source-ordered symbolic slots, the three distinct evidence references, candidate status, provenance, and the preserved reservation.

## Mandatory behavior

Identity, content references, slot order, opacity, provenance, and candidate status are normative. Identical valid evidence must produce structurally equal results. Failure must expose no partial result.

## Forbidden behavior

Do not assign runtime types to slots, evaluate the scientific content, execute the procedural slot, define encoding or transport, invent sender/receiver interfaces, merge evidence identities, or reorder the four slots.

## Left to the implementer

Language, API transport, storage, ownership, allocation, serialization format, internal data structures, validation decomposition, and construction strategy remain implementation-defined provided the observable contract is satisfied.

## Observable errors

- `MissingDefinitionEvidence`: a required evidence identity or source reference is absent.
- `MalformedFourSlotExpression`: the preserved formal expression does not expose exactly the four source-named slots in source order.

## Conformance

Conformance is verified by `acceptance.json`, including nominal structure, both error paths, content and identity preservation, order, determinism, serialization round-trip preservation, and rejection of execution or transport behavior.

## Unresolved scientific semantics

Slot runtime types, encoding, transport, execution semantics, and reservation `TLC-DUP-MESSAGE-001` remain unresolved or outside this package. This feature is structural only.