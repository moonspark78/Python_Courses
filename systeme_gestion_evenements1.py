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
            raise ValueError("Already registered")
        self.participants.add(user)
        
    def cancel(self, user):
        self.participants.discard(user)
        
    def __repr__(self):
        return f"{self.title} | {self.date.date()} | {len(self.participants)}/{self.capacity}"
    
class EventManager:
    def __init__(self):
        self.events = defaultdict(list)

    def create_event(self, event):
        self.events[event.date.year].append(event)

    def search(self, keyword):
        return [e for events in self.events.values()
                for e in events if keyword.lower() in e.title.lower()]