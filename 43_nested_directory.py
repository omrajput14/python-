# Safely create a nested directory
import os

path = "test_dir/sub_dir"
try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully")
except OSError as error:
    print(f"Directory '{path}' can not be created")
