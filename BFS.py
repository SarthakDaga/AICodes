from collections import deque

# Recursive BFS
def bfs(q, visited):
    if not q:
        return

    node = q.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)

    bfs(q, visited)   # recursive call


# Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = set([start])
q = deque([start])

print("BFS Traversal:")
bfs(q, visited)
