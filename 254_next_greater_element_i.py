# 254. Next Greater Element I
# Given two distinct integer arrays nums1 and nums2 where nums1 is a subset of nums2,
# find the next greater element for each element of nums1 in nums2.
# The next greater element of x in nums2 is the first element to its right that is greater.

def next_greater_element(nums1, nums2):
    """
    Use a monotonic decreasing stack to precompute next greater elements
    for all elements in nums2, then look up results for nums1.
    Time: O(n + m), Space: O(n)
    """
    # Map each element to its next greater element
    next_greater = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # Elements remaining in stack have no next greater element
    return [next_greater.get(num, -1) for num in nums1]


# Example usage
if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(f"nums1: {nums1}")
    print(f"nums2: {nums2}")
    print(f"Next greater elements: {next_greater_element(nums1, nums2)}")
    # Output: [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(f"\nnums1: {nums1}")
    print(f"nums2: {nums2}")
    print(f"Next greater elements: {next_greater_element(nums1, nums2)}")
    # Output: [3, -1]
