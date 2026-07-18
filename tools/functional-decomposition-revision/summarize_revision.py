"""Print the canonical revision summary from decision_required.yaml."""

from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    data = yaml.safe_load((ROOT / "reports/functional-decomposition-revision/decision_required.yaml").read_text(encoding="utf-8"))
    print("TLC functional decomposition revision")
    for key, value in data["summary"].items():
        print(f"{key}: {value}")
    print(f"recommended_decision: {data['recommended_decision']['value']}")
    print(f"ready_for_human_validation: {str(data['readiness']['ready_for_human_validation']).lower()}")


if __name__ == "__main__":
    main()
