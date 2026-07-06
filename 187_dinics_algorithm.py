class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev

class Graph:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.level = [0] * V

    def addEdge(self, u, v, C):
        a = Edge(v, 0, C, len(self.adj[v]))
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)

    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1
            
        self.level[s] = 0
        queue = []
        queue.append(s)
        
        while queue:
            u = queue.pop(0)
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flow < e.C:
                    self.level[e.v] = self.level[u] + 1
                    queue.append(e.v)
                    
        return False if self.level[t] < 0 else True

    def sendFlow(self, u, flow, t, start):
        if u == t:
            return flow
            
        for i in range(start[u], len(self.adj[u])):
            e = self.adj[u][i]
            if self.level[e.v] == self.level[u] + 1 and e.flow < e.C:
                curr_flow = min(flow, e.C - e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)
                if temp_flow > 0:
                    e.flow += temp_flow
                    self.adj[e.v][e.rev].flow -= temp_flow
                    return temp_flow
            start[u] += 1
            
        return 0

    def DinicMaxflow(self, s, t):
        if s == t:
            return -1
            
        total = 0
        while self.BFS(s, t) == True:
            start = [0] * (self.V + 1)
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break
                total += flow
                
        return total

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1, 16)
    g.addEdge(0, 2, 13)
    g.addEdge(1, 2, 10)
    g.addEdge(1, 3, 12)
    g.addEdge(2, 1, 4)
    g.addEdge(2, 4, 14)
    g.addEdge(3, 2, 9)
    g.addEdge(3, 5, 20)
    g.addEdge(4, 3, 7)
    g.addEdge(4, 5, 4)
    print("Maximum flow using Dinic's Algorithm is", g.DinicMaxflow(0, 5))
