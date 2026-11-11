import random
from collections import defaultdict, deque
from datetime import datetime

class IntrusionDetector:
    def __init__(self, threshold=5, window=60):
        self.threshold = threshold
        self.window = window
        self.attempts = defaultdict(deque)
        self.blocked = set()