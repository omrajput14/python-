class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] 
                      for row in range(V)]

    def is_bipartite_util(self, src, color_arr):
        color_arr[src] = 1
        queue = []
        queue.append(src)

        while queue:
            u = queue.pop(0)

            if self.graph[u][u] == 1:
                return False

            for v in range(self.V):
                if self.graph[u][v] == 1 and color_arr[v] == -1:
                    color_arr[v] = 1 - color_arr[u]
                    queue.append(v)
                elif self.graph[u][v] == 1 and color_arr[v] == color_arr[u]:
                    return False

        return True

    def is_bipartite(self):
        color_arr = [-1] * self.V

        for i in range(self.V):
            if color_arr[i] == -1:
                if not self.is_bipartite_util(i, color_arr):
                    return False
        return True

if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]
               
    if g.is_bipartite():
        print("Graph is Bipartite")
    else:
        print("Graph is not Bipartite")
