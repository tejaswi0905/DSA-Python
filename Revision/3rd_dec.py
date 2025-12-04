'''
Docstring for Revision.3rd_dec
1) We go through the graph and assign the least_time and discovered_time to each node, and add those nodes to the stack
2) When we are poping a node(or the dfs call for that node), we check if the lt[node] == dt[node] if so keep popping the stack until we get to the node, and those nodes that got popped does belong to one scc

stack = []
sccs = [[5], [4], [1, 2, 3]]

 1(1)1
   |  ^
   |   \
   v    \
 2(2)1->3(3)1-->4(4)4
             |
             |
             v
            5(5)5
'''

from collections import defaultdict

def get_centers(n, adj_list):
    g = defaultdict(list)
    degree = [0 for i in range(n + 1)]
    for u, v in adj_list:
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    cur_list = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            cur_list.append(i)
    count = len(cur_list)
    while count < n:
        new_list = []
        for u in cur_list:
            v = g[u][0]
            degree[v] -= 1
            if degree[v] == 1:
                new_list.append(v)
            degree[u] = 0
        count += len(new_list)
        cur_list = new_list
    return cur_list

edges = [
    (1, 2), (1, 3), (1, 4),
    (2, 5), (2, 6), (2, 7),
    (3, 8), (3, 9), (3, 10),
    (4, 11), (4, 12), (4, 13),
    (5, 14), (8, 15), (11, 16)
]


def get_sccs(n, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    sccs = []
    time = 0
    stack = []
    in_stack = [False] * (n + 1)
    dt = [-1] * (n + 1)
    lt = [0] * (n + 1)

    def dfs(node):
        nonlocal time
        in_stack[node] = True
        stack.append(node)
        dt[node] = time
        lt[node] = time
        time += 1

        for ch in g[node]:
            if dt[ch] == -1:
                dfs(ch)
                lt[node] = min(lt[ch], lt[node])
            elif in_stack[ch] == True:
                lt[node] = min(dt[ch], lt[node])
        if dt[node] == lt[node]:
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                in_stack[w] = False
                if w == node:
                    break
            sccs.append(scc)
    for node in range(1, n + 1):
        if dt[node] == -1:
            dfs(node)
    
    return sccs

edges2 = [[1,2],
 [2,3],
 [3,1],
 [3,4],
 [4,5]]

edges3 = [[1,2],
 [2,1],
 [2,3],
 [3,4],
 [4,5],
 [5,6],
 [6,4],
 [6,2],
 [5,7],
 [7,8],
 [8,7]]

print(get_sccs(5, edges2))
print(get_sccs(8, edges3))