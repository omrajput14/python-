from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)
                
    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack = stack.append(v)
        
    def get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
        
    def print_sccs(self):
        stack = []
        visited = [False] * self.V
        
        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)
                
        gr = self.get_transpose()
        
        visited = [False] * self.V
        
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs_util(i, visited)
                print()

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print("Following are strongly connected components in given graph:")
    g.print_sccs()
