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