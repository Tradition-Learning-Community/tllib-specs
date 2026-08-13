# TLC-FC-32-DRIFT-AND-CORRECTION-001 — Core diagnostic aggregate score

This finalized handoff preserves the source definition of `kappa(e)` as the exact unweighted `1/5` mean of the five supplied components. It does not normalize, clamp, reweight, or infer that the components or the aggregate belong to `[0,1]`.

`kappa_supp` remains provider-bound and undefined by the chapter. Domain 04 Invariants remains the scientific authority for invariants; this package creates no runtime dependency on 04 or Fidelity 35 and no `32 -> 35` dependency.