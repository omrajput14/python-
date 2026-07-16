# 247. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in [1, n],
# return all integers in [1, n] that do not appear in nums.

def find_disappeared_numbers(nums):
    """
    Find all numbers in [1, n] that are missing from the array.
    Uses index marking approach for O(n) time and O(1) extra space.
    """
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# Example usage
if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"Array: {nums}")
    print(f"Disappeared numbers: {find_disappeared_numbers(nums)}")
    # Output: [5, 6]

    nums2 = [1, 1]
    print(f"\nArray: {nums2}")
    print(f"Disappeared numbers: {find_disappeared_numbers(nums2)}")
    # Output: [2]
