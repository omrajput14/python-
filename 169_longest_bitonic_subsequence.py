def lbs(arr):
    n = len(arr)
    lis = [1 for _ in range(n)]
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    lds = [1 for _ in range(n)]
    
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    max_len = lis[0] + lds[0] - 1
    for i in range(1, n):
        max_len = max(max_len, lis[i] + lds[i] - 1)
        
    return max_len

if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(f"Length of LBS is {lbs(arr)}")
