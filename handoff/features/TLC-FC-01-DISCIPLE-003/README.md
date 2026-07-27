# TLC-FC-01-DISCIPLE-003 — Deferred dynamics

This package preserves the unresolved Disciple evolution operation as a deterministic, non-executable descriptor. It may prepare and expose the deferred operation, but every scientific execution request is refused with `DISCIPLE_UNRESOLVED_OPERATION`.

No differential or stochastic equation, solver, step size, type, dimension, trajectory, or numerical result is selected. Normative behavior is in `contract.json` and `acceptance.json`; evidence is in `traceability.json`.
