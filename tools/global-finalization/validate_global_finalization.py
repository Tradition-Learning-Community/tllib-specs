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


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def feature_id_from_text(text: str, path: Path) -> str:
    match = re.search(r"(?m)^feature_id:\s*['\"]?([^'\"\s]+)", text)
    if not match:
        fail(f"missing feature_id in {path.relative_to(ROOT)}")
    return match.group(1)


def changed_paths() -> list[str]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", f"{BASE}...HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def validate_domain(domain: str, expected: int) -> tuple[set[str], set[str], set[str]]:
    domain_root = ROOT / "registry/domain-finalization" / domain
    for name in DOMAIN_FILES:
        read(domain_root / name)

    ir_files = sorted((ROOT / "registry/optimized-ir" / domain).glob("*/ir.yaml"))
    algorithm_files = sorted((ROOT / "registry/algorithms" / domain).glob("*/algorithm.yaml"))
    oracle_files = sorted((ROOT / "registry/oracles" / domain).glob("*/oracle.yaml"))

    if len(ir_files) != expected:
        fail(f"{domain}: expected {expected} finalized IRs, found {len(ir_files)}")
    if len(algorithm_files) != expected:
        fail(f"{domain}: expected {expected} algorithms, found {len(algorithm_files)}")
    if len(oracle_files) != expected:
        fail(f"{domain}: expected {expected} oracles, found {len(oracle_files)}")

    ir_ids = {feature_id_from_text(read(path), path) for path in ir_files}
    algorithm_ids = {feature_id_from_text(read(path), path) for path in algorithm_files}
    oracle_ids = {feature_id_from_text(read(path), path) for path in oracle_files}

    if len(ir_ids) != expected:
        fail(f"{domain}: duplicate finalized IR feature identifiers")
    if ir_ids != algorithm_ids or ir_ids != oracle_ids:
        fail(f"{domain}: IR, algorithm and oracle populations differ")

    for path in ir_files:
        text = read(path)
        required = (
            "source_ir_preserved: true",
            "source_contract_preserved: true",
            "replaces_source_ir: false",
            "scientific_source_modified: false",
        )
        missing = [item for item in required if item not in text]
        if missing:
            fail(f"{path.relative_to(ROOT)} missing preservation flags: {missing}")

    return ir_ids, algorithm_ids, oracle_ids


def main() -> None:
    for relative in GLOBAL_FILES:
        read(ROOT / relative)

    if sum(DOMAIN_COUNTS.values()) != 166:
        fail("internal expected population does not sum to 166")

    all_ir: set[str] = set()
    all_algorithms: set[str] = set()
    all_oracles: set[str] = set()

    for domain, expected in DOMAIN_COUNTS.items():
        ir_ids, algorithm_ids, oracle_ids = validate_domain(domain, expected)
        if all_ir.intersection(ir_ids):
            fail(f"duplicate feature identifiers across domains: {domain}")
        all_ir.update(ir_ids)
        all_algorithms.update(algorithm_ids)
        all_oracles.update(oracle_ids)

    if not (len(all_ir) == len(all_algorithms) == len(all_oracles) == 166):
        fail("global artifact populations are not exactly 166")
    if all_ir != all_algorithms or all_ir != all_oracles:
        fail("global IR, algorithm and oracle feature sets differ")

    legacy = sorted(feature for feature in all_ir if re.match(r"TLC-FC-11-CAP-\d+$", feature))
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
        path for path in changed
        if path.endswith(".status")
        or "__pycache__" in path
        or path.endswith(".log")
        or path.startswith(".github/workflows/") and "global-finalization" not in path
    ]
    if temporary:
        fail(f"temporary or unrelated integration artifacts found: {temporary}")

    subprocess.run(["git", "diff", "--check", f"{BASE}...HEAD"], cwd=ROOT, check=True)

    print(
        "Global finalization validation: PASS "
        "(16 domains, 166 finalized IRs, 166 algorithms, 166 oracles, "
        "0 source modifications, 0 legacy promotions, 0 runtime implementations)"
    )


if __name__ == "__main__":
    main()
