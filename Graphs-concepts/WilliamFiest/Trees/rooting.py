#
from collections import defaultdict, deque
class Node:
    def __init__(self, id, parent, children = []):
        self.id = id
        self.parent = parent
        self.children = []
    

edges = [[0, 1], [0, 2], [0, 5], [2, 3], [5, 4], [5, 6]]

def build_graph(edges):
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def rootTree(edges, rootId = 0):
    g = build_graph(edges)
    rootNode = Node(rootId, None, [])
    root = build_tree(g, rootNode, None)
    return root


def build_tree(g, node, parent):
    for childId in g[node.id]:
        if parent != None and childId == parent.id:
            continue
        child_node = Node(childId, node, [])
        build_tree(g, child_node, node)
        node.children.append(child_node)
    return node

def treversal(rootNode):
    if len(rootNode.children) == 0:
        print(rootNode.id)
        return
    def dfs(node):
        if node.id == 4:
            print(node.children)
        print(node.id)
        for ch in node.children:
            if ch.id != node.id:
                dfs(ch)
    dfs(rootNode)

rootNode = rootTree(edges)
treversal(rootNode)
