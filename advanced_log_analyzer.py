
import re
import json
import hashlib
from collections import Counter, defaultdict

LOGS = [
    "2026-11-10 ERROR API timeout user=104",
    "2026-11-10 INFO LOGIN user=201",
    "2026-11-10 ERROR API timeout user=104",
    
]