#!/usr/bin/env python3
"""Reject tracked non-normative caches and generated local artifacts."""

from __future__ import annotations

import subprocess
import sys
from pathlib import PurePosixPath

FORBIDDEN_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "htmlcov"}
FORBIDDEN_NAMES = {".coverage", ".DS_Store"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo"}


class HygieneFailure(RuntimeError):
    pass


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def is_forbidden(path: str) -> bool:
    value = PurePosixPath(path)
    if any(part in FORBIDDEN_DIRS for part in value.parts):
        return True
    if value.name in FORBIDDEN_NAMES or value.name.startswith(".coverage."):
        return True
    return value.suffix.lower() in FORBIDDEN_SUFFIXES


def main() -> int:
    try:
        offenders = sorted(path for path in tracked_files() if is_forbidden(path))
        if offenders:
            raise HygieneFailure("tracked non-normative cache/generated files: " + ", ".join(offenders))
        print("Repository tracked-file hygiene: PASS")
        return 0
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError, HygieneFailure) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
