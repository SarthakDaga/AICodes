# Kruskal's MST

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

# Sort by weight
edges.sort(key=lambda x: x[2])

parent = list(range(n))
cost = 0

print("Edges in MST:")

for u, v, w in edges:

    # Find parent of u
    while parent[u] != u:
        u = parent[u]

    # Find parent of v
    while parent[v] != v:
        v = parent[v]

    # If no cycle
    if u != v:
        print(u, "-", v, "=", w)
        cost += w
        parent[v] = u

print("Total Cost:", cost)
