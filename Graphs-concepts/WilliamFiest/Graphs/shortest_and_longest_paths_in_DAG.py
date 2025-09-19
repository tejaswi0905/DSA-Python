import heapq as hq

from collections import defaultdict

edges = [[1, 2, 3], [1, 3, 6], [2, 3, 4], [2, 4, 4],[2, 5, 11], [3, 4, 8], [3, 7, 11], [4, 5, -4], [4, 6, 5], [4, 7, 2], [5, 8, 6], [6, 8, 1], [7, 8, 2]]

def top_sort(edges, n):
    g = defaultdict(list)
    in_degree = [0] * (n + 1)
    for u, v, w in edges:
        g[u].append((v, w))
        in_degree[v] += 1
    
    min_heap = []
    top_order = []
    for node in range(1, n + 1):
        if in_degree[node] == 0:
            hq.heappush(min_heap, node)
    while min_heap:
        node = hq.heappop(min_heap)
        top_order.append(node)
        for v, w in g[node]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                hq.heappush(min_heap, v)
    if len(top_order) != n:
        return []
    return top_order

def shortest_path_in_dag(edges, n):
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
    
    top_order = top_sort(edges, n)
    if not top_order:
        return -1
    
    dist = [float("inf")] * (n + 1)
    start = 1
    dist[start] = 0
    for node in top_order:
        cur_dist = dist[node]
        for ng, w in g[node]:
            if cur_dist + w < dist[ng]:
                dist[ng] = cur_dist + w
    return dist
print(shortest_path_in_dag(edges, 8))
