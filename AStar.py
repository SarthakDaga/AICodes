import heapq

# Vertex and Edge count
n, e = map(int, input("Nodes & Edges: ").split())
graph = {}
for _ in range(e):
    u, v, c = map(int, input("u v cost: ").split())
    graph.setdefault(u, []).append((v, c))
    graph.setdefault(v, []).append((u, c))

h = list(map(int, input("Heuristics: ").split()))
s, g_node = map(int, input("Start & Goal: ").split())

def astar():
    pq, vis = [(h[s], 0, s, [s])], set()
    while pq:
        f, g, u, path = heapq.heappop(pq)
        if u == g_node: return path, g
        if u not in vis:
            vis.add(u)
            # .get(u, []) prevents errors if a node has no edges
            for v, cost in graph.get(u, []):
                heapq.heappush(pq, (g + cost + h[v], g + cost, v, path + [v]))
    return None, -1

path, cost = astar()
print(f"Path: {path}\nCost: {cost}" if path else "No Path Found")
