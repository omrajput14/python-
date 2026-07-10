def interpolation_search(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x: return lo
            return -1
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x: return pos
        if arr[pos] < x: lo = pos + 1
        else: hi = pos - 1
    return -1

if __name__ == "__main__":
    print(interpolation_search([1,2,3], 2))