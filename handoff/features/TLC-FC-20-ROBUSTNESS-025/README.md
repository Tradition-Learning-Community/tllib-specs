# TLC-FC-20-ROBUSTNESS-025 — Faithful context expression

This finalized package evaluates `c_T=c_inv+alpha(env)c_spec+beta(env)grad_T c` from supplied components, coefficients and gradient, while preserving the source norm and fidelity constraints as supplied assessments. It does not construct gradients, norms, thresholds, environment coefficients, contexts, or fidelity measures, and it does not solve any adaptation dynamics.
