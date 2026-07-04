class BPM:
    def __init__(self, graph):
        self.graph = graph 
        self.applicants = len(graph)
        self.jobs = len(graph[0])

    def bpm_util(self, u, match_r, seen):
        for v in range(self.jobs):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True 
                
                if match_r[v] == -1 or self.bpm_util(match_r[v], match_r, seen):
                    match_r[v] = u
                    return True
        return False

    def max_bpm(self):
        match_r = [-1] * self.jobs
        result = 0
        
        for i in range(self.applicants):
            seen = [False] * self.jobs
            if self.bpm_util(i, match_r, seen):
                result += 1
                
        return result

if __name__ == '__main__':
    bpGraph = [[0, 1, 1, 0, 0, 0],
               [1, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1]]
               
    g = BPM(bpGraph)
    print("Maximum number of applicants that can get a job is %d " % g.max_bpm())
