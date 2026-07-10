def bubble_sort_recursive(arr, n):
    if n == 1: return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble_sort_recursive(arr, n-1)

if __name__ == "__main__":
    arr = [3,1,2]
    bubble_sort_recursive(arr, len(arr))
    print(arr)