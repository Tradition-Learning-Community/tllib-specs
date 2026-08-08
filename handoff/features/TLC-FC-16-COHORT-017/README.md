# TLC-FC-16-COHORT-017 — Cohort health assessment

This package evaluates the source Cohort-health product `kappa * H_type * expected_eta * synergy` and the four explicit alert predicates: diversity below supplied `H_min`, cohesion below supplied `kappa_min`, cohesion above supplied `kappa_max`, and negative synergy. The expected interaction efficiency and all alert thresholds are scientific inputs because the source does not calibrate them.

The source describes a healthy value as near one but does not provide a normalization that would justify that scale. The implementation must therefore return the raw unnormalized source product, must not create a “near one” healthy cutoff, and must emit alerts only from the four stated predicates.
