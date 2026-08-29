# Semantic and shared-contract governance

This document defines the structural governance used by the publication pipeline. It does not adjudicate scientific truth.

## Population authority

`handoff/catalog.json` is the only authority for the published population at the targeted commit. Domain, feature, and shared-contract totals are observations of that catalog, never governance limits.

The Wave C validator is:

```text
python tools/pipeline/validate_semantic_contract_governance.py --evidence <path>
```

The evidence records the exact Git commit, catalog population, semantic inventory, transition comparison, shared-contract dependency audit, and the commands used.

## Unresolved semantic inventory

For every feature in the canonical catalog, the validator reads the published package and preserves only structural signals that already exist there:

- scientific and execution statuses;
- explicit unresolved identifiers carried by the contract;
- explicit classifications when a package provides one;
- explicit blocker fields;
- authoritative source paths from package traceability;
- opaque/provider boundaries expressed by shared-contract dependencies.

Stable governance identifiers are deterministic hashes of feature identity, item kind, and the already-published structural payload. They are identifiers for governance evidence, not scientific identifiers and not scientific conclusions.

The evidence distinguishes occurrence-level governance items from the set of unique unresolved identifiers. Neither count is hard-coded: both are reconstructed from the catalog population at the targeted commit.

Classification is deliberately conservative. Explicit upstream classifications are preserved. `external_provider_required` maps to the external-provider class, an explicit `TLC-HC-OPAQUE-VALUE` boundary maps to opacity, explicit blockers map to blocker, and otherwise the validator records `unknown`. It does not infer a scientific answer. `contested` is preserved only when explicitly published by an upstream package.

Implementation impact is copied from the existing execution status: `executable`, `conditionally_executable`, or `structural_only`. The validator never upgrades a package to executable.

## No silent disappearance

When Git history is available, the validator reconstructs the same inventory from the first parent of the targeted commit. Additions are reported. Any item present in the parent and absent in the targeted commit is rejected unless its stable item ID is present in `handoff/semantic-resolutions.json`.

A resolution entry must provide:

- `item_id`;
- `status: resolved`;
- a non-empty `resolution_ref` pointing to the authoritative revision or decision;
- an explicit `authority` string or list of strings.

The resolution ledger is intentionally a transition ledger, not a replacement source of scientific truth. Entries authorize removal of a previously published unresolved item; they do not provide fallback values, equations, defaults, or runtime behavior.

## Shared structural contracts

For each shared contract and each feature package discovered from the canonical catalog, the validator checks the dependency declarations according to the package formats that already exist in the repository.

For a feature package, the top-level `dependencies` section of `contract.json` is the explicit dependency declaration. Every entry must carry an exact contract ID, version, and non-empty structural purpose. The set must equal `shared_dependencies` in the package manifest and the dependency set published in the canonical catalog. Every operational `shared_contract_ref` found in the feature contract must be contained in that declared set.

For a shared-contract package, direct dependencies are represented by structural `shared_contract_ref` values in its contract. After excluding its permitted self-reference, that direct set must equal `shared_dependencies` in its manifest and the canonical catalog entry.

Across the complete catalog population, the validator additionally:

1. checks every referenced shared contract and exact version exists;
2. computes the deterministic transitive closure of the shared dependency graph and rejects cycles;
3. audits cardinality and ordering declarations structurally;
4. audits feature error contracts and requires a structured-error boundary when error contracts are present;
5. records opaque/provider boundaries and externally supplied scientific features;
6. requires shared contracts to remain `structural_only` and rejects feature/object/relation scientific identities inside shared contract definitions;
7. reports every explicit `shared_contract_candidate` marker found while scanning all published feature documents.

The validator does not infer that a scientifically meaningful dependency is useless merely because its purpose is expressed by an error contract, opacity rule, preservation obligation, or other structural statement instead of a `shared_contract_ref`. Exactness is established from the repository's explicit dependency declaration surfaces; scientific necessity is not guessed.

## CI and deterministic evidence

The handoff workflow checks out full Git history, verifies the canonical catalog, executes the Wave C validator twice, and byte-compares the two evidence files. The successful evidence file is uploaded as a workflow artifact named with the exact GitHub Actions commit SHA.

Because the population is always read from `handoff/catalog.json`, a newly published domain or feature automatically enters both the unresolved-semantics inventory and the shared-contract audit.
