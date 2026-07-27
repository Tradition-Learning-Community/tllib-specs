# TLC-FC-12-COMPETENCIES-004 — Admissible evolution dynamics descriptor

## What is this feature?

This feature preserves five admissible evolution-dynamics equations as opaque scientific records: `TLC-SO-COMPETENCIES-066`, `096`, `097`, `098`, and `114`.

## What must be implemented?

Implement one structural operation that validates the exact feature identity, the exact five-object population, complete provenance, and request mode `structural_descriptor_only`. It returns one immutable descriptor in source order.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-004`; all five required objects must occur exactly once; no extra object is accepted; every object needs provenance; and only structural mode is valid.

## What is the required output?

Return a descriptor preserving category `evolution_dynamics`, boundary `admissible`, object order `[066, 096, 097, 098, 114]`, opaque equation payloads, provenance, reservations, and the Capacities dependency as `external_unreconciled` scientific-documentary metadata with `runtime_required=false`.

## What behavior is mandatory?

Preserve all identities and dependency status, validate before publication, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not integrate equations, sample stochastic terms, generate trajectories, calculate acquisition or development, infer initial conditions or parameters, or execute/resolve the Capacities domain dependency.

## What is left to the implementer?

Internal representation, validation architecture, storage, allocation, serialization, and concurrency are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies exact order, opacity, deterministic output, dependency preservation, rejection of dynamics and automatic dependency resolution, stable errors, and complete traceability.

## Are unresolved scientific semantics involved?

Yes. All five equations remain non-executable, and Capacities remains an external scientific provider requirement rather than a runtime dependency.