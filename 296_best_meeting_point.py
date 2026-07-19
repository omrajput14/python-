# 296. Best Meeting Point
# Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimum total travel distance.

def min_total_distance(grid):
    rows = []
    cols = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                rows.append(r)
                cols.append(c)
    cols.sort()
    
    def min_dist1d(points):
        i, j = 0, len(points) - 1
        dist = 0
        while i < j:
            dist += points[j] - points[i]
            i += 1
            j -= 1
        return dist
        
    return min_dist1d(rows) + min_dist1d(cols)

if __name__ == "__main__":
    grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    print(min_total_distance(grid))
