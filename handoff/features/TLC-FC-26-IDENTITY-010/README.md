# TLC-FC-26-IDENTITY-010 — Identity coherence metric

This finalized conditional package evaluates the displayed coherence metric exactly: `C_id(t) = 1 - (||R-X|| + ||dR/dt-dX/dt||)/(||X|| + ||R|| + 1)`. The caller supplies compatible subtraction and norm semantics, so the package does not choose a dual-primal identification or a concrete geometry.

The source calls this an indicator between zero and one, but the displayed formula does not guarantee that range. Therefore the raw formula result is returned unchanged: no clamp, saturation, renormalization, or postcondition asserting `[0,1]` is permitted.
