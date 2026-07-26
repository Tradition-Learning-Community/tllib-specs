#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "c34d40713bf444d38f92f76e1c6239ee596d5a18"
DOMAIN_COUNTS = {
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
    "decision-required.yaml",
]
FORBIDDEN_PREFIXES = (
    "maths/",
    "registry/math-contracts/",
    "registry/ir/",
    "registry/test-plans/",
    "registry/global-reconciliation/",
)
FORBIDDEN_SUFFIXES = (".cpp", ".cc", ".cxx", ".hpp", ".hxx", ".so", ".pyd")
EXPECTED_MANIFEST_STATUS = "status: integrated_structural_specification_finalized"
EXPECTED_LIBRARY_STATUS = "status: structurally_finalized_engineering_specification"
EXPECTED_SCIENTIFIC_DECISION_COUNT = "scientific_decision_count: 147"


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


def changed_paths() -> list[str]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", f"{BASE}...HEAD"],
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
    require_text(
        ROOT / "registry/global-finalization/manifest.yaml",
        EXPECTED_MANIFEST_STATUS,
    )
    require_text(
        ROOT / "registry/global-finalization/library-specification.yaml",
        EXPECTED_LIBRARY_STATUS,
    )
    require_text(
        ROOT / "registry/scientific-review/engineering-disposition.yaml",
        EXPECTED_SCIENTIFIC_DECISION_COUNT,
    )

    root_algorithms = ROOT / "algorithms"
    if root_algorithms.exists():
        active_files = sorted(path for path in root_algorithms.rglob("*") if path.is_file())
        if active_files:
            relative = [str(path.relative_to(ROOT)) for path in active_files]
            fail(
                "active root-level algorithm specifications are forbidden; "
                f"use registry/algorithms/: {relative}"
            )


def main() -> None:
    for relative in GLOBAL_FILES:
        require_file(ROOT / relative)

    validate_governance()

    if sum(DOMAIN_COUNTS.values()) != 166:
        fail("internal expected population does not sum to 166")

    all_features: set[str] = set()
    for domain, expected in DOMAIN_COUNTS.items():
        feature_ids = validate_domain(domain, expected)
        overlap = all_features.intersection(feature_ids)
        if overlap:
            fail(f"duplicate feature identifiers across domains: {sorted(overlap)}")
        all_features.update(feature_ids)

    if len(all_features) != 166:
        fail(f"expected 166 unique feature directories, found {len(all_features)}")

    legacy = sorted(feature for feature in all_features if re.match(r"TLC-FC-11-CAP-\d+$", feature))
    if legacy:
        fail(f"legacy Capacities identifiers promoted into active population: {legacy}")

    changed = changed_paths()
    forbidden = [path for path in changed if path.startswith(FORBIDDEN_PREFIXES)]
    if forbidden:
        fail(f"protected source paths changed since baseline: {forbidden}")

    runtime_files = [path for path in changed if path.endswith(FORBIDDEN_SUFFIXES)]
    if runtime_files:
        fail(f"runtime implementation files are out of scope: {runtime_files}")

    temporary = [
        path
        for path in changed
        if path.endswith(".status")
        or "__pycache__" in path
        or path.endswith(".log")
        or path.startswith(".github/workflows/")
        and "global-finalization" not in path
    ]
    if temporary:
        fail(f"temporary or unrelated integration artifacts found: {temporary}")

    subprocess.run(["git", "diff", "--check", f"{BASE}...HEAD"], cwd=ROOT, check=True)

    print(
        "Global structural finalization validation: PASS "
        "(16 domains, 166 finalized IRs, 166 algorithms, 166 oracles, "
        "147 scientific decisions preserved with non-blocking engineering disposition, "
        "canonical symbol registry present, 0 root-level algorithm specifications, "
        "0 source modifications, 0 legacy promotions, 0 runtime implementations)"
    )


if __name__ == "__main__":
    main()
