import mimetypes
import socket
import statistics
from pathlib import Path

def get_file_info(file_path):
    path = Path(file_path)
    if not path.is_file():
        return None
    mime_type, encoding = mimetypes.guess_type(path.name)
    return {"name": path.name, "size": path.stat().st_size,
            "type": mime_type or "unknown"}
    
def check_port(host, port, timeout=2):
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except (OSError, TimeoutError):
        return False
    
    
def analyze_sizes(file_paths):
    sizes = [get_file_info(p)["size"] for p in file_paths
             if get_file_info(p) is not None]
    if not sizes:
        return {"count": 0, "average": 0, "median": 0}
    return {"count": len(sizes),
            "average": round(statistics.mean(sizes), 2),
            "median": statistics.median(sizes)}


def main():
    files = ["report.pdf", "image.png", "notes.txt"]
    print(analyze_sizes(files))
    print(get_file_info("report.pdf"))
    print("Port 443 accessible:", check_port("example.com", 443))
    
if __name__ == "__main__":