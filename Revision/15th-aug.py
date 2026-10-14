from collections import deque


class Node:
    def __init__(self, val, ch):
        self.val = val
        self.ch = []


def rootTree(n, edges, rootVal=0):
    g = {i: [] for i in range(n)}

    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    rootNode = Node(rootVal, [])

    def dfs(node, par):
        for ch_val in g[node.val]:
            if par is not None and ch_val == par.val:
                continue
            chNode = Node(ch_val, [])
            dfs(chNode, node)
            node.ch.append(chNode)

    dfs(rootNode, None)

    return rootNode


def find_centers(n, edges):
    g = {i: [] for i in range(n)}
    degree = [0]*n

    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1

    leaves = []
    for u in range(n):
        if degree[u] == 1:
            leaves.append(u)

    count = len(leaves)

    while count < n:
        new_leaves = []
        for u in leaves:
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    new_leaves.append(v)

        count += len(new_leaves)
        leaves = new_leaves
    return leaves


# edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
# n1 = 5

# print(find_centers(n1, edges1))

# edges2 = [[0, 1], [0, 2], [0, 3]]
# n2 = 4

# print(find_centers(n2, edges2))


def get_scc(n, edges):
    g = {i: [] for i in range(n)}
    for u, v in edges:
        g[u].append(v)

    disc = [-1]*n
    low = [0]*n
    time = 0
    stack = []
    in_stack = [False]*n

    sccs = []

    def dfs(node):
        nonlocal time
        disc[node] = time
        low[node] = time
        time += 1

        stack.append(node)
        in_stack[node] = True

        for ch in g[node]:
            if disc[ch] == -1:
                dfs(ch)
                low[node] = min(low[node], low[ch])
            elif in_stack[ch] == True:
                low[node] = min(low[node], disc[ch])

        if low[node] == disc[node]:
            scc = []
            while True:
                cur = stack.pop()
                in_stack[cur] = False
                scc.append(cur)
                if cur == node:
                    break
            sccs.append(scc)

    for u in range(n):
        if disc[u] == -1:
            dfs(u)

    return sccs


n = 12

edges = [
    [0, 1],
    [1, 2],
    [2, 0],      # SCC A

    [2, 3],

    [3, 4],
    [4, 5],
    [5, 3],      # SCC B

    [4, 6],

    [6, 7],
    [7, 8],
    [8, 6],      # SCC C

    [8, 9],

    [9, 10],
    [10, 11],
    [11, 9]      # SCC D
]

# print(get_scc(n, edges))


# def condensation(n, edges):
#     sccs = get_scc(n, edges)
#     g = {}
#     node_to_root = {}

#     for comp in sccs:
#         root = comp[0]
#         for node in comp:
#             node_to_root[node] = root

#     for u, v in edges:
#         ru, rv = node_to_root[u], node_to_root[v]
#         if ru == rv:
#             continue
#         if ru not in g:
#             g[ru] = []
#         if rv not in g:
#             g[rv] = []
#         g[ru].append(rv)

#     return g


# # print(condensation(n, edges))


# def weighted_lca(n, wedges, queries):
#     g = {i: [] for i in range(n)}

#     for u, v, w in wedges:
#         g[u].append((v, w))
#         g[v].append((u, w))

#     depth = [0]*n
#     weight_to_root = [0]*n

#     LOG = 20
#     up = [[-1]*LOG for _ in range(n)]
#     upWeight = [[0]*LOG for _ in range(n)]
#     upMax = [[0]*LOG for _ in range(n)]

#     def dfs(node, par, cur_depth, cur_weight):
#         depth[node] = cur_depth
#         weight_to_root[node] = cur_weight

#         for ch, ch_w in g[node]:
#             if ch == par:
#                 continue
#             up[ch][0] = node
#             upWeight[ch][0] = ch_w
#             upMax[ch][0] = ch_w
#             dfs(ch, node, cur_depth + 1, cur_weight + ch_w)

#     dfs(0, -1, 0, 0)

#     for k in range(1, LOG):
#         for u in range(n):
#             ansc = up[u][k - 1]
#             if ansc != -1:
#                 up[u][k] = up[ansc][k - 1]
#                 upMax[u][k] = max(upMax[u][k - 1], upMax[ansc][k - 1])
#                 upWeight[u][k] = upWeight[u][k - 1] + upWeight[ansc][k - 1]

#     def get_kth_par(u, k):
#         if u == -1 or k == 0:
#             return u

#         for jump in range(LOG - 1, -1, -1):
#             if (k >= (1 << jump)) and (u != -1):
#                 u = up[u][jump]
#                 k -= (1 << jump)
#         return u

#     def lca(u, v):
#         du, dv = depth[u], depth[v]
#         if du > dv:
#             u = get_kth_par(u, du - dv)
#         if dv > du:
#             v = get_kth_par(v, dv - du)

#         if u == v:
#             return u

#         for jump in range(LOG - 1, -1, -1):
#             if up[u][jump] != up[v][jump]:
#                 u = up[u][jump]
#                 v = up[v][jump]
#         return up[u][0]

#     def find_max_edge(u, v):
#         du, dv = depth[u], depth[v]
#         maxEdge = float("-inf")

#         if du > dv:
#             diff = du - dv
#             for jump in range(LOG - 1, -1, -1):
#                 if (diff >= (1 << jump)):
#                     maxEdge = max(maxEdge, upMax[u][jump])
#                     u = up[u][jump]
#                     diff -= (1 << jump)

#         if dv > du:
#             diff = dv - du
#             for jump in range(LOG - 1, -1, -1):
#                 if (diff >= (1 << jump)):
#                     maxEdge = max(maxEdge, upMax[v][jump])
#                     v = up[v][jump]
#                     diff -= (1 << jump)
#         if u == v:
#             return maxEdge

#         for jump in range(LOG - 1, -1, -1):
#             if up[u][jump] != up[v][jump]:
#                 maxEdge = max(maxEdge, upMax[u][jump], upMax[v][jump])
#                 u = up[u][jump]
#                 v = up[v][jump]

#         return max(maxEdge, upMax[u][0], upMax[v][0])

#     ans = []
#     for u, v in queries:
#         ans.append(find_max_edge(u, v))
#     return ans

def weighted_lca(n, wEdges, queries):
    g = {i: [] for i in range(n)}
    for u, v, w in wEdges:
        g[u].append((v, w))
        g[v].append((u, w))

    depth = [0]*n
    weight_to_root = [0]*n

    LOG = 20
    # our goal is, up[u][k] = 2^kth parent of u
    up = [[-1]*LOG for _ in range(n)]
    # upWeight[u][k] = sum of weights from node to 2^kth parent
    upWeight = [[0]*LOG for _ in range(n)]
    # upMax[u][k] = max weight from node to 2^kth parent
    upMax = [[0]*LOG for _ in range(n)]

    def dfs(node, par, cur_depth, cur_weight):
        depth[node] = cur_depth
        weight_to_root[node] = cur_weight

        for ch, w in g[node]:
            if ch == par:
                continue
            up[ch][0] = node
            upWeight[ch][0] = w
            upMax[ch][0] = w
            dfs(ch, node, cur_depth + 1, cur_weight + w)

    dfs(0, -1, 0, 0)

    for k in range(1, LOG):
        for u in range(n):
            ansc = up[u][k - 1]
            if ansc != -1:
                up[u][k] = up[ansc][k - 1]
                upWeight[u][k] = upWeight[u][k - 1] + upWeight[ansc][k - 1]
                upMax[u][k] = max(upMax[u][k - 1], upMax[ansc][k - 1])

    def get_kth_par(u, k):
        if k == 0 or u == -1:
            return u

        for jump in range(LOG - 1, -1, -1):
            if k >= (1 << jump) and u != -1:
                u = up[u][jump]
                k -= (1 << jump)
        return u

    def lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            u = get_kth_par(u, du - dv)
        if dv > du:
            v = get_kth_par(v, dv - du)

        if u == v:
            return u

        for jump in range(LOG - 1, -1, -1):
            if up[u][jump] != up[v][jump]:
                u = up[u][jump]
                v = up[v][jump]
        return up[u][0]

    def get_max_edge_in_path(u, v):
        du, dv = depth[u], depth[v]
        max_edge = float("-inf")

        if du > dv:
            diff = du - dv
            for jump in range(LOG - 1, -1, -1):
                if diff >= (1 << jump):
                    max_edge = max(max_edge, upMax[u][jump])
                    u = up[u][jump]
                    diff -= (1 << jump)

        if dv > du:
            diff = dv - du
            for jump in range(LOG - 1, -1, -1):
                if diff >= (1 << jump):
                    max_edge = max(max_edge, upMax[v][jump])
                    v = up[v][jump]
                    diff -= (1 << jump)

        if u == v:
            return max_edge

        for jump in range(LOG - 1, -1, -1):
            if up[u][jump] != up[v][jump]:
                max_edge = max(max_edge, upMax[u][jump], upMax[v][jump])
                u = up[u][jump]
                v = up[v][jump]

        return max(max_edge, upMax[u][0], upMax[v][0])

    answer = []
    for u, v in queries:
        answer.append(get_max_edge_in_path(u, v))
    return answer


n = 16
wEdges = [[0, 1, -8], [0, 2, 4], [0, 3, -1], [1, 4, -10], [1, 5, 5], [1, 6, 3], [4, 7, -5],
          [6, 8, -3], [2, 9, 4], [2, 10, -8], [3, 11, 1], [3, 12, -6], [3, 13, -9], [3, 14, -4], [7, 15, 30]]

print(weighted_lca(n, wEdges, [[9, 14], [2, 9], [15, 8]]))


def euler_directed(n, edges):
    g = {i: [] for i in range(n)}
    indegree = [0]*n
    outdegree = [0]*n
    for u, v in edges:
        g[u].append(v)
        indegree[v] += 1
        outdegree[u] += 1

    plus = 0
    minus = 0
    start = -1

    for u in range(n):
        diff = outdegree[u] - indegree[u]
        if diff == 1:
            plus += 1
            start = u
        elif diff == -1:
            minus += 1
        elif diff != 0:
            return []

    valid = (plus == 1 and minus == 1) or (plus == 0 and minus == 0)
    if not valid:
        return []

    if (plus == 0 and minus == 0):
        for u in range(n):
            if outdegree[u] > 0:
                start = u
                break

    path = deque()

    def dfs(u):
        while g[u]:
            cur = g[u].pop()
            dfs(cur)
        path.appendleft(u)

    dfs(start)
    if len(path) == len(edges) + 1:
        return list(path)
    return []


n = 4
edges = [
    [0, 1],
    [1, 2],
    [2, 0],

    [0, 3],
    [3, 2]
]

# print(euler_directed(n, edges))


def euler_undirected(n, edges):
    g = {i: [] for i in range(n)}
    degree = [0]*n
    used = [False]*(len(edges))

    for i in range(len(edges)):
        edge = edges[i]
        u, v = edge[0], edge[1]
        g[u].append((v, i))
        g[v].append((u, i))
        degree[u] += 1
        degree[v] += 1

    odd = 0
    start = -1

    for u in range(n):
        if degree[u] % 2 == 1:
            odd += 1
            start = u

    valid = (odd == 0) or (odd == 2)
    if not valid:
        return []

    if odd == 0:
        for u in range(n):
            if degree[u] > 0:
                start = u
                break

    path = deque()

    def dfs(node):
        while g[node]:
            ch, eid = g[node].pop()
            if used[eid]:
                continue
            used[eid] = True
            dfs(ch)
        path.appendleft(node)

    dfs(start)

    if (len(edges) + 1) == len(path):
        return list(path)

    return []


n = 7
edges = [
    [0, 1],
    [1, 2],
    [2, 0],

    [0, 3],
    [3, 4],
    [4, 0],

    [2, 5],
    [5, 6],
    [6, 2]
]

# print(euler_undirected(n, edges))


class RollbackDSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

        self.history = []

    def find(self, x):
        while self.par[x] != x:
            x = self.par[x]
        return x

    def snapshot(self):
        return len(self.history)

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        # p2, old parent of p2, p1 old size of p1
        self.history.append((p2, self.par[p2], p1, self.rank[p1]))
        self.par[p2] = p1
        self.rank[p1] += self.rank[p2]
        return

    def rollback(self, k):
        while len(self.history) > k:
            p2, old_par_of_p2, p1, old_size_of_p1 = self.history.pop()
            self.par[p2] = old_par_of_p2
            self.rank[p1] = old_size_of_p1


class SegTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r

        self.edges = []

        self.left = None
        self.right = None


def dynaminConnectivity(n, operations):
    active_edges = {}  # to findout the start and end times of the edge
    edge_lifetimes = []  # to store(edge, [l, r)) of each edge

    queries_at_time = [None]*(len(operations) + 1)

    for time in range(len(operations) + 1):
        cur_op = operations[time - 1]
        op_type, u, v = cur_op
        edge = tuple(sorted((u, v)))

        if op_type == 1:
            active_edges[edge] = time
        elif op_type == 2:
            l = active_edges.pop(edge)
            r = time
            edge_lifetimes.append((edge, l, r))
        elif op_type == 3:
            queries_at_time[time] = edge

    for edge in active_edges:
        l = active_edges[edge]
        r = len(operations) + 1
        edge_lifetimes.append((edge, l, r))

    def build_seg_tree(start_time, end_time):
        cur_node = SegTreeNode(start_time, end_time)

        if end_time - start_time == 1:
            return cur_node

        m = (start_time + end_time) // 2
        cur_node.left = build_seg_tree(start_time, m)
        cur_node.right = build_seg_tree(m, end_time)
        return cur_node

    root = build_seg_tree(1, len(operations) + 1)

    def add_edge_to_node(cur_node, edge, edge_start_time, edge_end_time):
        node_start_time = cur_node.l
        node_end_time = cur_node.r

        # No overlap case
        if (node_end_time <= edge_start_time or edge_end_time <= node_start_time):
            return

        # Complete overlap of node's range inside the edges range
        if (edge_start_time <= node_start_time and node_end_time <= edge_end_time):
            cur_node.edges.append(edge)
            return

        # Partial overlap
        add_edge_to_node(cur_node.left, edge, edge_start_time, edge_end_time)
        add_edge_to_node(cur_node.right, edge, edge_start_time, edge_end_time)

    for edge, start_time, end_time in edge_lifetimes:
        add_edge_to_node(root, edge, start_time, end_time)

    rollback_dsu = RollbackDSU(n)
    answer = []

    def dfs(node):
        # remember the history position before any change
        snap = rollback_dsu.snapshot()

        # union all the edges of the current seg tree node
        for u, v in node.edges:
            rollback_dsu.union(u, v)

        if node.r - node.l == 1:  # meaning we are at leaf node
            query = queries_at_time[node.l]
            if query is not None:
                u, v = query
                pu, pv = rollback_dsu.find(u), rollback_dsu.find(v)
                answer.append(pu == pv)

        else:
            dfs(node.left)
            dfs(node.right)

        rollback_dsu.rollback(snap)

    dfs(root)
    return answer


n = 6

operations = [
    [1, 0, 1],   # 0-1
    [1, 1, 2],   # 1-2
    [1, 3, 4],   # 3-4

    [3, 0, 2],   # QUERY 0-2
    [3, 0, 4],   # QUERY 0-4

    [1, 2, 3],   # 2-3

    [3, 0, 4],   # QUERY 0-4

    [2, 1, 2],   # REMOVE 1-2

    [3, 0, 4],   # QUERY 0-4
    [3, 1, 4],   # QUERY 1-4
]

# print(dynaminConnectivity(n, operations))


# class ParityDSU:

#     def __init__(self, n):

#         self.parent = [i for i in range(n)]
#         self.size = [1] * n

#         # relation[x]:
#         #
#         # 0 → x and parent[x] are SAME
#         # 1 → x and parent[x] are DIFFERENT
#         self.relation = [0] * n

#     def find(self, node):

#         relationship_to_root = 0

#         current_node = node

#         while self.parent[current_node] != current_node:

#             relationship_to_root = relationship_to_root ^ self.relation[current_node]

#             current_node = self.parent[current_node]

#         return (current_node, relationship_to_root)

#     def union(self, first_node, second_node):

#         first_root, first_relation = self.find(first_node)
#         second_root, second_relation = self.find(second_node)

#         # The edge requires the two nodes
#         # to belong to DIFFERENT groups.
#         required_relation = 1

#         # -----------------------------------------
#         # Case 1:
#         # Already in the same connected component.
#         # -----------------------------------------

#         if first_root == second_root:
#             existing_relation = (first_relation ^ second_relation)

#             # Existing relationship conflicts
#             # with the new edge.
#             if existing_relation != required_relation:
#                 return False
#             # Constraint is already satisfied.
#             return True

#         # -----------------------------------------
#         # Case 2:
#         # Different connected components.
#         # -----------------------------------------

#         # We need:
#         #
#         # first_root
#         #     |
#         #     ?
#         #     |
#         # second_root
#         #
#         # The required relationship is:
#         #
#         # first_relation
#         # XOR
#         # required_relation
#         # XOR
#         # second_relation

#         relationship_between_roots = (first_relation ^ required_relation ^ second_relation)

#         # Union by size.
#         if self.size[first_root] < self.size[second_root]:

#             first_root, second_root = ( second_root, first_root)

#         # Attach second component under first component.
#         self.parent[second_root] = first_root
#         # Store the relationship between the new child
#         # root and its new parent.
#         self.relation[second_root] = relationship_between_roots

#         self.size[first_root] += self.size[second_root]

#         return True


'''
Now what do we know for certain is that when there is an edge between 2 nodes (u)-----(v), they should belong to different groups, but our realtion[] array will store 
the relation between (u) and its (root). So when we find out (ru) and (rv) then we need to fingure out what should be the relation between (ru) and (rv) such that (u) (v) belong to different groups.
'''
