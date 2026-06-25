# Copy the contents of one file to another
source_file = "50_tuple_size.py"
destination_file = "copy.txt"

try:
    with open(source_file, 'r') as source:
        content = source.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print("Content copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
