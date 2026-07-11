def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def findMax(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def pancakeSortRecursive(arr, n):
    if n <= 1:
        return
    mi = findMax(arr, n)
    if mi != n - 1:
        flip(arr, mi)
        flip(arr, n - 1)
    pancakeSortRecursive(arr, n - 1)

if __name__ == "__main__":
    arr = [23, 10, 20, 11, 12, 6, 7]
    pancakeSortRecursive(arr, len(arr))
    print("Pancake Sort Recursive:", arr)
