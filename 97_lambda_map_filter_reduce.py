# Lambda, Map, Filter, Reduce Example
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# map: square the even numbers
squares = list(map(lambda x: x**2, evens))

# reduce: sum the squared numbers
total = reduce(lambda x, y: x + y, squares)

if __name__ == "__main__":
    print("Original:", numbers)
    print("Evens:", evens)
    print("Squares:", squares)
    print("Total Sum of Squares:", total)
