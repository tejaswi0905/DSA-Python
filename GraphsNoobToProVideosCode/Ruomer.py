from collections import deque


def main():
    n, m = list(map(int, input().split()))
    cost_array = list(map(int, input().split()))
    edges = []

    for i in range(m):
        edge = list(map(int, input().split()))
        edges.append(edge)



    answer = 0
    graph = {i:[] for i in range(1, n + 1)}
    visited = set()

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # def dfs(node, cost_array, graph, visited):
    #     if node in visited:
    #         return
    #     visited.add(node)
    #     cur_min = cost_array[node - 1]
    #
    #     for ch in graph[node]:
    #         if ch in visited:
    #             continue
    #         child_min = dfs(ch, cost_array, graph, visited)
    #         cur_min = min(cur_min, child_min)
    #     return cur_min

    def bfs(node, graph, visited, cost_array):
        q = deque()
        q.append(node)
        current_min = cost_array[node - 1]
        while q:
            current_node = q.popleft()
            if current_node in visited:
                continue
            visited.add(current_node)
            for ch in graph[current_node]:
                if ch in visited:
                    continue
                current_min = min(current_min, cost_array[ch - 1])
                q.append(ch)
        return current_min


    for node in range(1, n + 1):
        if node in visited:
            continue
        # component_min = dfs(node, cost_array, graph, visited)
        component_min = bfs(node, graph, visited, cost_array)
        answer += component_min
    print(answer)



main()

