import sys

def optimal_bst(keys, freq, n):
    cost = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = sys.maxsize
            
            sum_freq = sum(freq[i:j+1])
            
            for r in range(i, j + 1):
                c = 0
                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]
                c += sum_freq
                
                if c < cost[i][j]:
                    cost[i][j] = c
                    
    return cost[0][n - 1]

if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print("Cost of Optimal BST is", optimal_bst(keys, freq, n))
