class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
        self.V = vertices

    def is_safe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def ham_cycle_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.ham_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1
                
        return False

    def ham_cycle(self):
        path = [-1] * self.V
        path[0] = 0

        if not self.ham_cycle_util(path, 1):
            print("Solution does not exist\n")
            return False

        print("Solution exists: Following is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0])
        return True

if __name__ == '__main__':
    g1 = Graph(5)
    g1.graph = [[0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0]]
    g1.ham_cycle()
