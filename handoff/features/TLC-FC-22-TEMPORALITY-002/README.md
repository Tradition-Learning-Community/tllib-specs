# TLC-FC-22-TEMPORALITY-002 — Temporal metric matrix

This finalized handoff evaluates only the exact 4×4 matrix written in `temporality.md` from caller-supplied scalar values. The fourth diagonal entry is deliberately `alpha4 * t3^3`; it must never be rewritten as a `t4` term. Matrix symmetry is structural, while positive definiteness is not certified by this feature because the source supplies no sufficient coefficient conditions.

No coefficient calibration, metric-distance construction, geometry, solver or runtime framework is selected. Implementations must preserve the exact source algebra and the scientific reservations referenced by this package.
