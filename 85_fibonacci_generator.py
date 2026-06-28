# Fibonacci Generator Example
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n_terms = 10
    print(f"First {n_terms} terms of Fibonacci series:")
    for num in fibonacci_gen(n_terms):
        print(num, end=" ")
    print()
