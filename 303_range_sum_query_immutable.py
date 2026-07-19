# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive.

class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sum_range(self, left, right):
        return self.prefix[right+1] - self.prefix[left]

if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sum_range(0, 2))
