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


class TF1Analyzer:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.programs = []
    @measure_time
    def load_data(self):
        try:
            data = json.loads(self.filename.read_text(encoding="utf-8"))
            self.programs = data.get("programs", [])
            return len(self.programs)
        except (OSError, json.JSONDecodeError) as error:
            logger.error("Erreur de lecture : %s", error)
            return 0
        
    def search(self, keyword):
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        return [p for p in self.programs if pattern.search(p.get("title", ""))]
    
    
    def categories(self):
        return Counter(p.get("category", "Inconnu") for p in self.programs)
    
    def export(self, output="report.json"):
        report = {"total": len(self.programs), "categories": dict(self.categories())}
        Path(output).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return report

if __name__ == "__main__":
    analyzer = TF1Analyzer("programs.json")
    print("Programmes chargés :", analyzer.load_data())
    print("Résultats :", analyzer.search("journal"))
    print("Catégories :", analyzer.categories())