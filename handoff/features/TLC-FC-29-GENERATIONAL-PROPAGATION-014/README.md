# Erosion-rate expression evaluator

Finalized Feature Handoff Package v1.0 for domain 29 Generational Propagation. This conditionally executable package evaluates d=(1-Q_rep)(1-R_auto)(1+kappa||grad E||) only from supplied final operands. R_auto and grad_E_norm remain external providers. The implementation must not construct providers, normalize terms, or repair the unresolved time consistency between Q_rep(t) and the erosion law.
