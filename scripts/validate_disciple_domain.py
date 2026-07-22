from pathlib import Path
import json,sys,yaml
ROOT=Path(__file__).resolve().parents[1]; errors=[]
status=yaml.safe_load((ROOT/"registry/domain-progress/disciple/domain-status.yaml").read_text(encoding="utf-8"))
if status.get("domain_status") != "complete_to_ir_with_reservations": errors.append("domain status invalid")
if status.get("features",{}).get("contract_complete") != 10 or status.get("features",{}).get("ir_complete") != 10: errors.append("domain feature totals invalid")
ua=yaml.safe_load((ROOT/"registry/domain-progress/disciple/unresolved-audit.yaml").read_text(encoding="utf-8"))
if (ua.get("source_unresolved"),ua.get("contract_propagated"),ua.get("ir_propagated"),ua.get("silently_removed")) != (32,32,32,0): errors.append("unresolved propagation invalid")
ma=yaml.safe_load((ROOT/"registry/domain-progress/disciple/master-dependency-audit.yaml").read_text(encoding="utf-8"))
if (ma.get("confirmed"),ma.get("propagated_to_contracts"),ma.get("propagated_to_irs"),ma.get("unresolved_subsymbols")) != (4,4,4,3): errors.append("Master dependency audit invalid")
for path in ["registry/pipeline-status/source-status.yaml","registry/pipeline-status/feature-status.yaml","registry/pipeline-status/git-publication-status.yaml"]:
    d=yaml.safe_load((ROOT/path).read_text(encoding="utf-8")); dp=d.get("domain_progress",{}).get("disciple",{})
    if dp.get("domain_status") != "complete_to_ir_with_reservations" or dp.get("contracts_total") != 10 or dp.get("irs_total") != 10: errors.append(f"manifest invalid {path}")
if list(ROOT.glob("**/*.cpp")) or list(ROOT.glob("**/*.hpp")): errors.append("C++ file detected")
if errors: print("DOMAIN VALIDATION FAILED\n"+"\n".join(errors)); sys.exit(1)
print("DOMAIN VALIDATION PASSED: Disciple complete to candidate IR with reservations.")
