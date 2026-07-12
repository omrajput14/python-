def contains_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1]))