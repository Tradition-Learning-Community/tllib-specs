# Functional decomposition revision tools

`build_revision.py` applies only explicit classifications from the independent scientific review and regenerates the derived candidate artefacts. It does not read or write `maths/`.

`validate_revision.py` checks traceability, critical reclassification, dependency separation, boundary and oracle gates, variants, YAML structure, and forbidden-path changes.

`summarize_revision.py` prints the canonical counts from the generated decision record.

Run from the repository root:

```text
python tools/functional-decomposition-revision/build_revision.py
python tools/functional-decomposition-revision/validate_revision.py
python tools/functional-decomposition-revision/summarize_revision.py
```
