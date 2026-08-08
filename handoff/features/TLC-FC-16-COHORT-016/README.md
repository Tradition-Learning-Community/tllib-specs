# TLC-FC-16-COHORT-016 — Type-pair interaction model

This package combines three source-defined interaction operations when all external scientific terms are supplied: logistic link probability `exp(theta_kl)/(1+exp(theta_kl))`, interaction efficiency `eta_base + alpha_kl*d_type + beta_kl*complementarity`, and the shape-compatible Hadamard performance matrix `Theta circle H`. The source does not construct `d_type` or complementarity and does not specify the dimensions or entry semantics of `Theta` and `H`.

The implementation therefore validates that every external term is supplied and that the two matrices have identical shapes, then evaluates only the stated formulas. It must not infer type geometry, complementarity, matrix dimensions, or matrix-entry meaning.
