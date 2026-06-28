# Depth First Search (DFS) Example
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

if __name__ == "__main__":
    print("DFS traversal starting from 'A':")
    dfs(graph, 'A')
    print()
