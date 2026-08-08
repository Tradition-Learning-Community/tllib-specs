"""Shared immutable constants for Feature Handoff Package v1.0 tooling.

This module contains model identity and population constants only. It performs no
validation and is not a second CLI or authority.
"""

from __future__ import annotations

MODEL_VERSION = "1.0.0"
VALIDATOR_VERSION = "1.0.0"
EXPORTER_VERSION = "1.0.0"
CATALOG_GENERATOR_VERSION = "1.0.0"
EXPECTED_DOMAIN_COUNT = 17
EXPECTED_FEATURE_COUNT = 183
EXPECTED_SHARED_CONTRACT_COUNT = 8
PILOT_ID = "TLC-FC-00-MASTER-005"

DOMAIN_ORDER = (
    "master",
    "disciple",
    "community",
    "huit-dimensions",
    "invariants",
    "dynamics",
    "theorems",
    "message",
    "principle",
    "values",
    "virtues",
    "capacities",
    "competencies",
    "practice",
    "lived-experience",
    "relations",
    "cohort",
)

SHARED_CONTRACT_IDS = frozenset(
    {
        "TLC-HC-FEATURE-ID",
        "TLC-HC-SCIENTIFIC-REFERENCE",
        "TLC-HC-REFERENCE-COLLECTION",
        "TLC-HC-UNRESOLVED-ITEM",
        "TLC-HC-OPAQUE-VALUE",
        "TLC-HC-STRUCTURED-ERROR",
        "TLC-HC-TRACEABILITY",
        "TLC-HC-DESCRIPTOR-ENVELOPE",
    }
)
