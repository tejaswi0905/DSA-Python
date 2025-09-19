def main():
    n, m = list(map(int, input().split()))

    edges = []

    for i in range(m):
        group = list(map(int, input().split()))
        group_size = group[0] + 1
        if group_size < 2:
            continue
        starting_node = group[1]
        for j in range(2, group_size):
            edges.append([starting_node, group[j]])
    parents = [i for i in range(n + 1)]
    rank = [1] * (n + 1)

    def find_parent_component(node, parents):
        result = node
        while result != parents[result]:
            parents[result] = parents[parents[result]]
            result = parents[result]
        return result

    def union(node1, node2, parents, rank):
        p1, p2 = find_parent_component(node1, parents), find_parent_component(node2, parents)
        if p1 == p2:
            return

        if rank[p1] > rank[p2]:
            parents[p2] = p1
            rank[p1] += rank[p2]
        else:
            parents[p1] = p2
            rank[p2] += rank[p1]
    for edge in edges:
        n1 = edge[0]
        n2 = edge[1]

        union(n1, n2, parents, rank)
    for i in range(1, n + 1):
        p1 = find_parent_component(i,parents)
        parents[i] = p1


    for i in range(1, n + 1):
        p = parents[i]
        comp_size = rank[p]
        print(comp_size, end = ' ')
main()