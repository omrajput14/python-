# 286. Longest Continuous Increasing Subsequence
# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence.

def find_length_of_lcis(nums):
    if not nums: return 0
    ans = 1
    anchor = 0
    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            anchor = i
        ans = max(ans, i - anchor + 1)
    return ans

if __name__ == "__main__":
    print(find_length_of_lcis([1,3,5,4,7]))  # 3
    print(find_length_of_lcis([2,2,2,2,2]))  # 1
