# List files in the current directory
import os

print("Files in the current directory:")
for item in os.listdir():
    if os.path.isfile(item):
        print("-", item)
