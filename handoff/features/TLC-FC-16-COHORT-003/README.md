# TLC-FC-16-COHORT-003 — Hybrid typology mixture

This package hands off the source hybrid-profile operation. The implementation receives six representative pure-type vectors and six coefficients `alpha_i`; it validates that all coefficients are nonnegative and sum to one, then evaluates the source weighted sum. The source does not define the six type centers and does not choose between projection and supervised learning for coefficient estimation. Therefore this feature never estimates coefficients or representative type vectors; those values must be supplied by an external scientific provider.

The package is conditionally executable only for supplied type vectors and coefficients. All unresolved typology decisions remain explicit in traceability and acceptance behavior.
