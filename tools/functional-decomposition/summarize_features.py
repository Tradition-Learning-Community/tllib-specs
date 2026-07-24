from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]


def load(relative):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def main():
    catalog = load("registry/features/feature-candidates.yaml")
    dependencies = load("registry/features/dependency-hints.yaml")
    variants = load("registry/features/feature-decomposition-variants.yaml")
    boundaries = load("registry/features/feature-boundary-issues.yaml")
    features = catalog["features"]
    print(f"feature_candidates: {len(features)}")
    for key, value in sorted(Counter(f["readiness"]["status"] for f in features).items()):
        print(f"{key}: {value}")
    print(f"decomposition_variants: {variants['count']}")
    print(f"boundary_issues: {boundaries['count']}")
    print(f"dependency_candidates: {dependencies['count']}")
    print("categories:")
    for key, value in Counter(f["category"] for f in features).most_common():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
