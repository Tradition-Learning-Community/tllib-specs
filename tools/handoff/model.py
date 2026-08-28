"""Shared Feature Handoff Package v1.0 model metadata.

Population is intentionally loaded from the committed global catalog.  This
module exposes convenient derived values to the handoff tooling, but it is not a
second population authority: ``handoff/catalog.json`` is canonical.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "handoff" / "catalog.json"
PILOT_ID = "TLC-FC-00-MASTER-005"


def _load_catalog() -> dict[str, Any]:
    try:
        value = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeError("handoff/catalog.json is required as population authority") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid handoff/catalog.json: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError("handoff/catalog.json must contain a JSON object")
    return value


def _required_list(catalog: dict[str, Any], key: str) -> list[Any]:
    value = catalog.get(key)
    if not isinstance(value, list):
        raise RuntimeError(f"handoff/catalog.json {key!r} must be a list")
    return value


_CATALOG = _load_catalog()
_DOMAINS = _required_list(_CATALOG, "domains")
_FEATURES = _required_list(_CATALOG, "features")
_SHARED = _required_list(_CATALOG, "shared_contracts")

MODEL_VERSION = _CATALOG.get("model_version")
VALIDATOR_VERSION = (_CATALOG.get("validator") or {}).get("version")
EXPORTER_VERSION = (_CATALOG.get("exporter") or {}).get("version")
CATALOG_GENERATOR_VERSION = (_CATALOG.get("generation") or {}).get("version")
for name, value in (
    ("model_version", MODEL_VERSION),
    ("validator.version", VALIDATOR_VERSION),
    ("exporter.version", EXPORTER_VERSION),
    ("generation.version", CATALOG_GENERATOR_VERSION),
):
    if not isinstance(value, str) or not value:
        raise RuntimeError(f"handoff/catalog.json {name} must be a non-empty string")

DOMAIN_ORDER = tuple(
    row.get("domain") for row in _DOMAINS if isinstance(row, dict) and isinstance(row.get("domain"), str)
)
if len(DOMAIN_ORDER) != len(_DOMAINS) or len(DOMAIN_ORDER) != len(set(DOMAIN_ORDER)):
    raise RuntimeError("handoff/catalog.json contains invalid or duplicate domain identities")

FEATURE_IDS = tuple(
    row.get("feature_id")
    for row in _FEATURES
    if isinstance(row, dict) and isinstance(row.get("feature_id"), str)
)
if len(FEATURE_IDS) != len(_FEATURES) or len(FEATURE_IDS) != len(set(FEATURE_IDS)):
    raise RuntimeError("handoff/catalog.json contains invalid or duplicate feature identities")

SHARED_CONTRACT_IDS = frozenset(
    row.get("shared_contract_id")
    for row in _SHARED
    if isinstance(row, dict) and isinstance(row.get("shared_contract_id"), str)
)
if len(SHARED_CONTRACT_IDS) != len(_SHARED):
    raise RuntimeError("handoff/catalog.json contains invalid or duplicate shared contract identities")

# Compatibility names retained for existing tooling.  They are derived from the
# canonical catalog at the targeted commit and are therefore not governance
# constants.
EXPECTED_DOMAIN_COUNT = len(DOMAIN_ORDER)
EXPECTED_FEATURE_COUNT = len(FEATURE_IDS)
EXPECTED_SHARED_CONTRACT_COUNT = len(SHARED_CONTRACT_IDS)
