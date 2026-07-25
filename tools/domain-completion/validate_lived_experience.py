#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[2]
PREFIX='TLC-FC-14-LIVED-EXPERIENCE'
EXPECTED=12

def load(p):
    with p.open(encoding='utf-8') as f: return yaml.safe_load(f)

def main():
    errors=[]
    manifest=load(ROOT/'execution-manifests/wave-3/lived-experience-domain-completion.yaml')
    features=load(ROOT/'registry/domain-progress/lived-experience/feature-inventory.yaml')['features']
    ids=[f['feature_id'] for f in features]
    if len(ids)!=EXPECTED or len(set(ids))!=EXPECTED: errors.append('feature catalogue count mismatch')
    if any(not x.startswith(PREFIX) for x in ids): errors.append('feature prefix mismatch')
    for fid in ids:
        c=ROOT/'registry/math-contracts'/fid/'contract.yaml'
        i=ROOT/'registry/ir'/fid/'ir.yaml'
        t=ROOT/'registry/test-plans'/fid/'test-plan.yaml'
        for p in (c,i,t):
            if not p.exists(): errors.append(f'missing {p}')
        if not (c.exists() and i.exists() and t.exists()): continue
        cd,ir,tp=load(c),load(i),load(t)
        if cd.get('feature_id')!=fid: errors.append(f'contract feature mismatch {fid}')
        if ir.get('feature_id')!=fid or ir.get('contract_id')!=cd.get('contract_id'): errors.append(f'ir linkage mismatch {fid}')
        if ir.get('contract_path')!=f'registry/math-contracts/{fid}/contract.yaml': errors.append(f'ir contract path mismatch {fid}')
        if tp.get('feature_id')!=fid or tp.get('contract_id')!=cd.get('contract_id') or tp.get('ir_id')!=ir.get('ir_id'): errors.append(f'test plan linkage mismatch {fid}')
        for ref in cd.get('source_references',[]):
            sp=ROOT/ref.get('source_path','')
            if not sp.exists(): errors.append(f'missing source path {sp}')
    new_artifacts=list(ROOT.glob('**/artifact.yaml'))
    if new_artifacts: errors.append('artifact.yaml present: '+', '.join(map(str,new_artifacts[:5])))
    # staged/working diff must not include maths/
    import subprocess
    diff=subprocess.check_output(['git','diff','--name-only'],cwd=ROOT,text=True).splitlines()+subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
    if any(p.startswith('maths/') for p in diff): errors.append('maths modification detected')
    if errors:
        print('LIVED EXPERIENCE DOMAIN VALIDATION FAILED')
        for e in errors: print('-',e)
        return 1
    print(f'LIVED EXPERIENCE DOMAIN VALIDATION PASSED features={EXPECTED} contracts={EXPECTED} ir={EXPECTED} test_plans={EXPECTED}')
    return 0
if __name__=='__main__': sys.exit(main())
