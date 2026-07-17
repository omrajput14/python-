# 274. Out of Boundary Paths
# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].

def find_paths(m, n, maxMove, startRow, startColumn):
    MOD = 10**9 + 7
    memo = {}
    
    def dfs(r, c, moves):
        if r < 0 or r == m or c < 0 or c == n:
            return 1
        if moves == 0:
            return 0
        if (r, c, moves) in memo:
            return memo[(r, c, moves)]
            
        ans = 0
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            ans = (ans + dfs(r+dr, c+dc, moves-1)) % MOD
            
        memo[(r, c, moves)] = ans
        return ans
        
    return dfs(startRow, startColumn, maxMove)

if __name__ == "__main__":
    print(find_paths(2, 2, 2, 0, 0))  # 6
