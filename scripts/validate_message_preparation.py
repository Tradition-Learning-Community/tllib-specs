from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/message"
REP = ROOT / "reports/domain-progress/message"
required = [
"source-inventory.yaml","scientific-coverage.yaml","feature-inventory.yaml","functional-coverage.yaml",
"message-semantics.yaml","concept-separation.yaml","message-structure.yaml","master-dependencies.yaml",
"disciple-dependencies.yaml","community-dependencies.yaml","huit-dimensions-dependencies.yaml",
"invariants-dependencies.yaml","dynamics-dependencies.yaml","theorems-dependencies.yaml",
"principle-dependencies.yaml","external-domain-dependencies.yaml","upstream-symbol-mapping.yaml",
"feature-dependencies.yaml","feature-classification.yaml","production-order.yaml",
"contract-production-plan.yaml","ir-production-plan.yaml","unresolved-status.yaml",
"historical-artifact-assessment.yaml","production-gates.yaml","feature-status.yaml",
"future-reconciliation.yaml","global-manifest-update-proposal.yaml","preparation-status.yaml"]
errors = []
docs = {}
for name in required:
    p = REG / name
    if not p.is_file():
        errors.append(f"missing {p.relative_to(ROOT)}")
        continue
    try:
        docs[name] = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid YAML {name}: {exc}")
    rp = REP / (p.stem + "-report.md")
    if not rp.is_file():
        errors.append(f"missing report {rp.relative_to(ROOT)}")

cov = docs.get("scientific-coverage.yaml", {}).get("counts", {})
if cov != {"objects":72,"relations":71,"unresolved":61,"features":6}:
    errors.append(f"canonical counts mismatch: {cov}")
features = docs.get("feature-inventory.yaml", {}).get("features", [])
ids = [f.get("feature_id") for f in features]
expected = [f"TLC-FC-07-MESSAGE-{i:03d}" for i in range(1,7)]
if ids != expected:
    errors.append(f"feature IDs mismatch: {ids}")
graph = docs.get("feature-dependencies.yaml", {})
if graph.get("cycles") != [] or graph.get("roots") != ["TLC-FC-07-MESSAGE-006"]:
    errors.append("feature graph is not the expected acyclic rooted graph")
status = docs.get("preparation-status.yaml", {})
expected_readiness = {
 "ready_for_contract_generation_now":True,"ready_for_full_contract_generation":False,
 "ready_for_ir_generation":False,"ready_for_implementation_or_code_generation":False}
for key, value in expected_readiness.items():
    if status.get(key) is not value:
        errors.append(f"invalid readiness {key}={status.get(key)!r}")
for forbidden in [ROOT/"contracts/message", ROOT/"ir/message"]:
    if forbidden.exists():
        errors.append(f"premature artifact directory exists: {forbidden.relative_to(ROOT)}")
sem = {x.get("claim"):x.get("status") for x in docs.get("message-semantics.yaml",{}).get("claims",[])}
if sem.get("execution") != "rejected" or sem.get("transport") != "unresolved" or sem.get("encoding") != "unresolved":
    errors.append("protocol/execution safeguards are incomplete")
if docs.get("global-manifest-update-proposal.yaml",{}).get("mutates_global_manifest") is not False:
    errors.append("global manifest proposal is not explicitly non-mutating")
if not (REP/"preparation-completion-report.md").is_file():
    errors.append("missing preparation completion report")

if errors:
    print("MESSAGE PREPARATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"MESSAGE PREPARATION: PASS ({len(required)} YAML artifacts, {len(list(REP.glob('*.md')))} reports)")
