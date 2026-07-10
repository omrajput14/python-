def odd_even_sort(arr, n):
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
    return arr

if __name__ == "__main__":
    print(odd_even_sort([3,1,2], 3))