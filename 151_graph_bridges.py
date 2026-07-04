from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, parent, low, disc):
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridge_util(v, visited, parent, low, disc)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    print(f"Bridge found between {u} and {v}")
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, parent, low, disc)

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print("Bridges in the graph:")
    g.bridge()
