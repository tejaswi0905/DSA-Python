edges = [[1,2], [2,3], [1,3], [2,4], [4,5], [5,6], [6,7], [4,7]] # should return [[3, 2, 1], [6,7,5,4]]

def print_cycles(edges, n):
    adj_list = {i:[] for i in range(1, n + 1)}
    visited = [0] * (n + 1)
    parents = [0] * (n + 1)
    cycles = []

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def cycle_treversal(parents, u, v):
        cycle = []
        cur = u
        while cur != v:
            cycle.append(cur)
            cur = parents[cur]
        cycle.append(v)
        return cycle


    def dfs(node, parent):
        visited[node] = 1
        parents[node] = parent

        for ch in adj_list[node]:
            if visited[ch] == 0:
                dfs(ch, node)
            elif ch != parent and visited[ch] == 1:
                u, v = node, ch
                cycle = cycle_treversal(parents, u, v)
                cycles.append(cycle)
        visited[node] = 2
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, 0)
    return cycles
                
        
print(print_cycles(edges, 7))