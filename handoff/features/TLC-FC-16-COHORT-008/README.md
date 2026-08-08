# TLC-FC-16-COHORT-008 — Cohesion assessment

This package evaluates the Cohort cohesion index `kappa` from supplied Laplacian spectral values, Cohort size, and six typological proportions using the formula stated by the source. It may additionally report whether `kappa` belongs to an optimal interval only when `kappa_min` and `kappa_max` are supplied as opaque scientific values. The theory does not calibrate those bounds, so no implementation default is permitted.

The largest Laplacian eigenvalue must be nonzero for the source ratio to be defined. The implementation is conditionally executable, preserves all threshold provenance, and must never infer a “good cohesion” range from examples or from another domain.
