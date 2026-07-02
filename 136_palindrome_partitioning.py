def min_pal_partition(string):
    n = len(string)
    C = [[0 for i in range(n)] for i in range(n)]
    P = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        P[i][i] = True
        C[i][i] = 0

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1

            if L == 2:
                P[i][j] = (string[i] == string[j])
            else:
                P[i][j] = (string[i] == string[j]) and P[i + 1][j - 1]

            if P[i][j]:
                C[i][j] = 0
            else:
                C[i][j] = float('inf')
                for k in range(i, j):
                    C[i][j] = min(C[i][j], C[i][k] + C[k + 1][j] + 1)

    return C[0][n - 1]

if __name__ == '__main__':
    string = "ababbbabbababa"
    print(f"Min cuts needed for Palindrome Partitioning is {min_pal_partition(string)}")
