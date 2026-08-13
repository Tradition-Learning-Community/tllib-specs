# TLC-FC-32-DRIFT-AND-CORRECTION-008 — Dogmatization index

This finalized handoff preserves the source expression `Delta_dog = 1 - (||epsilon||/||epsilon||_0) * (A_adapt/A_adapt^0)`. Both denominator references are guarded when zero, and required norm/adaptation values remain supplied inputs or providers.

The source explicitly does not guarantee that `Delta_dog` is bounded. This package therefore never clamps the result to `[0,1]`, converts it to a probability, adds numerical epsilon, or invents missing calibration assumptions.