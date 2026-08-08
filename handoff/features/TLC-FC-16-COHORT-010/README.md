# TLC-FC-16-COHORT-010 — Trait-distribution dynamics descriptor

This package preserves the source Fokker–Planck dynamics, the stated stationary-distribution relation, the potential term, and the convergence wording for Cohort trait distributions. It is deliberately structural-only. The theory does not specify the tensorial type of `Sigma`, boundary conditions, a spatial or temporal discretization, a time step, or a numerical PDE solver; the referenced peer-bifurcation spectral threshold is also absent.

A conforming implementation exposes a guarded descriptor and source provenance. It must reject requests to numerically evolve the distribution unless an external scientific solver contract supplies the missing choices. Euler, Runge–Kutta, finite differences, and any other method absent from the source are forbidden defaults.
