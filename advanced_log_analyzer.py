
import re
import json
import hashlib
from collections import Counter, defaultdict

LOGS = [
    "2026-11-10 ERROR API timeout user=104",
    "2026-11-10 INFO LOGIN user=201",
    "2026-11-10 ERROR API timeout user=104",
    "2026-11-10 WARNING AUTH failed user=305",
    "2026-11-10 ERROR DATABASE connection user=201",
    "2026-11-10 INFO LOGOUT user=201",
]

def analyze_logs(logs):
    stats = defaultdict(Counter)
    users = defaultdict(list)
    fingerprints = set()

    for entry in logs:
        match = re.search(
            r"(\d{4}-\d{2}-\d{2}) (\w+) (.+) user=(\d+)", entry
        )
        if not match:
            continue

        date, level, event, user = match.groups()
        fingerprint = hashlib.sha256(entry.encode()).hexdigest()