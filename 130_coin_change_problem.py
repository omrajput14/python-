def count_ways(coins, m, n):
    table = [0 for k in range(n + 1)]
    table[0] = 1

    for i in range(0, m):
        for j in range(coins[i], n + 1):
            table[j] += table[j - coins[i]]

    return table[n]

if __name__ == '__main__':
    coins = [1, 2, 3]
    m = len(coins)
    n = 4
    print(f"Number of ways to make change for {n} is {count_ways(coins, m, n)}")
