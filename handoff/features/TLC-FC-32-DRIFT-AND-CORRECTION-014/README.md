# TLC-FC-32-DRIFT-AND-CORRECTION-014 — Reset admissibility predicate

This finalized handoff evaluates a supplied reset candidate against exactly three simultaneous source conditions: projected distance to the original state is strictly `< epsilon_reset`, vitality strictly increases, and burden strictly decreases.

The feature does not generate `X'`, search for a candidate, optimize a reset, mutate state, or calibrate thresholds. Projection and norm semantics remain supplied/provider-backed, with domain 04 remaining the invariant authority and no dependency on Fidelity 35.