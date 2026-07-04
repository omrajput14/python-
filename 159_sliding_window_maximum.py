from collections import deque

def max_sliding_window(arr, k):
    q = deque()
    res = []
    
    for i in range(len(arr)):
        if q and q[0] == i - k:
            q.popleft()
            
        while q and arr[q[-1]] < arr[i]:
            q.pop()
            
        q.append(i)
        
        if i >= k - 1:
            res.append(arr[q[0]])
            
    return res

if __name__ == '__main__':
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Array: {arr}, k: {k}")
    print("Maximum elements of each sliding window:")
    print(max_sliding_window(arr, k))
