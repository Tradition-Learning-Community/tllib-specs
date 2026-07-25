# Specialized limited engineering contract — TLC-FC-04-INVARIANTS-003

- Responsibility: Build a catalogue of source-declared invariants and equation fragments without deciding whether any invariant holds.
- Callable: `build_invariant_declaration_catalog`
- Input: `InvariantDeclarationEvidence[]`
- Output: `InvariantDeclarationCatalog`
- Observable effect: Returns a catalogue whose entries preserve declaration IDs, object types, source scopes, and linked evidence relations.
- Reference Python ready: yes
- C++ prototype ready: yes
- Scientific reservations: preserved
