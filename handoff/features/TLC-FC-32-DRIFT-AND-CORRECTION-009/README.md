# TLC-FC-32-DRIFT-AND-CORRECTION-009 — Institutional rigidity index

This finalized handoff preserves `I_rig = (N_rules/N_rules^0) * (tau_decision/tau_decision^0) * (1 - A_adapt)` exactly. Zero values for either reference denominator are handled through structured guards rather than numerical regularization.

The source does not guarantee a bounded rigidity index, so this package performs no clamping or automatic normalization. Adaptation semantics and references remain supplied, and no hidden calibration engine is introduced.