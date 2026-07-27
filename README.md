<div align="center">

# tllib-specs

**Language-neutral scientific and engineering specifications for the TLC model.**

[Feature handoff](handoff/) · [Global catalog](handoff/catalog.json) · [Contributor guide](CONTRIBUTING.md) · [Repository guide](docs/REPOSITORY-GUIDE.md) · [Validation](#validation) · [Security](SECURITY.md)

</div>

## Production status

`tllib-specs` is the authoritative specification repository for the TLC model. It contains specifications, validation, traceability, and language-neutral handoff packages—not a runtime library.

| Published artifact | Finalized population |
|---|---:|
| Domain catalogs | **16** |
| Feature Handoff Packages | **166** |
| Shared structural contracts | **8** |
| Standalone exports validated by CI | **166** |

Feature Handoff Package v1.0 is finalized. The published model is independent of C++, Rust, Ruby, Python, or any other implementation language. Production runtime code, bindings, solvers, kernels, binary packages, and release archives belong in downstream implementation repositories.

## Choose your path

### Scientist or domain expert

Start with the authoritative text under [`maths/`](maths/), then identify the affected feature IDs and scientific review records. Clarify meaning, evidence, unresolved questions, and scientific authority without introducing software defaults.

### Mathematician

Start with [`registry/math-contracts/`](registry/math-contracts/) and the referenced scientific source. Work on definitions, assumptions, domains, invariants, proof obligations, and formal consistency. Missing mathematical semantics remain explicit.

### Algorithm designer

Start with [`registry/algorithms/`](registry/algorithms/), the finalized IR, and the corresponding oracle. Distinguish observable behavior, required partial order, and internal strategy. An upstream step list is not automatically a mandatory total runtime sequence.

### Specification engineer

Work across `registry/`, `handoff/`, schemas, catalogs, reports, and validators. Preserve identity, provenance, unresolved semantics, deterministic outputs, and language neutrality. Shared representation does not establish scientific equivalence.

### Runtime implementer

Start from a resolved standalone bundle exported from [`handoff/`](handoff/). Ordinary implementation should not require interpretation of the mathematical sources or intermediate pipeline. Report handoff ambiguities with the feature ID and bundle fingerprint.

### Reviewer or auditor

Review scientific integrity, structural correctness, implementation neutrality, and verifiability as separate dimensions. Use the committed reports and deterministic fingerprints as evidence.

Detailed role boundaries and workflows are in [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [`Repository operating guide`](docs/REPOSITORY-GUIDE.md).

## Repository architecture

```text
maths/                         authoritative scientific source texts
registry/                      compiler-like intermediate specification pipeline
  math-contracts/              mathematical contracts
  ir/                          source intermediate representations
  test-plans/                  source test plans
  optimized-ir/                finalized engineering-facing IR
  algorithms/                  authoritative algorithm specifications
  oracles/                     acceptance oracles
  domain-finalization/         domain decisions and inventories
  global-finalization/         integrated upstream model
handoff/                       final language-neutral programmer interface
  schemas/                     JSON Schemas
  shared/                      eight shared structural contracts
  domains/                     sixteen complete catalogs
  features/                    166 autonomous feature packages
  catalog.json                 deterministic global catalog
reports/handoff/               domain and global audit evidence
tools/handoff/                 official validation, catalog, and export tools
docs/                          contributor operations and decision records
```

The repository functions as a controlled transformation system:

```text
scientific authority
    → mathematical contracts
    → source IR
    → finalized engineering IR
    → algorithm specifications
    → acceptance oracles
    → Feature Handoff Packages
    → standalone implementation bundles
```

`registry/` is the auditable intermediate pipeline. `handoff/` is the published programmer-facing result.

## Where downstream programmers start

A resolved standalone bundle contains exactly:

```text
feature/
shared/
bundle-lock.json
```

The feature package states observable behavior, valid inputs, required outputs, invariants, errors, forbidden behavior, acceptance tests, traceability, and implementation freedoms. `shared/` contains the exact versioned structural dependencies needed by the feature. `bundle-lock.json` fixes versions, paths, and SHA-256 fingerprints without volatile timestamps.

Create or inspect one bundle:

```bash
python tools/handoff/export_bundle.py TLC-FC-00-MASTER-005 --check
python tools/handoff/export_bundle.py TLC-FC-00-MASTER-005 ./bundle
```

Exports do not copy scientific source texts, registry artifacts, intermediate IRs, or generated archives.

## Feature package contract

Every feature directory contains:

- `README.md` — human implementer guide;
- `manifest.json` — identity, version, statuses, files, and shared dependencies;
- `contract.json` — normative observable engineering contract;
- `acceptance.json` — mandatory conformance tests;
- `traceability.json` — audit links to upstream authority;
- optional `examples.json` only when a source-backed fixture is justified.

The authority order is documented in [`handoff/README.md`](handoff/README.md). README prose and examples cannot create obligations absent from the normative structured contracts.

## Language and low-level freedom

Unless a feature contract makes a property observable, an implementation remains free to choose:

- programming language and naming;
- storage, allocation, ownership, aliasing, and layout;
- copying, movement, retention, and lifetime strategy;
- serialization representation;
- concurrency, scheduling, and error transport;
- internal architecture and algorithm decomposition.

The handoff can express low-level obligations when required, but it does not select a language-specific mechanism without observable justification.

## Scientific boundary

Structural finalization does not authorize scientific invention. A contributor or downstream implementation must not invent missing:

- equations, solvers, convergence rules, domains, or types;
- proof completion or truth values;
- thresholds, scores, rankings, metrics, or categories;
- state transitions, evaluators, providers, or causal meaning;
- relation endpoints, direction, arity, composition, or membership;
- defaults for unresolved parameters or decisions.

Opaque values remain opaque. Unresolved items remain explicit. Provider-required features remain structurally implementable without fabricating provider behavior. The repository's **147 scientific review questions remain scientifically unresolved**.

## Global catalog

[`handoff/catalog.json`](handoff/catalog.json) is a deterministic projection of the sixteen domain catalogs, 166 feature manifests, and eight shared packages. It records:

- model and tool versions;
- authoritative domain order and populations;
- feature IDs, paths, package versions, and multidimensional statuses;
- optional example presence;
- exact shared dependencies;
- deterministic package and descriptor SHA-256 fingerprints;
- explicit deprecation and substitution fields.

The catalog contains no timestamp or other volatile normative field. CI reconstructs it and rejects any mismatch.

## Validation

The sole official handoff validation CLI is:

```bash
python tools/handoff/validate_handoff.py
```

Complete handoff validation:

```bash
python tools/handoff/generate_catalog.py --check
python tools/handoff/validate_handoff.py --self-test
python tools/handoff/export_bundle.py --all --check --verify-determinism
```

The validator checks exact populations and order, schemas, required files, feature ownership, shared dependencies, cross-file identities, traceability, errors, strategies, test uniqueness, global catalog equality, and absence of normative implementation-language code.

The permanent workflow also generates each of the 166 standalone bundles twice and compares their locks and fingerprints for determinism.

## Change workflow

Use the repository issue forms and pull request template rather than unstructured changes.

1. Choose the correct scientific, specification, handoff, validation, or documentation path.
2. Identify affected domains, feature IDs, and authority.
3. Preserve unresolved science explicitly.
4. Update all affected layers or state why they are unaffected.
5. Run the relevant validation.
6. Open a focused pull request with compatibility and reviewer guidance.
7. Merge only after required checks and reviews succeed.

Cross-domain or difficult-to-reverse decisions should use a record based on [`docs/decisions/0000-template.md`](docs/decisions/0000-template.md).

## Contradictions and unresolved items

When two authoritative artifacts appear contradictory:

1. stop the affected finalization or implementation path;
2. identify the exact feature ID, operation, files, and conflicting obligations;
3. preserve current scientific and execution statuses;
4. report a minimal reproducer or conflicting acceptance case;
5. request scientific or specification adjudication;
6. do not choose the most convenient meaning.

An unresolved item is a preserved boundary, not an invitation to create an implementation default.

## Domains

| # | Domain | Features |
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

## Governance and support

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — role-based contribution and review standard;
- [`docs/REPOSITORY-GUIDE.md`](docs/REPOSITORY-GUIDE.md) — operating model, decision ownership, change levels, and definitions of ready and done;
- [`SUPPORT.md`](SUPPORT.md) — correct pathway for scientific, specification, handoff, and tooling questions;
- [`SECURITY.md`](SECURITY.md) — sensitive integrity and validator disclosures;
- [`docs/decisions/`](docs/decisions/) — durable records for cross-domain or difficult-to-reverse choices.

## Audit evidence

Global evidence is under [`reports/handoff/global/`](reports/handoff/global/), including population validation, cross-domain consistency, shared-contract decisions, unresolved ambiguities, validator consolidation, export validation, representative simulations, protected-artifact changes, and the finalization report.

## Repository boundary

Changes are acceptable only when they preserve scientific identity, traceability, unresolved semantics, exact populations, deterministic validation, and language neutrality. Runtime implementation belongs in a separate downstream repository.