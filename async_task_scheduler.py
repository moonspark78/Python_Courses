import asyncio
import heapq
import time
import random
from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)
    callback: Callable = field(compare=False)
    retries: int = field(default=3, compare=False)
    
class TaskScheduler:
    def __init__(self):
        self.queue = []
        self.results = {}
        self.running = False

    def add_task(self, task: Task):
        heapq.heappush(self.queue, task)
        
    async def execute(self, task: Task):
        for attempt in range(task.retries):
            try:
                result = await task.callback()
                self.results[task.name] = result
                return result
            except Exception as error:
                if attempt == task.retries - 1:
                    self.results[task.name] = str(error)
                await asyncio.sleep(2 ** attempt)
                
                
    async def run(self):
        self.running = True
        while self.queue and self.running:
            batch = []
            while self.queue and len(batch) < 3:
                batch.append(heapq.heappop(self.queue))
            await asyncio.gather(*(self.execute(t) for t in batch))
        self.running = False
        
async def simulate_task():
    await asyncio.sleep(random.uniform(0.5, 2))
    if random.random() < 0.2:
        raise RuntimeError("Temporary execution failure")
    return {"status": "completed", "timestamp": time.time()}