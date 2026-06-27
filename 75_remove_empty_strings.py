# Remove empty strings from a list of strings
string_list = ["apple", "", "banana", " ", "cherry", "", "date"]

# Using list comprehension to remove empty strings
filtered_list = [s for s in string_list if s.strip()]

print("Original list:", string_list)
print("Filtered list:", filtered_list)
