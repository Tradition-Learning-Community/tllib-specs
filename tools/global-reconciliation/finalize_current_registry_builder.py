#!/usr/bin/env python3
"""One-time cleanup patch for the current registry builder.

Historical targeted scientific-review artifacts remain tied to their original
source commits.  The current baseline builder must update only the artifacts it
actually rebuilds and must not relabel historical review content as current.
"""

from __future__ import annotations

import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[2]
PATH = ROOT / "tools/global-reconciliation/build_current_global_registry.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise RuntimeError(f"missing patch marker: {label}")
    return text.replace(old, new, 1)


def main() -> int:
    text = PATH.read_text(encoding="utf-8")

    old_metadata = '''    for path in registry_dir.glob("*.yaml"):
        patch_generated_metadata(path, baseline_commit, tool_commit, timestamp)
'''
    new_metadata = '''    rebuilt_registry_names = (
        "blocker-registry.yaml",
        "contract-execution-plan.yaml",
        "cycle-registry.yaml",
        "decision-required.yaml",
        "dependency-graph.yaml",
        "domain-feature-matrix.yaml",
        "domain-registry.yaml",
        "existing-artifact-audit.yaml",
        "feature-contract-matrix.yaml",
        "feature-ir-matrix.yaml",
        "ir-execution-plan.yaml",
        "manifest.yaml",
        "readiness-registry.yaml",
    )
    for name in rebuilt_registry_names:
        patch_generated_metadata(registry_dir / name, baseline_commit, tool_commit, timestamp)
'''
    text = replace_once(text, old_metadata, new_metadata, "metadata scope")

    old_manifest = '''    manifest["artifacts"] = sorted(
        str(path.relative_to(root)).replace("\\\\", "/") for path in registry_dir.glob("*.yaml")
    ) + [
        "reports/global-reconciliation/reconciliation-report.md",
        "tools/global-reconciliation/build_global_reconciliation.py",
        "tools/global-reconciliation/build_current_global_registry.py",
        "tools/global-reconciliation/validate_global_reconciliation.py",
        "tools/global-reconciliation/validate_current_global_registry.py",
    ]
'''
    new_manifest = '''    current_registry_artifacts = sorted(
        [f"registry/global-reconciliation/{name}" for name in rebuilt_registry_names]
        + [
            "registry/global-reconciliation/current-baseline.yaml",
            "registry/global-reconciliation/domain-review-sequence.yaml",
            "registry/global-reconciliation/status-taxonomy.yaml",
        ]
    )
    manifest["artifacts"] = current_registry_artifacts + [
        "reports/global-reconciliation/phase4-current-baseline-work-item.md",
        "reports/global-reconciliation/reconciliation-report.md",
        "tools/global-reconciliation/build_global_reconciliation.py",
        "tools/global-reconciliation/build_current_global_registry.py",
        "tools/global-reconciliation/validate_global_reconciliation.py",
        "tools/global-reconciliation/validate_current_global_registry.py",
    ]
'''
    text = replace_once(text, old_manifest, new_manifest, "manifest artifact scope")

    PATH.write_text(text, encoding="utf-8", newline="\n")
    print("current registry builder now preserves historical targeted reviews")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
