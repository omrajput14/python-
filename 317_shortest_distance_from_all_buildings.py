# 317. Shortest Distance from All Buildings
# You are given an m x n grid grid of values 0, 1, or 2.

from collections import deque

def shortest_distance(grid):
    m, n = len(grid), len(grid[0])
    dist = [[0] * n for _ in range(m)]
    hits = [[0] * n for _ in range(m)]
    buildings = 0
    
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                buildings += 1
                q = deque([(r, c, 0)])
                visited = [[False] * n for _ in range(m)]
                visited[r][c] = True
                while q:
                    x, y, d = q.popleft()
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            dist[nx][ny] += d + 1
                            hits[nx][ny] += 1
                            q.append((nx, ny, d + 1))
                            
    res = float('inf')
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 0 and hits[r][c] == buildings:
                res = min(res, dist[r][c])
    return res if res != float('inf') else -1

if __name__ == "__main__":
    print(shortest_distance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
