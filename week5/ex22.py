"""
• exists: Checks whether the path exists in the filesystem and whether it is a file or a
directory.
• is_dir: Checks whether the path is a directory.
• is_file: Checks whether the path is a file.
• iterdir: Returns an iterator with path objects to all the files and directories
contained within the path object.
• mkdir: Creates a directory in the path indicated by the path object.
• open: Opens a file in the current path, similar to running open and passing the string
representation of the path. It returns a file object that can be operated like any
other.
• read_text: Returns the content of the file as a Unicode string. If the file is in binary
format, the read_bytes method should be used instead.
"""
import os
import pathlib

path = pathlib.Path()
print(repr(path))
print(os.getcwd())
