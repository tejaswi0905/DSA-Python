# When the graph have negative cycles.

from collections import defaultdict, deque

def bellman_ford_adj(n, edges, start):
    g = defaultdict(list)

    for u, v, w in edges:
        g[u].append((v, w))
    
    dist = [float("inf")] * (n)
    prev = [None] * (n)
    dist[start] = 0

    for _ in range(n - 1):
        for u in range(n):
            if dist[u] == float("inf"):
                continue
            for v, w in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    is_effected = False
    effected = set()
    for u in range(n):
        if dist[u] == float("inf"):
            continue
        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                effected.add(v)
                is_effected = True
    if not is_effected:
        return dist
    q = deque(effected)
    visited = set(effected)
    while q:
        node = q.popleft()
        for ng, w in g[node]:
            if ng not in visited:
                visited.add(ng)
                q.append(ng)
    return visited


edges = [[0, 1, 5], [1, 2, 20], [1, 5, 30], [1, 6, 60], [2, 3, 10], [2, 4, 75], [4, 9, 100], [5, 8, 50], [5, 6, 5], [5, 4, 25], [6, 7, -50], [7, 8, -10]]

print(bellman_ford_adj(10, edges, 0))