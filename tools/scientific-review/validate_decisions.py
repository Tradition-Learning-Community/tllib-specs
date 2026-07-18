#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import sys, yaml

ROOT = Path(__file__).resolve().parents[2]
errors = []
def read(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"YAML illisible {path.relative_to(ROOT)}: {exc}")
        return {}

source = read(ROOT / "reports/scientific-consolidation/human-review-queue.yaml").get("decisions", [])
index = read(ROOT / "reports/scientific-review/review-index.yaml").get("decisions", [])
ledger = read(ROOT / "registry/scientific-objects/review-decisions/decision-ledger.yaml")
for path in sorted((ROOT / "reports/scientific-review").rglob("*.yaml")):
    read(path)
for path in sorted((ROOT / "registry/scientific-objects/review-decisions").rglob("*.yaml")):
    read(path)
batches = []
for path in sorted((ROOT / "reports/scientific-review/batches").glob("batch-*/decisions.yaml")):
    data = read(path); batches.extend(data.get("decisions", []))
    ids = data.get("source_decision_ids", [])
    if ids != [x.get("source_decision_id") for x in data.get("decisions", [])]: errors.append(f"source_decision_ids incohérent: {path.relative_to(ROOT)}")
source_ids = [x.get("decision_id") for x in source]
batch_ids = [x.get("source_decision_id") for x in batches]
for did, n in Counter(batch_ids).items():
    if n != 1: errors.append(f"Identifiant présent {n} fois dans les paquets: {did}")
missing = sorted(set(source_ids)-set(batch_ids)); extra = sorted(set(batch_ids)-set(source_ids))
if missing: errors.append(f"Identifiants manquants: {missing}")
if extra: errors.append(f"Identifiants inconnus: {extra}")
if len(index) != len(source) or {x.get('decision_id') for x in index} != set(source_ids): errors.append("Index incomplet ou incohérent")
if len(ledger.get("decisions", [])) != len(source): errors.append("Ledger incomplet")
for d in batches:
    h=d.get("human_decision",{}); selected=h.get("selected_option"); status=h.get("status")
    if selected is not None and selected not in d.get("allowed_options",[]): errors.append(f"Option interdite pour {d.get('decision_id')}: {selected}")
    if status != "pending" and (not selected or not h.get("decided_by") or not h.get("decided_at") or not h.get("justification")): errors.append(f"Décision prise incomplète: {d.get('decision_id')}")
summary=ledger.get("summary",{})
if summary.get("total") != len(source): errors.append("Compte total du ledger incorrect")
dashboard=(ROOT / "reports/scientific-review/review-dashboard.md").read_text(encoding="utf-8")
if f"Décisions totales : **{len(source)}**" not in dashboard: errors.append("Compte total du tableau de bord incorrect")
if f"Paquets : **{len(list((ROOT / 'reports/scientific-review/batches').glob('batch-*')))}**" not in dashboard: errors.append("Compte des paquets du tableau de bord incorrect")
category_counts = Counter(x.get("category") for x in index)
priority_counts = Counter(x.get("priority") for x in index)
blocking_count = sum(x.get("blocking_scope") != "non_blocking" for x in index)
for category, count in category_counts.items():
    if f"| `{category}` | {count} |" not in dashboard: errors.append(f"Compte de catégorie absent ou incorrect: {category}")
for priority, count in priority_counts.items():
    if f"| `{priority}` | {count} |" not in dashboard: errors.append(f"Compte de priorité absent ou incorrect: {priority}")
if f"Décisions bloquantes : **{blocking_count}**" not in dashboard: errors.append("Compte bloquant du tableau de bord incorrect")
if f"Décisions non bloquantes : **{len(index)-blocking_count}**" not in dashboard: errors.append("Compte non bloquant du tableau de bord incorrect")
print(f"Décisions source: {len(source)}")
print(f"Décisions en paquets: {len(batches)}")
print(f"Erreurs: {len(errors)}")
for e in errors: print(f"ERROR: {e}")
sys.exit(1 if errors else 0)
