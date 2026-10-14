from collections import deque, defaultdict

def second_shortest_path(n, edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    INF = float('inf')

    best = [INF]*(n+1)
    second = [INF]*(n+1)

    q = deque()

    best[1] = 0
    q.append((1,0))

    while q:

        node, dist = q.popleft()

        for nei in graph[node]:

            new_dist = dist + 1

            if new_dist < best[nei]:

                second[nei] = best[nei]
                best[nei] = new_dist

                q.append((nei, new_dist))

            elif best[nei] < new_dist < second[nei]:

                second[nei] = new_dist
                q.append((nei, new_dist))

    return second[n]

edges = [[1, 2], [1, 3], [2, 4]]
print(second_shortest_path(4, edges))

import heapq as hq
def kth_shortest_path(n, k,edges):
    g = {}
    for u, v in edges:
        g.setdefault(u, []).append(v)
        g.setdefault(v, []).append(u)
    
    dist = [[] for _ in range(n + 1)]
    pq = [(0, 1)]
    while pq:
        d, u = hq.heappop(pq)
        if len(dist[u]) >= k:
            continue
        dist[u].append(d)
        for v in g[u]:
            hq.heappush(pq, (d + 1, v))
    if len(dist[n]) >= k:
        return dist[n][k - 1]
    return -1

print(kth_shortest_path(4, 2, edges))

