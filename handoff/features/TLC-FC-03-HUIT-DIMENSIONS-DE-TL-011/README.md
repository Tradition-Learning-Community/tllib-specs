# TLC-FC-03-HUIT-DIMENSIONS-DE-TL-011 — Riemannian metric declaration

Implement a pure structural operation that registers the opaque Riemannian metric claim identified by `TLC-SO-HUIT-DIMENSIONS-DE-TL-093`. Return an immutable `RiemannianMetricDeclaration` preserving the source claim, trace, nine unresolved identifiers, and `TLC-EA-HUIT-011-001`.

The fields `metric_tensor`, `carrier_space`, `geodesic_operation`, feature boundary, and identity remain unresolved. No tensor, coordinate system, topology, dimension, metric value, distance, path, or geodesic may be computed or accepted as resolved semantics.

Do not mutate input, infer a concrete carrier or tensor, execute geodesics, or publish partial success. Language, storage, ownership, allocation, serialization, concurrency, and internal decomposition remain free. Conformance requires all tests in `acceptance.json`; scientific metric semantics remain deferred.
