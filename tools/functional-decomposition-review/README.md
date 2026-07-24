# Functional decomposition scientific review tools

These tools validate and summarize the independent candidate review. They require Python 3 and PyYAML.

Rebuild the review deterministically from the candidate registries:

```console
python tools/functional-decomposition-review/summarize_review.py --build
```

Validate coverage, statuses, evidence, dependency scope, YAML syntax, and the absence of staged changes to protected
scientific and decomposition inputs:

```console
python tools/functional-decomposition-review/validate_review.py
```

Print the decision summary:

```console
python tools/functional-decomposition-review/summarize_review.py
```

The classification rules are intentionally conservative. Self-dependencies are invalid. Other relation-derived edges
remain shared scientific context because the candidate immediate-feature lists are generated from the same mapping and
are not independent evidence of software necessity. No classification changes its source artifact, and every generated
artifact remains `candidate`.
