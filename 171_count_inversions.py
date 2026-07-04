def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left     # Starting index to be sorted
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count

if __name__ == '__main__':
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    temp_arr = [0] * n
    result = merge_sort(arr, temp_arr, 0, n - 1)
    print("Array:", arr)
    print("Number of inversions are", result)
