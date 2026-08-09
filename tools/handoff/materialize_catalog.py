#!/usr/bin/env python3
"""Temporary PR-branch materializer for the exact official handoff catalog."""

from __future__ import annotations

import base64
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "handoff/catalog.json"
REPOSITORY = os.environ["GITHUB_REPOSITORY"]
BRANCH = os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_REF_NAME")
TOKEN = os.environ["GITHUB_TOKEN"]
PATH = "handoff/catalog.json"
API = f"https://api.github.com/repos/{REPOSITORY}/contents/{PATH}"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "Content-Type": "application/json",
}

get_request = urllib.request.Request(
    f"{API}?ref={urllib.parse.quote(BRANCH, safe='')}",
    headers=HEADERS,
)
with urllib.request.urlopen(get_request, timeout=30) as response:
    current = json.loads(response.read().decode("utf-8"))

payload = {
    "message": "Install exact generated Context global handoff catalog",
    "content": base64.b64encode(CATALOG.read_bytes()).decode("ascii"),
    "sha": current["sha"],
    "branch": BRANCH,
}
put_request = urllib.request.Request(
    API,
    data=json.dumps(payload).encode("utf-8"),
    method="PUT",
    headers=HEADERS,
)
with urllib.request.urlopen(put_request, timeout=60) as response:
    result = json.loads(response.read().decode("utf-8"))

print(f"CONTEXT_CATALOG_COMMIT_SHA={result['commit']['sha']}")
print(f"CONTEXT_CATALOG_CONTENT_SHA={result['content']['sha']}")
