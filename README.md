<div align="center">

# tllib-specs

**Language-neutral scientific and engineering specifications for the TLC model.**

[Feature handoff](handoff/) · [Global catalog](handoff/catalog.json) · [Validation](#validation) · [Export](#export-a-standalone-bundle) · [Scientific boundary](#scientific-boundary)

</div>

## Finalized scope

`tllib-specs` contains specifications, not a runtime library. Its finalized Feature Handoff Package v1.0 output covers:

| Artifact | Finalized population |
|---|---:|
| Domain catalogs | **16** |
| Feature packages | **166** |
| Shared structural contracts | **8** |
| Standalone exports validated by CI | **166** |

The model is independent of C++, Rust, Ruby, Python, or any other implementation language. No production implementation, binding, solver, kernel, package, or release archive belongs in this repository.

## Where programmers start

[`handoff/`](handoff/) is the final engineering output of this repository. A downstream programmer normally starts from a resolved standalone bundle containing:

```text
feature/
shared/
bundle-lock.json
```

The feature package states observable behavior, inputs, outputs, invariants, errors, forbidden behavior, acceptance tests, traceability, and implementation freedoms. `shared/` contains the exact versioned structural dependencies needed by that feature. `bundle-lock.json` fixes paths, versions, and SHA-256 fingerprints without a volatile timestamp.

Ordinary implementation should not require the programmer to interpret the mathematical sources or intermediate registry pipeline. Those upstream files remain available for audit, contradiction handling, and scientific review.

## Repository architecture

```text
maths/                         authoritative scientific source texts
registry/                      intermediate specification pipeline
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
```

`registry/` is not the normal downstream API. It is the compiler-like intermediate pipeline that preserves scientific authority and explains how each final package was derived. `handoff/` is the published result.

## What a feature package means

Every feature directory contains exactly:

- `README.md` — human implementer guide;
- `manifest.json` — identity, version, statuses, files, and shared dependencies;
- `contract.json` — normative observable engineering contract;
- `acceptance.json` — mandatory conformance tests;
- `traceability.json` — audit links to upstream authority;
- optional `examples.json` only when a source-backed fixture is honestly justified.

The authority order within a package is documented in [`handoff/README.md`](handoff/README.md). Examples and README prose cannot create obligations absent from the normative JSON contracts.

## Language and low-level freedom

The handoff abstracts low-level realization. Unless a package makes a constraint observable, an implementation is free to choose:

- programming language and naming;
- storage, allocation, ownership, aliasing, and layout;
- copying, movement, retention, and lifetime strategy;
- serialization representation;
- concurrency, scheduling, and error transport;
- internal architecture and algorithm decomposition.

An upstream algorithm file does not automatically impose a total runtime sequence. Final contracts publish only the ordering relationships supported by observable authority.

## Scientific boundary

Structural finalization does not authorize scientific invention. A downstream implementation must not invent missing:

- equations, solvers, convergence rules, domains, or types;
- proof completion or truth values;
- thresholds, scores, rankings, metrics, or categories;
- state transitions, evaluators, providers, or causal meaning;
- relation endpoints, direction, arity, composition, or membership;
- defaults for unresolved parameters or decisions.

Opaque values remain opaque. Unresolved items remain explicit. Provider-required features remain structurally implementable without fabricating provider behavior. The repository's 147 scientific review questions remain scientifically unresolved.

## Global catalog

[`handoff/catalog.json`](handoff/catalog.json) is generated deterministically from the sixteen domain catalogs, 166 manifests, and eight shared packages. It records:

- model and tool versions;
- authoritative domain order and counts;
- all feature IDs, paths, package versions, and multidimensional statuses;
- `examples.json` presence;
- exact shared dependencies;
- deterministic package and descriptor SHA-256 fingerprints;
- explicit deprecation and substitution fields.

The catalog contains no timestamp or other volatile normative field. CI regenerates its projection in memory and rejects any mismatch.

## Validation

The sole official handoff validation CLI is:

```bash
python tools/handoff/validate_handoff.py
```

Logical self-tests are available through:

```bash
python tools/handoff/validate_handoff.py --self-test
```

The validator checks the exact 16-domain and 166-feature population, authoritative inventory order, package schemas and files, feature ownership, shared dependencies, cross-file identities, traceability, errors, strategies, test uniqueness, global catalog equality, and absence of normative implementation-language code.

Historical inventory metadata aliases are accepted only in strict read mode. Every alias present must agree with the actual ordered population; compatibility never ignores divergence or changes a feature ID.

The permanent GitHub Actions workflow additionally validates all 166 deterministic standalone exports.

## Export a standalone bundle

Resolve and inspect one feature without retaining output:

```bash
python tools/handoff/export_bundle.py TLC-FC-00-MASTER-005 --check
```

Create a bundle in a new directory:

```bash
python tools/handoff/export_bundle.py TLC-FC-00-MASTER-005 ./bundle
```

Validate every catalog feature and generate each one twice for determinism:

```bash
python tools/handoff/export_bundle.py --all --check --verify-determinism
```

Exports copy only finalized `handoff/features/` and `handoff/shared/` files. They never copy scientific source texts, registry artifacts, or intermediate IRs. Generated archives are not committed.

## Contradictions and unresolved items

When a package appears internally contradictory:

1. stop the affected implementation path;
2. identify the exact feature ID, operation, files, and conflicting obligations;
3. preserve the current scientific and execution statuses;
4. report the contradiction with a minimal reproducer or acceptance-test conflict;
5. do not resolve it by choosing a convenient scientific meaning.

An `unresolved` item is a preserved boundary, not a request for an implementation default. It may be carried, serialized, displayed, or routed exactly as the package permits, but it cannot be silently answered.

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

## Audit evidence

Global handoff evidence is under [`reports/handoff/global/`](reports/handoff/global/), including population validation, cross-domain consistency, shared-contract decisions, unresolved ambiguities, validator consolidation, export validation, representative simulations, protected-artifact changes, and the finalization report.

## Contribution boundary

Changes are acceptable only when they preserve scientific identity, traceability, unresolved semantics, exact populations, and language neutrality. Implementation code belongs in a separate downstream repository.
