#!/usr/bin/env python3
"""Restore targeted historical reconciliation reviews from canonical main."""

from __future__ import annotations

import pathlib
import subprocess


ROOT = pathlib.Path(__file__).resolve().parents[2]
FILES = (
    "registry/global-reconciliation/cycle-scientific-review.yaml",
    "registry/global-reconciliation/dependency-scientific-review.yaml",
    "registry/global-reconciliation/first-contract-batches.yaml",
    "registry/global-reconciliation/pilot-artifact-review.yaml",
    "registry/global-reconciliation/scientific-review-decision-required.yaml",
    "registry/global-reconciliation/targeted-readiness-review.yaml",
)


def main() -> int:
    for relative in FILES:
        content = subprocess.check_output(["git", "show", f"origin/main:{relative}"], cwd=ROOT)
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        print(f"restored historical provenance: {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
