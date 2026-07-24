#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
F="TLC-FC-09-VALUES-018"; ROOT=Path(__file__).resolve().parents[3]; CD=ROOT/"registry/math-contracts"/F; RD=ROOT/"reports/math-contracts"/F
def main():
 e=[]; fs=list(CD.glob("*.yaml"))+list(RD.glob("*.yaml")); docs={}
 for p in fs:
  try: docs[p.name]=yaml.safe_load(p.read_text(encoding="utf-8"))
  except Exception as x:e.append(f"YAML {p}: {x}")
 wave=yaml.safe_load((ROOT/"registry/math-contract-entry/contract-wave-1.yaml").read_text(encoding="utf-8"))["feature_ids"]
 c=docs.get("contract.yaml",{}); s=docs.get("symbol-table.yaml",{}); tc=docs.get("type-constraints.yaml",{})
 if wave[3]!=F:e.append("wave position")
 if c.get("scientific_objects")!=["TLC-SO-VALUES-047"] or c.get("scientific_relations")!=[]:e.append("scope")
 declared={x["symbol_id"] for x in s.get("symbols",[])}
 if declared!={"SYM-C","SYM-M"}:e.append("symbols")
 if any(not set(x.get("referenced_symbols",[]))<=declared for x in tc.get("constraints",[])):e.append("constraint refs")
 if c.get("equations")!=[] or c.get("executable_oracle",{}).get("status")!="not_produced":e.append("excluded output")
 tex=(CD/"normalized-equations.tex").read_text(encoding="utf-8")
 if "[-1,1]^{m\\times m}" not in tex:e.append("source preservation")
 if e: print("VALIDATION FAILED: "+", ".join(e)); return 1
 print("CONTRACT VALIDATION PASSED feature=TLC-FC-09-VALUES-018 wave_position=4 artifacts=12"); return 0
if __name__=="__main__":sys.exit(main())
