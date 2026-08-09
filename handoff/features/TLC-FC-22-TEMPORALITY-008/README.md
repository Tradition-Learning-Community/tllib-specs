# TLC-FC-22-TEMPORALITY-008 — Raw temporal transition expression

This finalized handoff evaluates exactly the source expression `exp(-beta DeltaE_ij) / sum_k exp(-beta DeltaE_ik) * f(nabla_tau V)` using caller-supplied energy gaps, `beta` and the already supplied value of the modulation function `f`. The package calls the output a raw transition expression rather than a certified probability because the multiplicative factor may change total mass.

No regime energies, social temperature, modulation function, normalization or default candidate population is invented. The factor `f` is preserved exactly and any normalized-distribution semantics are delegated to the separate guard feature 009.
