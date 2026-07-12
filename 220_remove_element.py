def remove_element(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

if __name__ == "__main__":
    arr = [3,2,2,3]
    print(remove_element(arr, 3), arr)