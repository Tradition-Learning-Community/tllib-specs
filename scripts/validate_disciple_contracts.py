from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]; PREFIX="TLC-FC-01-DISCIPLE-"; errors=[]
expected={f"{PREFIX}{i:03d}" for i in range(1,11)}; found=set()
for p in ROOT.glob(f"registry/math-contracts/{PREFIX}*/contract.yaml"):
    try: d=yaml.safe_load(p.read_text(encoding="utf-8")); found.add(d["feature_id"])
    except Exception as e: errors.append(f"{p}: {e}"); continue
    if d.get("contract_id") != f"TLC-MC-{d['feature_id']}": errors.append(f"bad contract ID {p}")
    if d.get("execution_readiness") is not False or d.get("code_generation_readiness") is not False: errors.append(f"readiness violation {p}")
    for oid in d.get("master_symbol_dependencies", []):
        if oid != "TLC-SO-MASTER-001": errors.append(f"invalid Master symbol {oid}")
if found != expected: errors.append(f"contract coverage mismatch: {sorted(expected-found)}")
audit=yaml.safe_load((ROOT/"registry/domain-progress/disciple/contract-audit.yaml").read_text(encoding="utf-8"))
if audit.get("contracts_validated") != 10 or audit.get("decision") != "proceed_to_ir_with_reservations": errors.append("contract audit invalid")
if errors: print("CONTRACT VALIDATION FAILED\n"+"\n".join(errors)); sys.exit(1)
print("CONTRACT VALIDATION PASSED: 10/10 conservative Disciple contracts.")
