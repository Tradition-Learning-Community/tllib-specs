#!/usr/bin/env python3
"""Detect drift between the canonical catalog and current publication claims.

Current documentation claims are validated against ``handoff/catalog.json``.
Claims found under ``reports/`` are inventoried as historical evidence and are
never rewritten or compared with the current population.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "handoff" / "catalog.json"

NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
}
WORD_PATTERN = "|".join(NUMBER_WORDS)


class DriftFailure(RuntimeError):
    """Raised when a current publication claim diverges from the catalog."""


@dataclass(frozen=True)
class ClaimRule:
    name: str
    path: str
    pattern: str
    groups: dict[str, str]


RULES = (
    ClaimRule(
        "readme-community-domain-corpus",
        "README.md",
        r"Domain 02 of the (?P<domains>\d+) Tradition Learning domains",
        {"domains": "domain_count"},
    ),
    ClaimRule(
        "readme-production-corpus",
        "README.md",
        r"for the (?P<domains>\d+)-domain Tradition Learning corpus",
        {"domains": "domain_count"},
    ),
    ClaimRule(
        "readme-domain-table",
        "README.md",
        r"\| Domain catalogs \| \*\*(?P<domains>\d+)\*\* \|",
        {"domains": "domain_count"},
    ),
    ClaimRule(
        "readme-feature-table",
        "README.md",
        r"\| Feature Handoff Packages \| \*\*(?P<features>\d+)\*\* \|",
        {"features": "feature_count"},
    ),
    ClaimRule(
        "readme-shared-table",
        "README.md",
        r"\| Shared structural contracts \| \*\*(?P<shared>\d+)\*\* \|",
        {"shared": "shared_contract_count"},
    ),
    ClaimRule(
        "readme-export-table",
        "README.md",
        r"\| Standalone exports validated by CI \| \*\*(?P<features>\d+)\*\* \|",
        {"features": "feature_count"},
    ),
    ClaimRule(
        "readme-architecture-domains",
        "README.md",
        r"domains/\s+(?P<domains>\d+) complete catalogs",
        {"domains": "domain_count"},
    ),
    ClaimRule(
        "readme-architecture-features",
        "README.md",
        r"features/\s+(?P<features>\d+) autonomous feature packages",
        {"features": "feature_count"},
    ),
    ClaimRule(
        "readme-global-catalog",
        "README.md",
        rf"projection of the (?P<domains>\d+) domain catalogs, (?P<features>\d+) feature manifests, and (?P<shared>{WORD_PATTERN}|\d+) shared packages",
        {"domains": "domain_count", "features": "feature_count", "shared": "shared_contract_count"},
    ),
    ClaimRule(
        "handoff-introduction",
        "handoff/README.md",
        rf"contains (?P<domains>\d+) complete domain catalogs, (?P<features>\d+) autonomous feature packages, (?P<shared>{WORD_PATTERN}|\d+) shared structural contracts",
        {"domains": "domain_count", "features": "feature_count", "shared": "shared_contract_count"},
    ),
    ClaimRule(
        "handoff-examples",
        "handoff/README.md",
        rf"contains (?P<examples_present>{WORD_PATTERN}|\d+) package with examples and (?P<examples_absent>\d+) without them",
        {"examples_present": "examples_present", "examples_absent": "examples_absent"},
    ),
    ClaimRule(
        "handoff-complete-catalogs",
        "handoff/README.md",
        r"The (?P<domains>\d+) catalogs together declare exactly (?P<features>\d+) unique feature IDs",
        {"domains": "domain_count", "features": "feature_count"},
    ),
    ClaimRule(
        "handoff-shared-contracts",
        "handoff/README.md",
        rf"The model uses (?P<shared>{WORD_PATTERN}|\d+) versioned structural contracts",
        {"shared": "shared_contract_count"},
    ),
    ClaimRule(
        "handoff-validator-population",
        "handoff/README.md",
        rf"exactly (?P<domains>\d+) catalogs, (?P<features>\d+) feature packages, and (?P<shared>{WORD_PATTERN}|\d+) shared contracts",
        {"domains": "domain_count", "features": "feature_count", "shared": "shared_contract_count"},
    ),
    ClaimRule(
        "banner-population",
        "docs/assets/tllib-specs-banner.svg",
        r">(?P<domains>\d+) theory domains · (?P<features>\d+) feature packages · (?P<shared>\d+) shared contracts<",
        {"domains": "domain_count", "features": "feature_count", "shared": "shared_contract_count"},
    ),
    ClaimRule(
        "banner-handoff-packages",
        "docs/assets/tllib-specs-banner.svg",
        r">(?P<features>\d+) packages<",
        {"features": "feature_count"},
    ),
)

HISTORICAL_PATTERN = re.compile(
    r"(?i)(?:\b\d+\b.{0,20}\b(?:domains?|domain catalogs?|features?|feature packages?|shared contracts?)\b|"
    r"\b(?:domains?|domain catalogs?|features?|feature packages?|shared contracts?)\b.{0,20}\b\d+\b)"
)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DriftFailure(f"cannot read JSON {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise DriftFailure(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if check and proc.returncode:
        raise DriftFailure(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def catalog_values(catalog: dict[str, Any]) -> dict[str, int]:
    summary = catalog.get("summary")
    domains = catalog.get("domains")
    features = catalog.get("features")
    shared = catalog.get("shared_contracts")
    if not isinstance(summary, dict) or not isinstance(domains, list) or not isinstance(features, list) or not isinstance(shared, list):
        raise DriftFailure("canonical catalog population is invalid")
    expected = {
        "domain_count": len(domains),
        "feature_count": len(features),
        "shared_contract_count": len(shared),
        "examples_present": int(summary.get("examples_present", -1)),
        "examples_absent": int(summary.get("examples_absent", -1)),
    }
    for key in ("domain_count", "feature_count", "shared_contract_count"):
        if summary.get(key) != expected[key]:
            raise DriftFailure(f"catalog summary {key} diverges from canonical arrays")
    if expected["examples_present"] + expected["examples_absent"] != expected["feature_count"]:
        raise DriftFailure("catalog example counts do not cover the feature population")
    return expected


def parse_count(value: str) -> int:
    lowered = value.lower()
    if lowered in NUMBER_WORDS:
        return NUMBER_WORDS[lowered]
    try:
        return int(value)
    except ValueError as exc:
        raise DriftFailure(f"cannot parse population count {value!r}") from exc


def replacement_count(original: str, value: int) -> str:
    if original.lower() in NUMBER_WORDS:
        for word, count in NUMBER_WORDS.items():
            if count == value:
                return word
    return str(value)


def rule_matches(rule: ClaimRule, text: str, values: dict[str, int]) -> tuple[list[dict[str, Any]], list[str]]:
    matches = list(re.finditer(rule.pattern, text))
    if len(matches) != 1:
        return [], [f"{rule.path}: claim {rule.name!r} expected once, observed {len(matches)}"]
    match = matches[0]
    observations: list[dict[str, Any]] = []
    errors: list[str] = []
    for group, key in rule.groups.items():
        observed_text = match.group(group)
        observed = parse_count(observed_text)
        expected = values[key]
        observations.append(
            {
                "claim": rule.name,
                "path": rule.path,
                "metric": key,
                "observed": observed,
                "expected": expected,
                "classification": "current_catalog_derived",
            }
        )
        if observed != expected:
            errors.append(
                f"{rule.path}: {rule.name} {key} expected={expected}, observed={observed}"
            )
    return observations, errors


def rewrite_rule(rule: ClaimRule, text: str, values: dict[str, int]) -> str:
    matches = list(re.finditer(rule.pattern, text))
    if len(matches) != 1:
        raise DriftFailure(f"{rule.path}: cannot rewrite {rule.name}; expected exactly one match")
    match = matches[0]
    replacements: list[tuple[int, int, str]] = []
    for group, key in rule.groups.items():
        replacements.append(
            (match.start(group), match.end(group), replacement_count(match.group(group), values[key]))
        )
    updated = text
    for start, end, replacement in sorted(replacements, reverse=True):
        updated = updated[:start] + replacement + updated[end:]
    return updated


def verify_current_claims(values: dict[str, int], *, write: bool) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    rules_by_path: dict[str, list[ClaimRule]] = {}
    for rule in RULES:
        rules_by_path.setdefault(rule.path, []).append(rule)

    observations: list[dict[str, Any]] = []
    errors: list[str] = []
    rewritten: list[str] = []
    for relative, rules in sorted(rules_by_path.items()):
        path = ROOT / relative
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{relative}: cannot read current publication surface: {exc}")
            continue
        if write:
            updated = text
            for rule in rules:
                updated = rewrite_rule(rule, updated, values)
            if updated != text:
                path.write_text(updated, encoding="utf-8")
                rewritten.append(relative)
                text = updated
        for rule in rules:
            found, rule_errors = rule_matches(rule, text, values)
            observations.extend(found)
            errors.extend(rule_errors)
    return observations, errors, rewritten


def historical_claims() -> list[dict[str, Any]]:
    reports = ROOT / "reports"
    if not reports.is_dir():
        raise DriftFailure("reports/ is missing")
    claims: list[dict[str, Any]] = []
    for path in sorted(item for item in reports.rglob("*") if item.is_file() and item.suffix.lower() in {".md", ".json", ".yaml", ".yml"}):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, 1):
            if HISTORICAL_PATTERN.search(line):
                claims.append(
                    {
                        "classification": "historical_report",
                        "path": path.relative_to(ROOT).as_posix(),
                        "line": number,
                        "text": line.strip()[:500],
                    }
                )
    return claims


def domain_map(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = catalog.get("domains")
    if not isinstance(rows, list):
        raise DriftFailure("catalog domains must be a list")
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("domain"), str):
            raise DriftFailure("catalog domain row is invalid")
        result[row["domain"]] = {
            "domain_index": row.get("domain_index"),
            "feature_count": row.get("feature_count"),
            "catalog_sha256": row.get("catalog_sha256"),
        }
    return result


def population_diff(base: dict[str, Any], target: dict[str, Any]) -> dict[str, list[str]]:
    old = domain_map(base)
    new = domain_map(target)
    common = set(old) & set(new)
    return {
        "added_domains": sorted(set(new) - set(old)),
        "removed_domains": sorted(set(old) - set(new)),
        "modified_domains": sorted(name for name in common if old[name] != new[name]),
    }


def parent_catalog() -> dict[str, Any] | None:
    parent = git("rev-parse", "HEAD^", check=False)
    if not parent:
        return None
    proc = subprocess.run(
        ["git", "show", f"{parent}:handoff/catalog.json"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        return None
    try:
        value = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(*, write: bool) -> dict[str, Any]:
    catalog = load_json(CATALOG_PATH)
    values = catalog_values(catalog)
    current, errors, rewritten = verify_current_claims(values, write=write)
    historical = historical_claims()
    parent = parent_catalog()
    diff = population_diff(parent, catalog) if parent is not None else {
        "added_domains": [], "removed_domains": [], "modified_domains": []
    }
    summary = catalog.get("summary") or {}
    evidence = {
        "schema_version": "1.0",
        "audit": "publication-drift",
        "spec_commit": git("rev-parse", "HEAD"),
        "catalog_sha256": sha256_file(CATALOG_PATH),
        "population": {
            "domains": values["domain_count"],
            "features": values["feature_count"],
            "shared_contracts": values["shared_contract_count"],
        },
        "scientific_statuses": summary.get("scientific_statuses", {}),
        "execution_statuses": summary.get("execution_statuses", {}),
        "package_statuses": summary.get("package_statuses", {}),
        "examples": {
            "present": values["examples_present"],
            "absent": values["examples_absent"],
        },
        "current_claims": current,
        "current_claim_count": len(current),
        "historical_claims": historical,
        "historical_claim_count": len(historical),
        "historical_policy": "reports/** claims are immutable historical evidence and are never compared to the current catalog population",
        "domain_changes_vs_parent": diff,
        "rewritten_current_surfaces": rewritten,
        "status": "pass" if not errors else "fail",
        "errors": sorted(errors),
    }
    if errors:
        raise DriftFailure("; ".join(sorted(errors)))
    return evidence


def self_test() -> None:
    def catalog(rows: list[tuple[str, int, int, str]]) -> dict[str, Any]:
        return {
            "domains": [
                {"domain": name, "domain_index": index, "feature_count": count, "catalog_sha256": digest}
                for name, index, count, digest in rows
            ]
        }

    base = catalog([("alpha", 0, 2, "a"), ("beta", 1, 3, "b")])
    added = catalog([("alpha", 0, 2, "a"), ("beta", 1, 3, "b"), ("gamma", 2, 1, "c")])
    modified = catalog([("alpha", 0, 2, "a"), ("beta", 1, 4, "b2")])
    removed = catalog([("alpha", 0, 2, "a")])
    assert population_diff(base, added) == {
        "added_domains": ["gamma"], "removed_domains": [], "modified_domains": []
    }
    assert population_diff(base, modified) == {
        "added_domains": [], "removed_domains": [], "modified_domains": ["beta"]
    }
    assert population_diff(base, removed) == {
        "added_domains": [], "removed_domains": ["beta"], "modified_domains": []
    }
    assert parse_count("eight") == 8 and parse_count("12") == 12
    print("Publication drift add/modify/remove domain scenarios: PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate current catalog-derived publication claims")
    mode.add_argument("--write", action="store_true", help="rewrite known current claim counts from the canonical catalog")
    mode.add_argument("--self-test", action="store_true", help="run synthetic drift scenarios")
    parser.add_argument("--evidence", type=Path, help="write machine-readable audit evidence")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            return 0
        result = audit(write=args.write)
        rendered = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.evidence:
            args.evidence.parent.mkdir(parents=True, exist_ok=True)
            args.evidence.write_text(rendered, encoding="utf-8")
        print(
            "Publication drift validation: PASS "
            f"({result['population']['domains']} domains/"
            f"{result['population']['features']} features/"
            f"{result['population']['shared_contracts']} shared contracts; "
            f"{result['current_claim_count']} current claims; "
            f"{result['historical_claim_count']} historical report claims)"
        )
        return 0
    except DriftFailure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
