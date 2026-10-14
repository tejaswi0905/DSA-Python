from collections import defaultdict, deque

# edges1 = [[0, 1], [1, 2], [2, 1], [1, 3], [3, 4]]
# edges3 = [[1, 2], [1, 3], [2, 2], [2, 4], [2, 4], [3, 1], [3, 2], [3, 5], [4, 3], [4, 6], [5, 6], [6, 3]]

# def find_euler_path_directed(n, edges):
#     g = defaultdict(list)
#     indegree = [0] * n
#     outdegree = [0] * n

#     for u, v in edges:
#         g[u].append(v)
#         outdegree[u] += 1
#         indegree[v] += 1
    
#     # check euler path/circuit conditions
#     start_nodes = 0
#     end_nodes = 0
#     start = 0

#     for i in range(n):
#         if outdegree[i] - indegree[i] == 1:
#             start = i
#             start_nodes += 1
#         elif indegree[i] - outdegree[i] == 1:
#             end_nodes += 1
#         elif indegree[i] != outdegree[i]: # No euler path 
#             return []
    
#     if not((start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0)):
#         return []
    
#     # if euler circuit, start anywhere with outgoing edges
#     if start_nodes == 0:
#         for i in range(n):
#             if outdegree[i] > 0:
#                 start = i
#                 break
    
#     # now the actual logic,
#     path = deque()
#     stack = [start]

#     while stack:
#         u = stack[-1]
#         if g[u]:
#             v = g[u].pop()
#             stack.append(v)
#         else:
#             path.appendleft(stack.pop())
#     if len(path) != len(edges) + 1:
#         return [] # disconnected graph
#     return list(path)

# print(find_euler_path_directed(5, edges1))
# print(find_euler_path_directed(7, edges3))

# def find_euler_path_undirected(n, edges):
#     g = defaultdict(list)
#     degree = [0] * n
#     used = [False] * n
    
#     # build adj_list with degree count and edge_id
#     for i, (u, v) in enumerate(edges):
#         g[u].append((v, i))
#         g[v].append((u, i))
#         degree[u] += 1
#         degree[v] += 1
    
#     # get nodes with odd number of degree
#     odd_nodes = [i for i in range(n) if degree[i] % 2 == 1]

#     #check euler path/circuit conditions
#     if len(odd_nodes) not in [0, 2]:
#         return [] # no euler path can be made

#     if len(odd_nodes) == 2:
#         start = odd_nodes[0]
#     else:
#         start = 0
#         for i in range(n):
#             if degree[i] > 0:
#                 start = i # this is circuit, so we can pick any node with edges
#                 break
#     path = deque()

#     def dfs(u):
#         while g[u]:
#             v, eid = g[u].pop()
#             if used[eid]: # if the edge is already used, then skip
#                 continue
#             used[eid] = True # mark the edge as used
#             dfs(v)
#         path.appendleft(u)
#     dfs(start)
#     if len(path) == len(edges) + 1:
#         return list(path)
#     return []

# edges2 = [
#     (0, 1),  # id 0
#     (1, 2),  # id 1
#     (2, 3),  # id 2
#     (3, 4),  # id 3
#     (4, 5),  # id 4
#     (5, 0)   # id 5
# ]

# print(find_euler_path_undirected(6, edges2))


def get_euler_path_directed(n, edges):
    in_degree = [0] * n
    out_degree = [0] * n
    g = defaultdict(list)

    for u, v in edges:
        g[u].append(v)
        in_degree[v] += 1
        out_degree[u] += 1
    
    #check
    start_nodes = 0
    end_nodes = 0
    start = None

    for node in range(n):
        if out_degree[node] - in_degree[node] == 1:
            start_nodes += 1
            start = node
        elif in_degree[node] - out_degree[node] == 1:
            end_nodes += 1
        elif in_degree[node] != out_degree[node]:
            return []
    
    if not ((start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0)):
        return []
    
    if start_nodes == 0:
        for node in range(n):
            if out_degree[node] > 0:
                start = node
                break
    

    path = deque()
    stack = [start]
    while stack:
        u = stack[-1]
        if g[u]:
            v = g[u].pop()
            stack.append(v)
        else:
            path.appendleft(stack.pop())
    
    if len(path) != len(edges) + 1:
        return []
    return list(path)


def get_euler_path_undirected(n, edges):
    g = defaultdict(list)
    degree = [0] * n
    for i, (u, v) in enumerate(edges):
        g[u].append((v, i))
        g[v].append((u, i))
        degree[u] += 1
        degree[v] += 1
    visited = [False] * len(edges)
    #check
    diff = [node for node in range(n) if degree[node] % 2 != 0]
    if len(diff) not in [0, 2]:
        return []
    if len(diff) == 2:
        start = diff[0]
    
    else:
        start = None
        for node in range(n):
            if degree[node] > 0:
                start = node
                break
    
    path = deque()
    def dfs(node):
        while g[u]:
            v, idx = g[u].pop()
            if visited[idx]:
                continue
            visited[idx] = True
            dfs(v)
        path.appendleft(node)
    dfs(start)
    return list(path)

        
edges1 = [[0, 1], [1, 2], [2, 1], [1, 3], [3, 4]]
edges3 = [[1, 2], [1, 3], [2, 2], [2, 4], [2, 4], [3, 1], [3, 2], [3, 5], [4, 3], [4, 6], [5, 6], [6, 3]]
print(get_euler_path_directed(5, edges1))
print(get_euler_path_directed(7, edges3))