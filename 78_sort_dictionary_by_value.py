# Sort a dictionary by its values
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

# Sort by value using a lambda function
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Original dictionary:", my_dict)
print("Sorted dictionary by value:", sorted_dict)
