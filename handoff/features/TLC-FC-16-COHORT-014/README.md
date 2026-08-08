# TLC-FC-16-COHORT-014 — Synergy emergence conditions

This package evaluates the three emergence inequalities stated by the source: `H_type > H_crit`, `kappa_min < kappa < kappa_max`, and supplied expected complementarity greater than supplied `theta_comp`. Every threshold and the complementarity expectation are scientific inputs because the theory does not calibrate them or construct the complementarity function.

The result is the conjunction of the three strict source conditions. A conforming implementation preserves inequality direction exactly, rejects missing thresholds or complementarity values, and never infers a diversity optimum, a cohesion interval, or a complementarity cutoff from examples, another domain, or implementation convenience.
