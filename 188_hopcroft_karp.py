import queue

class BipGraph:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.adj = [[] for _ in range(m + 1)]
        self.pair_u = [0] * (m + 1)
        self.pair_v = [0] * (n + 1)
        self.dist = [0] * (m + 1)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def bfs(self):
        q = queue.Queue()
        for u in range(1, self.m + 1):
            if self.pair_u[u] == 0:
                self.dist[u] = 0
                q.put(u)
            else:
                self.dist[u] = float('inf')
                
        self.dist[0] = float('inf')
        
        while not q.empty():
            u = q.get()
            if self.dist[u] < self.dist[0]:
                for v in self.adj[u]:
                    if self.dist[self.pair_v[v]] == float('inf'):
                        self.dist[self.pair_v[v]] = self.dist[u] + 1
                        q.put(self.pair_v[v])
                        
        return self.dist[0] != float('inf')

    def dfs(self, u):
        if u != 0:
            for v in self.adj[u]:
                if self.dist[self.pair_v[v]] == self.dist[u] + 1:
                    if self.dfs(self.pair_v[v]) == True:
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True
            self.dist[u] = float('inf')
            return False
        return True

    def hopcroft_karp(self):
        result = 0
        while self.bfs():
            for u in range(1, self.m + 1):
                if self.pair_u[u] == 0 and self.dfs(u):
                    result += 1
        return result

if __name__ == '__main__':
    g = BipGraph(4, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 1)
    g.add_edge(3, 2)
    g.add_edge(4, 2)
    g.add_edge(4, 4)
    print("Maximum Bipartite Matching is", g.hopcroft_karp())
