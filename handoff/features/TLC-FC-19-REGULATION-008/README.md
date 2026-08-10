# TLC-FC-19-REGULATION-008 — Coupled X right-hand side

Evaluate only the source RHS `A(t)(X_ideal-X)+B(t)F+C(t)R+D(t) grad E_context+Sigma(t) epsilon(t)` from supplied compatible operands. Preserve `X_ideal-X` exactly. Do not infer dimensions, construct gradients, sample a perturbation distribution, repair the sign of `A`, or integrate an ODE.
