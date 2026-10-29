import re
import json
import logging
from pathlib import Path
from functools import wraps
from collections import Counter
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        logger.info("%s exécutée en %s", func.__name__, datetime.now() - start)
        return result
    return wrapper