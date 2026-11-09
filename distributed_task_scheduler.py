import asyncio
import uuid
import time
from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass
class Task:
    name: str
    function: Callable