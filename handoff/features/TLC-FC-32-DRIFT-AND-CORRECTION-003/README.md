# TLC-FC-32-DRIFT-AND-CORRECTION-003 — Core-periphery classification

This finalized handoff preserves the diagnostic rule exactly: an element is in the core iff `kappa(e) > kappa_min`; equality and lower values are peripheral. The comparison remains strict and `kappa_min` is supplied rather than calibrated by this feature.

This diagnostic classification does not redefine or replace domain 04 Invariants. The package has no runtime domain dependency and does not create a scientific dependency on Fidelity 35.