#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.handoff.model import (  # noqa: E402
    DOMAIN_ORDER,
    EXPECTED_DOMAIN_COUNT,
    EXPECTED_FEATURE_COUNT,
)

HISTORICAL_DOMAIN_COUNTS = {
    "master": 16,
    "disciple": 10,
    "community": 8,
    "huit-dimensions": 11,
    "invariants": 10,
    "dynamics": 7,
    "theorems": 9,
    "message": 6,
    "principle": 10,
    "values": 14,
    "virtues": 10,
    "capacities": 15,
    "competencies": 13,
    "practice": 10,
    "lived-experience": 12,
    "relations": 5,
}
HISTORICAL_DOMAIN_ORDER = tuple(HISTORICAL_DOMAIN_COUNTS)
HISTORICAL_FEATURE_COUNT = sum(HISTORICAL_DOMAIN_COUNTS.values())
EXTENSION_MANIFEST = ROOT / "registry/domain-progress/extension-16-35.yaml"
GLOBAL_CATALOG = ROOT / "handoff/catalog.json"
GLOBAL_FILES = [
    "registry/global-finalization/manifest.yaml",
    "registry/global-finalization/domain-status.yaml",
    "registry/global-finalization/feature-status.yaml",
    "registry/global-finalization/shared-types.yaml",
    "registry/global-finalization/shared-patterns.yaml",
    "registry/global-finalization/module-interfaces.yaml",
    "registry/global-finalization/dependency-graph.yaml",
    "registry/global-finalization/execution-order.yaml",
    "registry/global-finalization/decision-required.yaml",
    "registry/global-finalization/implementation-backlog.yaml",
    "registry/global-finalization/library-specification.yaml",
    "registry/scientific-review/engineering-disposition.yaml",
    "registry/symbols/README.md",
    "registry/symbols/namespaces.yaml",
    "registry/symbols/canonical-identifiers.yaml",
    "registry/symbols/representation-policy.yaml",
    "reports/global-finalization/finalization-report.md",
    "reports/global-finalization/implementation-readiness.md",
]
DOMAIN_FILES = [
    "manifest.yaml",
    "feature-status.yaml",
    "patterns.yaml",
    "module-specification.yaml",
    "implementation-tasks.yaml",
]
FORBIDDEN_SUFFIXES = (".cpp", ".cc", ".cxx", ".hpp", ".hxx", ".so", ".pyd")
ALLOWED_VALIDATION_WORKFLOWS = {
    ".github/workflows/global-finalization.yml",
    ".github/workflows/handoff.yml",
}
EXPECTED_MANIFEST_STATUS = "status: integrated_structural_specification_finalized"
EXPECTED_LIBRARY_STATUS = "status: structurally_finalized_engineering_specification"
EXPECTED_SCIENTIFIC_DECISION_COUNT = "scientific_decision_count: 147"
FEATURE_ID = re.compile(r"^TLC-FC-(?P<index>\d{2})-(?P<slug>[A-Z0-9-]+)-(?P<number>\d{3})$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")


def require_text(path: Path, expected: str) -> None:
    require_file(path)
    content = path.read_text(encoding="utf-8")
    if expected not in content:
        fail(f"{path.relative_to(ROOT)} does not contain required text: {expected}")


def load_json(path: Path) -> dict:
    require_file(path)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def load_yaml(path: Path) -> dict:
    require_file(path)
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected YAML mapping: {path.relative_to(ROOT)}")
    return value


def comparison_base() -> str:
    base_ref = os.environ.get("GITHUB_BASE_REF", "").strip()
    candidates = [f"origin/{base_ref}", base_ref] if base_ref else []
    for candidate in candidates:
        proc = subprocess.run(
            ["git", "rev-parse", "--verify", candidate],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if proc.returncode == 0:
            merge_base = subprocess.run(
                ["git", "merge-base", "HEAD", candidate],
                cwd=ROOT,
                check=True,
                text=True,
                capture_output=True,
            ).stdout.strip()
            if merge_base:
                return merge_base
    explicit = os.environ.get("GLOBAL_FINALIZATION_BASE_SHA", "").strip()
    if explicit:
        return explicit
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD^"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if proc.returncode == 0:
        return proc.stdout.strip()
    fail("unable to determine comparison base; set GITHUB_BASE_REF or GLOBAL_FINALIZATION_BASE_SHA")


def changed_paths(base: str) -> list[str]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def validate_domain(domain: str, expected: int) -> set[str]:
    domain_root = ROOT / "registry/domain-finalization" / domain
    for name in DOMAIN_FILES:
        require_file(domain_root / name)

    ir_files = sorted((ROOT / "registry/optimized-ir" / domain).glob("*/ir.yaml"))
    algorithm_files = sorted((ROOT / "registry/algorithms" / domain).glob("*/algorithm.yaml"))
    oracle_files = sorted((ROOT / "registry/oracles" / domain).glob("*/oracle.yaml"))

    if len(ir_files) != expected:
        fail(f"{domain}: expected {expected} finalized IRs, found {len(ir_files)}")
    if len(algorithm_files) != expected:
        fail(f"{domain}: expected {expected} algorithms, found {len(algorithm_files)}")
    if len(oracle_files) != expected:
        fail(f"{domain}: expected {expected} oracles, found {len(oracle_files)}")

    ir_ids = {path.parent.name for path in ir_files}
    algorithm_ids = {path.parent.name for path in algorithm_files}
    oracle_ids = {path.parent.name for path in oracle_files}

    if len(ir_ids) != expected:
        fail(f"{domain}: duplicate finalized IR feature directories")
    if ir_ids != algorithm_ids or ir_ids != oracle_ids:
        fail(f"{domain}: IR, algorithm and oracle feature directories differ")

    return ir_ids


def validate_governance() -> None:
    require_text(ROOT / "registry/global-finalization/manifest.yaml", EXPECTED_MANIFEST_STATUS)
    require_text(ROOT / "registry/global-finalization/library-specification.yaml", EXPECTED_LIBRARY_STATUS)
    require_text(ROOT / "registry/scientific-review/engineering-disposition.yaml", EXPECTED_SCIENTIFIC_DECISION_COUNT)

    root_algorithms = ROOT / "algorithms"
    if root_algorithms.exists():
        active_files = sorted(path for path in root_algorithms.rglob("*") if path.is_file())
        if active_files:
            relative = [str(path.relative_to(ROOT)) for path in active_files]
            fail(
                "active root-level algorithm specifications are forbidden; "
                f"use registry/algorithms/: {relative}"
            )


def historical_feature_path(path: str) -> bool:
    match = re.search(r"TLC-FC-(\d{2})-", path)
    return bool(match and int(match.group(1)) <= 15)


def historical_domain_path(path: str) -> bool:
    prefixes = (
        "registry/domain-finalization/",
        "registry/optimized-ir/",
        "registry/algorithms/",
        "registry/oracles/",
        "handoff/domains/",
    )
    for prefix in prefixes:
        if path.startswith(prefix):
            remainder = path[len(prefix):]
            slug = remainder.split("/", 1)[0]
            return slug in HISTORICAL_DOMAIN_COUNTS
    return False


def validate_historical_immutability(changed: list[str]) -> None:
    protected = []
    for path in changed:
        if path.startswith("maths/"):
            protected.append(path)
            continue
        if historical_feature_path(path):
            protected.append(path)
            continue
        if historical_domain_path(path):
            protected.append(path)
    if protected:
        fail(f"historical domains 00-15 or scientific sources changed in this PR: {protected}")


def extension_domains() -> tuple[list[dict], list[dict]]:
    manifest = load_yaml(EXTENSION_MANIFEST)
    domains = manifest.get("domains")
    if not isinstance(domains, list):
        fail("extension manifest domains must be a list")
    published: list[dict] = []
    unpublished: list[dict] = []
    for row in domains:
        if not isinstance(row, dict):
            fail("extension manifest domain entry must be a mapping")
        index = row.get("index")
        slug = row.get("slug")
        if isinstance(index, bool) or not isinstance(index, int) or not isinstance(slug, str):
            fail(f"invalid extension domain identity: {row}")
        if row.get("handoff_publication") is True:
            published.append(row)
        else:
            unpublished.append(row)
    return published, unpublished


def validate_unpublished_extensions(unpublished: list[dict]) -> None:
    handoff_feature_dirs = [path.name for path in (ROOT / "handoff/features").iterdir() if path.is_dir()]
    for row in unpublished:
        index = row["index"]
        slug = row["slug"]
        if row.get("feature_count") is not None:
            fail(f"unpublished domain {index} ({slug}) must keep feature_count null")
        pipeline = row.get("pipeline")
        if not isinstance(pipeline, dict):
            fail(f"unpublished domain {index} ({slug}) pipeline must be a mapping")
        for key in (
            "functional_decomposition",
            "registries",
            "ir",
            "contracts",
            "algorithms",
            "oracles",
            "handoff_packages",
        ):
            if pipeline.get(key) != "not_started":
                fail(f"unpublished domain {index} ({slug}) downstream state {key} must be not_started")
        forbidden_roots = [
            ROOT / "registry/domain-finalization" / slug,
            ROOT / "registry/optimized-ir" / slug,
            ROOT / "registry/algorithms" / slug,
            ROOT / "registry/oracles" / slug,
            ROOT / "handoff/domains" / slug,
        ]
        existing = [path.relative_to(ROOT).as_posix() for path in forbidden_roots if path.exists()]
        if existing:
            fail(f"unpublished domain {index} ({slug}) has publication artifacts: {existing}")
        prefix = f"TLC-FC-{index:02d}-"
        ghost = sorted(name for name in handoff_feature_dirs if name.startswith(prefix))
        if ghost:
            fail(f"unpublished domain {index} ({slug}) has handoff feature packages: {ghost}")


def validate_published_extensions(published: list[dict]) -> tuple[dict[int, tuple[str, list[str]]], set[str]]:
    populations: dict[int, tuple[str, list[str]]] = {}
    all_ids: set[str] = set()
    for row in published:
        index = row["index"]
        slug = row["slug"]
        feature_count = row.get("feature_count")
        if isinstance(feature_count, bool) or not isinstance(feature_count, int) or feature_count <= 0:
            fail(f"published domain {index} ({slug}) must declare a positive feature_count")
        pipeline = row.get("pipeline")
        if not isinstance(pipeline, dict):
            fail(f"published domain {index} ({slug}) pipeline must be a mapping")
        for key in ("scientific_source", "functional_decomposition", "registries", "ir", "contracts", "oracles", "handoff_packages"):
            if pipeline.get(key) != "complete":
                fail(f"published domain {index} ({slug}) state {key} must be complete")
        if pipeline.get("algorithms") not in {"complete", "complete_or_not_applicable"}:
            fail(f"published domain {index} ({slug}) algorithms state is not publishable")

        feature_ids = validate_domain(slug, feature_count)
        domain_catalog = load_json(ROOT / "handoff/domains" / slug / "catalog.json")
        ordered = domain_catalog.get("ordered_feature_ids")
        if not isinstance(ordered, list) or any(not isinstance(item, str) for item in ordered):
            fail(f"{slug}: ordered_feature_ids must be a list of strings")
        if len(ordered) != feature_count or set(ordered) != feature_ids:
            fail(f"{slug}: finalized artifacts and domain handoff catalog populations differ")
        if domain_catalog.get("expected_feature_count") != feature_count:
            fail(f"{slug}: domain catalog expected_feature_count mismatch")
        for feature_id in ordered:
            match = FEATURE_ID.fullmatch(feature_id)
            if match is None or int(match.group("index")) != index:
                fail(f"{slug}: malformed or wrong-domain feature id {feature_id}")
            if feature_id in all_ids:
                fail(f"duplicate extension feature id {feature_id}")
            all_ids.add(feature_id)
            package_dir = ROOT / "handoff/features" / feature_id
            if not package_dir.is_dir():
                fail(f"missing handoff package {package_dir.relative_to(ROOT)}")
        populations[index] = (slug, ordered)
    return populations, all_ids


def validate_global_catalog(published: list[dict], extension_ids: set[str]) -> None:
    catalog = load_json(GLOBAL_CATALOG)
    domains = catalog.get("domains")
    features = catalog.get("features")
    summary = catalog.get("summary")
    if not isinstance(domains, list) or not isinstance(features, list) or not isinstance(summary, dict):
        fail("global handoff catalog is missing domains, features, or summary")

    expected_domain_count = len(HISTORICAL_DOMAIN_COUNTS) + len(published)
    expected_feature_count = HISTORICAL_FEATURE_COUNT + len(extension_ids)
    if expected_domain_count != EXPECTED_DOMAIN_COUNT:
        fail(
            f"model/domain-progress authority mismatch: model expects {EXPECTED_DOMAIN_COUNT} domains, "
            f"extension registry implies {expected_domain_count}"
        )
    if expected_feature_count != EXPECTED_FEATURE_COUNT:
        fail(
            f"model/domain-progress authority mismatch: model expects {EXPECTED_FEATURE_COUNT} features, "
            f"extension registry implies {expected_feature_count}"
        )
    if summary.get("domain_count") != expected_domain_count:
        fail(f"global catalog domain_count must be {expected_domain_count}")
    if summary.get("feature_count") != expected_feature_count:
        fail(f"global catalog feature_count must be {expected_feature_count}")
    if len(domains) != expected_domain_count or len(features) != expected_feature_count:
        fail("global catalog list populations do not match summary")

    catalog_order = [row.get("domain") for row in domains if isinstance(row, dict)]
    if catalog_order != list(DOMAIN_ORDER):
        fail(f"global catalog domain order differs from handoff model: {catalog_order}")

    catalog_feature_ids = {row.get("feature_id") for row in features if isinstance(row, dict)}
    if None in catalog_feature_ids or len(catalog_feature_ids) != expected_feature_count:
        fail("global catalog feature identities are missing or duplicated")
    if not extension_ids.issubset(catalog_feature_ids):
        fail(f"global catalog is missing extension feature ids: {sorted(extension_ids - catalog_feature_ids)}")


def validate_changed_scope(changed: list[str], base: str) -> None:
    # Deleting an already-tracked generated artifact is cleanup, not an attempt
    # to publish one. Scope guards apply to files that still exist at HEAD.
    present = [path for path in changed if (ROOT / path).exists()]

    runtime_files = [path for path in present if path.endswith(FORBIDDEN_SUFFIXES)]
    if runtime_files:
        fail(f"runtime implementation files are out of scope: {runtime_files}")

    temporary = [
        path
        for path in present
        if path.endswith(".status")
        or "__pycache__" in path
        or path.endswith(".log")
        or (
            path.startswith(".github/workflows/")
            and path not in ALLOWED_VALIDATION_WORKFLOWS
        )
    ]
    if temporary:
        fail(f"temporary or unrelated integration artifacts found: {temporary}")

    subprocess.run(["git", "diff", "--check", f"{base}...HEAD"], cwd=ROOT, check=True)


def main() -> None:
    for relative in GLOBAL_FILES:
        require_file(ROOT / relative)
    validate_governance()

    if HISTORICAL_FEATURE_COUNT != 166:
        fail("internal historical population does not sum to 166")

    historical_features: set[str] = set()
    for domain, expected in HISTORICAL_DOMAIN_COUNTS.items():
        feature_ids = validate_domain(domain, expected)
        overlap = historical_features.intersection(feature_ids)
        if overlap:
            fail(f"duplicate historical feature identifiers across domains: {sorted(overlap)}")
        historical_features.update(feature_ids)
    if len(historical_features) != HISTORICAL_FEATURE_COUNT:
        fail(f"expected 166 historical feature directories, found {len(historical_features)}")

    legacy = sorted(feature for feature in historical_features if re.match(r"TLC-FC-11-CAP-\d+$", feature))
    if legacy:
        fail(f"legacy Capacities identifiers promoted into active population: {legacy}")

    base = comparison_base()
    changed = changed_paths(base)
    validate_historical_immutability(changed)

    published, unpublished = extension_domains()
    validate_unpublished_extensions(unpublished)
    _populations, extension_ids = validate_published_extensions(published)
    validate_global_catalog(published, extension_ids)
    validate_changed_scope(changed, base)

    print(
        "Global structural finalization validation: PASS "
        f"({len(HISTORICAL_DOMAIN_COUNTS)} historical domains/{HISTORICAL_FEATURE_COUNT} historical features immutable, "
        f"{len(published)} published extension domains/{len(extension_ids)} extension features, "
        f"{EXPECTED_DOMAIN_COUNT} total domains/{EXPECTED_FEATURE_COUNT} total features, "
        "future extension domains unpublished, 0 runtime implementations)"
    )


if __name__ == "__main__":
    main()
