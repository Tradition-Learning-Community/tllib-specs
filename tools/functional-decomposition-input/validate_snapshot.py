#!/usr/bin/env python3
"""Deterministically validate the functional-decomposition input snapshot."""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = ROOT / "registry/functional-decomposition/decomposition-input-snapshot.yaml"
OUT = ROOT / "reports/functional-decomposition-input"
ERRORS = []


def load(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"YAML illisible {path.relative_to(ROOT)}: {exc}")
        return {}


def require(value, message):
    if not value:
        ERRORS.append(message)


def main():
    paths = [SNAPSHOT, *OUT.glob("*.yaml")]
    documents = {path: load(path) for path in paths}
    source_objects = load(ROOT / "registry/scientific-objects/global-object-candidates.yaml")["objects"]
    source_ids = [item["source_object_id"] for item in source_objects]
    snapshot = documents[SNAPSHOT]
    groups = [snapshot.get("admissible_objects", []), snapshot.get("provisionally_separated_objects", []), snapshot.get("blocked_objects", [])]
    rows = [row for group in groups for row in group]
    ids = [row.get("object_id") for row in rows]
    require(Counter(ids) == Counter(source_ids), "Chaque objet source doit apparaître exactement une fois")
    require(len(ids) == len(set(ids)), "Un objet apparaît dans plusieurs statuts")
    require(not any("merge" in str(row.get("status", "")).lower() for row in rows), "Un statut de fusion est présent")
    require(not any(decision.get("selected_option") == "merge" for decision in snapshot.get("decisions_concerned", [])), "Une fusion est incluse")
    for row in snapshot.get("admissible_objects", []):
        require(bool(row.get("source")) and bool(row.get("source_reference")), f"Objet admissible sans source: {row.get('object_id')}")
    blockers = documents[OUT / "blockers.yaml"].get("blockers", [])
    for blocker in blockers:
        require(bool(blocker.get("decision_ids") or blocker.get("term_ids") or blocker.get("sources")), f"Blocage sans décision ni source: {blocker.get('object_id')}")
    text = "\n".join(path.read_text(encoding="utf-8") for path in paths)
    forbidden = ["feature_candidate", "functionality_candidate", "status: approved", "intermediate_representation"]
    require(not any(token in text for token in forbidden), "Fonctionnalité, IR ou statut approved détecté")
    if ERRORS:
        print("VALIDATION FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"VALIDATION OK: {len(ids)} objets uniques; {len(snapshot.get('admissible_relations', [])) + len(snapshot.get('blocked_relations', []))} relations; YAML lisibles; aucune fusion.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
