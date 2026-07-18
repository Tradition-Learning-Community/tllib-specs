#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import yaml
ROOT=Path(__file__).resolve().parents[2]
ledger=yaml.safe_load((ROOT/"registry/scientific-objects/review-decisions/decision-ledger.yaml").read_text(encoding="utf-8"))
ds=ledger["decisions"]
statuses=Counter(d["human_decision"]["status"] for d in ds)
decided=len(ds)-statuses["pending"]
approved=statuses["approved"]+statuses["approved_with_reservations"]
blocking_remaining=sum(d["blocking_scope"]!="non_blocking" and d["human_decision"]["status"]=="pending" for d in ds)
batch_state={}
for d in ds: batch_state.setdefault(d["batch_id"],[]).append(d["human_decision"]["status"])
complete=sum(all(s!="pending" for s in states) for states in batch_state.values())
for k,v in [("total",len(ds)),("pending",statuses["pending"]),("decided",decided),("approved",approved),("rejected",statuses["rejected"]),("deferred",statuses["deferred"]),("bloquants_restants",blocking_remaining),("paquets_termines",complete)]: print(f"{k}: {v}")
