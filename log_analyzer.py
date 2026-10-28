import re
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("server.log")
REPORT_FILE = Path("report.json")