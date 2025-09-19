from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, id, par, children = []):
        self.id = id
        self.par = par
        self.children = []


def rootTree(g, rootId = 0):
    
    rootNode = Node(rootId, None, [])

    def build_tree(g, node, par):
        for ch_id in g[node.id]:
            if par != None and ch_id == par.id:
                continue
            ch_node = Node(ch_id, node, [])
            build_tree(g, ch_node, node)
            node.children.append(ch_node)
        return node
    root = build_tree(g, rootNode, None)
    return root



def solve(edges, vals, m):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    rootNode = rootTree(g, 1)
    
    
    def dfs(node, cats): # we are passing the consecutive cats in the current path
        is_current_cat = None
        if vals[node.id - 1] == 1:
            is_current_cat = True
            cats += 1
        else:
            is_current_cat = False       
        if cats > m:
            return 0
        if len(node.children) == 0:
            return 1
        answer = 0
        for ch_node in node.children:
            if is_current_cat:
                temp = dfs(ch_node, cats)
            else:
                temp = dfs(ch_node, 0)
            answer += temp
            
        return answer
    
    return dfs(rootNode, 0)

def main():
    n, m = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        edge = list(map(int, input().split()))
        edges.append(edge)
    print(solve(edges, vals, m))

main()