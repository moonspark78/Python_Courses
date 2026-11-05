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
        return result
    return wrapper

class DataProcessor:
    def __init__(self, records: list[dict[str, Any]]):
        self.records = records
        self.cache = defaultdict(list)
        
    @execution_timer
    def analyze(self, key: str) -> dict:
        for record in self.records:
            try:
                value = float(record[key])
                self.cache[key].append(value)
            except (KeyError, ValueError, TypeError):
                logger.warning(f"Invalid record: {record}")
        values = self.cache[key]
        if not values:
            raise ValueError("No valid numerical data found")
        return {
            "count": len(values),
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "variance": statistics.variance(values) if len(values) > 1 else 0
        }
        
    def stream(self, threshold: float):
        for record in self.records:
            if any(isinstance(v, (int, float)) and v > threshold
                   for v in record.values()):
                yield record
                
    def export(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.records, file, indent=4)