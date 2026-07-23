from pathlib import Path
import sys,yaml,json
R=Path(__file__).resolve().parents[1]; D=R/'registry/domain-progress/lived-experience'; errors=[]
def y(n):
 try:return yaml.safe_load((D/n).read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{n}: {e}'); return {}
required=['source-inventory.yaml','scientific-inventory.yaml','relation-inventory.yaml','scientific-coverage.yaml','pattern-analysis.yaml','concept-boundaries.yaml','feature-inventory.yaml','functional-coverage.yaml','feature-classification.yaml','external-dependencies.yaml','internal-dependencies.yaml','dependency-matrix.yaml','unresolved-status.yaml','historical-artifact-assessment.yaml','contract-production-plan.yaml','ir-production-plan.yaml','feature-readiness.yaml','preparation-manifest.yaml','decision-required.yaml','preparation-status.yaml']; docs={n:y(n) for n in required}
cat=yaml.safe_load((R/'registry/features/revised/feature-candidates.yaml').read_text(encoding='utf-8')); ids={f['candidate_feature_id'] for f in cat['features'] if f['candidate_feature_id'].startswith('TLC-FC-14-LIVED-EXPERIENCE-')}
expected={'objects':70,'relations':69,'unresolved':43,'duplicate_candidates':1,'features_total':12}
for k,v in expected.items():
 if docs['source-inventory.yaml'].get(k)!=v: errors.append(f'{k}: expected {v}')
if len(docs['scientific-inventory.yaml'].get('objects',[]))!=70: errors.append('object inventory')
if len(docs['relation-inventory.yaml'].get('relations',[]))!=69: errors.append('relation inventory')
if docs['unresolved-status.yaml'].get('source_total')!=43 or docs['unresolved-status.yaml'].get('covered')!=43 or docs['unresolved-status.yaml'].get('silently_resolved')!=0: errors.append('unresolved coverage')
for n,key in [('feature-inventory.yaml','features'),('contract-production-plan.yaml','plans'),('ir-production-plan.yaml','plans'),('feature-readiness.yaml','features')]:
 if {x['feature_id'] for x in docs[n].get(key,[])}!=ids: errors.append(f'{n} feature coverage')
if len(ids)!=12 or docs['functional-coverage.yaml'].get('orphan_features'): errors.append('feature uniqueness/orphans')
if docs['functional-coverage.yaml'].get('objects_accounted_for')!=70 or docs['functional-coverage.yaml'].get('relations_accounted_for')!=69 or docs['functional-coverage.yaml'].get('unresolved_accounted_for')!=43: errors.append('functional coverage')
if docs['contract-production-plan.yaml'].get('planned_contracts')!=12 or docs['contract-production-plan.yaml'].get('definitive_contracts_created')!=0: errors.append('contract plans')
if docs['ir-production-plan.yaml'].get('planned_irs')!=12 or docs['ir-production-plan.yaml'].get('definitive_irs_created')!=0: errors.append('IR plans')
ext={x['domain']:x for x in docs['external-dependencies.yaml'].get('dependencies',[])}
for d in ['capacities','competencies','practice']:
 if ext.get(d,{}).get('dependency_status')!='external_unreconciled' or ext.get(d,{}).get('confirmed'): errors.append(f'{d} dependency policy')
if docs['internal-dependencies.yaml'].get('cycles'): errors.append('internal cycle')
hist=docs['historical-artifact-assessment.yaml']
if any(x.get('modified') for x in hist.get('artifacts',[])) or hist.get('automatic_promotion') is not False: errors.append('historical pilot guard')
patterns=docs['pattern-analysis.yaml']
if 'lived experience is not silently equated with practice, memory, state, perception, or learning' not in patterns.get('explicit_non_equivalences',[]): errors.append('concept ambiguity guard')
s=docs['preparation-status.yaml']
for k in ['ready_for_full_contract_generation','ready_for_ir_generation','ready_for_implementation_planning','ready_for_code_generation']:
 if s.get(k) is not False: errors.append(f'gate {k}')
if s.get('preparation_status')!='preparation_complete_with_reservations': errors.append('status')
for p in R.rglob('*.yaml'):
 try:yaml.safe_load(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'YAML {p}: {e}')
for p in R.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'JSON {p}: {e}')
if errors: print('LIVED EXPERIENCE PREPARATION VALIDATION FAILED\n'+'\n'.join('- '+e for e in errors));sys.exit(1)
print('LIVED EXPERIENCE PREPARATION VALIDATION PASSED: 70 objects, 69 relations, 43 unresolved, 1 duplicate, 12 features/plans; pilot preserved; Practice/Capacities/Competencies unreconciled; no definitive contract, IR, or code.')
