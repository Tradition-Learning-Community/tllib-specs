# TLC-FC-26-IDENTITY-003 — Identity health threshold assessment

This finalized conditional package evaluates only the source threshold semantics around `Phi_id` and caller-supplied `Phi_seuil`. A healthy identity is the strict case `Phi_id < Phi_seuil`; threshold exceeded is the strict case `Phi_id > Phi_seuil`. Equality remains an explicit boundary case because the chapter does not assign it to either side.

`Phi_seuil` is never calibrated or defaulted by this package. Absence of a threshold is a structured provider failure, preserving the scientific boundary rather than filling it with an arbitrary number.
