def lis(arr):
    n = len(arr)
    lis_arr = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_arr[i] < lis_arr[j] + 1:
                lis_arr[i] = lis_arr[j] + 1

    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis_arr[i])

    return maximum

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(f"Length of LIS is {lis(arr)}")
