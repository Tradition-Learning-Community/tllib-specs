#!/usr/bin/env python3
"""Validate the phase-0 production registry for domains 16 through 35."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "registry/domain-progress/extension-16-35.yaml"
CATALOG_PATH = ROOT / "handoff/catalog.json"
EXPECTED_INDICES = set(range(16, 36))
EXPECTED_WAVES = {
    "pilot": {16},
    "wave-1": {22, 23, 24, 25, 26, 27},
    "wave-2": {18, 19, 20, 21, 32, 35},
    "wave-3": {28, 29, 30, 31},
    "wave-4": {17, 34},
    "wave-5": {33},
}
EXPECTED_ANALYSIS_GROUPS = {
    frozenset({22, 23}),
    frozenset({24, 25}),
    frozenset({26, 27}),
    frozenset({18, 19}),
    frozenset({20, 21}),
    frozenset({32, 35}),
    frozenset({29, 30, 31}),
}
DOWNSTREAM_STATES = (
    "functional_decomposition",
    "registries",
    "ir",
    "contracts",
    "algorithms",
    "oracles",
    "handoff_packages",
)
FUTURE_FEATURE_ID = re.compile(
    r"\bTLC-FC-(?:1[6-9]|2[0-9]|3[0-5])-[A-Z0-9-]+-[0-9]{3}\b"
)
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"YAML parse failed: {path.relative_to(ROOT)}: {exc}")
        return None


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"JSON parse failed: {path.relative_to(ROOT)}: {exc}")
        return None


def scan_catalog_for_future_publication(value, path: str = "catalog") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key == "domain_index" and child in EXPECTED_INDICES:
                fail(f"Future domain {child} is already published at {child_path}")
            scan_catalog_for_future_publication(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            scan_catalog_for_future_publication(child, f"{path}[{index}]")
    elif isinstance(value, str) and FUTURE_FEATURE_ID.search(value):
        fail(f"Future feature identifier already appears in handoff catalog at {path}: {value}")


manifest = load_yaml(MANIFEST_PATH)
if not isinstance(manifest, dict):
    fail("Extension manifest must be a YAML mapping")
    manifest = {}

if manifest.get("schema_version") != 1:
    fail("schema_version must be 1")

program = manifest.get("program", {})
if program.get("id") != "domains-16-35-extension":
    fail("Unexpected program id")
if program.get("strategy") != "vertical-domain-completion":
    fail("Program strategy must be vertical-domain-completion")
if program.get("publication_policy") != "complete-domain-only":
    fail("Program publication policy must be complete-domain-only")
if program.get("pilot_domain") != 16:
    fail("Pilot domain must be 16")

baseline = manifest.get("baseline", {})
if baseline.get("completed_domain_range") != "00-15":
    fail("Baseline completed domain range must be 00-15")
if baseline.get("published_domain_count") != 16:
    fail("Baseline published domain count must remain 16")
if baseline.get("published_feature_count") != 166:
    fail("Baseline published feature count must remain 166")
if baseline.get("stable_catalog") != "handoff/catalog.json":
    fail("Stable catalog must remain handoff/catalog.json")

domains = manifest.get("domains")
if not isinstance(domains, list):
    fail("domains must be a list")
    domains = []
if len(domains) != 20:
    fail(f"Expected 20 domains, found {len(domains)}")

indices = [domain.get("index") for domain in domains if isinstance(domain, dict)]
slugs = [domain.get("slug") for domain in domains if isinstance(domain, dict)]
if len(indices) != len(set(indices)):
    fail("Domain indices must be unique")
if len(slugs) != len(set(slugs)):
    fail("Domain slugs must be unique")
if set(indices) != EXPECTED_INDICES:
    fail(f"Domain coverage must be exactly 16-35, got {sorted(set(indices))}")

waves = manifest.get("waves")
if not isinstance(waves, list):
    fail("waves must be a list")
    waves = []
wave_domains: dict[str, set[int]] = {}
seen_wave_members: list[int] = []
manifest_analysis_groups: set[frozenset[int]] = set()
for wave in waves:
    if not isinstance(wave, dict):
        fail("Each wave must be a mapping")
        continue
    wave_id = wave.get("id")
    members = wave.get("domains", [])
    if wave_id in wave_domains:
        fail(f"Duplicate wave id: {wave_id}")
        continue
    if not isinstance(members, list):
        fail(f"Wave {wave_id} domains must be a list")
        continue
    member_set = set(members)
    if len(member_set) != len(members):
        fail(f"Wave {wave_id} contains a duplicate domain")
    wave_domains[wave_id] = member_set
    seen_wave_members.extend(members)
    for group in wave.get("analysis_groups", []):
        if not isinstance(group, list) or len(group) < 2:
            fail(f"Wave {wave_id} contains an invalid analysis group: {group}")
            continue
        manifest_analysis_groups.add(frozenset(group))

if wave_domains != EXPECTED_WAVES:
    fail(f"Wave membership differs from the canonical plan: {wave_domains}")
if set(seen_wave_members) != EXPECTED_INDICES or len(seen_wave_members) != 20:
    fail("Every domain index 16-35 must belong to exactly one wave")
if manifest_analysis_groups != EXPECTED_ANALYSIS_GROUPS:
    fail("Analysis groups differ from the canonical pair/group plan")

expected_companions: dict[int, set[int]] = {index: set() for index in EXPECTED_INDICES}
for group in EXPECTED_ANALYSIS_GROUPS:
    for member in group:
        expected_companions[member].update(group - {member})

for domain in domains:
    if not isinstance(domain, dict):
        fail("Each domain entry must be a mapping")
        continue
    index = domain.get("index")
    slug = domain.get("slug")
    label = f"domain {index} ({slug})"

    if index not in EXPECTED_INDICES:
        continue
    declared_wave = domain.get("wave")
    if declared_wave not in EXPECTED_WAVES or index not in EXPECTED_WAVES[declared_wave]:
        fail(f"{label}: inconsistent wave {declared_wave}")

    companions = domain.get("analysis_companions", [])
    if set(companions) != expected_companions[index]:
        fail(
            f"{label}: analysis companions must be "
            f"{sorted(expected_companions[index])}, got {sorted(companions)}"
        )

    readme = domain.get("scientific_readme")
    if not isinstance(readme, str) or not (ROOT / readme).is_file():
        fail(f"{label}: missing scientific README {readme}")

    sources = domain.get("scientific_sources")
    if not isinstance(sources, list) or not sources:
        fail(f"{label}: scientific_sources must be a non-empty list")
    else:
        for source in sources:
            if not isinstance(source, str) or not (ROOT / source).is_file():
                fail(f"{label}: missing scientific source {source}")

    if domain.get("feature_count") is not None:
        fail(f"{label}: feature_count must remain null before decomposition")
    if domain.get("handoff_publication") is not False:
        fail(f"{label}: handoff_publication must remain false")

    pipeline = domain.get("pipeline", {})
    if pipeline.get("scientific_source") != "complete":
        fail(f"{label}: scientific_source must be complete")
    for state in DOWNSTREAM_STATES:
        if pipeline.get(state) != "not_started":
            fail(f"{label}: downstream state {state} must remain not_started")

    dependencies = domain.get("dependencies", {})
    confirmed = dependencies.get("confirmed", [])
    provisional = dependencies.get("provisional", [])
    for dependency in [*confirmed, *provisional]:
        if not isinstance(dependency, int) or dependency < 0 or dependency > 35:
            fail(f"{label}: invalid dependency index {dependency}")
        if dependency == index:
            fail(f"{label}: self-dependency is not allowed")
    if set(confirmed) & set(provisional):
        fail(f"{label}: a dependency cannot be both confirmed and provisional")

manifest_text = MANIFEST_PATH.read_text(encoding="utf-8") if MANIFEST_PATH.is_file() else ""
future_ids = sorted(set(FUTURE_FEATURE_ID.findall(manifest_text)))
if future_ids:
    fail(f"Future feature identifiers must not be instantiated in phase 0: {future_ids}")

catalog = load_json(CATALOG_PATH)
if catalog is not None:
    scan_catalog_for_future_publication(catalog)

if errors:
    print("Domains 16-35 extension validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Domains 16-35 extension validation: PASS (20 domains, exact coverage 16-35)")
