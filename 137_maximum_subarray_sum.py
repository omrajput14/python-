def max_subarray_sum(arr):
    n = len(arr)
    max_so_far = -float('inf')
    max_ending_here = 0

    for i in range(n):
        max_ending_here = max_ending_here + arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(f"Maximum contiguous sum is {max_subarray_sum(arr)}")
