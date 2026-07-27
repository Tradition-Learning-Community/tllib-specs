# TLC-FC-00-MASTER-005 — Master seven-tuple definition

This pilot package defines the observable structural behavior for describing the Master's seven-tuple declaration.

A conforming implementation accepts the exact feature identity, the exact scientific object reference `TLC-SO-MASTER-008`, the five exact relation references `TLC-SR-MASTER-007` through `TLC-SR-MASTER-011` in source order, and an empty unresolved collection. It emits an immutable declaration descriptor with complete provenance.

The package does not evaluate the seven-tuple, assign component runtime types, select a memory layout, invent dimensions or values, merge component identities, or require the total step sequence printed in the upstream algorithm artifact. Only the partial-order obligations in `contract.json` are normative.

## Authority

Apply the repository handoff authority order. `contract.json` and `acceptance.json` are normative. This README and `examples.json` add no obligations.

## Implementation freedom

Public naming, programming-language type design, storage, allocation, ownership mechanism, error transport, serialization, concurrency strategy, and internal validation decomposition remain free unless they affect a stated observable obligation.