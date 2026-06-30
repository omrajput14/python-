INF = 99999

def floyd_warshall(graph, V):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print_solution(dist, V)

def print_solution(dist, V):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print(f"{'INF':>7}", end=" ")
            else:
                print(f"{dist[i][j]:>7}", end=" ")
        print()

if __name__ == '__main__':
    V = 4
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]]
    floyd_warshall(graph, V)
