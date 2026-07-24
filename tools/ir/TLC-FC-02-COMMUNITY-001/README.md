# IR validator

Run from the repository root:

```text
python tools/ir/TLC-FC-02-COMMUNITY-001/validate_ir.py
```

The validator requires PyYAML. It checks JSON and YAML syntax, feature and source-commit identity, node/port/edge uniqueness and references, allowed node kinds and classifications, complete contract-element coverage, traceability, exact unresolved propagation, target-language and numerical-method exclusions, code-generation readiness, and single-feature scope. It is structural and does not constitute scientific validation.
