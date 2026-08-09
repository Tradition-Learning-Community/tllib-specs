# TLC-FC-22-TEMPORALITY-005 — Multiscale evolution right-hand sides

This finalized handoff evaluates the four source right-hand sides independently from caller-supplied `epsilon_i` values, `theta`-derived quantities, a supplied mnemonic value and external `F_i` providers. It returns derivatives only; it does not integrate the multiscale system and does not construct the mathematical spaces of `X`, `theta`, their gradients or the fields themselves.

The qualitative hierarchy `epsilon1 >> epsilon2 >> epsilon3 >> epsilon4` is preserved as externally supplied scientific evidence rather than converted into fabricated numerical ratios. The use of `M(X)` records Memory provenance without creating an undocumented runtime adapter.
