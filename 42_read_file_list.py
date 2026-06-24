# Read a File Line by Line Into a List
filename = "42_read_file_list.py"

with open(filename) as f:
    content_list = f.readlines()

content_list = [x.strip() for x in content_list]
print(f"Read {len(content_list)} lines from {filename}")
