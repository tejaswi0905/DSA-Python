from collections import defaultdict

class Node:
    def __init__(self, id, par, children):
        self.id = id
        self.par = par
        self.children = []

def build_graph(adj_list):
    g = defaultdict(list)
    for u, v in adj_list:
        g[u].append(v)
        g[v].append(u)
    return g


def build_tree(g, node, par):
    for ch in g[node.id]:
        if par is not None and ch != par.id:
            child = Node(ch, node, [])
            build_tree(g, child, node)
            node.children.append(child)
    return node

def rootTree(adj_list, rootId = 0):
    g = build_graph(adj_list)
    r1 = Node(rootId, None, [])
    rootNode = build_tree(g, r1, None)
    return rootNode
