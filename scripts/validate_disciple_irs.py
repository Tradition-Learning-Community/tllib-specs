from pathlib import Path
import json,sys,yaml
ROOT=Path(__file__).resolve().parents[1]; PREFIX="TLC-FC-01-DISCIPLE-"; errors=[]; expected={f"{PREFIX}{i:03d}" for i in range(1,11)}; found=set()
for p in ROOT.glob(f"ir/{PREFIX}*/ir.candidate.json"):
    try: d=json.loads(p.read_text(encoding="utf-8")); found.add(d["feature_id"])
    except Exception as e: errors.append(f"{p}: {e}"); continue
    contract=ROOT/d["contract_ref"]
    if not contract.exists(): errors.append(f"missing contract {contract}")
    if d.get("execution_ready") is not False or d.get("code_generation_readiness") is not False: errors.append(f"readiness violation {p}")
    cov=yaml.safe_load((p.parent/"ir-coverage.yaml").read_text(encoding="utf-8"))
    if cov.get("coverage_status") != "complete_with_reservations" or cov.get("missing_elements"): errors.append(f"coverage failure {p}")
if found != expected: errors.append(f"IR coverage mismatch: {sorted(expected-found)}")
audit=yaml.safe_load((ROOT/"registry/domain-progress/disciple/ir-audit.yaml").read_text(encoding="utf-8"))
if audit.get("irs_validated") != 10 or audit.get("decision") != "domain_ir_complete_with_reservations": errors.append("IR audit invalid")
if errors: print("IR VALIDATION FAILED\n"+"\n".join(errors)); sys.exit(1)
print("IR VALIDATION PASSED: 10/10 candidate Disciple IRs.")
