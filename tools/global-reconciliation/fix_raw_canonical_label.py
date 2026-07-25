#!/usr/bin/env python3
from __future__ import annotations

import pathlib

path = pathlib.Path(__file__).with_name("build_current_global_registry.py")
text = path.read_text(encoding="utf-8")
old = '        raw_canonical_label = bool(normalized_selection and "canonical" in normalized_selection)\n'
new = '''        raw_canonical_label = bool(
            normalized_selection
            and "canonical" in normalized_selection
            and "not_canonical" not in normalized_selection
            and "non_canonical" not in normalized_selection
        )
'''
if old not in text:
    raise SystemExit("raw canonical label marker not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
print("raw canonical label classification corrected")
