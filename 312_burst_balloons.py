# 312. Burst Balloons
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums.

def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    for left in range(n - 2, -1, -1):
        for right in range(left + 2, n):
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                coins += dp[left][i] + dp[i][right]
                dp[left][right] = max(dp[left][right], coins)
    return dp[0][n-1]

if __name__ == "__main__":
    print(max_coins([3,1,5,8]))
