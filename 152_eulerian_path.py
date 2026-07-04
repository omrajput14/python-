from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS_util(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS_util(i, visited)

    def is_connected(self):
        visited = [False] * self.V
        
        i = 0
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                break
        
        if i == self.V - 1 and len(self.graph[i]) == 0:
            return True
            
        self.DFS_util(i, visited)
        
        for i in range(self.V):
            if not visited[i] and len(self.graph[i]) > 0:
                return False
        return True

    def is_eulerian(self):
        if not self.is_connected():
            return 0
        
        odd = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                odd += 1
                
        if odd == 0:
            return 2 # Eulerian Circuit
        elif odd == 2:
            return 1 # Eulerian Path
        else:
            return 0 # Not Eulerian

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    res = g.is_eulerian()
    if res == 0:
        print("Graph is not Eulerian")
    elif res == 1:
        print("Graph has an Eulerian Path")
    else:
        print("Graph has an Eulerian Circuit")
