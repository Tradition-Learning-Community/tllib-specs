#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
FEATURE='TLC-FC-14-LIVED-EXPERIENCE-005'
ROOT=Path(__file__).resolve().parents[3]
def main():
    p=ROOT/'registry/ir'/FEATURE/'ir.yaml'
    d=yaml.safe_load(p.read_text(encoding='utf-8'))
    errors=[]
    if d.get('feature_id')!=FEATURE: errors.append('feature id mismatch')
    if d.get('contract_id')!='TLC-MC-'+FEATURE: errors.append('contract id mismatch')
    if d.get('contract_path')!=f'registry/math-contracts/{FEATURE}/contract.yaml': errors.append('canonical contract path mismatch')
    if 'ir/TLC-FC-14-LIVED-EXPERIENCE-005/ir-semantic.candidate.json' not in d.get('historical_inputs',[]): errors.append('historical candidate traceability missing')
    if d.get('readiness',{}).get('ready_for_production_implementation') is not False: errors.append('production readiness must remain false')
    if errors:
        print('IR VALIDATION FAILED: '+', '.join(errors)); return 1
    print('IR VALIDATION PASSED feature=TLC-FC-14-LIVED-EXPERIENCE-005 canonical_path=registry/ir/TLC-FC-14-LIVED-EXPERIENCE-005/ir.yaml')
    return 0
if __name__=='__main__': sys.exit(main())
