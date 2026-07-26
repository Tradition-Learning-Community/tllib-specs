<div align="center">

<img src="docs/assets/tllib-specs-banner.svg" alt="tllib-specs — scientific specifications before implementation" width="100%" />

# tllib-specs

**The specification repository for the TLC scientific library.**

[![Global finalization validation](https://github.com/Tradition-Learning-Community/tllib-specs/actions/workflows/global-finalization.yml/badge.svg)](https://github.com/Tradition-Learning-Community/tllib-specs/actions/workflows/global-finalization.yml)
[![Specification status](https://img.shields.io/badge/specification-implementation--ready-0f766e)](registry/global-finalization/manifest.yaml)
[![Active features](https://img.shields.io/badge/features-166-2563eb)](registry/global-finalization/feature-status.yaml)
[![Domains](https://img.shields.io/badge/domains-16-7c3aed)](registry/global-finalization/domain-status.yaml)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b)](LICENSE)

[Overview](#overview) · [Architecture](#specification-architecture) · [Domains](#domains) · [Repository map](#repository-map) · [Examples](#working-with-a-feature) · [Validation](#validation) · [Contributing](#contributing)

</div>

---

## Overview

`tllib-specs` contains the **scientific, mathematical, structural, and algorithmic contracts** that define the future `tllib` C++ library and its Python bindings.

This repository is deliberately **upstream of implementation**. Its job is to make every future implementation traceable, testable, and unable to silently replace missing scientific semantics with convenient defaults.

The current integrated specification covers:

| Coverage | Status |
|---|---:|
| Scientific domains | **16** |
| Active features | **166** |
| Mathematical contracts | **166** |
| Source intermediate representations | **166** |
| Source test plans | **166** |
| Finalized implementation IRs | **166** |
| Algorithm specifications | **166** |
| Acceptance oracles | **166** |

The global package is marked [`integrated_specification_ready_for_implementation`](registry/global-finalization/manifest.yaml). This means the **structural software layer is fully specified**. It does not mean that every preserved scientific equation, proof, metric, transition, or evaluator is already executable.

## Why this repository exists

Scientific software often fails at the boundary between theory and code: equations are reinterpreted, unresolved terms receive accidental defaults, similar concepts are merged, and tests validate the implementation rather than the original contract.

TLC uses an explicit compiler-like specification pipeline to prevent that drift:

```mermaid
flowchart LR
    A[Scientific sources<br/>maths/] --> B[Feature catalogues]
    B --> C[Mathematical contracts]
    C --> D[Source IR]
    D --> E[Finalized implementation IR]
    E --> F[Algorithm specification]
    F --> G[Acceptance oracle]
    G --> H[Implementation task]

    C -. preserved .-> I[Traceability and provenance]
    D -. preserved .-> I
    E -. validated .-> I
    G -. verifies .-> I
```

Every active feature is expected to remain connected through the complete chain:

```text
scientific source
  → mathematical contract
  → source IR
  → finalized implementation IR
  → algorithm specification
  → acceptance oracle
  → implementation task
```

## Specification architecture

The repository separates **scientific authority** from **software realization**.

### 1. Scientific sources

The [`maths/`](maths/) directory contains the original domain texts. These files remain authoritative and are not rewritten during IR optimization or software planning.

### 2. Source contracts and IR

Each active feature has:

- a mathematical contract in [`registry/math-contracts/`](registry/math-contracts/);
- a source IR in [`registry/ir/`](registry/ir/);
- a source test plan in [`registry/test-plans/`](registry/test-plans/).

### 3. Finalized implementation specifications

Each feature also has:

- a finalized IR in [`registry/optimized-ir/`](registry/optimized-ir/);
- an algorithm specification in [`registry/algorithms/`](registry/algorithms/);
- an acceptance oracle in [`registry/oracles/`](registry/oracles/).

These artifacts describe implementable structural behavior such as validation, immutable representation, traceability, error handling, opaque-value transport, unresolved propagation, and deterministic serialization where declared.

### 4. Domain and global integration

Domain packages live in [`registry/domain-finalization/`](registry/domain-finalization/). The integrated library-level specification lives in [`registry/global-finalization/`](registry/global-finalization/), including:

- shared structural types and patterns;
- module interfaces;
- dependency graph;
- implementation waves;
- decision register;
- implementation backlog;
- library specification.

## Domains

| # | Domain | Active features |
|---:|---|---:|
| 00 | Master | 16 |
| 01 | Disciple | 10 |
| 02 | Community | 8 |
| 03 | Huit Dimensions | 11 |
| 04 | Invariants | 10 |
| 05 | Dynamics | 7 |
| 06 | Theorems | 9 |
| 07 | Message | 6 |
| 08 | Principle | 10 |
| 09 | Values | 14 |
| 10 | Virtues | 10 |
| 11 | Capacities | 15 |
| 12 | Competencies | 13 |
| 13 | Practice | 10 |
| 14 | Lived Experience | 12 |
| 15 | Relations | 5 |
|  | **Total** | **166** |

The authoritative integrated order and counts are recorded in the [global finalization manifest](registry/global-finalization/manifest.yaml).

## Repository map

```text
tllib-specs/
├── maths/                         # Authoritative scientific domain texts
├── registry/
│   ├── math-contracts/            # One mathematical contract per active feature
│   ├── ir/                        # Preserved source intermediate representations
│   ├── test-plans/                # Preserved source test plans
│   ├── optimized-ir/              # Finalized implementation-facing IRs
│   ├── algorithms/                # Algorithm specifications and pseudocode
│   ├── oracles/                   # Acceptance oracles and test requirements
│   ├── domain-finalization/       # Module specs, patterns, decisions, tasks
│   ├── global-reconciliation/     # Authoritative baseline and feature matrices
│   └── global-finalization/       # Integrated library specification and backlog
├── reports/
│   ├── domain-finalization/       # Per-domain finalization reports
│   └── global-finalization/       # Global readiness and finalization reports
├── tools/
│   ├── domain-finalization/       # Domain validators
│   └── global-finalization/       # Integrated specification validator
├── .github/workflows/             # Specification integrity CI
└── docs/assets/                   # README and documentation visuals
```

## Working with a feature

A feature is identified by a stable ID such as:

```text
TLC-FC-00-MASTER-001
```

Its specification chain can be inspected directly:

```text
registry/math-contracts/TLC-FC-00-MASTER-001/contract.yaml
registry/ir/TLC-FC-00-MASTER-001/ir.yaml
registry/test-plans/TLC-FC-00-MASTER-001/test-plan.yaml
registry/optimized-ir/master/TLC-FC-00-MASTER-001/ir.yaml
registry/algorithms/master/TLC-FC-00-MASTER-001/algorithm.yaml
registry/oracles/master/TLC-FC-00-MASTER-001/oracle.yaml
```

A finalized IR is implementation-facing but still preserves its sources:

```yaml
feature_id: TLC-FC-00-MASTER-001
status: selected_for_master_implementation_specification

traceability:
  contract_ref: registry/math-contracts/TLC-FC-00-MASTER-001/contract.yaml
  ir_registry_ref: registry/ir/TLC-FC-00-MASTER-001/ir.yaml
  source_test_plan_ref: registry/test-plans/TLC-FC-00-MASTER-001/test-plan.yaml

representation:
  implementation_kind: immutable_descriptor

operations:
  - validate_feature_identity
  - validate_exact_reference_sets
  - construct_immutable_provenance
  - emit_declaration_descriptor
  - verify_preservation_obligations
```

The corresponding algorithm explains the ordered behavior, while the oracle defines the acceptance conditions an implementation must satisfy.

## What can be implemented now

The specifications authorize implementation of the shared structural layer, including:

- stable feature and source identifiers;
- immutable descriptors;
- exact identity, input, provenance, and reference validation;
- opaque scientific payload carriers;
- unresolved and reservation propagation;
- structured deterministic errors;
- serialization and round-trip behavior where declared;
- module interfaces;
- oracle-driven acceptance suites.

See the [implementation readiness report](reports/global-finalization/implementation-readiness.md), [library specification](registry/global-finalization/library-specification.yaml), and [implementation backlog](registry/global-finalization/implementation-backlog.yaml).

## Scientific boundary

This repository does **not** authorize an implementation to invent missing semantics.

Unless explicitly defined by the source contract, implementations must not introduce:

- numerical solvers or convergence policies;
- thresholds, scores, rankings, or measurement scales;
- theorem proofs or proof completion;
- state-transition rules;
- causal interpretations of relations;
- value, virtue, capacity, or competency evaluation;
- defaults for unresolved scientific parameters.

Unsupported scientific execution must remain explicit, traceable, and rejectable through structured errors or external-evaluator boundaries.

## Validation

The permanent GitHub Actions workflow validates the integrated specification package on relevant changes.

Run the global validator from the repository root:

```bash
python3 tools/global-finalization/validate_global_finalization.py
```

The validator checks, among other things:

- all 16 domain packages are present;
- exactly 166 IRs, algorithms, and oracles are discoverable;
- feature populations match across artifact layers;
- historical Capacities identifiers are not promoted;
- protected scientific sources and source artifacts are unchanged;
- no C++ implementation or Python binding is introduced in this repository;
- the Git diff is structurally clean.

Domain-specific validators are available under [`tools/domain-finalization/`](tools/domain-finalization/).

## Implementation roadmap

The integrated backlog organizes future development into dependency-aware waves:

1. shared identifiers, references, opaque values, unresolved propagation, traceability, and errors;
2. independent descriptor modules;
3. remaining structural modules in parallel dependency-aware lots;
4. cross-module acceptance suites;
5. Python bindings after the C++ structural interfaces pass their oracles.

Implementation code should live in the future implementation repository or explicitly designated implementation branch—not in this specification repository unless the project governance changes that boundary.

## Contributing

Contributions are welcome when they preserve the repository's scientific and traceability guarantees.

Before opening a pull request:

1. identify the affected feature IDs and source artifacts;
2. preserve the authoritative files under `maths/`, source contracts, source IRs, and source test plans unless the contribution is an explicitly approved scientific revision;
3. update all affected finalized IR, algorithm, oracle, module, and task references together;
4. preserve unresolved items rather than replacing them with assumptions;
5. run the relevant domain validator and the global validator;
6. keep implementation code outside this repository's current scope.

A good pull request explains **what changed, why it is scientifically authorized, which feature chain is affected, and which validation evidence passed**.

## Project status

| Phase | Status |
|---|---|
| Scientific source organization | Complete |
| Mathematical contracts | Complete for 166 active features |
| Source IR and test plans | Complete for 166 active features |
| Finalized implementation IRs | Complete |
| Algorithm specifications | Complete |
| Acceptance oracles | Complete |
| Domain integration | Complete |
| Global library specification | Complete |
| C++ implementation | Not started in this repository |
| Python bindings | Not started in this repository |
| Packaging and releases | Not started |

## License

Licensed under the [Apache License 2.0](LICENSE).

---

<div align="center">

**Tradition Learning Community — from scientific theory to verifiable software contracts.**

</div>
