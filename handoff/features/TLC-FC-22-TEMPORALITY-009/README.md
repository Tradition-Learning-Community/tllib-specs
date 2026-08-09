# TLC-FC-22-TEMPORALITY-009 — Transition distribution certification guard

This finalized structural guard preserves the source warning that multiplying the Boltzmann-like ratio by `f(nabla_tau V)` may prevent transition expressions from summing to one. No additional normalization rule is given. Consequently the feature refuses local normalization and refuses to certify the raw expression as a probability distribution unless an external scientific normalization rule is supplied.

The guard never removes `f`, rescales the source expression, assumes unit mass or invents a probabilistic interpretation. It separates safe structural handling from feature 008, which computes only the raw source algebra.
