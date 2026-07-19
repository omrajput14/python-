# 315. Count of Smaller Numbers After Self
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

import bisect

def count_smaller(nums):
    arr = []
    res = []
    for num in reversed(nums):
        idx = bisect.bisect_left(arr, num)
        res.append(idx)
        arr.insert(idx, num)
    return res[::-1]

if __name__ == "__main__":
    print(count_smaller([5,2,6,1]))
