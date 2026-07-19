# 321. Create Maximum Number
# You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

def max_number(nums1, nums2, k):
    def prep(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

    def merge(a, b):
        return [max(a, b).pop(0) for _ in a + b]

    return max(merge(prep(nums1, i), prep(nums2, k-i))
               for i in range(k + 1)
               if i <= len(nums1) and k - i <= len(nums2))

if __name__ == "__main__":
    print(max_number([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
