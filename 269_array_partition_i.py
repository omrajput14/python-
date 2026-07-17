# 269. Array Partition I
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.

def array_pair_sum(nums):
    nums.sort()
    return sum(nums[::2])

if __name__ == "__main__":
    print(array_pair_sum([1,4,3,2]))       # 4
    print(array_pair_sum([6,2,6,5,1,2]))   # 9
