import sys
sys.setrecursionlimit(10 ** 6)

def test_case(n, edges):
    parent = [i for i in range(n + 1)]
    size = [1 for _ in range(n + 1)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def find_pairs(x):
        return x * (x - 1) // 2
    
    total_pairs = find_pairs(n)
    res = []

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return 0
        removed = find_pairs(size[rx]) + find_pairs(size[ry])
        added = find_pairs(size[rx] + size[ry])
        parent[ry] = rx
        size[rx] += size[ry]
        return added - removed

    for u, v in edges:
        res.append(total_pairs)
        total_pairs -= union(u, v)
    
    return res[::-1]

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    reversed_edges = edges[::-1]
    result = test_case(n, reversed_edges)
    for val in result:
        print(val)

main()
