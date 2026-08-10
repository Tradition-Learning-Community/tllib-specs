# TLC-FC-27-REFLEXIVITY-003 — Adaptive self-correction right-hand side

This package evaluates only the source RHS `-grad_R Phi_id + eta(t) + zeta(t)(R*-R)` from supplied values. It preserves the negative gradient sign even though the coherent-identity operator uses a positive gradient term. `eta(t)` has no assumed distribution, `R*` is provider-supplied, and no trajectory integration is included.
