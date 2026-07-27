# TLC-FC-08-PRINCIPLE-007 — Uncomputable principle metric requirements

## What is this feature?
It records four source-stated metric challenges without defining or computing a metric.

## What must be implemented?
Implement `DESCRIBE-PRINCIPLE-METRIC-REQUIREMENTS`. Validate object `TLC-SO-PRINCIPLE-032`, preserve the four requirement statements and provenance, and return an immutable descriptor marked `computable = false` and `external_evaluator_required = true`.

## Valid inputs and required output
Input supplies the exact source object, opaque metric-requirement evidence, an empty unresolved collection, and provenance. Output contains exactly four requirements, no score/distance/threshold, and `evaluated = false`.

## Mandatory and forbidden behavior
Exact population, source order, explicit non-computability, opacity, and provenance are mandatory. Metric definition, calculation, aggregation, threshold comparison, and invented units or scales are forbidden.

## Implementer freedom
Descriptor storage, ownership, allocation, serialization, language, and concurrency policy are implementation-defined.

## Errors and conformance
Use the four `PRINCIPLE_*` errors in `contract.json`. `acceptance.json` verifies four requirements, `computable=false`, absence of numeric output, stable errors, and determinism.

## Unresolved scientific semantics
Metric signature, domain, codomain, scale, units, score, distance, thresholds, aggregation, and calculation rule are absent. A scientific metric provider is external.
