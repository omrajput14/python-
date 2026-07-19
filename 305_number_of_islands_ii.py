# 305. Number of Islands II
# You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land.

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0
    def add(self, p):
        self.parent[p] = p
        self.count += 1
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1

def num_islands2(m, n, positions):
    uf = UnionFind()
    ans = []
    for r, c in positions:
        if (r, c) in uf.parent:
            ans.append(uf.count)
            continue
        uf.add((r, c))
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if (nr, nc) in uf.parent:
                uf.union((r, c), (nr, nc))
        ans.append(uf.count)
    return ans

if __name__ == "__main__":
    print(num_islands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]))
