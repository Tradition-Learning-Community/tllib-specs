# TLC-FC-20-ROBUSTNESS-017 — Guidance proportional posterior descriptor

This finalized structural package preserves the source proportionality `P(P|O,G,T) ∝ ...`. No normalizing constant is supplied by the source, so the package must not complete Bayes, normalize weights, estimate KL divergence, build distributions, infer priors, or reinterpret the proportional expression as a normalized posterior. It remains a raw proportional score/descriptor.
