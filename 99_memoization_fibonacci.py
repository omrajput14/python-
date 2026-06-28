# Memoization with DP (Fibonacci) Example
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 50
    print(f"Fibonacci({n}) =", fib_memo(n))
