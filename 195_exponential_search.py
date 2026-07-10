def binary_search(arr, l, r, x):
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x: return m
        if arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

def exponential_search(arr, x):
    if arr[0] == x: return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, n-1), x)

if __name__ == "__main__":
    print(exponential_search([1,2,3], 2))