from pathlib import Path
import sys,yaml
R=Path(__file__).resolve().parents[1]; D=R/'registry/domain-progress/community'; errors=[]
def y(n):
 try:return yaml.safe_load((D/n).read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{n}: {e}'); return {}
required=['source-inventory.yaml','scientific-coverage.yaml','feature-inventory.yaml','functional-coverage.yaml','master-dependencies.yaml','disciple-dependencies.yaml','upstream-symbol-mapping.yaml','feature-dependencies.yaml','feature-classification.yaml','production-order.yaml','contract-production-plan.yaml','ir-production-plan.yaml','unresolved-status.yaml','production-gates.yaml','feature-status.yaml','historical-pilot-assessment.yaml']
docs={n:y(n) for n in required}; cat=yaml.safe_load((R/'registry/features/revised/feature-candidates.yaml').read_text(encoding='utf-8')); expected={f['candidate_feature_id'] for f in cat['features'] if f['candidate_feature_id'].startswith('TLC-FC-02-COMMUNITY-')}
if len(expected)!=8: errors.append('canonical feature count != 8')
for n,key in [('feature-inventory.yaml','features'),('feature-status.yaml','features'),('contract-production-plan.yaml','features'),('ir-production-plan.yaml','features')]:
 if {x['feature_id'] for x in docs[n].get(key,[])}!=expected: errors.append(f'{n} feature coverage')
if docs['functional-coverage.yaml'].get('objects_accounted_for')!=57 or docs['functional-coverage.yaml'].get('relations_accounted_for')!=56: errors.append('scientific coverage mismatch')
if docs['unresolved-status.yaml'].get('total')!=29: errors.append('unresolved coverage mismatch')
for n in ['master-dependencies.yaml','disciple-dependencies.yaml']:
 if any(x.get('dependency_status') not in ['confirmed','rejected_not_a_dependency'] for x in docs[n].get('dependencies',[])): errors.append(f'{n} not reconciled')
 if any(x.get('required_level')=='executable_semantics' for x in docs[n].get('dependencies',[])): errors.append(f'{n} invented executable dependency')
p=docs['historical-pilot-assessment.yaml'];
if p.get('audit_decision')!='reuse_schema_regenerate_content' or p.get('historical_preserved') is not True: errors.append('pilot audit incomplete')
g=docs['production-gates.yaml'];
for k,v in [('ready_for_contract_generation_now',True),('ready_for_full_contract_generation',True),('ready_for_ir_generation',False),('ready_for_implementation_planning',False),('ready_for_code_generation',False)]:
 if g.get(k) is not v: errors.append(f'gate {k}')
if docs['contract-production-plan.yaml'].get('contracts_created')!=0 or docs['ir-production-plan.yaml'].get('irs_created')!=0: errors.append('premature contract or IR claimed')
if errors: print('RECONCILIATION VALIDATION FAILED\n'+'\n'.join('- '+e for e in errors)); sys.exit(1)
print('RECONCILIATION VALIDATION PASSED: 8 features, 57 objects, 56 relations, 29 unresolved; upstream symbol-only mappings reconciled; pilot audited; no new contract or IR.')
