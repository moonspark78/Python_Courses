import asyncio
import uuid
import time
from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass
class Task:
    name: str
    function: Callable
    args: tuple = ()
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    retries: int = 3
    status: str = "PENDING"
    
class TaskScheduler:
    def __init__(self, workers=5):
        self.queue = asyncio.PriorityQueue()
        self.workers = workers
        self.results = {}
        
    async def submit(self, task: Task, priority=1):
        await self.queue.put((priority, time.time(), task))
        
        
    async def execute(self, task: Task):
        for attempt in range(task.retries + 1):
            try:
                task.status = "RUNNING"
                result = await asyncio.to_thread(task.function, *task.args)
                task.status = "COMPLETED"
                self.results[task.id] = result
                return
            except Exception as error:
                task.status = "RETRYING"
                if attempt == task.retries:
                    task.status = "FAILED"
                    self.results[task.id] = str(error)
                    return
                await asyncio.sleep(2 ** attempt)

    async def worker(self, worker_id):
        while True:
            priority, timestamp, task = await self.queue.get()
            try:
                await self.execute(task)
            finally:
                self.queue.task_done()
                
    async def start(self):
        workers = [asyncio.create_task(self.worker(i))
                   for i in range(self.workers)]