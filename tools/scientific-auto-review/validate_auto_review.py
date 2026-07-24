#!/usr/bin/env python3
"""Validate completeness, policy compliance and non-application of candidates."""
from __future__ import annotations

import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "scientific-auto-review"
ERRORS = []


def load(path):
    try:
        with path.open(encoding="utf-8") as stream:
            return yaml.safe_load(stream)
    except Exception as exc:
        ERRORS.append(f"YAML illisible {path.relative_to(ROOT)}: {exc}")
        return {}


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def original_ids():
    ids = []
    for path in sorted((ROOT / "reports/scientific-review/batches").glob("batch-*/decisions.yaml")):
        ids.extend(item["decision_id"] for item in load(path).get("decisions", []))
    return ids


def main():
    for path in [ROOT / "framework/scientific-review-automation-policy.yaml", *OUT.glob("*.yaml")]:
        load(path)
    originals = original_ids()
    classification = load(OUT / "decision-classification.yaml").get("decisions", [])
    seen = [item.get("source_decision_id") for item in classification]
    require(len(originals) == 147, f"147 décisions attendues, {len(originals)} trouvées")
    require(Counter(seen) == Counter(originals), "Chaque décision originale doit apparaître exactement une fois")
    for item in classification:
        risk = item.get("risk_level")
        require(risk in {"AUTO", "AUTO_WITH_SECOND_REVIEW", "HUMAN_REQUIRED"}, f"Niveau invalide: {risk}")
        require("pass_a" in item and "pass_b" in item, f"Deux passes absentes: {item.get('source_decision_id')}")
        if item.get("pass_a", {}).get("proposal") != item.get("pass_b", {}).get("proposal"):
            require(risk == "HUMAN_REQUIRED", f"Divergence non humaine: {item.get('source_decision_id')}")
        if risk != "HUMAN_REQUIRED":
            require(item.get("reversible") is True, f"Décision auto irréversible: {item.get('source_decision_id')}")
            require(item.get("confidence", 0) >= 0.98, f"Confiance auto trop basse: {item.get('source_decision_id')}")
        if item.get("selected_option") == "merge":
            scores = item.get("evidence_score", {})
            mandatory = ["type_match", "definition_match", "equation_match", "role_match", "domain_match",
                         "codomain_match", "constraint_match", "relation_match"]
            require(all(scores.get(key) == 1.0 for key in mandatory), f"Fusion incomplètement prouvée: {item.get('source_decision_id')}")
            require(item.get("consensus", {}).get("status") == "concordant", "Fusion sans concordance")
        require("human_decision" not in item, f"Décision humaine préremplie: {item.get('source_decision_id')}")
    for path in OUT.glob("*.yaml"):
        text = path.read_text(encoding="utf-8")
        require("human_decision:" not in text, f"Bloc human_decision présent dans {path.name}")
    require(load(OUT / "coverage-reextraction.yaml").get("signals_analyzed") == 496, "496 signaux de couverture attendus")
    unresolved = load(OUT / "unresolved-term-analysis.yaml")
    require(unresolved.get("total") == 830, "830 termes non résolus attendus")
    require(unresolved.get("automatically_resolved") == 0, "Résolution de terme non conservatrice")
    changed = subprocess.run(["git", "diff", "--name-only", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()
    protected = ("maths/", "algorithms/", "registry/scientific-objects/", "reports/scientific-review/batches/")
    violations = [path for path in changed if path.replace("\\", "/").startswith(protected)]
    require(not violations, f"Fichiers protégés modifiés: {violations}")
    counts = Counter(item["risk_level"] for item in classification)
    if ERRORS:
        print("VALIDATION FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"VALIDATION OK: 147 décisions; AUTO={counts['AUTO']}; AUTO_WITH_SECOND_REVIEW={counts['AUTO_WITH_SECOND_REVIEW']}; HUMAN_REQUIRED={counts['HUMAN_REQUIRED']}")
    print("YAML lisibles; deux passes présentes; aucune décision humaine préremplie; aucun registre scientifique modifié.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
