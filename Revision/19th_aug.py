
# I am starting with the LCA of a tree in both class based and n-ary tree
from collections import deque

import sys
from math import ceil, log2
sys.setrecursionlimit(1<<20)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(9)
node2 = Node(6)
node3 = Node(4)
node4 = Node(2)
node5 = Node(3)
node6 = Node(8)
node7 = Node(5)
node8 = Node(-3)
node9 = Node(10)
node10 = Node(11)
node11 = Node(17)
root.left = node2
root.right = node3
node2.left = node4
node4.left = node7
node4.right = node8
node3.left = node5
node3.right = node6
node5.left = node9
node5.right = node10
node6.right = node11

# class based, there is an iterative way and a recursive way, first lets do the iterative way

# --> Trevese the tree and recored parent and depth of each node is a hash-map
# --> Build the ancestry path of node p
# --> Then walk up from node q, until we hit the first common node in p's ancestors and that is the lca of p and q

def find_lca(root, p, q):
    depth = {root.val: 0}
    parents = {root.val: None}

    que = deque()
    que.append([root, 0])
    while que:
        node, cur_depth = que.popleft()
        if node.left:
            parents[node.left.val] = node.val
            depth[node.left.val] = cur_depth + 1
            que.append([node.left, cur_depth + 1])
        if node.right:
            parents[node.right.val] = node.val
            depth[node.right.val] = cur_depth + 1
            que.append([node.right, cur_depth + 1])
    if depth[p.val] > depth[q.val]:
        p, q = q, p
    ancestors_p = set()
    cur = p.val
    while cur != None:
        ancestors_p.add(cur)
        cur = parents[cur]
    lca = q.val
    while lca not in ancestors_p:
        lca = parents[lca]
    return lca

print(find_lca(root, node7, node7))


def lca(root, queries, n = None):
    if len(queries) == 0:
        return []
    
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    if n is None:
        n = count_nodes(root)
    
    LOG = ceil(log2(n)) + 1
    up = [[-1] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)
    id_map = {} # Node-object to uniqueID --> (1 to n)
    node_map = {} # uniqueID to node-object
    node_id = 1
    
    # Assign depths, assign immediate parents in the up binary lifting table and fill the id_map and node_map tables
    def dfs(node, p_id, d):
        nonlocal node_id
        if not node:
            return 
        cur_id = node_id
        node_id += 1
        id_map[node] = cur_id
        node_map[cur_id] = node
        depth[cur_id] = d
        up[cur_id][0] = p_id
        if node.left:
            dfs(node.left, cur_id, d + 1)
        if node.right:
            dfs(node.right, cur_id, d + 1)
    
    dfs(root, -1, 0)

    #build binary lifting table
    for k in range(1, LOG):
        for u in range(1, n + 1):
            if up[u][k - 1] != -1:
                up[u][k] = up[up[u][k-1]][k-1]

    
    def get_kt_ancestor(node_id, k):
        if k == 0 or node_id == -1:
            return node_id
        for i in range(LOG - 1, -1, -1):
            if k >= (1 << i) and node_id != -1:
                node_id = up[node_id][i]
                k -= (1 << i)
        return node_id
    
    def find_lca(u_node, v_node):
        uid = id_map[u_node]
        vid = id_map[v_node]

        if depth[uid] > depth[vid]:
            uid = get_kt_ancestor(uid, depth[uid] - depth[vid])
        elif depth[vid] > depth[uid]:
            vid = get_kt_ancestor(vid, depth[vid] - depth[uid])
        
        if uid == vid:
            return node_map[uid].val
        
        for k in range(LOG - 1, -1, -1):
            if up[uid][k] != up[vid][k]:
                uid = up[uid][k]
                vid = up[vid][k]
        lca_id = up[uid][0]
        if lca_id == -1:
            return node_map[uid].val
        return node_map[lca_id].val
    
    answers = []
    for u, v in queries:
        answers.append(find_lca(u, v))
    return answers

print(lca(root, [[node5, node6], [node8, node8], [node10, node3], [node11, node7], [root, node5]]))