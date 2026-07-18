#!/usr/bin/env python3
"""Print a concise summary of mathematical-contract entry preparation."""

from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]


def load(relative: str):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


features = load("registry/math-contract-entry/contractable-features.yaml")["features"]
dependencies = load("registry/math-contract-entry/contract-dependencies.yaml")["contract_dependencies"]
bases = load("registry/math-contract-entry/oracle-basis.yaml")["features"]
wave = load("registry/math-contract-entry/contract-wave-1.yaml")
counts = Counter(item["contract_entry_status"] for item in features)

for status in (
    "READY_FOR_MATH_CONTRACT",
    "READY_WITH_CONTRACT_RESERVATIONS",
    "REQUIRES_TARGETED_SOURCE_REVIEW",
    "REQUIRES_SCIENTIFIC_DECISION",
    "NOT_CONTRACTABLE_AS_FEATURE",
):
    print(f"{status}: {counts[status]}")
print(f"CONTRACT_WAVE_1: {wave['count']}")
print("SELECTED_FEATURES:")
for feature_id in wave["feature_ids"]:
    print(f"- {feature_id}")
print(f"CONTRACT_DEPENDENCY_RECORDS: {len(dependencies)}")
print(f"ORACLE_BASES_AVAILABLE: {len(bases)}")
print("READINESS: contract wave only; IR and implementation remain false")
