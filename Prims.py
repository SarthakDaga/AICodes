import heapq

n = int(input("Enter no. of vertices: "))
e = int(input("Enter no. of edges: "))

graph = {i: [] for i in range(n)}

print(f"Enter {e} edges (u v weight): ")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

start = int(input("Start Node: "))

pq = [(0, start, None)]
visited = set()
mst = []
total_cost = 0

while pq and len(visited) < n:
    w, curr, prev = heapq.heappop(pq)

    if curr not in visited:
        visited.add(curr)
        total_cost += w

        if prev is not None:
            mst.append((prev, curr, w))

        for nw, nei in graph[curr]:
            if nei not in visited:
                heapq.heappush(pq, (nw, nei, curr))

print(f"MST: {mst}\nTotal Cost: {total_cost}")
