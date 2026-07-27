# Pilot simulation: TLC-FC-00-MASTER-005 low-level work item

## Purpose

This document simulates downstream use of the Feature Handoff Package v1.0. C++ is used only as a verification lens for low-level concerns. No implementation source file is created, and this report does not make C++ normative.

## Inputs available to the implementer

The simulated implementer receives only:

- `handoff/features/TLC-FC-00-MASTER-005/`;
- the eight resolved shared contracts;
- `bundle-lock.json` produced by the exporter.

The mathematical contract, source IR, finalized IR, algorithm YAML, oracle YAML, and scientific prose are not needed during ordinary implementation.

## Derivable public behavior

A possible API can expose one descriptor-producing operation corresponding to `DESCRIBE-MASTER-SEVEN-TUPLE`. The public name and concrete type syntax are free. The input must carry:

- exact feature identity `TLC-FC-00-MASTER-005`;
- exact object-reference set containing only `TLC-SO-MASTER-008`;
- exact ordered relation-reference set `TLC-SR-MASTER-007` through `TLC-SR-MASTER-011`;
- an empty unresolved-reference set;
- source provenance.

Success returns an immutable descriptor with the seven required envelope fields. Requests for scientific calculation or concrete component layout fail with `MASTER_UNSUPPORTED_EXECUTION_MODE`.

## C++ verification lens

A C++ work item could choose a value-returning function, a result wrapper, or another error-aware interface. The handoff does not require exceptions, a particular expected/result utility, heap allocation, reference counting, templates, inheritance, or a specific standard-library container.

The following conclusions are derivable:

| Concern | Derivable requirement | Remaining freedom |
|---|---|---|
| Result ownership | The public result must remain valid according to the implementation's documented API and must not expose a partial success on failure. | Owned value, shared storage, arena-backed value, or another model may be used. |
| Lifetime | No result lifetime duration is prescribed beyond the implementation's public contract. Inputs need not be retained. | Stack, heap, arena, static tables, and interning remain possible. |
| Mutability | The observable descriptor is immutable after successful emission. | Internal construction may use mutation before publication. |
| Aliasing | No aliasing model is prescribed. Aliasing must not permit observable mutation or identity merging. | Copying, sharing, views, or handles may be used. |
| Layout | Component and descriptor layout are not constrained. | Field order in memory, padding, alignment, and binary ABI are implementation choices. |
| Allocation | No allocation count or allocation prohibition is specified. | Zero, one, or multiple allocations may be used. |
| Concurrency | Thread safety and reentrancy are implementation-defined. | Stateless, synchronized, thread-local, or externally synchronized designs are possible. |
| Errors | Four stable codes and their triggering conditions are public. | Exceptions, return objects, status codes, callbacks, or protocol errors are possible. |
| Failure atomicity | Failure exposes no successful partial descriptor and mutates no scientific or external domain state. | Internal temporary state and cleanup strategy are free. |

## Strategy simulation

The upstream algorithm lists a total sequence, but the handoff intentionally compiles only observable ordering constraints:

1. feature identity validation must occur before successful publication;
2. exact reference validation must occur before successful publication;
3. preservation obligations must be verified before successful publication;
4. a complete descriptor must exist before successful publication.

Validation order relative to provenance construction, error-object construction, caching, and internal descriptor assembly is otherwise free. A low-level implementation may short-circuit, combine checks, precompute constants, use table-driven validation, or use generated metadata.

## Error derivation

The programmer can derive the following without upstream artifacts:

- `MASTER_INVALID_FEATURE_ID` for any non-exact feature identity;
- `MASTER_REFERENCE_SET_MISMATCH` for membership, cardinality, identity, or required-order mismatch;
- `MASTER_PRESERVATION_VIOLATION` when identity, distinctness, order, opacity, or provenance cannot be preserved;
- `MASTER_UNSUPPORTED_EXECUTION_MODE` for calculation, concrete layout, or another invented execution request.

All four errors are transport-neutral and expose no partial successful result.

## Test derivation

The acceptance package supplies:

- the exact valid fixture;
- required descriptor fields and immutability;
- missing-relation rejection;
- relation distinctness and source order;
- deterministic semantic output for identical input;
- non-invention checks;
- unsupported calculation rejection;
- upstream source-integrity preservation;
- invalid-feature rejection;
- preservation-failure behavior.

These tests can be translated into any low-level test framework without consulting the oracle YAML.

## Ambiguities deliberately preserved

The simulation identified real choices that remain unsupported by authoritative sources and therefore stay implementation-defined:

- exact public function and type names;
- result ownership model and lifetime duration;
- copying, moving, borrowing, sharing, and aliasing mechanisms;
- memory layout, alignment, contiguity, address stability, and ABI;
- allocation strategy and maximum input size;
- canonical serialization and binary encoding;
- thread safety, reentrancy, and concurrent scheduling;
- diagnostic context beyond the stable error code and condition;
- scientific meaning, runtime representation, dimensions, values, and evaluation of each seven-tuple component.

No model correction was required for these ambiguities because the handoff exposes them explicitly as unconstrained or implementation-defined.

## Concrete model defect found and corrected

The simulation showed that copying the upstream `execution_order` list as a prescribed algorithm would unnecessarily restrict low-level implementations. The feature contract therefore uses `partially_constrained` strategy semantics and records only validation-before-success, preservation-before-success, and descriptor-before-success dependency pairs.

## Result

The pilot is sufficient to create an autonomous low-level work item. A programmer can derive a possible API, observable immutability, stable errors, failure atomicity, test obligations, and architecture freedoms without reading the intermediate pipeline.