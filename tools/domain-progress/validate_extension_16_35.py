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


def load_yaml(path: Path, errors: list[str]):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"YAML parse failed: {path.relative_to(ROOT)}: {exc}")
        return None


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON parse failed: {path.relative_to(ROOT)}: {exc}")
        return None


def validate_global_catalog(catalog, errors: list[str]) -> None:
    """Reject publication of any domain or feature from the reserved 16-35 range."""
    if not isinstance(catalog, dict):
        errors.append("handoff/catalog.json must contain a JSON object")
        return

    domains = catalog.get("domains")
    if not isinstance(domains, list):
        errors.append("handoff/catalog.json domains must be a list")
    else:
        for position, domain in enumerate(domains):
            path = f"catalog.domains[{position}]"
            if not isinstance(domain, dict):
                errors.append(f"{path} must be an object")
                continue
            domain_index = domain.get("domain_index")
            if isinstance(domain_index, bool) or not isinstance(domain_index, int):
                errors.append(f"{path}.domain_index must be an integer")
                continue
            if domain_index in EXPECTED_INDICES:
                errors.append(
                    f"Future domain {domain_index} is already published at {path}.domain_index"
                )

    features = catalog.get("features")
    if not isinstance(features, list):
        errors.append("handoff/catalog.json features must be a list")
    else:
        for position, feature in enumerate(features):
            path = f"catalog.features[{position}]"
            if not isinstance(feature, dict):
                errors.append(f"{path} must be an object")
                continue
            feature_id = feature.get("feature_id")
            if not isinstance(feature_id, str):
                errors.append(f"{path}.feature_id must be a string")
                continue
            if FUTURE_FEATURE_ID.fullmatch(feature_id):
                errors.append(f"Future feature identifier is already published at {path}: {feature_id}")

    summary = catalog.get("summary")
    if not isinstance(summary, dict):
        errors.append("handoff/catalog.json summary must be an object")
    else:
        if summary.get("domain_count") != 16:
            errors.append("Global handoff catalog domain_count must remain 16 during phase 0")
        if summary.get("feature_count") != 166:
            errors.append("Global handoff catalog feature_count must remain 166 during phase 0")


def print_failure(errors: list[str]) -> int:
    print("Domains 16-35 extension validation: FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


def main() -> int:
    errors: list[str] = []
    manifest = load_yaml(MANIFEST_PATH, errors)
    if manifest is None:
        return print_failure(errors)
    if not isinstance(manifest, dict):
        errors.append("Extension manifest must be a YAML mapping")
        return print_failure(errors)

    if manifest.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    program = manifest.get("program")
    if not isinstance(program, dict):
        errors.append("program must be a mapping")
    else:
        if program.get("id") != "domains-16-35-extension":
            errors.append("Unexpected program id")
        if program.get("strategy") != "vertical-domain-completion":
            errors.append("Program strategy must be vertical-domain-completion")
        if program.get("publication_policy") != "complete-domain-only":
            errors.append("Program publication policy must be complete-domain-only")
        if program.get("pilot_domain") != 16:
            errors.append("Pilot domain must be 16")

    baseline = manifest.get("baseline")
    if not isinstance(baseline, dict):
        errors.append("baseline must be a mapping")
    else:
        if baseline.get("completed_domain_range") != "00-15":
            errors.append("Baseline completed domain range must be 00-15")
        if baseline.get("published_domain_count") != 16:
            errors.append("Baseline published domain count must remain 16")
        if baseline.get("published_feature_count") != 166:
            errors.append("Baseline published feature count must remain 166")
        if baseline.get("stable_catalog") != "handoff/catalog.json":
            errors.append("Stable catalog must remain handoff/catalog.json")

    domains = manifest.get("domains")
    if not isinstance(domains, list):
        errors.append("domains must be a list")
        return print_failure(errors)
    if len(domains) != 20:
        errors.append(f"Expected 20 domains, found {len(domains)}")

    typed_domains: list[dict] = []
    indices: list[int] = []
    slugs: list[str] = []
    for position, domain in enumerate(domains):
        if not isinstance(domain, dict):
            errors.append(f"domains[{position}] must be a mapping")
            continue
        typed_domains.append(domain)
        index = domain.get("index")
        slug = domain.get("slug")
        if isinstance(index, bool) or not isinstance(index, int):
            errors.append(f"domains[{position}].index must be an integer")
        else:
            indices.append(index)
        if not isinstance(slug, str) or not slug:
            errors.append(f"domains[{position}].slug must be a non-empty string")
        else:
            slugs.append(slug)

    if len(indices) != len(set(indices)):
        errors.append("Domain indices must be unique")
    if len(slugs) != len(set(slugs)):
        errors.append("Domain slugs must be unique")
    if set(indices) != EXPECTED_INDICES:
        errors.append(f"Domain coverage must be exactly 16-35, got {sorted(set(indices))}")

    waves = manifest.get("waves")
    if not isinstance(waves, list):
        errors.append("waves must be a list")
        return print_failure(errors)

    wave_domains: dict[str, set[int]] = {}
    seen_wave_members: list[int] = []
    manifest_analysis_groups: set[frozenset[int]] = set()
    for position, wave in enumerate(waves):
        if not isinstance(wave, dict):
            errors.append(f"waves[{position}] must be a mapping")
            continue
        wave_id = wave.get("id")
        members = wave.get("domains")
        if not isinstance(wave_id, str) or not wave_id:
            errors.append(f"waves[{position}].id must be a non-empty string")
            continue
        if wave_id in wave_domains:
            errors.append(f"Duplicate wave id: {wave_id}")
            continue
        if not isinstance(members, list) or any(
            isinstance(member, bool) or not isinstance(member, int) for member in members
        ):
            errors.append(f"Wave {wave_id} domains must be a list of integers")
            continue
        member_set = set(members)
        if len(member_set) != len(members):
            errors.append(f"Wave {wave_id} contains a duplicate domain")
        wave_domains[wave_id] = member_set
        seen_wave_members.extend(members)

        groups = wave.get("analysis_groups", [])
        if not isinstance(groups, list):
            errors.append(f"Wave {wave_id} analysis_groups must be a list")
            continue
        for group in groups:
            if (
                not isinstance(group, list)
                or len(group) < 2
                or any(isinstance(member, bool) or not isinstance(member, int) for member in group)
            ):
                errors.append(f"Wave {wave_id} contains an invalid analysis group: {group}")
                continue
            manifest_analysis_groups.add(frozenset(group))

    if wave_domains != EXPECTED_WAVES:
        errors.append(f"Wave membership differs from the canonical plan: {wave_domains}")
    if set(seen_wave_members) != EXPECTED_INDICES or len(seen_wave_members) != 20:
        errors.append("Every domain index 16-35 must belong to exactly one wave")
    if manifest_analysis_groups != EXPECTED_ANALYSIS_GROUPS:
        errors.append("Analysis groups differ from the canonical pair/group plan")

    expected_companions: dict[int, set[int]] = {index: set() for index in EXPECTED_INDICES}
    for group in EXPECTED_ANALYSIS_GROUPS:
        for member in group:
            expected_companions[member].update(group - {member})

    for domain in typed_domains:
        index = domain.get("index")
        slug = domain.get("slug")
        label = f"domain {index} ({slug})"
        if isinstance(index, bool) or not isinstance(index, int) or index not in EXPECTED_INDICES:
            continue

        declared_wave = domain.get("wave")
        if declared_wave not in EXPECTED_WAVES or index not in EXPECTED_WAVES[declared_wave]:
            errors.append(f"{label}: inconsistent wave {declared_wave}")

        companions = domain.get("analysis_companions")
        if not isinstance(companions, list) or any(
            isinstance(companion, bool) or not isinstance(companion, int) for companion in companions
        ):
            errors.append(f"{label}: analysis_companions must be a list of integers")
        elif set(companions) != expected_companions[index]:
            errors.append(
                f"{label}: analysis companions must be "
                f"{sorted(expected_companions[index])}, got {sorted(companions)}"
            )

        scientific_directory = domain.get("scientific_directory")
        if not isinstance(scientific_directory, str) or not (ROOT / scientific_directory).is_dir():
            errors.append(f"{label}: missing scientific directory {scientific_directory}")

        readme = domain.get("scientific_readme")
        if not isinstance(readme, str) or not (ROOT / readme).is_file():
            errors.append(f"{label}: missing scientific README {readme}")

        sources = domain.get("scientific_sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{label}: scientific_sources must be a non-empty list")
        else:
            for source in sources:
                if not isinstance(source, str) or not (ROOT / source).is_file():
                    errors.append(f"{label}: missing scientific source {source}")

        if domain.get("feature_count") is not None:
            errors.append(f"{label}: feature_count must remain null before decomposition")
        if domain.get("handoff_publication") is not False:
            errors.append(f"{label}: handoff_publication must remain false")

        pipeline = domain.get("pipeline")
        if not isinstance(pipeline, dict):
            errors.append(f"{label}: pipeline must be a mapping")
        else:
            if pipeline.get("scientific_source") != "complete":
                errors.append(f"{label}: scientific_source must be complete")
            for state in DOWNSTREAM_STATES:
                if pipeline.get(state) != "not_started":
                    errors.append(f"{label}: downstream state {state} must remain not_started")

        dependencies = domain.get("dependencies")
        if not isinstance(dependencies, dict):
            errors.append(f"{label}: dependencies must be a mapping")
            continue
        confirmed = dependencies.get("confirmed")
        provisional = dependencies.get("provisional")
        if not isinstance(confirmed, list) or any(
            isinstance(item, bool) or not isinstance(item, int) for item in confirmed
        ):
            errors.append(f"{label}: dependencies.confirmed must be a list of integers")
            confirmed = []
        if not isinstance(provisional, list) or any(
            isinstance(item, bool) or not isinstance(item, int) for item in provisional
        ):
            errors.append(f"{label}: dependencies.provisional must be a list of integers")
            provisional = []
        for dependency in [*confirmed, *provisional]:
            if dependency < 0 or dependency > 35:
                errors.append(f"{label}: invalid dependency index {dependency}")
            if dependency == index:
                errors.append(f"{label}: self-dependency is not allowed")
        if set(confirmed) & set(provisional):
            errors.append(f"{label}: a dependency cannot be both confirmed and provisional")

    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")
    future_ids = sorted(set(FUTURE_FEATURE_ID.findall(manifest_text)))
    if future_ids:
        errors.append(f"Future feature identifiers must not be instantiated in phase 0: {future_ids}")

    catalog = load_json(CATALOG_PATH, errors)
    if catalog is None:
        return print_failure(errors)
    validate_global_catalog(catalog, errors)

    if errors:
        return print_failure(errors)

    print("Domains 16-35 extension validation: PASS (20 domains, exact coverage 16-35)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
