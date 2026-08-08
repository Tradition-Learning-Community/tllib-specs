# TLC-FC-16-COHORT-015 — Robustness functional descriptor

This package preserves the robustness functional stated by the Cohort source, including the minimization over perturbations, inverse gradient-norm term, coefficient `lambda`, and Hessian spectral-radius term. It is structural-only because the theory does not specify the admissible domain for `Delta p`, does not construct the gradient or Hessian provider, does not choose a minimizer, and does not calibrate `lambda`.

A conforming implementation exposes the source functional, provider references, and unresolved items as a guarded descriptor. Numeric robustness evaluation must fail with the declared external-evaluator requirement rather than selecting an optimizer, perturbation domain, differentiation scheme, or derivative construction absent from the theory.
