# TLC-FC-10-VIRTUES-010 — Essential-property indicator registration

## What is this feature?

A declarative structural operation that records essential-property categories and their opaque indicator, metric, and progression descriptors.

## What must be implemented?

Implement `REGISTER-ESSENTIAL-PROPERTY-INDICATORS`: validate the exact feature identity and provenance for `TLC-SO-VIRTUES-003` and `TLC-SO-VIRTUES-067`, preserve supplied categories and descriptors, propagate `scientific ambiguity`, and return a deterministic descriptor.

## Valid inputs and required output

The artifact may contain stability, developability, contextual flexibility, integration, measurability, indicators, and progression descriptors. Success returns supplied values unchanged; failure returns a named error and no accepted result.

## Mandatory and forbidden behavior

Category identity, presentation order, opaque descriptors, reservations, source order, and unresolved status must be preserved. Interpreting indicators, computing metrics or degrees, evaluating progression, deriving hierarchy, scoring, comparing, ranking, or inventing transitions is forbidden.

## Implementation freedom

Data structures, storage, ownership, serialization, and internal decomposition remain implementation-defined. Presentation order is preserved but is not a priority order.

## Errors and conformance

The public error aliases preserve the source identifiers. Conformance requires exact category round-trip, unresolved propagation, opacity, deterministic output, and atomic failure.

## Unresolved science

Indicator, metric, degree, and progression semantics remain `preserved_unresolved`; this package is not a progression engine.