# 307. Range Sum Query - Mutable
# Given an integer array nums, handle multiple queries of the following types: Update and Sum Range.

class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i, num in enumerate(nums):
            self.tree[self.n + i] = num
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def sum_range(self, left, right):
        left += self.n
        right += self.n
        s = 0
        while left <= right:
            if left % 2 == 1:
                s += self.tree[left]
                left += 1
            if right % 2 == 0:
                s += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return s

if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print(na.sum_range(0, 2))
    na.update(1, 2)
    print(na.sum_range(0, 2))
