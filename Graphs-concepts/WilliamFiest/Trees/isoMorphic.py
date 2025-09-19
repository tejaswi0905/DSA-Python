from collections import defaultdict, deque

def find_centers(edges):
    n = len(edges) + 1
    g = defaultdict(list)
    degree = [0] * (n + 1)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    leaves = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            leaves.append(i)
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

class Node:
    def __init__(self, id, par, children = []):
        self.id = id
        self.par = par
        self.children = children

def rooted_tree(edges, rootId = 0):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    

    def build_tree(g, node, par):
        for ch in g[node.id]:
            if par != None and ch == par.id:
                continue
            ch_node = Node(ch, node, [])
            build_tree(g, ch_node, node)
            node.children.append(ch_node)
        return node
    filled_root = build_tree(g, Node(rootId, None, []), None)
    return filled_root

def isomorphic_check(edges1, edges2):
    c1 = find_centers(edges1)
    c2 = find_centers(edges2)

    roots1 = [rooted_tree(edges1, c) for c in c1]
    roots2 = [rooted_tree(edges2, c) for c in c2]

    def get_signature(node):
        if not node.children:
            # return "()"
            return f"({node.id})"
        child_sigs = [get_signature(ch) for ch in node.children]
        child_sigs.sort()
        # return "(" + "".join(child_sigs) + ")"
        return f"({node.id}{''.join(child_sigs)})"
    

    def is_isomorphic(root1, root2):
        return get_signature(root1) == get_signature(root2)
    for root1 in roots1:
        for root2 in roots2:
            print(get_signature(root1))
            print(get_signature(root2))
            if is_isomorphic(root1, root2) == True:
                return True
    return False

edges1 = [
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
edges2 = [
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

print(isomorphic_check(edges1, edges2))
edges3 = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (4, 8),
    (4, 9),
    (5, 10),
    (5, 11),
    (6, 12),
    (6, 13),
    (7, 14),
    (7, 15)
]

edges4 = [
    (1, 3),
    (1, 2),
    (2, 5),
    (2, 4),
    (3, 7),
    (3, 6),
    (4, 9),
    (4, 8),
    (5, 11),
    (5, 10),
    (6, 13),
    (6, 12),
    (7, 15),
    (7, 14)
]
print(isomorphic_check(edges3, edges4))