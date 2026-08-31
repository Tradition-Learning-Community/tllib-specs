# Consumer acceptance, compatibility, and migration

This document defines how a future `tllib` consumer may use the published handoff without importing repository-internal scientific work. It is an engineering compatibility contract; it does not adjudicate scientific truth.

## Standalone consumer acceptance

The canonical population is always read from `handoff/catalog.json` at the targeted commit.

Run:

```text
python tools/pipeline/validate_consumer_acceptance.py --evidence <path>
```

For every published feature, the validator exports the standalone bundle twice and compares the complete exported trees and `bundle-lock.json` records. The neutral consumer then reads only:

- `feature/manifest.json`;
- `feature/contract.json`;
- `feature/acceptance.json`;
- `feature/traceability.json`;
- the resolved shared contracts and lock file inside the bundle.

Traceability and acceptance documents may preserve source strings such as `maths/...` or `registry/...`; these are provenance, not runtime dependencies. The reference consumer never opens those paths.

The consumer exposes the already-published scientific and execution statuses and discovers obligations from required, forbidden, deferred, operation, acceptance, invariant, implementation-mode, error-contract, traceability, and shared-contract surfaces. It never computes a scientific result.

Execution gates are structural:

- `executable`: eligible for a later implementation that still obeys the feature contract;
- `conditionally_executable`: rejected by the neutral consumer with `TLLIB_CONSUMER_CONDITIONS_REQUIRED` until published conditions are satisfied;
- `structural_only`: rejected with `TLLIB_CONSUMER_EXECUTION_NOT_AVAILABLE`;
- `unsupported`: rejected with `TLLIB_CONSUMER_UNSUPPORTED_EXECUTION`.

These errors are consumer safety signals, not invented scientific behavior.

## Version surfaces

The machine policy is `handoff/compatibility-policy.json`.

The published system already carries versioned surfaces. Wave D makes their compatibility meaning explicit:

- model: `handoff/catalog.json -> model_version`;
- catalog serialization: `schema_version`;
- domain: domain catalog `schema_version`, `package_model_version`, deterministic `catalog_sha256`, and its ordered feature-package version vector;
- feature and feature contract: `package_version` shared by manifest and contract;
- shared structural contract: shared package `package_version`;
- JSON schema: each schema's machine-readable `properties.schema_version.const` plus its content fingerprint;
- validator/exporter/generator: the versions published by the canonical catalog.

A domain therefore has a deterministic composite revision without inventing a second independent scientific version number. Adding a domain is distinct from modifying an existing domain because the diff compares domain identities, indices, catalog fingerprints, and feature version vectors.

## Machine-readable catalog diff

Run:

```text
python tools/pipeline/validate_catalog_compatibility.py --base <commit-or-ref> --evidence <path>
```

If `--base` is omitted, the first parent of the targeted commit is used. `--target` may be supplied to compare two committed refs; otherwise the current checkout is the target.

The result classifies changes as `compatible`, `incompatible`, `scientific_review_required`, or `invalid` and records the exact base/target commits and populations.

The validator rejects unversioned changes to versioned normative surfaces. In particular, a changed feature or shared-contract package must change its package version, a changed schema must change its schema version, and a changed published validator/exporter/generator implementation must change its published tool version.

Major version changes and removals are machine-visible as incompatible. Additive domains/features and minor/patch changes are compatible unless another rule makes them incompatible. A scientific-status transition is explicitly surfaced as `scientific_review_required`; the validator does not decide the scientific outcome.

## Identifier and fingerprint stability

Published feature IDs, shared-contract IDs, and domain indices are identities and are not reusable for different meanings. Content fingerprints are content addresses: changing content changes its fingerprint. A feature identity may not silently move to another domain.

## Deprecation, substitution, and support windows

There are currently no active feature deprecations or substitutions in the canonical catalog. Future entries are explicit and machine-readable.

A deprecation must provide:

- `introduced_in`;
- `supported_through`;
- `reason`.

There is no implicit calendar duration. The support window is the explicit version interval declared by the deprecation, avoiding an invented date or policy.

A substitution must provide:

- `target_feature_id`;
- `introduced_in`;
- `relation`.

A consumer must never infer a substitute merely from similar titles, domains, shapes, equations, or scientific objects.

## Migration procedure

Before execution, a consumer should:

1. read the target catalog and its version surfaces;
2. run or consume the machine compatibility diff against the version it currently supports;
3. refuse execution when compatibility is `invalid`;
4. require an explicit migration decision for `incompatible` changes;
5. route `scientific_review_required` changes through the scientific authority rather than guessing a behavior;
6. apply explicit deprecation/substitution records only when present;
7. re-run standalone bundle acceptance for the complete target catalog.

The CI performs the consumer and compatibility audits deterministically and stores evidence named with the exact specification commit.
