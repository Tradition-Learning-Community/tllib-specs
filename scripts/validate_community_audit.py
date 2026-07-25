from __future__ import annotations
from pathlib import Path
import sys
try:
    import yaml
except ModuleNotFoundError:
    print("PyYAML is required", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'community'
PREFIX = 'TLC-FC-02-COMMUNITY-'
EXPECTED_COUNT = 8
VALID_READINESS = {"ready_for_contract_planning", "ready_with_reservations", "blocked", "non_computational", "scientific_decision_required"}
DP = ROOT / "registry" / "domain-progress" / DOMAIN
REPORT = ROOT / "reports" / "domain-audits" / f"{DOMAIN}-audit-001" / "report.md"
errors = []

def load(name: str):
    path = DP / name
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig")) or {}
    except Exception as exc:
        errors.append(f"invalid {path}: {exc}")
        return {}

source = load("source-inventory.yaml")
catalogue = load("feature-catalogue.yaml")
readiness = load("readiness.yaml")
deps = load("dependency-matrix.yaml")

if source.get("domain_id") != DOMAIN: errors.append("source inventory domain mismatch")
if source.get("source_file") != 'maths/02-community.md': errors.append("source file mismatch")
if not (ROOT / 'maths/02-community.md').is_file(): errors.append("authoritative source missing")

features = catalogue.get("features", [])
ids = [f.get("feature_id") for f in features]
if len(ids) != EXPECTED_COUNT or len(set(ids)) != EXPECTED_COUNT:
    errors.append(f"feature count/uniqueness mismatch: {len(ids)}/{len(set(ids))} expected {EXPECTED_COUNT}")
if any(not isinstance(fid, str) or not fid.startswith(PREFIX) for fid in ids): errors.append("feature prefix mismatch")
if set(ids) != set(source.get("feature_ids", [])): errors.append("source inventory/catalogue feature mismatch")

ritems = readiness.get("features", [])
rids = [x.get("feature_id") for x in ritems]
if set(rids) != set(ids) or len(rids) != len(ids): errors.append("readiness/catalogue feature mismatch")
for item in ritems:
    if item.get("status") not in VALID_READINESS: errors.append(f"invalid readiness for {item.get('feature_id')}")

known = set(ids)
for group in ("internal_dependencies", "external_dependencies", "advisory_dependencies"):
    for dep in deps.get(group, []):
        affected = dep.get("affected_feature_ids", [])
        unknown = sorted(set(affected) - known)
        if unknown: errors.append(f"unknown affected features in {group}: {unknown}")

scan = source.get("artifact_scan", {})
for key in ("contracts", "candidate_irs", "semantic_ir_variants", "prototype_irs", "canonical_irs", "test_plans", "validation_reports"):
    for rel in scan.get(key, []):
        if not (ROOT / rel).is_file(): errors.append(f"declared artifact missing: {rel}")

if not REPORT.is_file(): errors.append("audit report missing")
if source.get("audit_scope") != "audit_only_no_new_scientific_artifacts": errors.append("audit scope mismatch")
if catalogue.get("audit_scope") != "audit_only_no_new_scientific_artifacts": errors.append("catalogue scope mismatch")

if errors:
    print(f"{DOMAIN.upper()} WAVE 0 AUDIT VALIDATION FAILED")
    for error in errors: print("- " + error)
    sys.exit(1)
print(f"{DOMAIN.upper()} WAVE 0 AUDIT VALIDATION PASSED features={EXPECTED_COUNT}")
print("audit_only=true maths_modified=false contracts_created=0 irs_created=0 test_plans_created=0")
