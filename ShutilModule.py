""" 
Shutil module provides a higher-level interface for file operations,
including copying, moving, and removing files and directories. It also includes functions for archiving and unpacking files.
"""

import shutil
shutil.copy("hello.py", "files")  # Copy a file to a directory

shutil.copytree("files","files_copy")  # Copy an entire directory tree to a new location

shutil.rmtree("files_copy")  # Remove an entire directory tree