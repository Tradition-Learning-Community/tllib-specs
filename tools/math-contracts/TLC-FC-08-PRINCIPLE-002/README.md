# TLC-FC-08-PRINCIPLE-002 contract validator

Run from the repository root:

```text
python tools/math-contracts/TLC-FC-08-PRINCIPLE-002/validate_contract.py
```

The validator is read-only. It checks YAML parsing, wave selection and position, single-feature scope, required artifacts, identifiers, scientific object references, symbol/equation references, exact preservation of the authorized equation, traceability, unresolved markers, forbidden implementation choices, and absence of an executable oracle. It requires PyYAML and does not execute scientific or numerical code.
