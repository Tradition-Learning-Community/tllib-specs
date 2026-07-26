#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
FEATURES = [
    'TLC-FC-08-PRINCIPLE-001','TLC-FC-08-PRINCIPLE-002','TLC-FC-08-PRINCIPLE-003',
    'TLC-FC-08-PRINCIPLE-004','TLC-FC-08-PRINCIPLE-005','TLC-FC-08-PRINCIPLE-006',
    'TLC-FC-08-PRINCIPLE-007','TLC-FC-08-PRINCIPLE-008','TLC-FC-08-PRINCIPLE-010',
    'TLC-FC-08-PRINCIPLE-011'
]
REQUIRED_ROOT = [
    'registry/domain-finalization/principle/manifest.yaml',
    'registry/domain-finalization/principle/feature-status.yaml',
    'registry/domain-finalization/principle/patterns.yaml',
    'registry/domain-finalization/principle/module-specification.yaml',
    'registry/domain-finalization/principle/implementation-tasks.yaml',
    'registry/domain-finalization/principle/decision-required.yaml',
    'reports/domain-finalization/principle/finalization-report.md'
]

def fail(message):
    print('FAIL:', message)
    raise SystemExit(1)

def read(path):
    p = ROOT / path
    if not p.is_file(): fail(f'missing {path}')
    return p.read_text(encoding='utf-8')

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def main():
    baseline = read('registry/global-reconciliation/current-baseline.yaml')
    if 'domain_id: principle' not in baseline or 'feature_count: 10' not in baseline:
        fail('baseline does not confirm Principle count 10')
    manifest = read(REQUIRED_ROOT[0])
    if 'active_feature_count: 10' not in manifest: fail('manifest count mismatch')
    for path in REQUIRED_ROOT: read(path)
    for feature in FEATURES:
        contract = f'registry/math-contracts/{feature}/contract.yaml'
        source_ir = f'registry/ir/{feature}/ir.yaml'
        test_plan = f'registry/test-plans/{feature}/test-plan.yaml'
        final_ir = f'registry/optimized-ir/principle/{feature}/ir.yaml'
        algorithm = f'registry/algorithms/principle/{feature}/algorithm.yaml'
        oracle = f'registry/oracles/principle/{feature}/oracle.yaml'
        for path in [contract, source_ir, test_plan, final_ir, algorithm, oracle]: read(path)
        ir_text = read(final_ir)
        for token in [feature, contract, source_ir, test_plan, algorithm, oracle,
                      'source_ir_preserved: true','source_contract_preserved: true',
                      'replaces_source_ir: false','scientific_source_modified: false',
                      'principle_invented: false','unresolved_propagated:',
                      'opaque_values:','conditions_of_application:']:
            if token not in ir_text: fail(f'{final_ir} missing {token}')
        if feature not in read(algorithm) or feature not in read(oracle):
            fail(f'IR-algorithm-oracle coherence failed for {feature}')
    optimized = ROOT / 'registry/optimized-ir/principle'
    actual = sorted(p.parent.name for p in optimized.glob('*/ir.yaml'))
    if actual != sorted(FEATURES): fail(f'population mismatch: {actual}')
    base = 'c34d40713bf444d38f92f76e1c6239ee596d5a18'
    changed = git('diff','--name-only',f'{base}...HEAD').splitlines()
    allowed_prefixes = (
        'registry/domain-finalization/principle/', 'registry/optimized-ir/principle/',
        'registry/algorithms/principle/', 'registry/oracles/principle/',
        'reports/domain-finalization/principle/', 'tools/domain-finalization/validate_principle_finalization.py',
        '.github/workflows/principle-finalization-validation.yml')
    bad = [p for p in changed if not p.startswith(allowed_prefixes)]
    if bad: fail(f'paths outside Principle scope: {bad}')
    forbidden = [p for p in changed if p.startswith('maths/') or p.startswith('registry/global-reconciliation/')]
    if forbidden: fail(f'forbidden source/global changes: {forbidden}')
    if any(p.endswith(('.cpp','.cc','.cxx','.hpp','.h')) for p in changed): fail('C++ file found')
    if any('binding' in p.lower() for p in changed): fail('binding file found')
    subprocess.check_call(['git','diff','--check',f'{base}...HEAD'], cwd=ROOT)
    print(f'PASS: Principle finalization validated for {len(FEATURES)} features')

if __name__ == '__main__': main()
