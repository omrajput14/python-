def stooge_sort(arr, l, h):
    if l >= h: return
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h)
        stooge_sort(arr, l, h - t)
    return arr

if __name__ == "__main__":
    arr = [3,1,2]
    print(stooge_sort(arr, 0, 2))