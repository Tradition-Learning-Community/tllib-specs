# TLC-FC-26-IDENTITY-011 — Identity stability metric

This finalized conditional package preserves `S_id` as the source time-averaged integral of the velocity-mismatch norm weighted by `exp(-||grad c(t)||²/(2 sigma²))`. The caller supplies `T`, `sigma`, context-gradient and mismatch norm semantics, plus an exact or externally selected integration provider. This specification does not choose quadrature or discretization.

The source interpretation is preserved exactly: a lower `S_id` denotes stronger identity stability and a higher value denotes fragility. The package never reverses that orientation, invents `sigma`, or turns publication of Context into a runtime dependency.
