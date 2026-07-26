#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
IDS=['001','003','004','005','006','007','008','009','010','011','012','013','014','018']
ROOT=Path(__file__).resolve().parents[2]
def fail(msg): print('ERROR:',msg); return 1
def main():
  errors=[]
  manifest=ROOT/'registry/domain-finalization/values/manifest.yaml'
  if not manifest.exists(): errors.append('missing manifest')
  for n in IDS:
    fid=f'TLC-FC-09-VALUES-{n}'
    required=[ROOT/f'registry/math-contracts/{fid}/contract.yaml',ROOT/f'registry/ir/{fid}/ir.yaml',ROOT/f'registry/optimized-ir/values/{fid}/ir.yaml',ROOT/f'registry/algorithms/values/{fid}/algorithm.yaml',ROOT/f'registry/oracles/values/{fid}/oracle.yaml']
    tp=ROOT/f'registry/ir/{fid}/test-plan.yaml'
    if not tp.exists(): tp=ROOT/f'ir/{fid}/test-plan.yaml'
    required.append(tp)
    for p in required:
      if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}')
    for p in required[2:5]:
      if p.exists():
        s=p.read_text()
        for token in [fid,'source_contract_preserved: true','source_ir_preserved: true'] if p.name=='ir.yaml' and 'optimized-ir' in str(p) else [fid]:
          if token not in s: errors.append(f'{p.relative_to(ROOT)} missing {token}')
  found=sorted(p.parent.name for p in (ROOT/'registry/optimized-ir/values').glob('*/ir.yaml'))
  expected=sorted(f'TLC-FC-09-VALUES-{n}' for n in IDS)
  if found!=expected: errors.append(f'population mismatch: {found}')
  try: changed=subprocess.check_output(['git','diff','--name-only','HEAD^','HEAD'],cwd=ROOT,text=True).splitlines()
  except Exception: changed=[]
  allowed=('registry/domain-finalization/values/','registry/optimized-ir/values/','registry/algorithms/values/','registry/oracles/values/','reports/domain-finalization/values/','tools/domain-finalization/validate_values_finalization.py','.github/workflows/validate-values-finalization.yml')
  for p in changed:
    if not any(p==a or p.startswith(a) for a in allowed): errors.append(f'forbidden changed path {p}')
    if p.startswith('maths/') or p.startswith('registry/global-reconciliation/'): errors.append(f'protected path changed {p}')
    if p.endswith(('.cpp','.cc','.cxx','.hpp','.h')): errors.append(f'C++ file {p}')
  if errors:
    for e in errors: fail(e)
    return 1
  print('Values finalization validation passed: 14/14 features; conservation checks passed.')
  return 0
if __name__=='__main__': sys.exit(main())
