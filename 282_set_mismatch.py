# 282. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n.

def find_error_nums(nums):
    n = len(nums)
    s = sum(set(nums))
    return [sum(nums) - s, n * (n + 1) // 2 - s]

if __name__ == "__main__":
    print(find_error_nums([1,2,2,4]))  # [2, 3]
    print(find_error_nums([1,1]))      # [1, 2]
