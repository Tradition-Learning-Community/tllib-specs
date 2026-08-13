# TLC-FC-32-DRIFT-AND-CORRECTION-002 — Resistance-to-change expression

This finalized handoff preserves exactly `kappa_res(e) = 1 - ||Delta e|| / ||Delta e||_max`, including the subtraction sign. The norm is provider-backed, and a zero reference denominator is a structured error rather than an epsilon repair, clamp, or silent NaN.

The package performs no norm construction, calibration, or normalization. It introduces no Fidelity 35 dependency and does not replace the domain-04 invariant model.