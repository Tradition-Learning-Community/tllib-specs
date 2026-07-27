# TLC-FC-01-DISCIPLE-008 — Structural operator

This package preserves the Disciple operator references and emits a deterministic, non-executable operator descriptor. Any request to apply the operator is refused with `DISCIPLE_UNRESOLVED_OPERATION`.

No state transition, input schema, output schema, type, dimension, or updated state value is invented. Normative behavior is in `contract.json` and `acceptance.json`; evidence is in `traceability.json`.
