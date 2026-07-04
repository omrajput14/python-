def catalan_dp(n):
    if n <= 1:
        return 1

    catalan = [0 for i in range(n + 1)]
    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan[n]

if __name__ == '__main__':
    for i in range(10):
        print(f"Catalan number C({i}) is {catalan_dp(i)}")
