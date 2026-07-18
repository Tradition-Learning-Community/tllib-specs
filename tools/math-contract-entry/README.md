# Math contract entry tools

Run from the repository root:

```text
python tools/math-contract-entry/validate_contract_entry.py
python tools/math-contract-entry/summarize_contract_entry.py
```

The validator checks exact coverage of the 66 retained-with-reservations features, source and behavior presence, source-grounded oracle bases, justified minimal dependencies, first-wave exclusions, absence of executable-oracle claims, protected input paths, and YAML readability.

The summarizer reports classification totals, selected wave identifiers, dependency records, oracle bases, and downstream readiness. Neither tool generates contracts, tests, reference values, IR, or implementation artifacts.
