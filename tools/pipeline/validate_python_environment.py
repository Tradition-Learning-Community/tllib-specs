#!/usr/bin/env python3
"""Validate the repository's pinned Python tooling environment."""

from __future__ import annotations

import importlib.metadata
import platform
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIRECT = ROOT / "requirements.in"
LOCK = ROOT / "requirements.lock"
PYTHON_VERSION = ROOT / ".python-version"
EXPECTED_IMPLEMENTATION = "CPython"


class EnvironmentFailure(RuntimeError):
    pass


def normalized(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def parse_pins(path: Path) -> dict[str, tuple[str, str]]:
    pins: dict[str, tuple[str, str]] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "==" not in line:
            raise EnvironmentFailure(f"{path.name}: dependency is not exactly pinned: {line}")
        name, version = (item.strip() for item in line.split("==", 1))
        if not name or not version or any(marker in version for marker in (";", " ", "\t")):
            raise EnvironmentFailure(f"{path.name}: unsupported pin: {line}")
        key = normalized(name)
        if key in pins:
            raise EnvironmentFailure(f"{path.name}: duplicate dependency: {name}")
        pins[key] = (name, version)
    if not pins:
        raise EnvironmentFailure(f"{path.name}: no dependencies declared")
    return pins


def validate_runtime() -> None:
    declared = PYTHON_VERSION.read_text(encoding="utf-8").strip()
    expected = tuple(int(part) for part in declared.split("."))
    if len(expected) != 2:
        raise EnvironmentFailure(f"invalid .python-version: {declared!r}")
    observed = sys.version_info[:2]
    if observed != expected:
        raise EnvironmentFailure(
            f"validator runtime must be Python {declared}; observed {observed[0]}.{observed[1]}"
        )
    if platform.python_implementation() != EXPECTED_IMPLEMENTATION:
        raise EnvironmentFailure(
            f"validator runtime must use {EXPECTED_IMPLEMENTATION}; observed {platform.python_implementation()}"
        )


def validate_lock() -> dict[str, tuple[str, str]]:
    direct = parse_pins(DIRECT)
    locked = parse_pins(LOCK)
    missing = sorted(set(direct) - set(locked))
    if missing:
        raise EnvironmentFailure(f"requirements.lock omits direct dependencies: {missing}")
    mismatched = sorted(
        direct[key][0]
        for key in direct
        if direct[key][1] != locked[key][1]
    )
    if mismatched:
        raise EnvironmentFailure(f"direct dependency pins differ from requirements.lock: {mismatched}")
    return locked


def validate_installed(locked: dict[str, tuple[str, str]]) -> None:
    failures: list[str] = []
    for _, (name, expected) in sorted(locked.items()):
        try:
            observed = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"{name} is not installed")
            continue
        if observed != expected:
            failures.append(f"{name}: expected {expected}, observed {observed}")
    if failures:
        raise EnvironmentFailure("locked environment mismatch: " + "; ".join(failures))


def main() -> int:
    try:
        validate_runtime()
        locked = validate_lock()
        validate_installed(locked)
        print(
            f"Pinned Python environment: PASS (CPython {sys.version_info.major}.{sys.version_info.minor}, "
            f"{len(locked)} locked packages)"
        )
        return 0
    except (OSError, ValueError, EnvironmentFailure) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
