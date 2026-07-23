from pathlib import Path
import sys,yaml
R=Path(__file__).resolve().parents[1]; cat=yaml.safe_load((R/'registry/features/revised/feature-candidates.yaml').read_text(encoding='utf-8')); ids=sorted(f['candidate_feature_id'] for f in cat['features'] if f['candidate_feature_id'].startswith('TLC-FC-02-COMMUNITY-')); errors=[]; required=['feature_id','canonical_name','source_file','source_objects','source_relations','source_locations','scientific_status','contract_kind','computational_status','inputs','outputs','variables','parameters','constants','states','spaces','sets','functions','operators','relations','equations','constraints','invariants','assumptions','preconditions','postconditions','failure_conditions','determinism','stochasticity','dimensional_information','master_dependencies','disciple_dependencies','external_dependencies','unresolved','execution_readiness','implementation_planning_readiness','code_generation_readiness','validation_status']
for fid in ids:
 p=R/'registry/math-contracts'/fid/'contract.yaml'
 try:c=yaml.safe_load(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{fid}: {e}'); continue
 if c.get('feature_id')!=fid: errors.append(f'{fid}: identity')
 if [k for k in required if k not in c]: errors.append(f'{fid}: missing fields')
 if len({x['unresolved_id'] for x in c.get('unresolved',[])})!=29: errors.append(f'{fid}: unresolved')
 if c.get('execution_readiness') is not False or c.get('implementation_planning_readiness') is not False or c.get('code_generation_readiness') is not False: errors.append(f'{fid}: readiness')
if len(ids)!=8: errors.append('feature count')
if errors: print('CONTRACT VALIDATION FAILED\n'+'\n'.join(errors));sys.exit(1)
print('CONTRACT VALIDATION PASSED: 8 canonical contracts, complete schemas, 29 unresolved preserved, execution and code gates false.')
