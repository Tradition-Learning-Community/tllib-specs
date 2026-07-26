# Implementation readiness

## Ready now

The repository contains an implementation-facing structural package for all 166 active features. Developers can implement:

- immutable structural descriptors;
- exact input, identity, provenance and reference validation;
- opaque scientific payload transport;
- unresolved and reservation propagation;
- deterministic structural errors;
- serialization and round-trip behavior where declared;
- module-level interfaces and oracle-driven acceptance tests.

## Not asserted

This readiness statement does not assert that every feature is scientifically executable. Domain-level unresolved items remain authoritative. No missing scientific semantics may be replaced by defaults.

## Planned implementation waves

1. shared identifiers, references, opaque values, unresolved propagation, traceability and errors;
2. independent descriptor modules;
3. remaining domain structural modules in dependency-aware parallel lots;
4. cross-module acceptance suites;
5. Python bindings only after the C++ structural interfaces pass their oracles.

## Acceptance gate

Implementation begins from the global backlog and the sixteen domain task files. A feature is accepted only when its finalized IR, algorithm and oracle remain mutually consistent and all source-preservation obligations pass.
