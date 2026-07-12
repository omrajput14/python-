def third_max(nums):
    s = set(nums)
    if len(s) < 3: return max(s)
    s.remove(max(s))
    s.remove(max(s))
    return max(s)

if __name__ == "__main__":
    print(third_max([3,2,1]))