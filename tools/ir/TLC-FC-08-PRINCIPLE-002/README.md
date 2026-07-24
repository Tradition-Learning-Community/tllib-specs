# TLC-FC-08-PRINCIPLE-002 IR validator

Run from the repository root:

```powershell
python tools/ir/TLC-FC-08-PRINCIPLE-002/validate_ir.py
```

The validator parses all candidate JSON and YAML artifacts, checks identifiers and provenance, validates node/port/edge references, confirms exact unresolved propagation and zero missing coverage, rejects unauthorized target-language or numerical choices, and requires `ready_for_code_generation: false`.

Compile-check the validator separately with:

```powershell
python -m py_compile tools/ir/TLC-FC-08-PRINCIPLE-002/validate_ir.py
```
