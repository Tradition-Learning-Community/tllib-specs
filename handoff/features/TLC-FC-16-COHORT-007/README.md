# TLC-FC-16-COHORT-007 — Weighted graph topology metrics

This package hands off the graph formulas explicitly stated for Cohort: weighted degree from adjacency row sums, diagonal degree matrix, Laplacian `L=D-A`, the strict non-fragmentation test `lambda_2(L)>0`, and diameter as the maximum of supplied graph-distance values. The source does not define how graph distance `d(u,v)` is constructed from edge weights, so the implementation must receive compatible graph distances rather than selecting a shortest-path or edge-weight interpretation.

An implementation may use an implementation-defined linear-algebra routine to obtain the Laplacian spectrum because the scientific result is the stated eigenvalue condition; it must not invent graph semantics that change the source contract.
