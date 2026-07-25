from pathlib import Path
import sys, yaml, json

FEATURE_IDS = ['TLC-FC-01-DISCIPLE-001', 'TLC-FC-01-DISCIPLE-002', 'TLC-FC-01-DISCIPLE-003', 'TLC-FC-01-DISCIPLE-004', 'TLC-FC-01-DISCIPLE-005', 'TLC-FC-01-DISCIPLE-006', 'TLC-FC-01-DISCIPLE-007', 'TLC-FC-01-DISCIPLE-008', 'TLC-FC-01-DISCIPLE-009', 'TLC-FC-01-DISCIPLE-010']
errors = []
for fid in FEATURE_IDS:
    paths = [
        Path(f"registry/math-contracts/{fid}/contract.yaml"),
        Path(f"registry/ir/{fid}/ir.yaml"),
        Path(f"registry/test-plans/{fid}/test-plan.yaml"),
        Path(f"ir/{fid}/ir.candidate.json"),
    ]
    for path in paths:
        if not path.is_file():
            errors.append(f"missing: {path}")
            continue
        try:
            if path.suffix == ".json":
                data = json.loads(path.read_text(encoding="utf-8-sig"))
            else:
                data = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
            if isinstance(data, dict) and data.get("feature_id") != fid:
                errors.append(f"feature_id mismatch: {path}")
        except Exception as exc:
            errors.append(f"parse error {path}: {exc}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("DISCIPLE DOMAIN COMPLETION VALIDATION PASSED features=10")
print("canonical_selection=false code_generation_ready=false")
