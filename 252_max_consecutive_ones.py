# 252. Max Consecutive Ones
# Given a binary array nums, return the maximum number
# of consecutive 1s in the array.

def find_max_consecutive_ones(nums):
    """
    Single pass: track current streak and max streak.
    Reset current streak when a 0 is encountered.
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


def find_max_consecutive_ones_pythonic(nums):
    """Pythonic approach using string join and split."""
    return max(len(group) for group in ''.join(map(str, nums)).split('0'))


# Example usage
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print(f"Array: {nums}")
    print(f"Max consecutive ones: {find_max_consecutive_ones(nums)}")
    # Output: 3

    nums2 = [1, 0, 1, 1, 0, 1]
    print(f"\nArray: {nums2}")
    print(f"Max consecutive ones: {find_max_consecutive_ones(nums2)}")
    # Output: 2

    print(f"Pythonic method: {find_max_consecutive_ones_pythonic(nums)}")
