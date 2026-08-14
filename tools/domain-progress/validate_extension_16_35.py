#!/usr/bin/env python3
"""Validate progressive publication state for domains 16 through 35."""

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
ALLOWED_PUBLISHED_EXTENSION_INDICES = {16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 32, 35}
BASELINE_DOMAIN_COUNT = 16
BASELINE_FEATURE_COUNT = 166
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
PUBLISHED_REQUIRED_COMPLETE = (
    "functional_decomposition",
    "registries",
    "ir",
    "contracts",
    "oracles",
    "handoff_packages",
)
FEATURE_ID = re.compile(r"^TLC-FC-(?P<index>\d{2})-(?P<slug>[A-Z0-9-]+)-(?P<number>\d{3})$")


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


def slug_token(slug: str) -> str:
    return slug.upper().replace("_", "-")


def feature_population_from_status(path: Path, errors: list[str]) -> list[str]:
    data = load_yaml(path, errors)
    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(ROOT)} must contain a YAML mapping")
        return []
    features = data.get("features")
    if not isinstance(features, list):
        errors.append(f"{path.relative_to(ROOT)} features must be a list")
        return []
    ids: list[str] = []
    for position, feature in enumerate(features):
        if not isinstance(feature, dict) or not isinstance(feature.get("feature_id"), str):
            errors.append(f"{path.relative_to(ROOT)} features[{position}] must expose feature_id")
            continue
        ids.append(feature["feature_id"])
    declared = data.get("authoritative_feature_count")
    if declared is not None and declared != len(ids):
        errors.append(
            f"{path.relative_to(ROOT)} authoritative_feature_count={declared} does not match {len(ids)} features"
        )
    return ids


def validate_feature_ids(index: int, slug: str, ids: list[str], label: str, errors: list[str]) -> None:
    expected_prefix = f"TLC-FC-{index:02d}-{slug_token(slug)}-"
    if len(ids) != len(set(ids)):
        errors.append(f"{label}: feature identifiers must be unique")
    for feature_id in ids:
        match = FEATURE_ID.fullmatch(feature_id)
        if match is None:
            errors.append(f"{label}: malformed feature identifier {feature_id}")
            continue
        if int(match.group("index")) != index or not feature_id.startswith(expected_prefix):
            errors.append(
                f"{label}: feature identifier {feature_id} does not match index {index} and slug {slug}"
            )


def validate_published_domain(domain: dict, errors: list[str]) -> list[str]:
    index = domain["index"]
    slug = domain["slug"]
    label = f"domain {index} ({slug})"
    feature_count = domain.get("feature_count")
    if isinstance(feature_count, bool) or not isinstance(feature_count, int) or feature_count <= 0:
        errors.append(f"{label}: published feature_count must be an integer > 0")
        return []
    if domain.get("handoff_publication") is not True:
        errors.append(f"{label}: published domain must set handoff_publication=true")

    pipeline = domain.get("pipeline")
    if not isinstance(pipeline, dict):
        errors.append(f"{label}: pipeline must be a mapping")
    else:
        if pipeline.get("scientific_source") != "complete":
            errors.append(f"{label}: scientific_source must be complete")
        for state in PUBLISHED_REQUIRED_COMPLETE:
            if pipeline.get(state) != "complete":
                errors.append(f"{label}: published downstream state {state} must be complete")
        if pipeline.get("algorithms") not in {"complete", "complete_or_not_applicable"}:
            errors.append(f"{label}: algorithms must be complete or complete_or_not_applicable for publication")

    status_path = ROOT / f"registry/domain-finalization/{slug}/feature-status.yaml"
    domain_catalog_path = ROOT / f"handoff/domains/{slug}/catalog.json"
    if not status_path.is_file():
        errors.append(f"{label}: missing finalized feature status {status_path.relative_to(ROOT)}")
        return []
    if not domain_catalog_path.is_file():
        errors.append(f"{label}: missing domain handoff catalog {domain_catalog_path.relative_to(ROOT)}")
        return []

    registry_ids = feature_population_from_status(status_path, errors)
    validate_feature_ids(index, slug, registry_ids, label, errors)
    if len(registry_ids) != feature_count:
        errors.append(f"{label}: feature_count={feature_count} but finalization registry contains {len(registry_ids)} features")

    domain_catalog = load_json(domain_catalog_path, errors)
    if not isinstance(domain_catalog, dict):
        return registry_ids
    if domain_catalog.get("domain") != slug:
        errors.append(f"{label}: domain catalog slug must be {slug}")
    if domain_catalog.get("domain_index") != index:
        errors.append(f"{label}: domain catalog index must be {index}")
    if domain_catalog.get("expected_feature_count") != feature_count:
        errors.append(f"{label}: domain catalog expected_feature_count must be {feature_count}")
    catalog_ids = domain_catalog.get("ordered_feature_ids")
    if not isinstance(catalog_ids, list) or any(not isinstance(item, str) for item in catalog_ids):
        errors.append(f"{label}: domain catalog ordered_feature_ids must be a list of strings")
        catalog_ids = []
    validate_feature_ids(index, slug, catalog_ids, f"{label} domain catalog", errors)
    if catalog_ids != registry_ids:
        errors.append(f"{label}: domain catalog population must exactly match finalization registry order")

    package_rows = domain_catalog.get("feature_packages")
    if not isinstance(package_rows, list):
        errors.append(f"{label}: domain catalog feature_packages must be a list")
    else:
        package_ids = [row.get("feature_id") for row in package_rows if isinstance(row, dict)]
        if package_ids != registry_ids:
            errors.append(f"{label}: feature_packages population must exactly match finalization registry")
        for feature_id in registry_ids:
            package_dir = ROOT / "handoff/features" / feature_id
            if not package_dir.is_dir():
                errors.append(f"{label}: missing package directory handoff/features/{feature_id}")
    return registry_ids


def validate_unpublished_domain(domain: dict, errors: list[str]) -> None:
    index = domain["index"]
    slug = domain["slug"]
    label = f"domain {index} ({slug})"
    if domain.get("feature_count") is not None:
        errors.append(f"{label}: unpublished feature_count must remain null")
    if domain.get("handoff_publication") is not False:
        errors.append(f"{label}: unpublished handoff_publication must remain false")
    pipeline = domain.get("pipeline")
    if not isinstance(pipeline, dict):
        errors.append(f"{label}: pipeline must be a mapping")
        return
    if pipeline.get("scientific_source") != "complete":
        errors.append(f"{label}: scientific_source must be complete")
    for state in DOWNSTREAM_STATES:
        if pipeline.get(state) != "not_started":
            errors.append(f"{label}: unpublished downstream state {state} must remain not_started")


def validate_global_catalog(catalog, published_populations: dict[int, tuple[str, list[str]]], errors: list[str]) -> None:
    if not isinstance(catalog, dict):
        errors.append("handoff/catalog.json must contain a JSON object")
        return
    expected_published_indices = set(published_populations)
    expected_feature_ids = {feature_id for _slug, feature_ids in published_populations.values() for feature_id in feature_ids}
    domains = catalog.get("domains")
    extension_catalog_indices: set[int] = set()
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
                extension_catalog_indices.add(domain_index)
                expected = published_populations.get(domain_index)
                if expected is None:
                    errors.append(f"Unpublished extension domain {domain_index} is present in global catalog")
                    continue
                slug, ids = expected
                if domain.get("domain") != slug:
                    errors.append(f"{path}.domain must be {slug}")
                if domain.get("feature_count") != len(ids):
                    errors.append(f"{path}.feature_count must be {len(ids)}")
                expected_path = f"handoff/domains/{slug}/catalog.json"
                if domain.get("catalog_path") != expected_path:
                    errors.append(f"{path}.catalog_path must be {expected_path}")
    if extension_catalog_indices != expected_published_indices:
        errors.append(f"Global catalog extension-domain population differs from published registry: expected {sorted(expected_published_indices)}, got {sorted(extension_catalog_indices)}")

    features = catalog.get("features")
    extension_feature_ids: set[str] = set()
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
            match = FEATURE_ID.fullmatch(feature_id)
            if match is None:
                continue
            index = int(match.group("index"))
            if index in EXPECTED_INDICES:
                extension_feature_ids.add(feature_id)
                if feature_id not in expected_feature_ids:
                    errors.append(f"Unpublished or ghost extension feature in global catalog: {feature_id}")
    if extension_feature_ids != expected_feature_ids:
        missing = sorted(expected_feature_ids - extension_feature_ids)
        extra = sorted(extension_feature_ids - expected_feature_ids)
        errors.append(f"Global catalog extension feature population mismatch; missing={missing}, extra={extra}")

    summary = catalog.get("summary")
    if not isinstance(summary, dict):
        errors.append("handoff/catalog.json summary must be an object")
    else:
        expected_domain_count = BASELINE_DOMAIN_COUNT + len(published_populations)
        expected_feature_count = BASELINE_FEATURE_COUNT + sum(len(ids) for _slug, ids in published_populations.values())
        if summary.get("domain_count") != expected_domain_count:
            errors.append(f"Global handoff catalog domain_count must be {expected_domain_count}")
        if summary.get("feature_count") != expected_feature_count:
            errors.append(f"Global handoff catalog feature_count must be {expected_feature_count}")


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
            errors.append("Baseline completed domain range must remain 00-15")
        if baseline.get("published_domain_count") != BASELINE_DOMAIN_COUNT:
            errors.append("Baseline published domain count must remain 16")
        if baseline.get("published_feature_count") != BASELINE_FEATURE_COUNT:
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
        index = domain.get("index")
        slug = domain.get("slug")
        if isinstance(index, bool) or not isinstance(index, int):
            errors.append(f"domains[{position}].index must be an integer")
            continue
        if not isinstance(slug, str) or not slug:
            errors.append(f"domains[{position}].slug must be a non-empty string")
            continue
        typed_domains.append(domain)
        indices.append(index)
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
        if not isinstance(members, list) or any(isinstance(member, bool) or not isinstance(member, int) for member in members):
            errors.append(f"Wave {wave_id} domains must be a list of integers")
            continue
        wave_domains[wave_id] = set(members)
        seen_wave_members.extend(members)
        groups = wave.get("analysis_groups", [])
        if not isinstance(groups, list):
            errors.append(f"Wave {wave_id} analysis_groups must be a list")
            continue
        for group in groups:
            if not isinstance(group, list) or len(group) < 2 or any(isinstance(member, bool) or not isinstance(member, int) for member in group):
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

    published_populations: dict[int, tuple[str, list[str]]] = {}
    for domain in typed_domains:
        index = domain["index"]
        slug = domain["slug"]
        label = f"domain {index} ({slug})"
        if index not in EXPECTED_INDICES:
            continue
        declared_wave = domain.get("wave")
        if declared_wave not in EXPECTED_WAVES or index not in EXPECTED_WAVES[declared_wave]:
            errors.append(f"{label}: inconsistent wave {declared_wave}")
        companions = domain.get("analysis_companions")
        if not isinstance(companions, list) or any(isinstance(item, bool) or not isinstance(item, int) for item in companions):
            errors.append(f"{label}: analysis_companions must be a list of integers")
        elif set(companions) != expected_companions[index]:
            errors.append(f"{label}: analysis companions must be {sorted(expected_companions[index])}")

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

        dependencies = domain.get("dependencies")
        if not isinstance(dependencies, dict):
            errors.append(f"{label}: dependencies must be a mapping")
        else:
            confirmed = dependencies.get("confirmed")
            provisional = dependencies.get("provisional")
            if not isinstance(confirmed, list) or any(isinstance(item, bool) or not isinstance(item, int) for item in confirmed):
                errors.append(f"{label}: dependencies.confirmed must be a list of integers")
                confirmed = []
            if not isinstance(provisional, list) or any(isinstance(item, bool) or not isinstance(item, int) for item in provisional):
                errors.append(f"{label}: dependencies.provisional must be a list of integers")
                provisional = []
            for dependency in [*confirmed, *provisional]:
                if dependency < 0 or dependency > 35:
                    errors.append(f"{label}: invalid dependency index {dependency}")
                if dependency == index:
                    errors.append(f"{label}: self-dependency is not allowed")
            if set(confirmed) & set(provisional):
                errors.append(f"{label}: a dependency cannot be both confirmed and provisional")

        published = domain.get("handoff_publication") is True
        if published:
            if index not in ALLOWED_PUBLISHED_EXTENSION_INDICES:
                errors.append(f"{label}: domain 17-35 must not be published before its own production PR")
            ids = validate_published_domain(domain, errors)
            published_populations[index] = (slug, ids)
        else:
            validate_unpublished_domain(domain, errors)

    catalog = load_json(CATALOG_PATH, errors)
    if catalog is None:
        return print_failure(errors)
    validate_global_catalog(catalog, published_populations, errors)
    if errors:
        return print_failure(errors)

    published_feature_count = sum(len(ids) for _slug, ids in published_populations.values())
    print(
        "Domains 16-35 extension validation: PASS "
        f"(published extension domains={len(published_populations)}, "
        f"published extension features={published_feature_count}, future domains remain unpublished)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())