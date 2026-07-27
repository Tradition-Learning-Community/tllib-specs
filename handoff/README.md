# Feature Handoff Package v1.0

The `handoff/` tree is the final, language-independent output of the `tllib-specs` specification pipeline. It is intended for implementers who should not need to read mathematical contracts, intermediate representations, algorithm YAML, or scientific source prose during ordinary implementation work.

## Authority order

When two package files appear to differ, apply this order from highest to lowest authority:

1. `contract.json`
2. `acceptance.json`
3. referenced shared contracts
4. `manifest.json`
5. `README.md`
6. `examples.json`
7. `traceability.json`

A README or example cannot create an obligation absent from the normative JSON files.

## Package model

- `schemas/` defines the machine-validatable v1.0 structures.
- `shared/` contains reusable, versioned structural contracts.
- `features/` contains autonomous feature packages.
- `domains/<domain-slug>/catalog.json` declares a complete domain population when that domain is compiled.
- `catalog.json` remains the foundation-level catalog until global integration.

Markdown is the human interface. JSON is the normative machine interface. JSON Schema validates structure. YAML remains an upstream pipeline format and is not part of the handoff interface.

## Progressive domain validation

The foundation pilot `TLC-FC-00-MASTER-005` is always required. Domain compilation is progressive: no domain catalog is required for the foundation alone, but every catalog that is present is authoritative for its complete local population.

For each directory under `handoff/domains/`, `catalog.json` must conform to `schemas/domain-catalog.schema.json`. It must list every package for that domain in authoritative order, point to `handoff/features/<feature-id>`, declare the exact union of shared dependencies used by those packages, and reference `registry/domain-finalization/<domain-slug>/feature-status.yaml` as its authoritative inventory.

The validator computes the expected feature population as:

```text
{TLC-FC-00-MASTER-005} union all feature IDs declared by present domain catalogs
```

That computed population must exactly equal the directories under `handoff/features/`. Therefore:

- a complete Master catalog may coexist with no Disciple catalog;
- a later Disciple catalog becomes mandatory only when Disciple is introduced;
- a declared but missing package is rejected;
- an undeclared package is rejected;
- duplicate feature ownership across domains is rejected;
- a partial domain catalog is rejected;
- the pilot-specific identity, status, reference, error, strategy, and acceptance checks remain active.

## Scientific boundary

The handoff compiles observable obligations conservatively. It preserves unresolved or opaque scientific material explicitly, does not select an implementation language, and does not prescribe internal algorithms, storage, ownership models, serialization formats, performance bounds, or concurrency policies unless an authoritative source makes them observable requirements.

## Validation and export

`tools/handoff/validate_handoff.py` validates package structure, cross-file coherence, progressive population, authoritative domain inventories, dependency resolution, traceability, and the pilot package. Its `--self-test` mode exercises the logical foundation, completeness, orphan, collision, progressive-domain, and altered-pilot scenarios. `tools/handoff/export_bundle.py` resolves one feature with all required shared contracts and emits a directory bundle plus `bundle-lock.json`; generated archives are not committed.

## Current scope

Version 1.0 establishes eight shared contracts and the pilot package `TLC-FC-00-MASTER-005`. The complete catalog of 166 feature packages is not yet finalized, and domains may be integrated independently only as complete catalog-declared populations.
