# Publication pipeline contract

This document defines how a commit of `tllib-specs` is considered published and validated. It describes repository engineering only; it does not add or resolve scientific semantics.

## Canonical population

`handoff/catalog.json` is the canonical inventory of the population published by a target commit.

The domain, feature, and shared-contract totals are observations of the arrays and `summary` in that file. They are not repository governance constants. Historical numbers embedded in v1 field names or reports are compatibility metadata only and must never cap future publication.

A published domain must be present in the global catalog and its `handoff/domains/<domain>/catalog.json` must declare:

- `statuses.population: complete`;
- `statuses.validation: validated`;
- a unique `domain_index`;
- an ordered, unique feature population consistent with `feature_packages` and `expected_feature_count`.

The deterministic catalog reconstruction rejects missing or ghost domain directories, missing or ghost feature package directories, duplicate identities, incomplete domain status, count divergence, package identity/version/status divergence, and fingerprint drift.

## Catalog-derived CI

`.github/workflows/global-finalization.yml` resolves its domain matrix at runtime with:

```text
python tools/pipeline/catalog_snapshot.py --matrix
```

No domain name or domain cardinality is manually enumerated in the workflow matrix. `tools/pipeline/catalog_snapshot.py --self-test` proves that adding a synthetic catalog domain changes the matrix without a YAML edit. `tools/pipeline/validate_ci_triggers.py` verifies that both publication workflows cover every normative source family on pull requests and pushes to `main`.

Normative source families covered by the full publication validation are:

- `maths/**`;
- `framework/**`;
- `registry/**`;
- `handoff/**`;
- `reports/**`;
- `execution-manifests/**`;
- `tools/**`;
- `.github/workflows/**`.

Purely unrelated documentation does not need to trigger the complete publication pipeline.

## Exact `main` validation

A successful pull-request run is not treated as proof for the commit eventually published on `main`.

Every relevant push to `main` runs the publication workflows again against the exact checked-out commit. The global workflow writes `pipeline-evidence.json` and uploads it as an artifact named with `${{ github.sha }}`. The evidence records:

- the exact specification commit SHA;
- the SHA-256 of `handoff/catalog.json`;
- schema and model versions;
- catalog status;
- observed domain, feature, and shared-contract population;
- every catalogued domain, index, feature count, catalog path, and domain-catalog fingerprint.

This artifact is the commit-pinned population proof for post-merge validation. Release certification adds further controls in issue #178.

## Required `main` protection

Repository administrators should configure `main` so changes are merged through pull requests and the aggregate publication checks are required before merge. The minimum required checks are:

- `Global integrity` from **Global finalization validation**; this job depends on successful catalog resolution and every catalog-derived domain matrix job;
- `Validate finalized handoff v1.0` from **Feature handoff validation**.

The repository must still retain the post-merge `push` validation described above: branch protection and pull-request success do not replace exact validation of the resulting `main` SHA.

Protection configuration is a GitHub repository setting rather than a normative file in this repository. Its effective state should be audited when certifying a release.

## Reproducible verification commands

From a clean checkout of a target commit, after installing the validation dependencies:

```text
python tools/pipeline/validate_ci_triggers.py
python tools/pipeline/catalog_snapshot.py --self-test
python tools/pipeline/catalog_snapshot.py
python tools/handoff/generate_catalog.py --check
python tools/handoff/validate_handoff.py --self-test
python tools/handoff/validate_handoff.py
python tools/handoff/export_bundle.py --all --check --verify-determinism
python tools/global-finalization/validate_global_finalization.py
```

The Python environment itself is standardized separately by issue #170.
