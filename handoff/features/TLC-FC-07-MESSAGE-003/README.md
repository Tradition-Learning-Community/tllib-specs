# Existential discourse evidence

## What is this feature?

`TLC-FC-07-MESSAGE-003` assembles the two source-declared existential-discourse records into candidate oracle evidence. It preserves their distinct identities and shared source subsection while leaving scientific acceptance unresolved.

## What must be implemented?

Implement `assemble_existential_discourse_evidence`. Validate exactly `TLC-SO-MESSAGE-020` and `TLC-SO-MESSAGE-049`, require that they are distinct and cite the same source subsection, and return a two-sided descriptor with `oracle_acceptance_rule=unresolved_propagated`.

## Valid input

A complete pair containing both exact object identities, unchanged source references to the same subsection, opaque candidate payloads, candidate status, and provenance.

## Required output

One candidate evidence descriptor preserving both sides, their roles, shared subsection provenance, opaque values, and an explicit unresolved acceptance-rule marker.

## Mandatory behavior

Pair completeness, identity distinction, shared-context validation, content conservation, provenance, candidate status, unresolved propagation, determinism, and no partial result on failure are normative.

## Forbidden behavior

Do not classify the evidence scientifically, infer energetic semantics, decide acceptance, create an executable oracle, merge the two identities, define transport, or execute the evidence.

## Left to the implementer

Internal representation, language, storage, ownership, allocation, serialization format, and validation decomposition remain implementation-defined.

## Observable errors

- `IncompleteExistentialEvidencePair`: either required side is missing, duplicated, or replaced.
- `MismatchedSourceSubsection`: the two records do not cite the same authoritative subsection.

## Conformance

`acceptance.json` verifies the exact pair, both errors, identity and content conservation, unresolved acceptance, determinism, round-trip preservation, and prohibition of a scientific acceptance decision.

## Unresolved scientific semantics

Existential classification, energetic semantics, and acceptance criteria remain preserved unresolved. The structural evidence assembly is still executable.