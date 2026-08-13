# Wave 3 dependency analysis

Baseline: `890bd7ab0822747aae5c8b9a49054609ef50d106`.

Confirmed scientific edges: `28 -> 04`, `29 -> 04`, `30 -> 04`, `30 -> 24`, `30 -> 29`, `31 -> 04`, `31 -> 29`. The `31 -> 24` relation remains unresolved because Institutionalization and Context use conflicting `tau_adapt` conventions.

Rejected: all other intra-Wave-3 edges, including any direct dependency between 30 and 31. Fidelity 35 and Drift 32 are not Wave-3 providers.

Locked publication order: `28 -> 29 -> 30 -> 31`.

No Wave-3 domain is published; global population remains 29 domains / 373 features / 8 shared contracts.