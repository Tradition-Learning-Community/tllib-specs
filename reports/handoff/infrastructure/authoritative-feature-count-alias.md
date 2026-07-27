# Authoritative feature-count alias

Some finalized domain inventories name their authoritative population total `authoritative_feature_count`. Progressive validation now accepts this established key alongside `feature_count` and `population_count`.

When multiple aliases are present, every declared value must equal the actual ordered feature population. Missing counts and conflicting or inaccurate values remain validation failures. No inventory, scientific artifact, package, schema, shared contract, or domain semantics is changed.
