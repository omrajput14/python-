def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

if __name__ == "__main__":
    print(single_number([4,1,2,1,2]))