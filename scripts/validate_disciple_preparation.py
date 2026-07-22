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
    "production-gates.yaml", "global-manifest-update-proposal.yaml", "master-symbol-mapping.yaml",
    "local-blocker-reassessment.yaml", "post-master-reconciliation.yaml",
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
groups = docs.get("production-order.yaml", {}).get("groups", [])
ordered = [x for group in groups for x in group.get("feature_ids", [])]
if set(ordered) != expected or len(ordered) != len(set(ordered)):
    errors.append("production order must cover every stable feature exactly once")
if list((ROOT / "registry/math-contracts").glob(f"{PREFIX}*")):
    errors.append("Disciple mathematical contract artifact detected")
if list((ROOT / "ir").rglob(f"{PREFIX}*")):
    errors.append("Disciple IR artifact detected")
for dep in docs.get("master-dependencies.yaml", {}).get("dependencies", []):
    if dep.get("dependency_status") != "confirmed":
        errors.append("Master dependency reconciliation is incomplete")
mappings = docs.get("master-symbol-mapping.yaml", {}).get("mappings", [])
if len([m for m in mappings if m.get("mapping_status") == "confirmed"]) != 4:
    errors.append("expected four confirmed Master mappings")
if len(docs.get("feature-dependencies.yaml", {}).get("confirmed_edges", [])) != 9:
    errors.append("expected nine confirmed internal edges")
if len(docs.get("unresolved-status.yaml", {}).get("items", [])) != 32:
    errors.append("expected 32 unresolved records")
gates = docs.get("production-gates.yaml", {})
if gates.get("master_gate", {}).get("master_commit") != "eb977485b7314e32e643e52461e086eb3a753724":
    errors.append("canonical Master gate commit mismatch")
if gates.get("ready_for_contract_generation_now") is not True or gates.get("ready_for_ir_generation") is not False:
    errors.append("production readiness gates are inconsistent")
if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"VALIDATION PASSED: {len(expected)} features, 4 confirmed Master dependencies, 4 confirmed mappings, 9 internal edges, 32 unresolved, no Disciple contract or IR.")
