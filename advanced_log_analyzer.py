
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