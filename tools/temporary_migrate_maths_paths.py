from pathlib import Path
import subprocess

REPLACEMENTS = {
    'maths/00-master.md': 'maths/00-master/master.md',
    'maths/01-disciple.md': 'maths/01-disciple/disciple.md',
    'maths/02-community.md': 'maths/02-community/community.md',
    'maths/03-huit-dimensions-de-tl.md': 'maths/03-huit-dimensions-de-tl/huit-dimensions-de-tl.md',
    'maths/04-invariants.md': 'maths/04-invariants/invariants.md',
    'maths/05-dynamics.md': 'maths/05-dynamics/dynamics.md',
    'maths/06-theorems.md': 'maths/06-theorems/theorems.md',
    'maths/07-message.md': 'maths/07-message/message.md',
    'maths/08-principle.md': 'maths/08-principle/principle.md',
    'maths/09-values.md': 'maths/09-values/values.md',
    'maths/10-virtues.md': 'maths/10-virtues/virtues.md',
    'maths/11-capacities.md': 'maths/11-capacities/capacities.md',
    'maths/12-competencies.md': 'maths/12-competencies/competencies.md',
    'maths/13-practice.md': 'maths/13-practice/practice.md',
    'maths/14-lived-experience.md': 'maths/14-lived-experience/lived-experience.md',
    'maths/15-relations.md': 'maths/15-relations/relations.md',
}

tracked = subprocess.check_output(['git', 'ls-files', '-z']).decode().split('\0')
changed = 0
for name in tracked:
    if not name:
        continue
    path = Path(name)
    if path.is_symlink() or not path.is_file():
        continue
    try:
        text = path.read_bytes().decode('utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    updated = text
    for old, new in REPLACEMENTS.items():
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding='utf-8', newline='')
        changed += 1

for old in REPLACEMENTS:
    path = Path(old)
    if path.exists() or path.is_symlink():
        path.unlink()

for temporary in [
    Path('docs/temporary-maths-path-migration-trigger.txt'),
    Path('tools/temporary_migrate_maths_paths.py'),
]:
    if temporary.exists():
        temporary.unlink()

remaining = []
for name in subprocess.check_output(['git', 'ls-files', '-z']).decode().split('\0'):
    if not name:
        continue
    path = Path(name)
    if path.is_symlink() or not path.is_file():
        continue
    try:
        text = path.read_bytes().decode('utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    for old in REPLACEMENTS:
        if old in text:
            remaining.append((name, old))

if remaining:
    for name, old in remaining[:50]:
        print(f'{name}: {old}')
    raise SystemExit(f'{len(remaining)} historical source-path references remain')

print(f'Updated {changed} tracked text files and removed {len(REPLACEMENTS)} compatibility links.')
