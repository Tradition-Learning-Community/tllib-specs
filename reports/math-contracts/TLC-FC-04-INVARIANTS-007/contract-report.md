# Specialized limited engineering contract — TLC-FC-04-INVARIANTS-007

- Responsibility: Construct the source-backed disintegration-relation record linking its evidence object to the invariant root.
- Callable: `construct_disintegration_relation`
- Input: `RelationEndpointsAndEvidence`
- Output: `DisintegrationRelationRecord`
- Observable effect: Returns one immutable refers_to edge with source, target, relation ID, and evidence reference preserved.
- Reference Python ready: yes
- C++ prototype ready: yes
- Scientific reservations: preserved
