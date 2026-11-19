from datetime import datetime
from collections import defaultdict
from uuid import uuid4

class Event:
    def __init__(self, title, date, capacity):
        self.id = str(uuid4())[:8]
        self.title = title
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.capacity = capacity
        self.participants = set()