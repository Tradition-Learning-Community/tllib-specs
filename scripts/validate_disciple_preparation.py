from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/disciple"
REP = ROOT / "reports/domain-progress/disciple"
PREFIX = "TLC-FC-01-DISCIPLE-"
required_yaml = {
    "source-inventory.yaml", "scientific-coverage.yaml", "feature-status.yaml", "master-dependencies.yaml",
    "feature-dependencies.yaml", "feature-classification.yaml", "production-order.yaml",
    "contract-production-plan.yaml", "ir-production-plan.yaml", "unresolved-status.yaml",
    "production-gates.yaml", "global-manifest-update-proposal.yaml",
}
required_reports = {f"{i:02d}-{name}.md" for i, name in enumerate([
    "source-inventory", "scientific-coverage", "master-dependencies", "feature-dependencies",
    "feature-classification", "production-order", "contract-production-plan", "ir-production-plan",
    "unresolved-status", "completion-report"], 1)}
errors = []
errors += [f"missing registry {x}" for x in sorted(required_yaml - {p.name for p in REG.glob("*.yaml")})]
errors += [f"missing report {x}" for x in sorted(required_reports - {p.name for p in REP.glob("*.md")})]
docs = {}
for p in REG.glob("*.yaml"):
    try:
        docs[p.name] = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid YAML {p}: {exc}")
catalogue = yaml.safe_load((ROOT / "registry/features/feature-candidates.yaml").read_text(encoding="utf-8"))
expected = {f["candidate_feature_id"] for f in catalogue["features"] if f["candidate_feature_id"].startswith(PREFIX)}
covered = {f["feature_id"] for f in docs.get("scientific-coverage.yaml", {}).get("features", [])}
if len(expected) != 10 or covered != expected:
    errors.append(f"feature coverage mismatch: expected={len(expected)} covered={len(covered)}")
for key, field in [("feature-status.yaml", "features"), ("feature-classification.yaml", "features")]:
    actual = {x["feature_id"] for x in docs.get(key, {}).get(field, [])}
    if actual != expected:
        errors.append(f"{key} does not cover all stable IDs")
groups = docs.get("production-order.yaml", {}).get("groups", {})
ordered = [x for xs in groups.values() for x in xs]
if set(ordered) != expected or len(ordered) != len(set(ordered)):
    errors.append("production order must cover every stable feature exactly once")
if list((ROOT / "registry/math-contracts").glob(f"{PREFIX}*")):
    errors.append("Disciple mathematical contract artifact detected")
if list((ROOT / "ir").rglob(f"{PREFIX}*")):
    errors.append("Disciple IR artifact detected")
for dep in docs.get("master-dependencies.yaml", {}).get("dependencies", []):
    if dep.get("status") == "confirmed":
        errors.append("Master dependency was over-confirmed")
if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"VALIDATION PASSED: 12 registries, 10 reports, {len(expected)} stable features, no contract or IR.")
