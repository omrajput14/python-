# Count the frequency of elements in a list
my_list = [1, 1, 2, 3, 2, 2, 4, 5, 4]
frequency = {}

for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("List:", my_list)
print("Frequency:", frequency)
