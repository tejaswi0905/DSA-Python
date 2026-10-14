from collections import deque


def tree_distances(n, edges):
    g = {i: [] for i in range(n)}
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    depth = [0]*n
    sizes = [1]*n

    def dfs(u, p, d):
        depth[u] = d

        for v in g[u]:
            if v == p:
                continue
            dfs(v, u, d + 1)
            sizes[u] += sizes[v]

    dfs(0, -1, 0)

    ans = [0]*n
    ans[0] = sum(depth)

    def reroot(u, p):
        for v in g[u]:
            if v == p:
                continue
            ans[v] = ans[u] + (n - 2 * sizes[v])
            reroot(v, u)
    reroot(0, -1)
    return ans


def counting_paths(n, edges, paths):
    g = {i: [] for i in range(n)}
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    LOG = 20
    up = [[-1]*LOG for _ in range(n)]

    depth = [0]*n
    values = [0]*n

    def dfs1(u, p, d):
        depth[u] = d
        for v in g[u]:
            if v == p:
                continue
            up[v][0] = u
            dfs1(v, u, d + 1)
    dfs1(0, -1, 0)

    for k in range(1, LOG):
        for u in range(n):
            ancs = up[u][k - 1]
            if ancs != -1:
                up[u][k] = up[ancs][k - 1]

    def get_kth_par(u, k):
        if u == -1 or k == 0:
            return u

        for jump in range(LOG - 1, -1, -1):
            if k >= (1 << jump):
                u = up[u][jump]
                k -= (1 << jump)
        return u

    def lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            diff = du - dv
            u = get_kth_par(u, diff)
        if dv > du:
            diff = dv - du
            v = get_kth_par(v, diff)

        if u == v:
            return u

        for jump in range(LOG - 1, -1, -1):
            if up[u][jump] != up[v][jump]:
                u = up[u][jump]
                v = up[v][jump]
        return up[u][0]

    for u, v in paths:
        l = lca(u, v)
        values[u] += 1
        values[v] += 1
        values[l] -= 1
        if l != 0:
            values[up[l][0]] -= 1

    def dfs(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs(v, u)
            values[u] += values[v]

    dfs(0, -1)
    return values


def main():
    n, m = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        edge = list(map(int, input().split()))
        edges.append([edge[0] - 1, edge[1] - 1])
    queries = []
    for _ in range(m):
        query = list(map(int, input().split()))
        queries.append([query[0] - 1, query[1] - 1])

    print(edges, queries)

    ans = counting_paths(n, edges, queries)
    print(ans)


