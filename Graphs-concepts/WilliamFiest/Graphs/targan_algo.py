from collections import defaultdict

def targan_algo(n, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    
    low = [0] * n
    disc = [-1] * n
    time = 0
    stack = []
    in_stack = [False] * n
    sccs = []

    def dfs(node):
        nonlocal time
        disc[node] = low[node] = time
        time += 1
        in_stack[node] = True
        stack.append(node)

        #explore neighbors
        for v in g[node]:
            if disc[v] == -1:
                dfs(v)
                low[node] = min(low[node], low[v])
            elif in_stack[node] == True:
                low[node] = min(low[node], disc[v])
        
        # if node is the root of scc then pop the stack upto to the root, 

        if disc[node] == low[node]:
            scc = []
            while True:
                w = stack.pop()
                in_stack[w] = False
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)
    
    for u in range(n):
        if disc[u] == -1:
            dfs(u)
    return sccs

edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [2, 3],
    [3, 2],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 4],
    [6, 7],
    [7, 8],
    [8, 6]
]
adj_list = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2, 4],
    4: [5],
    5: [6, 7],
    6: [4],
    7: [8],
    8: [7, 9],
    9:  [10],
    10: [11],
    11: [9, 12],
    12: [13],
    13: [14],
    14: [12, 15],
    15: []
}

def make_edges_from_adj_list(adj_list):
    edges = []
    for u in adj_list:
        for v in adj_list[u]:
            edges.append([u, v])
    return edges

edges2 = make_edges_from_adj_list(adj_list)


def targeon_alog_2(n, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    
    # as long as we found a child that has a lower dt and it is in the stack then only we update the lt of our current node is the assence of it.

    low = [0] * n
    disc = [-1] * n # we are using the disc as visited for this targen algo
    sccs = []
    time = 0
    stack = []
    in_stack = [False] * n



    def dfs(node):
        nonlocal time
        low[node] = disc[node] = time
        time += 1
        in_stack[node] = True
        stack.append(node)
        for ng in g[node]:
            if disc[ng] == -1:
                dfs(ng)
                low[node] = min(low[node], low[ng])
            elif in_stack[node] == True:
                low[node] = min(low[node], disc[ng])
        
        if low[node] == disc[node]: # this means we are the start of the scc, so pop all the elements upto and including the start of scc form the stack.
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                in_stack[w] = False
                if w == node:
                    break
            sccs.append(scc)
    for u in range(n):
        if disc[u] == -1:
            dfs(u)
    return sccs

def build_condensation(n, edges):
    sccs = targeon_alog_2(n, edges)
    print(sccs)
    comp_id = {}
    for comp in sccs:
        root = comp[0]
        for node in comp:
            comp_id[node] = root
    dag = defaultdict(set)

    for u, v in edges:
        cu, cv = comp_id[u], comp_id[v]
        if cu != cv:
            dag[cu].add(cv)
    condensed = {i: list(neigh) for i, neigh in dag.items()}
    return condensed

print(build_condensation(16, edges2))