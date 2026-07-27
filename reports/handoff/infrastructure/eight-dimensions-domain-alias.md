# Eight Dimensions domain identifier normalization

The authoritative feature identifiers use the token `HUIT-DIMENSIONS-DE-TL`, while the authoritative domain registry and package namespace use `huit-dimensions`.

The handoff validator compatibility entry point normalizes a trailing `-de-tl` identifier token only when the corresponding authoritative `registry/domain-finalization/<normalized-domain>/` directory exists. This preserves strict index, inventory, package-path, ownership, and artifact checks while avoiding a lexical false negative.

The compatibility entry point also accepts the established non-scientific inventory count keys `feature_count`, `population_count`, `active_feature_count`, and `summary.active_features`. Every count that is present must equal the exact authoritative feature-list cardinality; no scientific status or feature identity is changed.
