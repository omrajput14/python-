# Calculate the average of a list of numbers
numbers = [10, 20, 30, 40, 50]

if numbers:
    average = sum(numbers) / len(numbers)
    print("Numbers:", numbers)
    print("Average:", average)
else:
    print("List is empty")
