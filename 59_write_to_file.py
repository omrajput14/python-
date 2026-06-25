# Write a list of strings to a file
lines_to_write = ["First line", "Second line", "Third line"]
output_file = "output.txt"

with open(output_file, 'w') as file:
    for line in lines_to_write:
        file.write(line + "\n")

print(f"Successfully wrote to {output_file}")
