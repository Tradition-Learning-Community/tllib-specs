# TLC-FC-26-IDENTITY-004 — Objective social identity right-hand side

This finalized conditional package represents the exact objective-state right-hand side `dX_i/dt = F_i(X_i,R_i) + sum_{j != i} gamma_ij (X_j-X_i)`. `F_i`, peer states, coefficients, and compatible primal subtraction are supplied by the caller. The operation returns the right-hand side only; it does not advance the state in time.

The peer sum must exclude `j=i`, and no `gamma_ij` values are synthesized. The package selects no ODE solver, integration step, synchronization policy, or social-network model beyond the source-backed expression.
