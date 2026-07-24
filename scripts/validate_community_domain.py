from pathlib import Path
import sys,yaml,json,subprocess
R=Path(__file__).resolve().parents[1]; errors=[]
def y(p): return yaml.safe_load((R/p).read_text(encoding='utf-8'))
for p in R.rglob('*.yaml'):
 try:yaml.safe_load(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'YAML {p}: {e}')
for p in R.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'JSON {p}: {e}')
cat=y('registry/features/revised/feature-candidates.yaml'); allids=[f['candidate_feature_id'] for f in cat['features']]
if len(allids)!=224 or len(allids)!=len(set(allids)): errors.append('canonical 224 identifiers')
s=y('registry/domain-progress/community/domain-status.yaml'); expected={'objects':57,'relations':56,'unresolved':29,'features':8,'contracts':8,'validated_contracts':8,'irs':8,'validated_irs':8}
for k,v in expected.items():
 if s.get(k)!=v: errors.append(f'{k} != {v}')
u=y('registry/domain-progress/community/unresolved-audit.yaml')
for k,v in {'source_unresolved':29,'contract_propagated':29,'ir_propagated':29,'silently_removed':0,'arbitrarily_resolved':0}.items():
 if u.get(k)!=v: errors.append(f'unresolved {k}')
if s.get('domain_status')!='complete_to_ir_with_reservations' or s.get('ready_for_implementation_planning') is not False or s.get('ready_for_code_generation') is not False: errors.append('domain gates')
if s.get('master_scientific_modifications') or s.get('disciple_scientific_modifications') or s.get('huit_dimensions_production') or s.get('cpp_generated') or s.get('python_bindings_generated'): errors.append('scope guard')
if errors: print('DOMAIN VALIDATION FAILED\n'+'\n'.join(errors));sys.exit(1)
print('DOMAIN VALIDATION PASSED: YAML/JSON parse, 224 unique canonical features, Community 57/56/29/8/8/8, scope and readiness gates valid.')
