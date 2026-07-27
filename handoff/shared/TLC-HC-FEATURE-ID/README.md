# TLC-HC-FEATURE-ID

Defines the stable, opaque identifier carried by a handoff feature package.

The identifier is compared exactly. Implementations must not trim, case-fold, translate, decompose into scientific meaning, or treat a shared representation as evidence of aliasing. Storage, interning, binary layout, and allocation are implementation choices.

Normative behavior is defined by `contract.json` and `acceptance.json`.