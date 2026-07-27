# TLC-FC-08-PRINCIPLE-011 — Principle familiar-context association

## What is this feature?
It constructs a provenance-bearing structural association between one Principle reference and one or more caller-identified familiar discourse or situation references.

## What must be implemented?
Implement `ASSOCIATE-PRINCIPLE-WITH-FAMILIAR-CONTEXT`. Validate the exact source object, one non-empty Principle ID, and a non-empty sequence of unique context IDs. Preserve caller order, attach provenance, and freeze the association.

## Valid inputs and required output
Input supplies object `TLC-SO-PRINCIPLE-059`, one opaque Principle ID, at least one unique context ID, an empty unresolved collection, and provenance. Output preserves all IDs and order with `evaluated = false`.

## Mandatory and forbidden behavior
Non-empty cardinality, uniqueness, caller order, exact association shape, opacity, provenance, and determinism are mandatory. Ranking, familiarity inference, interpretation, similarity, validation, or claims about understanding are forbidden.

## Implementer freedom
Association storage, ownership, allocation, serialization, language, and concurrency policy are implementation-defined.

## Errors and conformance
Use the four `PRINCIPLE_*` errors in `contract.json`. `acceptance.json` verifies non-empty input, duplicate rejection, exact order, non-interpretation, stable errors, and determinism.

## Unresolved scientific semantics
Familiarity, interpretation meaning, ranking, similarity, validation, and effect on understanding remain opaque.
