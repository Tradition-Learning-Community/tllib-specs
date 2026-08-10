# TLC-FC-19-REGULATION-011 — Adaptive A right-hand side

Evaluate exactly `dA/dt = eta_A (X_ideal-X) X^T - lambda_A A + mu_A(A_opt-A)` using supplied transpose, `A_opt`, and shape-compatibility evidence. Preserve every source sign. Do not infer dimensions, integrate the learning equation, project `A` for stability, or repair the negative-`A` convergence contradiction.
