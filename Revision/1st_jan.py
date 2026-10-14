from collections import deque
import heapq as hq

edges = [[1,2],[1,4],[1,6],[2,3],[2,5],[6,7],[5,8],[8,12],[8,9],[9,10],[10,11]]
n = 12

def print_matrix(grid):
    for row in grid:
        print(row)


def build_graph(n, edges):
    adj_list = {}
    for i in range(1, n + 1):
        adj_list[i] = []
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


log = 3
up = [[-1] * log for _ in range(n + 1)]
depth = [0] * (n + 1)
g = build_graph(n, edges)

def dfs(u, du, p):
    up[u][0] = p
    depth[u] = du
    for ch in g[u]:
        if ch != p:
            dfs(ch, du+1,u)

dfs(1,0, -1)

for u in range(1, n + 1):
    for k in range(1, log):
        if up[u][k - 1]!= -1:
            v = up[u][k-1]
            up[u][k] = up[v][k-1]

def get_kth_ancestor(u, k):
    if k == 0 or u == -1:
        return u
    for i in range(log-1, -1, -1):
        if k >= (1<<i):
            u = up[u][i]
            k-=(1<<i)
    return u

def lca(u, v):
    du, dv = depth[u], depth[v]
    if du > dv:
        u = get_kth_ancestor(u, du - dv)
    elif dv > du:
        v = get_kth_ancestor(v, dv - du)
    if u == v:
        return u
    for i in range(log - 1, -1, -1):
        if up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
    return up[u][0]

class Node:
    def __init__(self, val, par, ch = []):
        self.val = val
        self.par = par
        self.ch = ch



def buildTree(node,par,g):
    for ch_val in g[node.val]:
        if par != None and ch_val == par.val:
            continue
        ch_node = Node(ch_val, node, [])
        buildTree(ch_node, node, g)
        node.ch.append(ch_node)
    return node

def rootTree(g, root=0):
    temp = Node(root, None, [])
    rootNode = buildTree(temp, None, g)
    return rootNode


def get_centers(n, edges):
    degree = [0] * (n + 1)
    g = {}
    for i in range(1, n + 1):
        g[i] = []
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    cur_list = []
    for i in range(1,n + 1):
        if degree[i] == 1:
            cur_list.append(i)
    cnt = len(cur_list)
    while cnt < n:
        new_list = []
        for u in cur_list:
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    new_list.append(v)
        cnt += len(new_list)
        cur_list = new_list
    return cur_list

print(get_centers(12, edges))

def get_sign(node):
    if len(node.ch) == 0:
        return f"()"
    ch_strings = [get_sign(ch) for ch in node.ch]
    return f"({"".join(ch_strings)})"

root = rootTree(g, 1)
print(get_sign(root))

def is_isomorphic(n1, n2, edges1, edges2):
    c1 = get_centers(n1, edges1)
    c2 = get_centers(n2, edges2)
    g1 = build_graph(n1, edges1)
    g2 = build_graph(n2, edges2)
    r1 = [rootTree(g1, c) for c in c1]
    r2 = [rootTree(g2, c) for c in c2]
    for root1 in r1:
        for root2 in r2:
            if get_sign(root1) == get_sign(root2):
                return True
    return False


edges3 = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (5, 7),
    (5, 8),
    (6, 9),
    (6, 10),
    (4, 11),
    (4, 12),
    (11, 13),
    (11, 14),
    (12, 15),
    (12, 16)
]
n3 = 16
edges4 = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (5, 7),
    (5, 8),
    (6, 9),
    (6, 10),
    (4, 11),
    (4, 12),
    (11, 15),
    (11, 16),
    (12, 13),
    (12, 14)
]
n4 = 16
print(is_isomorphic(n3, n4, edges3, edges4))

# Now weighted graphs, for DAG with weights, we can use top-sort + relaxation graph can have negative edges, Now graphs with cycles, if it dosent have any negaive edges we can use dikstra, if it does have negative edges but it dosent have any negative cycles then we can use Bellaman ford

edgesw = [[1, 2, 3], [1, 3, 6], [2, 3, 4], [2, 4, 4],[2, 5, 11], [3, 4, 8], [3, 7, 11], [4, 5, 4], [4, 6, 5], [4, 7, 2], [5, 8, 6], [6, 8, 1], [7, 8, 2]]

def top_sort(n, edges):
    g = {}
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        g[i] = []
    for u, v, w in edges:
        g[u].append(v)
        indegree[v] += 1

    q = deque()
    
    for u in range(1, n + 1):
        if indegree[u] == 0:
            q.append(u)
    top_order = []
    while q:
        u = q.popleft()
        top_order.append(u)
        for v in g[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    if len(top_order) == n:
        return top_order
    return []

def shortest_path_in_DAG(n, edges, start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    top_order = top_sort(n, edges)
    g = {}
    for i in range(1, n + 1):
        g[i] = []
    for u, v, w in edges:
        g[u].append([v, w])
    
    for u in top_order:
        cur = dist[u]
        for v, w in g[u]:
            new = cur + w
            if new < dist[v]:
                dist[v] = new
    return dist

def dijkstra(n, edges, start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    g = {}
    for i in range(1, n + 1):
        g[i] = []
    for u, v, w in edges:
        g[u].append([v, w])
    min_heap = []
    hq.heappush(min_heap, (0, start))
    while min_heap:
        cur, u = hq.heappop(min_heap)
        for v, w in g[u]:
            new = cur + w
            if new < dist[v]:
                dist[v] = new
                hq.heappush(min_heap, (new, v))
    return dist

print(dijkstra(8, edgesw, 1))
print(shortest_path_in_DAG(8, edgesw, 1))
