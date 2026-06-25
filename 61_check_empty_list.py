# Check if a list is empty
list1 = []
list2 = [1, 2, 3]

def check_empty(lst):
    if not lst:
        return "List is empty"
    return "List is not empty"

print("List 1:", check_empty(list1))
print("List 2:", check_empty(list2))
