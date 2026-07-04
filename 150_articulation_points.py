from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def ap_util(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self.ap_util(v, visited, ap, parent, low, disc)
                low[u] = min(low[u], low[v])
                
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def ap(self):
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V
        ap = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.ap_util(i, visited, ap, parent, low, disc)

        print("Articulation points in the graph are:")
        for index, value in enumerate(ap):
            if value:
                print(index, end=" ")
        print()

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.ap()
