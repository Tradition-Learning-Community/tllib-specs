#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
IDS=['001','003','004','005','006','007','008','009','010','011','012','013','014','018']
ROOT=Path(__file__).resolve().parents[2]
def main():
  errors=[]
  for n in IDS:
    fid=f'TLC-FC-09-VALUES-{n}'
    required=[ROOT/f'registry/math-contracts/{fid}/contract.yaml',ROOT/f'registry/ir/{fid}/ir.yaml',ROOT/f'registry/test-plans/{fid}/test-plan.yaml',ROOT/f'registry/optimized-ir/values/{fid}/ir.yaml',ROOT/f'registry/algorithms/values/{fid}/algorithm.yaml',ROOT/f'registry/oracles/values/{fid}/oracle.yaml']
    for p in required:
      if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}')
    for p in required[3:]:
      if p.exists() and fid not in p.read_text(): errors.append(f'{p.relative_to(ROOT)} missing feature id')
    ir=required[3]
    if ir.exists():
      text=ir.read_text()
      for token in ['source_contract_preserved: true','source_ir_preserved: true','replaces_source_ir: false','scientific_source_modified: false','value_invented: false','ordering_invented: false']:
        if token not in text: errors.append(f'{ir.relative_to(ROOT)} missing {token}')
  found=sorted(p.parent.name for p in (ROOT/'registry/optimized-ir/values').glob('*/ir.yaml'))
  expected=sorted(f'TLC-FC-09-VALUES-{n}' for n in IDS)
  if found!=expected: errors.append(f'population mismatch: {found}')
  changed=subprocess.check_output(['git','diff','--name-only','HEAD^','HEAD'],cwd=ROOT,text=True).splitlines()
  allowed=('registry/domain-finalization/values/','registry/optimized-ir/values/','registry/algorithms/values/','registry/oracles/values/','reports/domain-finalization/values/','tools/domain-finalization/validate_values_finalization.py','.github/workflows/validate-values-finalization.yml')
  for p in changed:
    if not any(p==a or p.startswith(a) for a in allowed): errors.append(f'forbidden changed path {p}')
    if p.startswith('maths/') or p.startswith('registry/global-reconciliation/'): errors.append(f'protected path changed {p}')
    if p.endswith(('.cpp','.cc','.cxx','.hpp','.h')): errors.append(f'C++ file {p}')
  if errors:
    for e in errors: print('ERROR:',e)
    return 1
  print('Values finalization validation passed: 14/14 features; traceability and conservation checks passed.')
  return 0
if __name__=='__main__': sys.exit(main())
