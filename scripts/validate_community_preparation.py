from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/community"
REP = ROOT / "reports/domain-progress/community"
PREFIX = "TLC-FC-02-COMMUNITY-"
required_yaml = {"source-inventory.yaml", "scientific-coverage.yaml", "feature-status.yaml", "master-dependencies.yaml", "disciple-dependencies.yaml", "external-domain-dependencies.yaml", "feature-dependencies.yaml", "feature-classification.yaml", "historical-pilot-assessment.yaml", "production-order.yaml", "contract-production-plan.yaml", "ir-production-plan.yaml", "unresolved-status.yaml", "production-gates.yaml", "global-manifest-update-proposal.yaml"}
required_reports = {"source-inventory-report.md", "scientific-coverage-report.md", "master-dependencies-report.md", "disciple-dependencies-report.md", "external-domain-dependencies-report.md", "feature-dependency-report.md", "feature-classification-report.md", "historical-pilot-assessment.md", "production-order.md", "contract-production-plan.md", "ir-production-plan.md", "unresolved-report.md", "preparation-completion-report.md"}
errors = []
errors += [f"missing registry: {x}" for x in sorted(required_yaml - {p.name for p in REG.glob("*.yaml")})]
errors += [f"missing report: {x}" for x in sorted(required_reports - {p.name for p in REP.glob("*.md")})]
docs = {}
for p in REG.glob("*.yaml"):
    try: docs[p.name] = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as exc: errors.append(f"invalid YAML {p.name}: {exc}")
catalogue = yaml.safe_load((ROOT / "registry/features/revised/feature-candidates.yaml").read_text(encoding="utf-8"))
expected = {f["candidate_feature_id"] for f in catalogue["features"] if f["candidate_feature_id"].startswith(PREFIX)}
if len(expected) != 8: errors.append(f"expected 8 active revised Community features, found {len(expected)}")
for name, field in [("feature-status.yaml", "features"), ("feature-classification.yaml", "features"), ("contract-production-plan.yaml", "features"), ("ir-production-plan.yaml", "features")]:
    actual = {x["feature_id"] for x in docs.get(name, {}).get(field, [])}
    if actual != expected: errors.append(f"{name} feature coverage mismatch")
groups = docs.get("production-order.yaml", {}).get("groups", {})
ordered = [fid for group in groups.values() for fid in group]
if set(ordered) != expected or len(ordered) != len(set(ordered)): errors.append("production order must cover each feature once")
coverage = docs.get("scientific-coverage.yaml", {})
if coverage.get("objects", {}).get("missing") or coverage.get("relations", {}).get("missing"): errors.append("scientific consolidation coverage incomplete")
pilot = docs.get("historical-pilot-assessment.yaml", {})
if pilot.get("modified_by_preparation") is not False: errors.append("historical pilot modification guard missing")
if docs.get("contract-production-plan.yaml", {}).get("contracts_created") != 0: errors.append("new contract claimed")
if docs.get("ir-production-plan.yaml", {}).get("irs_created") != 0: errors.append("new IR claimed")
if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"VALIDATION PASSED: 15 registries, 13 reports, {len(expected)} active revised features, historical pilot unchanged, no new contract or IR.")
