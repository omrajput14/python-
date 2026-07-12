def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map: return [num_map[diff], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))