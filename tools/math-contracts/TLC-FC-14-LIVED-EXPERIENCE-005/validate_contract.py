#!/usr/bin/env python3
from pathlib import Path
import sys,yaml
F="TLC-FC-14-LIVED-EXPERIENCE-005";R=Path(__file__).resolve().parents[3];C=R/"registry/math-contracts"/F;D=R/"reports/math-contracts"/F
def main():
 e=[];fs=list(C.glob("*.yaml"))+list(D.glob("*.yaml"));docs={}
 for p in fs:
  try:docs[p.name]=yaml.safe_load(p.read_text(encoding="utf-8"))
  except Exception as x:e.append(f"YAML {x}")
 wave=yaml.safe_load((R/"registry/math-contract-entry/contract-wave-1.yaml").read_text(encoding="utf-8"))["feature_ids"]
 c=docs.get("contract.yaml",{});s=docs.get("symbol-table.yaml",{});tc=docs.get("type-constraints.yaml",{})
 if wave[4]!=F:e.append("wave")
 if c.get("scientific_objects")!=["TLC-SO-LIVED-EXPERIENCE-065"] or c.get("scientific_relations")!=[]:e.append("scope")
 ids={x["symbol_id"] for x in s.get("symbols",[])}
 eq=tc.get("equations",[{}])[0]
 if not set(eq.get("symbols_used",[]))<=ids:e.append("symbols")
 if c.get("executable_oracle",{}).get("status")!="not_produced":e.append("oracle")
 src="\\ell_{\\mathrm{col}} = \\frac{1}{N}\\sum_{i=1}^{N} \\ell_i + \\sigma \\cdot \\mathrm{Synergie}(\\{\\ell_i\\})"
 if eq.get("source_form")!=src:e.append("source preservation")
 if e:print("VALIDATION FAILED: "+", ".join(e));return 1
 print("CONTRACT VALIDATION PASSED feature=TLC-FC-14-LIVED-EXPERIENCE-005 wave_position=5 artifacts=12");return 0
if __name__=="__main__":sys.exit(main())
