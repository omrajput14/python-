def four_sum(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]: continue
            l, r = j+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif s < target: l += 1
                else: r -= 1
    return res

if __name__ == "__main__":
    print(four_sum([1,0,-1,0,-2,2], 0))