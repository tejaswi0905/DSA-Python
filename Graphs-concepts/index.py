
# def divide_the_graph(edges, n):
#     g = {i: [] for i in range(n)}
#     for u, v in edges:
#         g[u].append(v)
#         g[v].append(u)

#     colored = [0]*n

#     def dfs(node, color):
#         if colored[node] != 0:
#             if colored[node] == color:
#                 return True
#             else:
#                 return False

#         colored[node] = color
#         if color == 1:
#             new_color = 2
#         else:
#             new_color = 1

#         for ng in g[node]:
#             is_poss = dfs(ng, new_color)
#             if is_poss == False:
#                 return False
#         return True

#     ans = True

#     for node in range(n):
#         if colored[node] == 0:
#             ans = ans and dfs(node, 1)
#     return ans


# print(divide_the_graph(edges, n))

# The main components of DSU, the union, rank and find

# from collections import deque


from collections import deque


def paths(edges, n, queries):
    par = [i for i in range(n)]
    rnk = [1 for i in range(n)]

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False
        if rnk[p1] < rnk[p2]:
            p1, p2 = p2, p1
        par[p2] = p1
        rnk[p1] += rnk[p2]
        return True


# n = 4
# queries = [[1, 1, 2], [3, 2, 3], [2, 3]]


# class Team:
#     def __init__(self, parent, count, strength):
#         self.parent = parent
#         self.count = count
#         self.strength = strength


# def teamUp(n, queries):
#     teamOf = [i for i in range(n + 1)]
#     teams = [None]
#     for i in range(1, n + 1):
#         team = Team(i, 1, i)
#         teams.append(team)

#     def findTeam(u):
#         currentTeam = teamOf[u]
#         while currentTeam != teams[currentTeam].parent:
#             currentTeam = teams[currentTeam].parent
#         teamOf[u] = currentTeam
#         return currentTeam

#     def merge(n1, n2):
#         t1, t2 = findTeam(n1), findTeam(n2)
#         if t1 == t2:
#             return
#         teams[t2].count += teams[t1].count
#         teams[t2].strength += teams[t1].strength

#         teams[t1].parent = t2
#         teams[t1].count = 0
#         teams[t1].strength = 0

#     def move(n1, n2):
#         t1, t2 = findTeam(n1), findTeam(n2)
#         if t1 == t2:
#             return
#         teams[t2].count += 1
#         teams[t2].strength += n1

#         teams[t1].count -= 1
#         teams[t1].strength -= n1

#         teamOf[n1] = t2

#     for q in queries:
#         if q[0] == 1:
#             _, c1, c2 = q
#             merge(c1, c2)
#         if q[0] == 3:
#             _, c1, c2 = q
#             move(c1, c2)
#         if q[0] == 2:
#             _, c = q
#             teamIdx = findTeam(c)
#             team = teams[teamIdx]
#             print(
#                 f"The count and strength of node {c} are {team.count}, and {team.strength}")


class Team:
    def __init__(self, parent, member_count, total_strength):
        self.parent = parent
        self.member_count = member_count
        self.total_strength = total_strength


def team_up(n, queries):
    # person_to_node[u] = the DSU node currently representing person u
    person_to_node = [i for i in range(n + 1)]

    # teams[i] = information about DSU node i
    teams = [None]

    for person in range(1, n + 1):
        teams.append(
            Team(
                parent=person,
                member_count=1,
                total_strength=person
            )
        )

    def find_team_root(person):
        """
        Find the root team containing 'person'.

        person
            ↓
        person_to_node[person]
            ↓
        DSU node
            ↓
        parent
            ↓
        ...
            ↓
        root team
        """

        current_node = person_to_node[person]

        while current_node != teams[current_node].parent:
            current_node = teams[current_node].parent

        # Path compression:
        # Next time, start this person directly at the root.
        person_to_node[person] = current_node

        return current_node

    def merge_teams(person1, person2):
        """
        Merge the teams containing person1 and person2.
        """

        team1_root = find_team_root(person1)
        team2_root = find_team_root(person2)

        if team1_root == team2_root:
            return

        # Add team1's information into team2.
        teams[team2_root].member_count += teams[team1_root].member_count
        teams[team2_root].total_strength += teams[team1_root].total_strength

        # Attach team1's root underneath team2's root.
        teams[team1_root].parent = team2_root

        # team1_root is no longer a root,
        # so its aggregate information is no longer used.
        teams[team1_root].member_count = 0
        teams[team1_root].total_strength = 0

    def move_person(person, destination_person):
        """
        Move 'person' into the team containing 'destination_person'.
        """

        source_team_root = find_team_root(person)
        destination_team_root = find_team_root(destination_person)

        if source_team_root == destination_team_root:
            return

        # Remove person from their old team's aggregate information.
        teams[source_team_root].member_count -= 1
        teams[source_team_root].total_strength -= person

        # Add person to the destination team's aggregate information.
        teams[destination_team_root].member_count += 1
        teams[destination_team_root].total_strength += person

        # Change the person's entry point into the DSU.
        person_to_node[person] = destination_team_root

    for query in queries:

        if query[0] == 1:
            _, person1, person2 = query
            merge_teams(person1, person2)

        elif query[0] == 2:
            _, person = query

            team_root = find_team_root(person)
            team = teams[team_root]

            print(
                f"The count and strength of team containing "
                f"person {person} are "
                f"{team.member_count}, {team.total_strength}"
            )

        elif query[0] == 3:
            _, person1, person2 = query
            move_person(person1, person2)


queries = [[1, 1, 2], [1, 1, 3], [3, 1, 4], [2, 2], [2, 3], [2, 1], [2, 5]]
# team_up(5, queries)

"""
Now we are dealing with the DUS + rollback and SegTree over time and dfs through the tree.

"""


class RollbackDSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rnk = [1 for i in range(n)]
        self.history = []

    def find(self, x):
        while self.par[x] != x:
            x = self.par[x]
        return x

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return

        if self.rnk[p1] < self.rnk[p2]:
            p1, p2 = p2, p1

        self.history.append((p2, self.par[p2], p1, self.rnk[p1]))

        self.par[p2] = p1
        self.rnk[p1] += self.rnk[p2]

    def snapshot(self):
        return len(self.history)

    def rollback(self, k):
        while len(self.history) > k:
            (n2, old_par_n2, n1, old_size_n1) = self.history.pop()
            self.par[n2] = old_par_n2
            self.rnk[n1] = old_size_n1


class TimeSegmentTreeNode:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

        self.left_child = None
        self.right_child = None

        self.edges = []


def dynaminConnectivity(n, operations):
    active_edges = {}
    edge_lifetime = []

    queries_at_time = [None] * (len(operations) + 1)
    rollback_dsu = RollbackDSU(n)

    answers = []

    # -----------------------------------------
    # Find edge lifetimes and queries
    # -----------------------------------------

    for time in range(1, len(operations) + 1):
        cur_op = operations[time - 1]
        op_type, u, v = cur_op
        edge = tuple(sorted((u, v)))

        if op_type == 1:
            active_edges[edge] = time

        elif op_type == 2:
            added_time = active_edges.pop(edge)
            edge_lifetime.append((edge, added_time, time))

        elif op_type == 3:
            queries_at_time[time] = edge

    # -----------------------------------------
    # Edges still alive
    # -----------------------------------------

    for edge in active_edges:
        added_time = active_edges[edge]
        edge_lifetime.append((edge, added_time, len(operations) + 1))

    # -----------------------------------------
    # Build segment tree
    # -----------------------------------------

    def build_seg_tree(start_time, end_time):
        cur_node = TimeSegmentTreeNode(start_time, end_time)

        if end_time - start_time == 1:
            return cur_node

        middle_time = (start_time + end_time) // 2

        cur_node.left_child = build_seg_tree(start_time, middle_time)
        cur_node.right_child = build_seg_tree(middle_time, end_time)

        return cur_node

    # -----------------------------------------
    # Add edge to segment tree
    # -----------------------------------------

    def add_edge_to_node(cur_node, edge, edge_start_time, edge_end_time):
        node_start = cur_node.start_time
        node_end = cur_node.end_time

        # No overlap
        if (node_end <= edge_start_time or edge_end_time <= node_start):
            return

        # Complete overlap
        if (edge_start_time <= node_start and node_end <= edge_end_time):
            cur_node.edges.append(edge)
            return

        # Partial overlap
        add_edge_to_node(cur_node.left_child, edge,
                         edge_start_time, edge_end_time)
        add_edge_to_node(cur_node.right_child, edge,
                         edge_start_time, edge_end_time)
    # -----------------------------------------
    # DFS
    # -----------------------------------------

    def dfs(cur_node):
        snap = rollback_dsu.snapshot()

        # Add all edges belonging to this interval
        for u, v in cur_node.edges:
            rollback_dsu.union(u, v)

        # Leaf = one exact time
        if cur_node.end_time - cur_node.start_time == 1:
            cur_time = cur_node.start_time

            if queries_at_time[cur_time] is not None:
                u, v = queries_at_time[cur_time]
                pu = rollback_dsu.find(u)
                pv = rollback_dsu.find(v)
                answers.append(pu == pv)

        else:
            dfs(cur_node.left_child)
            dfs(cur_node.right_child)

        # Restore DSU
        rollback_dsu.rollback(snap)

    # -----------------------------------------
    # Start
    # -----------------------------------------

    root = build_seg_tree(1, len(operations) + 1)
    for edge, start_time, end_time in edge_lifetime:
        add_edge_to_node(root, edge, start_time, end_time)

    dfs(root)

    return answers


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

print(dynaminConnectivity(n, operations))


'''--------------------------------------------------------------------------'''

'''
finding centers,
rooted tree,
isomorphic trees (needs some more clarification),

lca,
lca weighted

scc, ✔️
condendation of scc ✔️
'''

# n = 12

# edges = [
#     [0, 1],
#     [1, 2],
#     [2, 0],      # SCC A

#     [2, 3],

#     [3, 4],
#     [4, 5],
#     [5, 3],      # SCC B

#     [4, 6],

#     [6, 7],
#     [7, 8],
#     [8, 6],      # SCC C

#     [8, 9],

#     [9, 10],
#     [10, 11],
#     [11, 9]      # SCC D
# ]


def find_sccs(n, edges):
    g = {i: [] for i in range(n)}
    for u, v in edges:
        g[u].append(v)

    low = [0]*n
    disc = [-1]*n

    stack = []
    in_stack = [False]*n

    time = 0
    sccs = []

    def dfs(node):
        nonlocal time
        low[node] = time
        disc[node] = time
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

    for node in range(n):
        if disc[node] == -1:
            dfs(node)
    return sccs


def condensation(n, edges):
    sccs = find_sccs(n, edges)
    g = {}

    node_to_root = {}
    for comp in sccs:
        root = comp[0]
        for node in comp:
            node_to_root[node] = root

    for u, v in edges:
        ru, rv = node_to_root[u], node_to_root[v]
        if ru != rv:
            if ru not in g:
                g[ru] = []
            if rv not in g:
                g[rv] = []
            g[ru].append(rv)
    return g


'''---------------------------------------------------------------------------'''

'''
finding centers,
rooted tree,
isomorphic trees (needs some more clarification),

lca, ✔️
lca weighted✔️

scc, 
condendation of scc 
'''
# n = 16
# edges = [
#     [0, 1],
#     [0, 2],
#     [0, 3],

#     [1, 4],
#     [1, 5],
#     [1, 6],

#     [4, 7],
#     [6, 8],

#     [2, 9],
#     [2, 10],

#     [3, 11],
#     [3, 12],
#     [3, 13],
#     [3, 14],

#     [7, 15]
# ]


# wEdges = [[0, 1, -8], [0, 2, 4], [0, 3, -1], [1, 4, -10], [1, 5, 5], [1, 6, 3], [4, 7, -5],
#           [6, 8, -3], [2, 9, 4], [2, 10, -8], [3, 11, 1], [3, 12, -6], [3, 13, -9], [3, 14, -4], [7, 15, 30]]


def find_lca(n, edges, queries):
    g = {i: [] for i in range(n)}
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    LOG = 20

    depth = [0]*n
    up = [[-1]*LOG for _ in range(n)]

    def dfs(u, p, d):
        depth[u] = d
        for v in g[u]:
            if v == p:
                continue
            up[v][0] = u
            dfs(v, u, d + 1)

    dfs(0, -1, 0)

    for k in range(1, LOG):
        for u in range(n):
            ancs = up[u][k - 1]
            if ancs != -1:
                up[u][k] = up[ancs][k - 1]

    def get_kt_par(u, k):
        if u == -1 or k == 0:
            return u

        for jump in range(LOG - 1, -1, -1):
            if k >= (1 << jump) and u != -1:
                u = up[u][jump]
                k -= (1 << jump)

        return u

    def lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            u = get_kt_par(u, du - dv)
        if dv > du:
            v = get_kt_par(v, dv - du)

        if u == v:
            return u

        for jump in range(LOG - 1, -1, -1):
            if up[u][jump] != up[v][jump]:
                u = up[u][jump]
                v = up[v][jump]
        return up[u][0]

    lcas = []
    for u, v in queries:
        lcas.append(lca(u, v))
    return lcas


# print(find_lca(n, edges, [[9, 14], [2, 9], [15, 8]]))


def lcaWeighted(n, edges, queries):
    g = {i: [] for i in range(n)}
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    depth = [0]*n
    weight_from_root = [0]*n

    LOG = 20
    up = [[-1]*LOG for _ in range(n)]
    upWeight = [[0]*LOG for _ in range(n)]
    upMax = [[0]*LOG for _ in range(n)]

    def dfs(u, par, d, cur_weight):
        depth[u] = d
        weight_from_root[u] = cur_weight

        for v, w in g[u]:
            if v == par:
                continue
            up[v][0] = u
            upWeight[v][0] = w
            upMax[v][0] = w
            dfs(v, u, d + 1, cur_weight + w)

    dfs(0, -1, 0, 0)

    for k in range(1, LOG):
        for u in range(n):
            ancs = up[u][k - 1]
            if ancs != -1:
                up[u][k] = up[ancs][k - 1]
                upWeight[u][k] = upWeight[u][k - 1] + upWeight[ancs][k - 1]
                upMax[u][k] = max(upMax[u][k - 1], upMax[ancs][k - 1])

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

    ans = []
    for u, v in queries:
        ans.append(get_max_edge_in_path(u, v))
    return ans


# print(lcaWeighted(n, wEdges, [[9, 14], [2, 9], [15, 8]]))

'''--------------------------------------------------------------------------------'''
'''
finding centers,✔️
rooted tree,✔️
isomorphic trees (needs some more clarification),✔️

lca,✔️
lca weighted✔️

scc, ✔️
condendation of scc ✔️
'''
# edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
# n1 = 5

# edges2 = [[0, 1], [0, 2], [0, 3]]
# n2 = 4


def get_centers(n, edges):
    g = {i: [] for i in range(n)}
    degree = [0]*n

    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

        degree[u] += 1
        degree[v] += 1

    leaves = []
    for node in range(n):
        if degree[node] == 1:
            leaves.append(node)

    count = len(leaves)

    while count < n:
        new_leaves = []
        for u in leaves:
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    new_leaves.append(v)
            degree[u] = 0
        count += len(new_leaves)
        leaves = new_leaves

    return leaves


class Node:
    def __init__(self, val, ch=[]):
        self.val = val
        self.ch = []


def rootTree(n, edges, rootVal):
    g = {}
    for i in range(n):
        g[i] = []

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


def getSign(node):
    if len(node.ch) == 0:
        return "()"
    ch_signs = []
    for chNode in node.ch:
        ch_signs.append(getSign(chNode))

    return f"({"".join(ch_signs)})"


def is_isomorphic(n1, n2, edges1, edges2):
    c1 = get_centers(n1, edges1)
    c2 = get_centers(n2, edges2)

    r1 = [rootTree(n1, edges1, c) for c in c1]
    r2 = [rootTree(n2, edges2, c) for c in c2]

    for root1 in r1:
        for root2 in r2:
            if getSign(root1) == getSign(root2):
                return True
    return False


# print(is_isomorphic(n1, n2, edges1, edges2))

'''-------------------------------------End of a section-----------------------------------------'''

'''
Eluer path
1) Directed ✔️
2) Un-directed ✔️

All single source shortest path (sssp) algorighms
1) bfs
2) 0/1 bfs
3) top-sort and relaxing
4) dijakstra
5) bellman ford
6) A*
7) Floyd warshell
'''


def euler_directed(n, edges):
    g = {i: [] for i in range(n)}
    indegree = [0]*n
    outdegree = [0]*n
    for u, v in edges:
        g[u].append(v)
        outdegree[u] += 1
        indegree[v] += 1

    start = -1
    plus = 0
    minus = 0

    for u in range(n):
        diff = outdegree[u] - indegree[u]
        if diff == 1:
            start = u
            plus += 1
        elif diff == -1:
            minus += 1
        elif diff != 0:
            return []

    valid = (plus == 0 and minus == 0) or (plus == 1 and minus == 1)
    if valid == False:
        return []

    if plus == 0 and minus == 0:
        for u in range(n):
            if outdegree[u] > 0:
                start = u
                break

    path = deque()

    def dfs(u):
        while g[u]:
            v = g[u].pop()
            dfs(v)
        path.appendleft(u)

    dfs(start)
    if len(path) == len(edges) + 1:
        return list(path)
    return []


def euler_undirected(n, edges):
    g = {i: [] for i in range(n)}
    degree = [0]*n

    for i in range(len(edges)):
        edge = edges[i]
        u = edge[0]
        v = edge[1]
        g[u].append((v, i))
        g[v].append((u, i))
        degree[u] += 1
        degree[v] += 1

    start = -1
    odd_count = 0

    for u in range(n):
        if degree[u] % 2 == 1:
            start = u
            odd_count += 1

    valid = (odd_count == 0) or (odd_count == 2)
    if not valid:
        return []

    if odd_count == 0:
        for u in range(n):
            if degree[u] > 0:
                start = u
                break

    path = deque()
    used = [False]*len(edges)

    def dfs(node):
        while g[node]:
            ch, eid = g[node].pop()
            if used[eid]:
                continue
            used[eid] = True
            dfs(ch)
        path.appendleft(node)

    dfs(start)

    if len(path) == len(edges) + 1:
        return list(path)
    return []


# n = 4
# edges = [
#     [0, 1],
#     [1, 2],
#     [2, 0],

#     [0, 3],
#     [3, 2]
# ]

# print(euler_directed(n, edges))

# n = 7
# edges = [
#     [0, 1],
#     [1, 2],
#     [2, 0],

#     [0, 3],
#     [3, 4],
#     [4, 0],

#     [2, 5],
#     [5, 6],
#     [6, 2]
# ]

# print(euler_undirected(n, edges))
