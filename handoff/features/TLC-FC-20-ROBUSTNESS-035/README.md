# TLC-FC-20-ROBUSTNESS-035 — Resilience index expression

This finalized package evaluates the source resilience index only from provider-supplied `sigma(R_syst)`, minimum derivative value, alignment efficiency, fidelity, gradient norms and state norms. `sigma(R_syst)=0`, `||E||=0`, and `||R||=0` are structured singularities. No variance estimator, derivative/minimum search, numerical differentiation, gradient estimator, trajectory inference, norm construction, smoothing, or epsilon repair is introduced.
