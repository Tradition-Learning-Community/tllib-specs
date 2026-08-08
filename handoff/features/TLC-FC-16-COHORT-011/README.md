# TLC-FC-16-COHORT-011 — Typological composition dynamics

This package implements the six coupled right-hand sides for typological proportions exactly as written by the Cohort source. The caller supplies the current proportions, the `alpha_i`, `beta_ij`, `gamma_i` coefficients, and the external `eta_i(t)` values; the implementation validates compatible six-type shapes and returns `dp_i/dt` for each type. The cross-type sum excludes `j=i` as stated.

The feature does not advance time. The source provides no Euler, Runge–Kutta, adaptive stepping, or other integration prescription, so a conforming implementation returns only the instantaneous right-hand side and never fabricates a future state or calibrates the supplied parameters.
