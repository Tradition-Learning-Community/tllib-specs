# Contract validator

Run from the repository root:

```text
python tools/math-contracts/TLC-FC-02-COMMUNITY-001/validate_contract.py
```

The script requires PyYAML. It validates the authorized wave position, singleton feature/object scope, YAML readability, identifier and symbol references, traceability fields, dependency autonomy evidence, normalization status, implementation exclusions, and absence of an executable oracle. It performs structural validation only; it is not a scientific or executable oracle.
