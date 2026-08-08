# TLC-FC-16-COHORT-009 — Trait drift field

This package implements the source drift field for a supplied trait profile: attraction toward the supplied Master profile plus the supplied expected peer-profile displacement, scaled by caller-provided coefficients `alpha` and `beta`. All profile dimensions must be compatible. The mathematical result is fully specified once those inputs are present; the source does not calibrate the coefficients, so the implementation may not choose values for them.

The scientific dependency on Master is explicit because the source formula names `mu_M`; the dependency on Disciple is explicit because the evolving state is a Disciple trait profile. These are scientific references only and do not create a runtime package dependency.
