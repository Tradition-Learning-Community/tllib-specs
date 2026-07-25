from __future__ import annotations
from pathlib import Path
import sys, subprocess
try:
    import yaml
except ModuleNotFoundError:
    sys.path.append('/usr/lib/python3/dist-packages')
    import yaml
ROOT=Path(__file__).resolve().parents[1]
PREFIX='TLC-FC-12-COMPETENCIES-'
errors=[]
def load(p):
    try: return yaml.safe_load((ROOT/p).read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'invalid YAML {p}: {e}'); return {}
cat=load(Path('registry/domain-progress/competencies/feature-catalogue.yaml'))
features=[f['feature_id'] for f in cat.get('features',[]) if f.get('feature_id','').startswith(PREFIX)]
if len(features)!=13 or len(set(features))!=13: errors.append(f'feature count expected 13 got {len(features)}/{len(set(features))}')
for fid in features:
    c=Path(f'registry/math-contracts/{fid}/contract.yaml'); i=Path(f'registry/ir/{fid}/ir.yaml'); t=Path(f'registry/test-plans/{fid}/test-plan.yaml')
    for p in (c,i,t):
        if not (ROOT/p).exists(): errors.append(f'missing {p}')
    cy=load(c); iy=load(i); ty=load(t)
    if cy.get('feature_id')!=fid or cy.get('contract_id')!=f'TLC-MC-{fid}': errors.append(f'contract id mismatch {fid}')
    if iy.get('feature_id')!=fid or iy.get('contract_id')!=cy.get('contract_id') or iy.get('contract_path')!=str(c): errors.append(f'IR contract reference mismatch {fid}')
    if ty.get('feature_id')!=fid or ty.get('contract_id')!=cy.get('contract_id') or ty.get('ir_id')!=iy.get('ir_id'): errors.append(f'test plan reference mismatch {fid}')
    if set(cy.get('inputs',[{},{}])[1].get('required_keys',[])) != set(next(f for f in cat['features'] if f['feature_id']==fid).get('source_objects',[])): errors.append(f'covered objects mismatch {fid}')
    if cy.get('execution_status') is None: errors.append(f'execution status missing {fid}')
    if 'readiness' not in iy or 'python' not in iy['readiness'] or 'cpp' not in iy['readiness']: errors.append(f'IR readiness missing {fid}')
new_artifacts=list(ROOT.rglob('artifact.yaml'))
# Existing artifact.yaml files would be reported only if under competencies canonical outputs.
if any(PREFIX in str(p) for p in new_artifacts): errors.append('new competencies artifact.yaml found')
changed=subprocess.run(['git','diff','--name-only','HEAD'],cwd=ROOT,text=True,capture_output=True).stdout.splitlines()
if any(p.startswith('maths/') for p in changed): errors.append('maths/ modified')
allowed_prefixes=('registry/math-contracts/TLC-FC-12-COMPETENCIES-','registry/ir/TLC-FC-12-COMPETENCIES-','registry/test-plans/TLC-FC-12-COMPETENCIES-','registry/domain-progress/competencies/','registry/ir-batches/competencies-domain-completion-001/','reports/ir-batches/competencies-domain-completion-001/','scripts/validate_competencies_domain.py')
bad=[p for p in changed if not p.startswith(allowed_prefixes)]
if bad: errors.append(f'out-of-scope paths: {bad}')
if errors:
    print('COMPETENCIES DOMAIN VALIDATION FAILED')
    print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('COMPETENCIES DOMAIN VALIDATION PASSED')
print('features=13 contracts=13 irs=13 test_plans=13')
print('maths_modified=false new_artifact_yaml=false ir_contract_references=true test_plan_feature_references=true')
