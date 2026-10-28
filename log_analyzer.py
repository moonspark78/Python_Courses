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