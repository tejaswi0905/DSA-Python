'''
Docstring for Revision.18th_dec

Complete graphs, and trees
'''

edges0 = [
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


from collections import defaultdict

class Node:
    def __init__(self, val, par, ch):
        self.val = val
        self.par = par
        self.ch = []


def build_adj_list(edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g

def build_tree(g, node, par):
    for ch_val in g[node.val]:
        if par != None and ch_val == par.val:
            continue
        ch_node = Node(ch_val, node, [])
        build_tree(g, ch_node, node)
        node.ch.append(ch_node)
    return node

def rootedTree(edges, rootVal = 0):
    g = build_adj_list(edges)
    temp_root = Node(rootVal, Node, [])
    root = build_tree(g, temp_root, None)
    return root

root = rootedTree(edges0, 1)


def dfs(node):
    print(node.val)
    for ch in node.ch:
        dfs(ch)

#Centers for an undirected tree

edges1 = [
    (1, 2), (1, 3), (1, 4),
    (2, 5), (2, 6), (2, 7),
    (3, 8), (3, 9), (3, 10),
    (4, 11), (4, 12), (4, 13),
    (5, 14), (8, 15), (11, 16)
]

def get_centers(n, edges):
    g = defaultdict(list)
    degree = [0] * (n + 1)

    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    leaves = [i for i in range(1, n + 1) if degree[i] == 1]
    count = len(leaves)

    while count < n:
        new_leaves = []
        for leaf in leaves:
            for ng in g[leaf]:
                degree[ng] -= 1
                if degree[ng] == 1:
                    new_leaves.append(ng)
            degree[leaf] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


def get_sign(node):
    if len(node.ch) == 0:
        return '()'
    ch_sign = [get_sign(ch) for ch in node.ch]
    return "(" + "".join(ch_sign) + ")"

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

def is_isomorphic(n1, n2, edges1, edges2):
    if n1 != n2:
        return False
    c1 = get_centers(n1, edges1)
    c2 = get_centers(n2, edges2)

    r1 = [rootedTree(edges1, c) for c in c1]
    r2 = [rootedTree(edges2, c) for c in c2]

    for root1 in r1:
        for root2 in r2:
            if get_sign(root1) == get_sign(root2):
                return True
    return False

# Now Shortest and longest paths in DAG, first top-sort + relaxation, this can handle negative edges. But the condition for top-sort is that the grpah should not have any cycles. 
# If there are cycles then we need to use dikjstara, but with dikjstara we should not have any negative edges. We can have cycles but all the edges need to be +ve. 
# Now if we have negative edges and cycles and no negative cycles then we can use bellman_ford. 
# If we have negative edges, and negative cycles then we need to use floyd_warshell.
edges = [[1, 2, 3], [1, 3, 6], [2, 3, 4], [2, 4, 4],[2, 5, 11], [3, 4, 8], [3, 7, 11], [4, 5, 4], [4, 6, 5], [4, 7, 2], [5, 8, 6], [6, 8, 1], [7, 8, 2]]

from collections import deque
import heapq as hq


def top_sort(n, edges):
    g = defaultdict(list)
    in_degree =[0] * (n + 1)

    for u, v, _ in edges:
        g[u].append(v)
        in_degree[v] += 1
    
    q = deque()
    for node in range(1, n + 1):
        if in_degree[node] == 0:
            q.append(node)
    top_order = []
    while q:
        cur = q.popleft()
        top_order.append(cur)
        for ng in g[cur]:
            in_degree[ng] -= 1
            if in_degree[ng] == 0:
                q.append(ng)
    
    if len(top_order) != n:
        return []
    return top_order

def shortest_path_in_dag(edges, n, start):
    top_order = top_sort(n, edges)
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    for node in top_order:
        cur_dist = dist[node]
        for v, w in g[node]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
    return dist


def dijkstra(n, edges, start):
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
    
    min_heap = []
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    hq.heappush(min_heap, (0, start))

    while min_heap:
        cur_dist, u = hq.heappop(min_heap)
        for v, w in g[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                hq.heappush(min_heap, (new_dist, v))
    return dist


# print(shortest_path_in_dag(edges, 8, 1))
# print(dijkstra(8, edges, 1))

class Seg:
    def __init__(self, arr, neutral, merge_fn):
        self.arr = arr
        self.n = len(arr)
        self.neutral = neutral
        self.merge_fn = merge_fn
        self.tree = [neutral] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)

    
    def build_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        
        m = (start + end) // 2
        self.build_tree(arr, 2 * node + 1, start, m)
        self.build_tree(arr, 2 * node + 2, m + 1, end)
        left_ele = self.tree[2*node + 1]
        right_ele = self.tree[2*node + 2]
        self.tree[node] = self.merge_fn(left_ele, right_ele)
    
    def update(self, idx, val, node, start, end):
        if start == end:
            self.tree[node] = val
            return
        
        m = (start + end) // 2
        if idx <= m:
            self.update(idx, val, 2 * node + 1, start, m, merge_fn)
        else:
            self.update(idx, val, 2 * node + 2, m + 1, end, merge_fn)
        
        left = self.tree[2*node + 1]
        right = self.tree[2*node + 2]
        self.tree[node] = self.merge_fn(left, right)
    
    def query(self, arr, left, right, node, start, end):
        if end < left or start > right: # case of no overlap
            return self.neutral
        if left <= start and right >= end:# case of complete overlap
            return self.tree[node]
        
        m = (start + end) // 2
        left_val = self.query(arr, left, right, 2 * node + 1,  start, m)
        right_val = self.query(arr, left, right, 2 * node + 2, m + 1, end)
        return self.merge_fn(left_val, right_val)

def merge_fn(a, b):
    return a + b

neutral = 0

arr = [2, 4, 5, 7, 8]
seg = Seg(arr, neutral, merge_fn)
print(seg.tree)
print(seg.query(arr, 1, 3, 0, 0, 4))


# The segment tree implementation with lazy propgation and the push function 


