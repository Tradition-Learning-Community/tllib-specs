#!/usr/bin/env python3
"""Validate that publication workflows cover every normative path family."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = (
    ROOT / ".github/workflows/global-finalization.yml",
    ROOT / ".github/workflows/handoff.yml",
)
EVENTS = ("pull_request", "push")
REQUIRED_PATHS = {
    "maths/**",
    "framework/**",
    "registry/**",
    "handoff/**",
    "reports/**",
    "execution-manifests/**",
    "tools/**",
    ".github/workflows/**",
}


class TriggerFailure(RuntimeError):
    pass


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def event_block(lines: list[str], event: str) -> list[str]:
    marker = f"  {event}:"
    try:
        start = next(index for index, line in enumerate(lines) if line.rstrip() == marker)
    except StopIteration as exc:
        raise TriggerFailure(f"missing {event} trigger") from exc
    block: list[str] = []
    for line in lines[start + 1 :]:
        if line.strip() and len(line) - len(line.lstrip()) <= 2:
            break
        block.append(line)
    return block


def list_values(block: list[str], key: str) -> set[str]:
    marker = f"    {key}:"
    for index, line in enumerate(block):
        stripped = line.rstrip()
        if stripped.startswith(marker):
            suffix = stripped[len(marker) :].strip()
            if suffix:
                if not (suffix.startswith("[") and suffix.endswith("]")):
                    raise TriggerFailure(f"unsupported inline {key} syntax: {suffix}")
                values = suffix[1:-1].split(",") if suffix[1:-1].strip() else []
                return {unquote(value) for value in values if value.strip()}
            values: set[str] = set()
            for child in block[index + 1 :]:
                if child.strip() and len(child) - len(child.lstrip()) <= 4:
                    break
                item = child.strip()
                if item.startswith("- "):
                    values.add(unquote(item[2:]))
            return values
    raise TriggerFailure(f"missing {key} list")


def validate_workflow(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    for event in EVENTS:
        block = event_block(lines, event)
        branches = list_values(block, "branches")
        if "main" not in branches:
            raise TriggerFailure(f"{path.relative_to(ROOT)} {event}: main branch is not covered")
        paths = list_values(block, "paths")
        missing = sorted(REQUIRED_PATHS - paths)
        if missing:
            raise TriggerFailure(
                f"{path.relative_to(ROOT)} {event}: normative path families missing: {missing}"
            )


def validate_dynamic_matrix() -> None:
    path = ROOT / ".github/workflows/global-finalization.yml"
    text = path.read_text(encoding="utf-8")
    required_fragments = (
        "python tools/pipeline/catalog_snapshot.py --matrix",
        "matrix: ${{ fromJSON(needs.catalog.outputs.matrix) }}",
    )
    for fragment in required_fragments:
        if fragment not in text:
            raise TriggerFailure(f"global-finalization workflow is not catalog-driven: missing {fragment!r}")
    if re.search(r"strategy:\s*\n(?:\s+.*\n)*?\s+matrix:\s*\n\s+include:", text):
        raise TriggerFailure("global-finalization workflow contains a manually enumerated matrix")


def main() -> int:
    try:
        for workflow in WORKFLOWS:
            validate_workflow(workflow)
        validate_dynamic_matrix()
        print("CI trigger and catalog-driven matrix validation: PASS")
        return 0
    except (OSError, TriggerFailure) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
