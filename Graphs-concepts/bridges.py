edges = [[1,2], [2,3], [1,3], [2,4], [4,5], [5,6], [6,7], [4,7], [5,8], [8,9]]

def bridges_and_articulation_points(edges, n):
    adj_list = {i:[] for i in range(1, n + 1)}
    visited = [0] * (n + 1)
    parents = [0] * (n + 1)
    discovery_time = [0] * (n + 1)
    low_time = [0] * (n + 1)
    bridge_edges = []
    articulation_points = []
    time = [1]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def dfs(node, parent):
        child_count = 0
        visited[node] = 1
        parents[node] = parent
        discovery_time[node] = time[0]
        low_time[node] = time[0]
        time[0] += 1

        for ch in adj_list[node]:
            if visited[ch] == 0:
                dfs(ch, node)
                child_count += 1
                low_time[node] = min(low_time[node], low_time[ch])
                if low_time[ch] > discovery_time[node]:
                    bridge_edges.append((node, ch))
                if parent != 0 and low_time[ch] >= discovery_time[node]:
                    articulation_points.append(node)
            elif ch != parent and visited[ch] == 1:
                low_time[node] = min(low_time[node], discovery_time[ch])
        visited[node] = 2
        if parent == 0 and child_count > 1:
            articulation_points.append(node)
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, 0)

    print(articulation_points)
    print(bridge_edges)

print(bridges_and_articulation_points(edges, 9))



