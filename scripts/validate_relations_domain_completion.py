#!/usr/bin/python3
from pathlib import Path
import sys
try:
    import yaml
except Exception as exc:
    print(f'PyYAML unavailable: {exc}')
    sys.exit(2)
ROOT=Path(__file__).resolve().parents[1]
FEATURES=['TLC-FC-15-RELATIONS-002','TLC-FC-15-RELATIONS-003','TLC-FC-15-RELATIONS-004','TLC-FC-15-RELATIONS-007','TLC-FC-15-RELATIONS-008']
errors=[]
for fid in FEATURES:
    paths=[ROOT/'registry/math-contracts'/fid/'contract.yaml', ROOT/'registry/ir'/fid/'ir.yaml', ROOT/'registry/test-plans'/fid/'test-plan.yaml']
    for p in paths:
        if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}'); continue
        data=yaml.safe_load(p.read_text())
        if data.get('feature_id')!=fid: errors.append(f'feature mismatch {p.relative_to(ROOT)}')
    irp=paths[1]; tpp=paths[2]
    if irp.exists() and yaml.safe_load(irp.read_text()).get('contract_path')!=f'registry/math-contracts/{fid}/contract.yaml': errors.append(f'bad contract ref {fid}')
    if tpp.exists() and yaml.safe_load(tpp.read_text()).get('ir_path')!=f'registry/ir/{fid}/ir.yaml': errors.append(f'bad ir ref {fid}')
if list(ROOT.glob('**/artifact.yaml')): errors.append('artifact.yaml present')
if errors:
    print('relations domain completion validation failed')
    print('\n'.join(errors)); sys.exit(1)
print(f'relations domain completion validation passed: {len(FEATURES)} features, contracts/IR/test-plans present')
