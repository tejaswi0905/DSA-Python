# The concept of a back edge comes from the dfs treversal of a graph. Lets say we have a graph like this
#

edges = [[1,2], [2,3], [1,3], [2,4], [4,5], [5,6], [6,7], [4,7]]

def back_edges(edges, n):
    answer = []
    adj_list = {i:[] for i in range(1, n + 1)}
    visited = [0] * (n + 1)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def dfs(node, parent):
        #1 means visited but still in the call stack.
        visited[node] = 1
        for ch in adj_list[node]:
            if visited[ch] == 0:
                dfs(ch, node)
            elif ch != parent and visited[ch] == 1:
                answer.append([node, ch])
        visited[node] = 2
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, 0)
    return answer

print(back_edges(edges, 7))

    