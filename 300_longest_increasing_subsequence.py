# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

import bisect

def length_of_lis(nums):
    sub = []
    for num in nums:
        i = bisect.bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)

if __name__ == "__main__":
    print(length_of_lis([10,9,2,5,3,7,101,18]))
