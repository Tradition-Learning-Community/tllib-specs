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
- `catalog.json` indexes the packages currently compiled into this output.

Markdown is the human interface. JSON is the normative machine interface. JSON Schema validates structure. YAML remains an upstream pipeline format and is not part of the handoff interface.

## Scientific boundary

The handoff compiles observable obligations conservatively. It preserves unresolved or opaque scientific material explicitly, does not select an implementation language, and does not prescribe internal algorithms, storage, ownership models, serialization formats, performance bounds, or concurrency policies unless an authoritative source makes them observable requirements.

## Validation and export

`tools/handoff/validate_handoff.py` validates package structure, cross-file coherence, dependency resolution, traceability, and the pilot package. `tools/handoff/export_bundle.py` resolves one feature with all required shared contracts and emits a directory bundle plus `bundle-lock.json`; generated archives are not committed.

## Current scope

Version 1.0 establishes eight shared contracts and the pilot package `TLC-FC-00-MASTER-005`. The complete catalog of 166 feature packages is not yet finalized.
