import mimetypes
import socket
import statistics
from pathlib import Path

def get_file_info(file_path):
    path = Path(file_path)
    if not path.is_file():
        return None
    mime_type, encoding = mimetypes.guess_type(path.name)