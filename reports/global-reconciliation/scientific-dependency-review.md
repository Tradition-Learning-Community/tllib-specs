# Targeted scientific dependency and cycle review

- Authority: `origin/main`
- Source commit: `febec3e14a938adb2480bd09d257e6879ccf564e`
- Dependencies reviewed: 156
- Explicitly confirmed: 9
- Documentary references only: 20
- Compatible but unconfirmed: 30
- Ambiguous: 72
- Human decisions required: 25

## Cycles

- `TLC-GCYCLE-DOMAIN-001`: `ambiguous_cycle`; human classification is required before full contract or IR ordering.
- `TLC-GCYCLE-DOMAIN-002`: `documentary_non_blocking`; Master/Community symbol references do not import execution.

## Pilots

All four pilot contracts remain `to_revise`. All four pilot IRs remain `pilot_only`. None is promoted.

## Targeted readiness and first batch

Six affected features were recalculated. Two are ready for limited contracts, none for a full contract,
and none for IR. The economic first batch contains `TLC-FC-15-RELATIONS-004` and
`TLC-FC-15-RELATIONS-007`. The safest batch contains only `TLC-FC-15-RELATIONS-004`.
