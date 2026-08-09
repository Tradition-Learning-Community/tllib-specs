# TLC-FC-22-TEMPORALITY-006 — Inter-scale coupling aggregation

This finalized handoff preserves the source coupling `C_scale` as the sum over all declared scale pairs `i<j`. Derivatives and `gamma_ij` coefficients are caller-supplied, while the tensor product is delegated to an external provider because the source does not construct the state or tensor spaces needed to define it locally.

The feature performs only pairwise weighting and aggregation. It does not approximate derivatives, choose finite differences or automatic differentiation, construct tensor geometry, or calibrate coupling coefficients. Missing terms fail structurally rather than being synthesized.
