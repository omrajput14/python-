# JSON Read/Write Example
import json

data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Write to JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded JSON data:", loaded_data)
