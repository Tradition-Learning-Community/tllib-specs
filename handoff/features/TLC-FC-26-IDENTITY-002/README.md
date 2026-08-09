# TLC-FC-26-IDENTITY-002 — Identity dissonance cost

This finalized conditional package exposes the exact source cost `Phi_id = ||R-X||² + lambda||grad R||² + mu||dR/dt-dX/dt||²`. Execution is permitted only when the caller supplies compatible dual-primal subtraction and norm semantics together with the required gradient and derivative values, and when `lambda > 0` and `mu > 0`.

The package never chooses a Riesz identification, norm, differentiation rule, discretization, or numerical solver. Missing geometry is a provider error rather than permission to complete the science silently.
