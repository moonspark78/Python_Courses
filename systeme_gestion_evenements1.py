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
        
    def register(self, user):
        if len(self.participants) >= self.capacity:
            raise ValueError("Event is full")
        if user in self.participants: