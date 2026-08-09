# TLC-FC-26-IDENTITY-005 — Subjective social identity right-hand side

This finalized conditional package preserves the subjective source RHS exactly: intrinsic `G_i`, the printed positive `alpha_i(R_i-X_i)` term, the printed positive `beta_i grad_Ri Phi_id` term, the `delta_ij(R_j-R_i)` peer sum, and the `zeta_i(t)(R_i* - R_i)` ideal-image term. All scientific values and incompatible-space arithmetic are supplied externally.

The implementation must not “correct” the source signs, choose a dual-primal identification, invent coefficients or gradients, or advance the ODE. Its responsibility ends at a source-faithful RHS value or a structured missing-provider error.
