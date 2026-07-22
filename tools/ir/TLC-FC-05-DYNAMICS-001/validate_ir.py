#!/usr/bin/env python3
from pathlib import Path
import re, subprocess, sys, yaml
F="TLC-FC-05-DYNAMICS-001"; ROOT=Path(__file__).resolve().parents[3]; ID=ROOT/"ir"/F; RD=ROOT/"reports/ir"/F
EXPECTED=["manifest.yaml","ir.yaml","types.yaml","nodes.yaml","operations.yaml","constraints.yaml","unresolved.yaml","traceability.yaml","issues.yaml"]
def load(p): return yaml.safe_load(p.read_text(encoding="utf-8"))
def main():
 e=[]; docs={}
 for n in EXPECTED:
  p=ID/n
  try: docs[n]=load(p)
  except Exception as x:e.append(f"{n}: {x}")
 try: load(RD/"decision_required.yaml")
 except Exception as x:e.append(f"decision YAML: {x}")
 m=docs.get("manifest.yaml",{}); ir=docs.get("ir.yaml",{}); nodes=docs.get("nodes.yaml",{}); ops=docs.get("operations.yaml",{}); cons=docs.get("constraints.yaml",{}); unr=docs.get("unresolved.yaml",{})
 if m.get("source",{}).get("contract_commit")!="41028d616ab28af0ae1ba2f328c8bb8add2d68dd":e.append("wrong contract commit")
 if m.get("status")!="engineering_candidate" or m.get("scientific_validation")!="pending":e.append("wrong statuses")
 if ir.get("feature_id")!=F or ir.get("executable") is not False:e.append("identity/executable")
 node_ids={x["node_id"] for x in nodes.get("nodes",[])}; op_ids={x["operation_id"] for x in ops.get("operations",[])}; pred_ids={x["predicate_id"] for x in cons.get("predicates",[])}
 if len(node_ids)!=len(nodes.get("nodes",[])) or len(op_ids)!=len(ops.get("operations",[])) or len(pred_ids)!=4:e.append("identifier/count")
 if pred_ids!={"IR-CON-SIZE","IR-CON-CONNECTIVITY","IR-CON-VALUES","IR-CON-MEMORY"}:e.append("predicate preservation")
 if {x["unresolved_id"] for x in unr.get("items",[])}!={"UNRES-TIME","UNRES-L","UNRES-NORM","UNRES-MEMORY-NOTATION","UNRES-OUTPUT"}:e.append("unresolved propagation")
 text="\n".join(p.read_text(encoding="utf-8") for p in list(ID.iterdir())+list(RD.iterdir()) if p.is_file())
 forbidden=re.compile(r"\b(?:numpy|Eigen|std::|float32|float64|Runge.Kutta|Euler method|tolerance\s*:\s*[0-9])\b",re.I)
 if forbidden.search(text):e.append("implementation/numerical choice introduced")
 contract=load(ROOT/"registry/math-contracts"/F/"contract.yaml")
 if contract.get("constraints")!=["CON-SIZE","CON-CONNECTIVITY","CON-VALUES","CON-MEMORY"]:e.append("source contract constraints changed")
 if e: print("IR VALIDATION FAILED\n- "+"\n- ".join(e)); return 1
 print("IR VALIDATION PASSED feature=TLC-FC-05-DYNAMICS-001 predicates=4 unresolved=5 artifacts=13"); return 0
if __name__=="__main__":sys.exit(main())
