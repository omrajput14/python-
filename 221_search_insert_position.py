def search_insert(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target: return mid
        if nums[mid] < target: l = mid + 1
        else: r = mid - 1
    return l

if __name__ == "__main__":
    print(search_insert([1,3,5,6], 5))