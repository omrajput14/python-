# 275. Longest Harmonious Subsequence
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

from collections import Counter

def find_lhs(nums):
    count = Counter(nums)
    max_len = 0
    for num in count:
        if num + 1 in count:
            max_len = max(max_len, count[num] + count[num+1])
    return max_len

if __name__ == "__main__":
    print(find_lhs([1,3,2,2,5,2,3,7]))  # 5
    print(find_lhs([1,2,3,4]))          # 2
