# Feature Handoff Package v1.0

`handoff/` is the final, language-neutral output of `tllib-specs`. It contains sixteen complete domain catalogs, 166 autonomous feature packages, eight shared structural contracts, and a deterministic global catalog.

A programmer normally begins with a standalone exported bundle, not with `registry/` or the mathematical source texts.

## Standalone bundle

Every logical export contains exactly:

```text
feature/
shared/
bundle-lock.json
```

- `feature/` is one autonomous feature package.
- `shared/` contains the exact transitive shared contracts required by that feature.
- `bundle-lock.json` records model and package versions, resolved contracts, ordered paths, and SHA-256 fingerprints without a timestamp.

The bundle contains no scientific source file, registry artifact, intermediate IR, or implementation code.

## Authority order

When package files appear to differ, apply this order from highest to lowest authority:

1. `contract.json`
2. `acceptance.json`
3. referenced shared contracts
4. `manifest.json`
5. `README.md`
6. `examples.json`
7. `traceability.json`

A README, example, traceability role, historical candidate, or upstream comparison artifact cannot create an obligation absent from the normative contracts.

## Package model

Each feature package declares exactly five mandatory files:

- `README.md`;
- `manifest.json`;
- `contract.json`;
- `acceptance.json`;
- `traceability.json`.

`examples.json` is optional and is present only when `manifest.json` declares it. The finalized model contains one package with examples and 165 without them.

`manifest.json` states the feature identity, domain, package version, scientific status, execution status, file population, examples presence, and exact shared dependencies.

`contract.json` defines observable operations, inputs, outputs, required and forbidden behavior, preconditions, postconditions, invariants, strategy constraints, runtime freedoms, determinism, errors, resource statements, implementation modes, and conformance.

`acceptance.json` is mandatory. Every listed test must pass; forbidden behavior is nonconforming.

`traceability.json` preserves upstream authority for audit. Its paths are not runtime dependencies and are not copied into standalone bundles.

## Complete catalogs

`domains/<domain>/catalog.json` contains the exact authoritative population and order of one domain. The sixteen catalogs together declare exactly 166 unique feature IDs.

`catalog.json` is the deterministic global projection. It contains all domains and features, multidimensional statuses, examples presence, shared dependencies, deterministic fingerprints, and tool versions. It is autonomous enough for population audit and export selection without becoming a competing scientific source.

The global catalog is rebuilt by:

```bash
python tools/handoff/generate_catalog.py --write
```

CI verifies the committed result with:

```bash
python tools/handoff/generate_catalog.py --check
```

No timestamp or volatile normative field is permitted.

## Shared contracts

The model uses eight versioned structural contracts:

- `TLC-HC-FEATURE-ID`;
- `TLC-HC-SCIENTIFIC-REFERENCE`;
- `TLC-HC-REFERENCE-COLLECTION`;
- `TLC-HC-UNRESOLVED-ITEM`;
- `TLC-HC-OPAQUE-VALUE`;
- `TLC-HC-STRUCTURED-ERROR`;
- `TLC-HC-TRACEABILITY`;
- `TLC-HC-DESCRIPTOR-ENVELOPE`.

A shared carrier does not imply scientific equivalence. Feature-local cardinality, order, errors, negative semantics, provider boundaries, and unresolved meanings remain explicit.

All 42 reported sharing candidates were reconciled globally. None was promoted in v1.0 because no candidate met every requirement for independent-domain equivalence, semantic neutrality, parameterizable local differences, net benefit, and non-invented shared tests.

## Scientific boundary

The handoff compiles observable obligations conservatively. It never supplies missing science.

Implementers must not invent equations, proof completion, types, domains, thresholds, categories, transitions, providers, evaluators, endpoints, relation properties, causal meaning, or defaults for unresolved decisions.

Opaque payloads remain unchanged and uninterpreted. Unresolved items remain explicit. `external_provider_required` means the package may define a structural provider boundary but does not define the provider's scientific behavior.

A source algorithm's total step list is not automatically a normative runtime order. Only observable ordering obligations published in `contract.json` constrain implementation sequencing.

## Low-level implementation freedom

Unless a contract explicitly says otherwise, the implementation may choose:

- language and naming;
- storage, ownership, allocation, aliasing, and layout;
- copying, movement, retention, and lifetime;
- serialization representation;
- concurrency, scheduling, and error transport;
- internal data structures and algorithm decomposition.

These freedoms do not permit changes to observable identity, population, order, invariants, errors, atomicity, determinism, or forbidden scientific behavior.

## Validation

The single official CLI is:

```bash
python tools/handoff/validate_handoff.py
```

Its logical tests are:

```bash
python tools/handoff/validate_handoff.py --self-test
```

The validator enforces:

- exactly sixteen catalogs, 166 feature packages, and eight shared contracts;
- exact equality with authoritative inventory populations and order;
- exact mandatory and optional file populations;
- JSON Schema and cross-file identity coherence;
- unique feature, test, operation, and error identities where required;
- complete traceability categories and resolvable audit paths;
- exact shared dependency versions and domain dependency unions;
- valid partial-order strategy constraints;
- deterministic equality of the global catalog projection;
- absence of normative C++, Rust, Ruby, or Python implementation code.

Historical inventory metadata aliases are read strictly. Every alias present must equal the actual ordered population. A conflict, missing evidence, or irreversible identity change is an error.

## Export

Inspect one resolved lock without retaining output:

```bash
python tools/handoff/export_bundle.py TLC-FC-00-MASTER-005 --check
```

Create one bundle in a new directory:

```bash
python tools/handoff/export_bundle.py TLC-FC-00-MASTER-005 ./bundle
```

Validate all features and double-generation determinism:

```bash
python tools/handoff/export_bundle.py --all --check --verify-determinism
```

Each selected bundle is generated twice in independent temporary directories during CI. The lock objects and every relative-path file hash must match exactly.

## Reporting contradictions

When a contradiction is found:

1. identify the exact feature ID and operation;
2. cite the conflicting package files and acceptance expectations;
3. preserve the current package, scientific, and execution statuses;
4. stop only the affected implementation behavior;
5. report the contradiction without choosing a convenient scientific resolution.

An unresolved item can be preserved, transported, serialized, or surfaced only as authorized. It cannot be silently converted into `true`, `false`, zero, an empty value, a default type, or an inferred relation.

## Repository boundary

`registry/` remains the intermediate specification pipeline and upstream audit authority. `handoff/` is the final programmer-facing output. This repository contains no production implementation code.
