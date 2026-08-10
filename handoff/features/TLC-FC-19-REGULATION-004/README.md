# TLC-FC-19-REGULATION-004 — 360-degree feedback expression

Evaluate `F_ij = W_f · Theta(X_i, X_j, Interactions_ij) + b_f` only from a provider-evaluated `Theta` value and supplied contraction compatibility. `Theta` is opaque: the implementation must not derive it from states or interactions, infer matrix dimensions, reshape inputs, or alter the affine source expression.
