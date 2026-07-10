def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x: return m
        elif arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1,2,3], 2))