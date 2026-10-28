import re
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("server.log")
REPORT_FILE = Path("report.json")

PATTERN = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+).*?"
    r"\[(?P<date>[^\]]+)\].*?"
    r'"(?P<method>\w+) (?P<path>[^ ]+).*?" '
    r"(?P<status>\d{3})"
)

def analyze_logs(file_path):
    stats = Counter()
    ips = defaultdict(Counter)
    errors = []
    total = 0
    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            match = PATTERN.search(line)
            if not match:
                continue
            data = match.groupdict()
            status = int(data["status"])
            total += 1
            stats[f"HTTP_{status}"] += 1
            ips[data["ip"]][status] += 1
            if status >= 400:
                errors.append({
                    "line": line_number,
                    "ip": data["ip"],
                    "path": data["path"],
                    "status": status,
                })
                
    suspicious = {
        ip: dict(counts)
        for ip, counts in ips.items()
        if sum(n for code, n in counts.items() if code >= 400) >= 5
    }