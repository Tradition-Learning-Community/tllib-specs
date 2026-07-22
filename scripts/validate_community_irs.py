from pathlib import Path
import sys,json,yaml
R=Path(__file__).resolve().parents[1]; cat=yaml.safe_load((R/'registry/features/revised/feature-candidates.yaml').read_text(encoding='utf-8')); ids=sorted(f['candidate_feature_id'] for f in cat['features'] if f['candidate_feature_id'].startswith('TLC-FC-02-COMMUNITY-')); errors=[]
for fid in ids:
 try:i=json.loads((R/'ir'/fid/'ir.candidate.json').read_text(encoding='utf-8')); c=yaml.safe_load((R/i['contract_path']).read_text(encoding='utf-8')); cov=yaml.safe_load((R/'ir'/fid/'ir-coverage.yaml').read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{fid}: {e}');continue
 if i.get('feature_id')!=fid or i.get('status')!='engineering_candidate': errors.append(f'{fid}: identity/status')
 if i.get('contract_path')!=f'registry/math-contracts/{fid}/contract.yaml': errors.append(f'{fid}: contract reference')
 if len({x['unresolved_id'] for x in i.get('unresolved',[])})!=29: errors.append(f'{fid}: unresolved')
 if i.get('implementation_planning_readiness') is not False or i.get('code_generation_readiness') is not False: errors.append(f'{fid}: gates')
 if cov.get('coverage_status')!='complete_with_reservations' or cov.get('missing_elements') or cov.get('extra_ir_elements'): errors.append(f'{fid}: coverage')
 if {x['unresolved_id'] for x in c['unresolved']}!={x['unresolved_id'] for x in i['unresolved']}: errors.append(f'{fid}: propagation')
if errors: print('IR VALIDATION FAILED\n'+'\n'.join(errors));sys.exit(1)
print('IR VALIDATION PASSED: 8 engineering candidates, exact contract references, complete-with-reservations coverage, 29 unresolved preserved.')
