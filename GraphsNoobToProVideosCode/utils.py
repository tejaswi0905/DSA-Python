from collections import defaultdict, deque

def lca_array(edges, queries):
    graph = defaultdict(list)
    n = len(edges) + 1
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    LOG = 10
    parent = [[-1] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)

    def bfs(root):
        q = deque()
        q.append([root, -1])

        while q:
            node, parnet = q.popleft()
            for ch in graph[node]:
                if ch != parnet:
                    depth[ch] = depth[node] + 1
                    q.append([ch, node])
                    parent[ch][0] = node
    bfs(1)
    for k in range(1, LOG):
        for v in range(1, n + 1):
            if parent[v][k - 1] != -1:
                parent[v][k] = parent[parent[v][k-1]][k-1]
    
    def getKthAncestor(node, k):
        if k == 0 or node == -1:
            return node
        for i in range(LOG - 1, -1, -1):
            if k >= (1 << i) and node != -1:
                node = parent[node][i]
                k = k - (1 << i)
        return node
    
    def lca(u, v):
        if depth[u] > depth[v]:
            u = getKthAncestor(u, depth[u] - depth[v])
        if depth[v] > depth[u]:
            v = getKthAncestor(v, depth[v] - depth[u])
        if u == v:
            return u
        for i in range(LOG - 1, -1, -1):
            if parent[u][i] != parent[v][i]:
                u = parent[u][i]
                v = parent[v][i]
        return parent[u][0]

    print(lca(6, 4)) 
    

print(lca_array([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)], []))
                    

    
