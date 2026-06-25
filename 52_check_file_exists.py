# Check if a file exists
import os

file_path = "50_tuple_size.py"
if os.path.exists(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")
