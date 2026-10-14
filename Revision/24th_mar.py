from collections import deque


def second_shortest_path(n, edges):
    g = {i:[] for i in range(1, n + 1)}

    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    inf = float("inf")
    first = [inf]*(n + 1)
    second = [inf]*(n + 1)

    first[1] = 0
    q = deque()
    q.append((1, 0))
    while q:
        u, d = q.popleft()
        for v in g[u]:
            new_d = d + 1
            if new_d < first[v]:
                second[v] = first[v]
                first[v] = new_d
                q.append((v, new_d))
            elif first[v] < new_d < second[v]:
                second[v] = new_d
                q.append((v, new_d))
    return second