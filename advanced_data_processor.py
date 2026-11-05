import json
import logging
import statistics
from collections import defaultdict
from datetime import datetime
from functools import wraps
from typing import Any, Callable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execution_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        elapsed = (datetime.now() - start).total_seconds()
        logger.info(f"{func.__name__} executed in {elapsed:.4f}s")