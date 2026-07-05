class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

if __name__ == '__main__':
    ds = DisjointSet(5)
    ds.union(0, 2)
    ds.union(4, 2)
    ds.union(3, 1)

    print(f"Are 4 and 0 in the same set? {ds.find(4) == ds.find(0)}")
    print(f"Are 1 and 0 in the same set? {ds.find(1) == ds.find(0)}")

    ds.union(1, 0)
    print(f"Are 1 and 0 in the same set now? {ds.find(1) == ds.find(0)}")
