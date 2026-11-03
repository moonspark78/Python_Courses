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