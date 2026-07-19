# 310. Minimum Height Trees
# A tree is an undirected graph in which any two vertices are connected by exactly one path.

from collections import defaultdict

def find_min_height_trees(n, edges):
    if n == 1: return [0]
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    leaves = [i for i in range(n) if len(adj[i]) == 1]
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1:
                new_leaves.append(j)
        leaves = new_leaves
    return leaves

if __name__ == "__main__":
    print(find_min_height_trees(4, [[1,0],[1,2],[1,3]]))
