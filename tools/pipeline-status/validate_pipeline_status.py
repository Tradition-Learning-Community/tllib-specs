#!/usr/bin/env python3
from pathlib import Path
import yaml
root=Path(__file__).resolve().parents[2]
files=[root/'registry/pipeline-status/source-status.yaml',root/'registry/pipeline-status/feature-status.yaml',root/'registry/pipeline-status/git-publication-status.yaml',root/'registry/pipeline-status/pilot-ir-audit.yaml',root/'reports/pipeline-status/decision_required.yaml']
docs=[]
for p in files:
    assert p.is_file(),p
    with open(p,encoding='utf-8') as f: docs.append(yaml.safe_load(f))
assert docs[0]['count']==16
assert docs[1]['count']==224
assert docs[3]['pilot_count_expected']==5 and docs[3]['pilot_contracts_present']==5 and docs[3]['pilot_irs_present']==5
ids=[x['feature_id'] for x in docs[1]['features']]
assert len(ids)==len(set(ids))
print('pipeline-status validation: PASS (16 sources, 224 features, 5 contracts, 5 available IRs)')
