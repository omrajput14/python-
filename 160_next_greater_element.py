def print_next_greater_element(arr):
    n = len(arr)
    nge = [-1] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
            
        if stack:
            nge[i] = stack[-1]
            
        stack.append(arr[i])
        
    for i in range(n):
        print(f"{arr[i]} --> {nge[i]}")

if __name__ == '__main__':
    arr = [11, 13, 21, 3]
    print("Next Greater Elements:")
    print_next_greater_element(arr)
