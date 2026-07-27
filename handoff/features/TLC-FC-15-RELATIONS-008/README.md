# TLC-FC-15-RELATIONS-008 — Provisional relation tuple bundle structural record

## What is this feature?

This package defines the final implementable structural behavior for the Relations relation classified as `provisionally_separated`. It does not define executable scientific relation semantics.

## What must be implemented?

Implement exact validation and guarded construction of an immutable structural record. Preserve the feature identity, the 2 participant reference(s) in the declared order, scope `relations_008_virtue_value_tuple_records`, context `master_virtue_and_master_value_formalizations`, opaque source material, and all 5 unresolved items.

## Valid inputs and required output

A valid request contains the exact feature ID, the exact ordered participants (TLC-SO-RELATIONS-014, TLC-SO-RELATIONS-020), resolvable source references, unchanged opaque values, complete unresolved metadata, and no request for semantic evaluation. Success returns a deterministic structural record with the non-execution guard enabled.

## Mandatory and forbidden behavior

Mandatory behavior is exact preservation, deterministic structural validation, stable errors, and rejection of unsupported evaluation. It is forbidden to invent endpoints, direction, runtime arity, relation properties, types, dimensions, thresholds, numeric methods, graphs, membership, composition, inversion, projection, deduction, or causality.

## Implementation freedom

Internal data structures, programming language, allocation, ownership transport, concurrency policy, and serialization format are implementation-defined provided observable preservation and error behavior remain conforming.

## Observable errors

The contract preserves the authoritative PascalCase errors, including `FeatureIdentityMismatch`, participant and preservation errors, `ScientificPropertyInvented`, and `ExternalRelationEvaluatorRequired`, plus `IdentityMergeProhibited`.

## Conformance and unresolved science

All acceptance tests in `acceptance.json` must pass. Scientific evaluation remains `external_provider_required`; TLC-HR-0074 stays unresolved evidence and is not converted into a default.
