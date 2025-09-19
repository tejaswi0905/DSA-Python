from collections import defaultdict

edges = [
    (1, 2), (1, 3), (1, 4),
    (2, 5), (2, 6), (2, 7),
    (3, 8), (3, 9), (3, 10),
    (4, 11), (4, 12), (4, 13),
    (5, 14), (8, 15), (11, 16)
]

def build_graph(edges):
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def get_center(g):
    n = len(g)
    degree = [0] * (n + 1) # we can actually fill the degree array while creating the adj_list to save some time.
    leaves = []
    for i in range(1, n + 1):
        degree[i] = len(g[i])
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)
    count = len(leaves)
    while count < n:
        new_leaves = []
        for node in leaves:
            for ng in g[node]:
                degree[ng] -= 1
                if degree[ng] == 1:
                    new_leaves.append(ng)
            degree[node] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves

g = build_graph(edges)
print(get_center(g))

def find_center(edges):
    n = len(edges) + 1
    degree = [0] * (n + 1)
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    leaves = []
    for i in range(1, n + 1):
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)
    count = len(leaves)
    while count < n:
        new_leaves = []
        for node in leaves:
            for ng in g[node]:
                degree[ng] -= 1
                if degree[ng] == 1:
                    new_leaves.append(ng)
            degree[node] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves
print(find_center(edges))