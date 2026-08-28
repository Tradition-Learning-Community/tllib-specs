# Reproducible Python validation environment

This repository is a specification and validation repository, not the future `tllib` runtime package. The Python dependencies described here exist only to run repository tooling and publication validation.

## Supported validator runtime

The supported runtime is **CPython 3.12**, declared in `.python-version` and consumed by GitHub Actions with `actions/setup-python`.

`requirements.in` declares direct validation dependencies. `requirements.lock` pins the complete resolved environment, including transitive dependencies. CI and local validation install from `requirements.lock`; they do not install floating package names.

## Clean-checkout installation

From the repository root with CPython 3.12 available:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install --disable-pip-version-check --no-deps -r requirements.lock
python -m pip check
python tools/pipeline/validate_python_environment.py
```

On Windows PowerShell, create the environment with `py -3.12 -m venv .venv` and activate it with `.venv\\Scripts\\Activate.ps1`; the remaining commands are identical.

`--no-deps` is intentional: every direct and transitive package must already be present in `requirements.lock`. `pip check` then proves that the locked set satisfies installed package metadata.

## Updating the lock

Lock updates are explicit maintenance work, not part of normal validation. Use a fresh CPython 3.12 virtual environment so unrelated globally installed packages cannot enter the lock.

1. Edit direct pins in `requirements.in` only when a dependency change is intended.
2. Create and activate a fresh CPython 3.12 virtual environment.
3. Run `python -m pip install --upgrade -r requirements.in`.
4. Inspect `python -m pip freeze --exclude pip` and update `requirements.lock` so every resolved direct and transitive dependency is exactly pinned with `==`.
5. Recreate a fresh environment and install it with `python -m pip install --no-deps -r requirements.lock`.
6. Run `python -m pip check` and `python tools/pipeline/validate_python_environment.py`.
7. Run the full repository validation suite before committing the lock change.

The lock validator rejects unpinned entries, missing direct dependencies, direct-pin divergence, the wrong Python major/minor, and installed-version divergence.

## Full validation

With the locked environment active, run:

```bash
python tools/pipeline/validate_ci_triggers.py
python tools/pipeline/validate_repository_hygiene.py
python tools/pipeline/catalog_snapshot.py --self-test
python tools/handoff/generate_catalog.py --check
python tools/handoff/validate_handoff.py --self-test
python tools/handoff/validate_handoff.py
python tools/handoff/export_bundle.py --all --check --verify-determinism
python tools/global-finalization/validate_global_finalization.py
git diff --check
git status --short
```

A clean checkout must remain clean after validation. Python caches and local diagnostics are ignored, while CI separately rejects non-normative cache files if they are ever committed.
