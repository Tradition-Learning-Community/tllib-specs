#!/usr/bin/env python3
"""Remove temporary Phase 4 generation machinery and diagnostics before merge."""

from __future__ import annotations

import pathlib
import shutil


ROOT = pathlib.Path(__file__).resolve().parents[2]
TEMP_FILES = (
    ".github/workflows/phase4-global-registry-current.yml",
    "registry/global-reconciliation/.phase4-trigger",
    "tools/global-reconciliation/upgrade_current_registry_builder.py",
    "tools/global-reconciliation/finalize_current_registry_builder.py",
    "tools/global-reconciliation/restore_historical_reconciliation_reviews.py",
    "reports/global-reconciliation/current-baseline-upgrade.log",
    "reports/global-reconciliation/current-baseline-upgrade.status",
    "reports/global-reconciliation/current-baseline-finalize.log",
    "reports/global-reconciliation/current-baseline-finalize.status",
    "reports/global-reconciliation/current-baseline-build.log",
    "reports/global-reconciliation/current-baseline-build.status",
    "reports/global-reconciliation/current-baseline-validation.log",
    "reports/global-reconciliation/current-baseline-validation.status",
    "reports/global-reconciliation/current-baseline-whitespace.log",
    "reports/global-reconciliation/current-baseline-whitespace.status",
)


def main() -> int:
    for relative in TEMP_FILES:
        path = ROOT / relative
        if path.exists():
            path.unlink()
            print(f"removed temporary file: {relative}")
    cache = ROOT / "tools/global-reconciliation/__pycache__"
    if cache.exists():
        shutil.rmtree(cache)
        print("removed temporary __pycache__")
    pathlib.Path(__file__).unlink()
    print("removed cleanup helper")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
