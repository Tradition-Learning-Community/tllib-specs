#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FEATURES = [f"TLC-FC-07-MESSAGE-{i:03d}" for i in range(1, 7)]
ALLOWED_PREFIXES = (
    "registry/domain-finalization/message/",
    "registry/optimized-ir/message/",
    "registry/algorithms/message/",
    "registry/oracles/message/",
    "reports/domain-finalization/message/",
    "tools/domain-finalization/validate_message_finalization.py",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        fail(f"missing file: {path}")
    return p.read_text(encoding="utf-8")


def changed_paths() -> list[str]:
    commands = [
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        ["git", "diff", "--name-only", "main...HEAD"],
        ["git", "diff", "--name-only", "HEAD~1..HEAD"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        if result.returncode == 0:
            return [line for line in result.stdout.splitlines() if line]
    fail("unable to determine changed paths")
    return []


def main() -> None:
    baseline = read("registry/global-reconciliation/current-baseline.yaml")
    if "domain_id: message" not in baseline or "feature_count: 6" not in baseline:
        fail("baseline does not confirm exactly six Message features")

    manifest = read("registry/domain-finalization/message/manifest.yaml")
    status = read("registry/domain-finalization/message/feature-status.yaml")
    if manifest.count("TLC-FC-07-MESSAGE-") != 6:
        fail("manifest population is not exactly six")
    if "rejected_features: []" not in status:
        fail("feature status does not explicitly preserve all features")

    for feature in FEATURES:
        source_contract = f"registry/math-contracts/{feature}/contract.yaml"
        source_ir = f"registry/ir/{feature}/ir.yaml"
        source_test = f"registry/test-plans/{feature}/test-plan.yaml"
        finalized_ir = f"registry/optimized-ir/message/{feature}/ir.yaml"
        algorithm = f"registry/algorithms/message/{feature}/algorithm.yaml"
        oracle = f"registry/oracles/message/{feature}/oracle.yaml"
        for path in (source_contract, source_ir, source_test, finalized_ir, algorithm, oracle):
            read(path)

        ir_text = read(finalized_ir)
        required = [
            f"feature_id: {feature}",
            f"source_contract: {source_contract}",
            f"source_ir: {source_ir}",
            f"source_test_plan: {source_test}",
            "status: selected_for_message_implementation_specification",
            "source_ir_preserved: true",
            "source_contract_preserved: true",
            "replaces_source_ir: false",
            "scientific_source_modified: false",
            "message_content_invented: false",
            f"algorithm: {algorithm}",
            f"oracle: {oracle}",
            "unresolved_propagated:",
            "preservation_obligations:",
        ]
        for token in required:
            if token not in ir_text:
                fail(f"{finalized_ir} missing required token: {token}")
        if feature not in read(algorithm) or feature not in read(oracle):
            fail(f"algorithm/oracle traceability mismatch for {feature}")

    for path in (
        "registry/domain-finalization/message/patterns.yaml",
        "registry/domain-finalization/message/module-specification.yaml",
        "registry/domain-finalization/message/implementation-tasks.yaml",
        "registry/domain-finalization/message/decision-required.yaml",
        "reports/domain-finalization/message/finalization-report.md",
    ):
        read(path)

    paths = changed_paths()
    forbidden_suffixes = (".cpp", ".cc", ".cxx", ".hpp", ".h", ".pyi")
    for path in paths:
        if path.startswith(".github/workflows/"):
            continue
        if not path.startswith(ALLOWED_PREFIXES):
            fail(f"modified path outside Message finalization scope: {path}")
        if path.startswith("maths/"):
            fail(f"scientific source modified: {path}")
        if path.startswith("registry/global-reconciliation/"):
            fail(f"global registry modified: {path}")
        if path.endswith(forbidden_suffixes):
            fail(f"implementation code or binding file added: {path}")
        if "reference" in path.lower() and path.endswith(".py"):
            fail(f"reference implementation suspected: {path}")

    diff_check = subprocess.run(["git", "diff", "--check", "origin/main...HEAD"], cwd=ROOT)
    if diff_check.returncode != 0:
        fail("git diff --check failed")

    print("Message finalization validation: PASS")
    print(f"Validated features: {', '.join(FEATURES)}")
    print(f"Validated changed paths: {len(paths)}")


if __name__ == "__main__":
    main()
