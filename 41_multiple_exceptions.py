# Catch multiple exceptions
string = "Python Exceptions"

try:
    num = int(string)
    print(num)
except (ValueError, TypeError) as e:
    print(f"Caught an exception: {e}")
