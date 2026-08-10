# TLC-FC-21-FAIRNESS-013 — Alignment efficiency expression

Evaluate the source alignment-efficiency expression from supplied constraint values, derivatives, norms, alignment, and the declared constraint count `m`. The factor `1/m` makes `m = 0` invalid, so the package returns `AlignmentConstraintCountZero` rather than a fallback. Derivatives, gradients, norms, and constraint values remain providers; the package performs no numerical differentiation or calculus synthesis.
