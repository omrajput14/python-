import sys

def tsp_dp(graph):
    n = len(graph)
    VISITED_ALL = (1 << n) - 1
    
    # Memoization table: dp[mask][i]
    dp = [[-1 for _ in range(n)] for _ in range(1 << n)]
    
    def tsp_util(mask, pos):
        if mask == VISITED_ALL:
            return graph[pos][0]
            
        if dp[mask][pos] != -1:
            return dp[mask][pos]
            
        ans = sys.maxsize
        
        for city in range(n):
            if (mask & (1 << city)) == 0:
                new_ans = graph[pos][city] + tsp_util(mask | (1 << city), city)
                ans = min(ans, new_ans)
                
        dp[mask][pos] = ans
        return ans

    return tsp_util(1, 0)

if __name__ == "__main__":
    graph = [
        [0, 20, 42, 25],
        [20, 0, 30, 34],
        [42, 30, 0, 10],
        [25, 34, 10, 0]
    ]
    print("Minimum weight Hamiltonian Cycle for TSP is:", tsp_dp(graph))
