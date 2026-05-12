# DFS and BFS for an undirected graph (user input)

from collections import deque

# Input number of vertices and edges
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Create adjacency list
graph = {i: [] for i in range(n)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # undirected graph

# Recursive DFS
visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

# BFS
def bfs(start):
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

# Start vertex
start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start)

print("\nBFS Traversal:")
bfs(start)
