# Read a file line by line
filename = "50_tuple_size.py"

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"Line {i+1}: {line.strip()}")
except FileNotFoundError:
    print(f"File {filename} not found.")
