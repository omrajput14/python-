def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
            
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return max_so_far, start, end

if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum, start, end = max_subarray_sum(arr)
    print(f"Array: {arr}")
    print(f"Maximum contiguous sum is {max_sum}")
    print(f"Subarray starts at index {start} and ends at index {end}")
