# TLC-FC-19-REGULATION-016 — Negative-A convergence contradiction guard

Structural guard preserving the source contradiction. With `e = X-X_ideal` and the source term `dX/dt = A(X_ideal-X)+...`, the homogeneous error term is `de/dt = -A e`; a negative-definite `A` therefore makes `-A` positive and repulsive. The package preserves both source statements and blocks convergence certification without authoritative resolution. It never changes either sign or substitutes positive definiteness.
