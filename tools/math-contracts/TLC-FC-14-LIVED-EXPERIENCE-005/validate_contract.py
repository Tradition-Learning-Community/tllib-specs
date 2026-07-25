#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
FEATURE='TLC-FC-14-LIVED-EXPERIENCE-005'
ROOT=Path(__file__).resolve().parents[3]
def main():
    p=ROOT/'registry/math-contracts'/FEATURE/'contract.yaml'
    d=yaml.safe_load(p.read_text(encoding='utf-8'))
    errors=[]
    if d.get('feature_id')!=FEATURE: errors.append('feature id mismatch')
    if d.get('contract_id')!='TLC-MC-'+FEATURE: errors.append('contract id mismatch')
    if not d.get('covered_objects') or d['covered_objects'][0].get('object_id')!='TLC-SO-LIVED-EXPERIENCE-065': errors.append('covered object scope mismatch')
    if d.get('equations')!=['EQ-COLLECTIVE-MEMORY']: errors.append('exact equation identifier not preserved')
    if d.get('executable_oracle',{}).get('status')!='not_produced': errors.append('executable oracle must remain not_produced')
    if d.get('historical_pilot_audit',{}).get('classification')!='comparison_only_input_audited': errors.append('historical pilot audit missing')
    if errors:
        print('CONTRACT VALIDATION FAILED: '+', '.join(errors)); return 1
    print('CONTRACT VALIDATION PASSED feature=TLC-FC-14-LIVED-EXPERIENCE-005 canonical_path=registry/math-contracts/TLC-FC-14-LIVED-EXPERIENCE-005/contract.yaml')
    return 0
if __name__=='__main__': sys.exit(main())
