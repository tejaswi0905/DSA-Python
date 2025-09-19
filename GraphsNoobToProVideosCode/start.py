# def main():
#     n, t = list(map(int, input().split()))

#     a = list(map(int, input().split()))

#     graph = {i:0 for i in range(1, n + 1)}

#     j = 1
#     for ele in a:
#         graph[j] = j + ele
#         j += 1

#     found_target_node = [False]

#     def dfs(node, found_target_node, graph):
#         current = node
#         while True:
#             if current == t:
#                 found_target_node[0] = True
#                 break
#             if current == n:
#                 break
#             ch = graph[current]
#             current = ch
#     dfs(1, found_target_node, graph)
#     if found_target_node[0]:
#         print("YES")
#         return
#     print("NO")

# main()


from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

def solve(n, edges, t):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    found_t = [False]
    
    def dfs(node):
        if node == t:
            found_t[0] = True
            return
        for ng in g[node]:
            dfs(ng)
    dfs(1)
    return found_t[0]
    

def main():
    n, t = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    edges = []
    for i, val in enumerate(arr):
        idx = i + 1
        edge = [idx, val + idx]
        edges.append(edge)
    if solve(n, edges, t):
        print("YES")
        return
    print("NO")
    return
main()
        
    