# 262. K-diff Pairs in an Array
# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

from collections import Counter

def find_pairs(nums, k):
    if k < 0:
        return 0
    count = Counter(nums)
    pairs = 0
    for num in count:
        if k > 0 and num + k in count:
            pairs += 1
        elif k == 0 and count[num] > 1:
            pairs += 1
    return pairs

if __name__ == "__main__":
    print(find_pairs([3, 1, 4, 1, 5], 2))  # 2
    print(find_pairs([1, 2, 3, 4, 5], 1))  # 4
