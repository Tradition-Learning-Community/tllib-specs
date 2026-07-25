from pathlib import Path
import sys, yaml, json

FEATURE_IDS = ['TLC-FC-02-COMMUNITY-001', 'TLC-FC-02-COMMUNITY-003', 'TLC-FC-02-COMMUNITY-004', 'TLC-FC-02-COMMUNITY-005', 'TLC-FC-02-COMMUNITY-006', 'TLC-FC-02-COMMUNITY-007', 'TLC-FC-02-COMMUNITY-008', 'TLC-FC-02-COMMUNITY-009']
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
print("COMMUNITY DOMAIN COMPLETION VALIDATION PASSED features=8")
print("canonical_selection=false code_generation_ready=false")
