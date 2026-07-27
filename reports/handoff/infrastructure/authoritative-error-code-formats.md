# Authoritative error-code formats

Feature sources use two stable public error-code conventions: uppercase snake case and PascalCase. The feature contract schema now accepts exactly those two forms so handoff packages can preserve authoritative identifiers without renaming them.

The change does not alter any existing code, error meaning, package, shared contract, scientific artifact, or runtime transport. Codes must still begin with an uppercase letter and contain only ASCII letters, digits, and—only for the uppercase convention—underscores.
