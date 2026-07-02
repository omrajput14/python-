def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return float('inf')

    jumps = [float('inf') for _ in range(n)]
    jumps[0] = 0

    for i in range(1, n):
        for j in range(i):
            if i <= j + arr[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break

    return jumps[n - 1]

if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(f"Minimum number of jumps to reach end is {min_jumps(arr)}")
