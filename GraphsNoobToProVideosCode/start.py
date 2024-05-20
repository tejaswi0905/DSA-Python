def main():
    n, t = list(map(int, input().split()))

    a = list(map(int, input().split()))

    graph = {i:0 for i in range(1, n + 1)}

    j = 1
    for ele in a:
        graph[j] = j + ele
        j += 1

    found_target_node = [False]

    def dfs(node, found_target_node, graph):
        current = node
        while True:
            if current == t:
                found_target_node[0] = True
                break
            if current == n:
                break
            ch = graph[current]
            current = ch
    dfs(1, found_target_node, graph)
    if found_target_node[0]:
        print("YES")
        return
    print("NO")

main()


'''
8 5
1 2 1 2 1 2 1
'''
