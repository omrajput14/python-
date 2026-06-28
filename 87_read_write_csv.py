# CSV Read/Write Example
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Write to CSV
with open("people.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read from CSV
print("Reading CSV data:")
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(", ".join(row))
