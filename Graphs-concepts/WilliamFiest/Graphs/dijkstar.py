from collections import defaultdict
import heapq as hq

edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5], [3, 4, 3]]

def lazy_dijkstra(edges, n):
    g = defaultdict(list) # the adj_list
    prev = [None] * n
    min_heap = [] # we are going to store the {dist, node} pairs in this min_heap
    for u, v, w in edges:
        g[u].append([v, w])
    
    dist = [float("inf")] * (n)
    dist[0] = 0
    hq.heappush(min_heap, (0, 0)) # append (dist, node) pairs

    while min_heap:
        cur_dist, node = hq.heappop(min_heap)
        if dist[node] < cur_dist:
            continue
        for ng, w in g[node]:
            ng_dist = cur_dist + w
            if ng_dist < dist[ng]:
                dist[ng] = ng_dist
                prev[ng] = node
                hq.heappush(min_heap, (ng_dist, ng))
    for i, val in enumerate(prev):
        print(i, val)
    return dist

print(lazy_dijkstra(edges, 5))