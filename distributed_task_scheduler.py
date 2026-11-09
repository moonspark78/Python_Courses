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