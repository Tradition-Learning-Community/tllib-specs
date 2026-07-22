from pathlib import Path
import sys,yaml,json
R=Path(__file__).resolve().parents[1]; D=R/'registry/domain-progress/virtues'; P=R/'reports/domain-progress/virtues'; errors=[]
def y(n):
 try:return yaml.safe_load((D/n).read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{n}: {e}');return {}
required=['source-inventory.yaml','scientific-inventory.yaml','relation-inventory.yaml','scientific-coverage.yaml','virtue-semantics.yaml','virtue-structure.yaml','concept-separation.yaml','feature-inventory.yaml','functional-coverage.yaml','feature-classification.yaml','external-domain-dependencies.yaml','internal-dependencies.yaml','dependency-graph.yaml','unresolved-status.yaml','historical-artifact-assessment.yaml','production-order.yaml','contract-production-plan.yaml','ir-production-plan.yaml','production-readiness.yaml','preparation-status.yaml']; docs={n:y(n) for n in required}
for n in ['master','disciple','community','huit_dimensions','invariants','dynamics','theorems','message','principle','values','capacities','competencies','practice','lived_experience','relations']:
 y(n+'-dependencies.yaml')
cat=yaml.safe_load((R/'registry/features/revised/feature-candidates.yaml').read_text(encoding='utf-8')); ids={f['candidate_feature_id'] for f in cat['features'] if f['candidate_feature_id'].startswith('TLC-FC-10-VIRTUES-')}
if len(ids)!=10: errors.append('canonical feature count')
if len(docs['scientific-inventory.yaml'].get('objects',[]))!=218: errors.append('object coverage')
if len(docs['relation-inventory.yaml'].get('relations',[]))!=217: errors.append('relation coverage')
if docs['unresolved-status.yaml'].get('source_unresolved_total')!=171 or docs['unresolved-status.yaml'].get('unresolved_covered')!=171: errors.append('unresolved coverage')
for n,key in [('feature-inventory.yaml','features'),('contract-production-plan.yaml','plans'),('ir-production-plan.yaml','plans')]:
 if {x['feature_id'] for x in docs[n].get(key,[])}!=ids: errors.append(f'{n} feature coverage')
if docs['contract-production-plan.yaml'].get('definitive_contracts_created')!=0 or docs['ir-production-plan.yaml'].get('definitive_irs_created')!=0: errors.append('premature production')
if docs['virtue-structure.yaml'].get('hierarchy')!='not_explicit' or docs['virtue-structure.yaml'].get('ordering')!='not_explicit': errors.append('invented structure')
value=[x for x in docs['concept-separation.yaml'].get('comparisons',[]) if x['pair']=='Virtue vs Value']
if not value or value[0]['classification']!='explicit_non_equivalence': errors.append('Value separation')
if docs['internal-dependencies.yaml'].get('cycles'): errors.append('unclassified cycle')
for x in docs['external-domain-dependencies.yaml'].get('dependencies',[]):
 if x.get('confirmed'): errors.append(f"unjustified confirmed dependency {x['domain']}")
s=docs['preparation-status.yaml']
for k in ['ready_for_full_contract_generation','ready_for_ir_generation','ready_for_implementation_planning','ready_for_code_generation']:
 if s.get(k) is not False: errors.append(f'gate {k}')
if s.get('preparation_status')!='preparation_complete_with_reservations': errors.append('preparation status')
for p in R.rglob('*.yaml'):
 try:yaml.safe_load(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'YAML {p}: {e}')
for p in R.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'JSON {p}: {e}')
if errors: print('VIRTUES PREPARATION VALIDATION FAILED\n'+'\n'.join('- '+e for e in errors));sys.exit(1)
print('VIRTUES PREPARATION VALIDATION PASSED: 218 objects, 217 relations, 171 unresolved, 10 features, 10 contract plans, 10 IR plans; no definitive contract, IR, code, hierarchy, or confirmed noncanonical dependency.')
