edges = [[1, 2], [2, 3], [2, 5], [3, 4], [5, 6],[7, 8], [7, 11], [7, 8], [8, 9], [9, 10]]

from collections import defaultdict, deque

def buld_graph2(edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g


def rumor(n, edges, value_array):
    g = buld_graph2(edges)

    answer = 0 # we have to add the min of each component to the answer

    visited = set()
    

    # def dfs(node):
    #     visited.add(node)
    #     cur_min = value_array[node - 1]
    #     for ng in g[node]:
    #         if ng not in visited:
    #             sub_graph_min = dfs(ng)
    #             cur_min = min(cur_min, sub_graph_min)
    #     return cur_min
    # for node in range(1, n + 1):
    #     if node not in visited:
    #         component_min = dfs(node)
    #         answer += component_min
    # return answer
    
    def bfs(start):
        q = deque()
        q.append(start)
        cur_min = value_array[start - 1]
        while q:
            cur_node = q.popleft()
            visited.add(cur_node)
            for ng in g[cur_node]:
                if ng not in visited:
                    cur_min = min(cur_min, value_array[ng - 1])
                    q.append(ng)
        return cur_min
    
    for node in range(1, n + 1):
        if node not in visited:
            component_min = bfs(node)
            answer += component_min
    return answer




def main():
    n, m = list(map(int, input().split()))
    value_array = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        edge = list(map(int, input().split()))
        edges.append(edge)
    print(rumor(n, edges, value_array))

main()