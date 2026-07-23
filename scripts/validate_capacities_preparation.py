from pathlib import Path
import sys,yaml,json,subprocess
R=Path(__file__).resolve().parents[1]; D=R/'registry/domain-progress/capacities'; errors=[]
def y(n):
 try:return yaml.safe_load((D/n).read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{n}: {e}'); return {}
required=['goose-audit.yaml','source-inventory.yaml','scientific-inventory.yaml','relation-inventory.yaml','scientific-coverage.yaml','pattern-analysis.yaml','feature-inventory.yaml','functional-coverage.yaml','feature-classification.yaml','external-dependencies.yaml','internal-dependencies.yaml','dependency-matrix.yaml','unresolved-status.yaml','contract-production-plan.yaml','ir-production-plan.yaml','feature-readiness.yaml','decision-required.yaml','preparation-status.yaml']; docs={n:y(n) for n in required}
cat=yaml.safe_load((R/'registry/features/revised/feature-candidates.yaml').read_text(encoding='utf-8')); ids={f['candidate_feature_id'] for f in cat['features'] if f['candidate_feature_id'].startswith('TLC-FC-11-CAPACITIES-')}
if len(ids)!=15 or any(x.startswith('TLC-FC-11-CAP-') for x in ids): errors.append('canonical feature identifiers')
for k,v in {'objects':100,'relations':99,'unresolved':54,'duplicate_candidates':1,'features_total':15}.items():
 if docs['source-inventory.yaml'].get(k)!=v: errors.append(f'{k} count')
if len(docs['scientific-inventory.yaml'].get('objects',[]))!=100: errors.append('object coverage')
if len(docs['relation-inventory.yaml'].get('relations',[]))!=99: errors.append('relation coverage')
if docs['unresolved-status.yaml'].get('source_total')!=54 or docs['unresolved-status.yaml'].get('covered')!=54 or docs['unresolved-status.yaml'].get('silently_resolved')!=0: errors.append('unresolved coverage')
for n,key in [('feature-inventory.yaml','features'),('contract-production-plan.yaml','plans'),('ir-production-plan.yaml','plans'),('feature-readiness.yaml','features')]:
 if {x['feature_id'] for x in docs[n].get(key,[])}!=ids: errors.append(f'{n} feature coverage')
fc=docs['functional-coverage.yaml']
if fc.get('objects_accounted_for')!=100 or fc.get('relations_accounted_for')!=99 or fc.get('unresolved_accounted_for')!=54 or fc.get('orphan_features'): errors.append('functional/orphan coverage')
if docs['contract-production-plan.yaml'].get('planned_contracts')!=15 or docs['contract-production-plan.yaml'].get('definitive_contracts_created')!=0: errors.append('contract plans')
if docs['ir-production-plan.yaml'].get('planned_irs')!=15 or docs['ir-production-plan.yaml'].get('definitive_irs_created')!=0: errors.append('IR plans')
if docs['internal-dependencies.yaml'].get('cycles'): errors.append('cycles')
if any(x.get('confirmed') for x in docs['external-dependencies.yaml'].get('dependencies',[])): errors.append('unjustified external dependency')
if docs['external-dependencies.yaml'].get('noncanonical_branches_used_as_authority') is not False: errors.append('authority guard')
defects={x['defect'] for x in docs['goose-audit.yaml'].get('detected_defects',[])}
for x in ['feature_identifier_namespace_mismatch','incomplete_feature_coverage','missing_validator','contract_and_ir_plans_are_wave_lists_only']:
 if x not in defects: errors.append(f'missing Goose audit defect {x}')
s=docs['preparation-status.yaml']
for k in ['ready_for_full_contract_generation','ready_for_ir_generation','ready_for_implementation_planning','ready_for_code_generation']:
 if s.get(k) is not False: errors.append(f'gate {k}')
for o in docs['scientific-inventory.yaml'].get('objects',[]):
 ref=o.get('source_reference',{}); p=R/ref.get('source_path','')
 if not p.is_file() or not ref.get('start_line') or not ref.get('end_line'): errors.append(f"invalid object source reference {o.get('object_id')}")
for p in R.rglob('*.yaml'):
 try:yaml.safe_load(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'YAML {p}: {e}')
for p in R.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'JSON {p}: {e}')
changed=subprocess.run(['git','diff','--name-only','origin/main...HEAD'],cwd=R,text=True,capture_output=True,check=True).stdout.splitlines()
allowed=('registry/domain-preparation/capacities/','reports/domain-preparation/capacities/','registry/domain-progress/capacities/','reports/domain-progress/capacities/','scripts/build_capacities_preparation.py','scripts/validate_capacities_preparation.py')
for p in changed:
 if not p.startswith(allowed): errors.append(f'out of scope: {p}')
if any(p.startswith(('registry/math-contracts/','ir/','src/','bindings/')) for p in changed): errors.append('final artifact or code scope violation')
if errors: print('CAPACITIES PREPARATION VALIDATION FAILED\n'+'\n'.join('- '+e for e in errors));sys.exit(1)
print('CAPACITIES PREPARATION VALIDATION PASSED: 100 objects, 99 relations, 54 unresolved, 1 duplicate, 15 canonical features/plans; Goose defects audited; no final contract, IR, or code.')
