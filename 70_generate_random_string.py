# Generate a random string of a given length
import string
import random

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

random_str = generate_random_string(10)
print(f"Random string of length 10: {random_str}")
