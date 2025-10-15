# non-weighted graphs
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

def print_adv(text, func, *args, **kwargs):
    print(text, end = ' ')
    result = func(*args, **kwargs)
    print(result)


def solve(n, edges):
    g = defaultdict(list)
    parents = [0] * (n + 1)
    edges_hash = defaultdict(int)
    edge_weight = defaultdict(int)
    for idx  in range(len(edges)):
        u, v = edges[idx]
        g[u].append(v)
        g[v].append(u)
        edges_hash[tuple(sorted((u, v)))] = idx
    
    edge_weight[tuple(sorted((0, 1)))] = 1
    edges_hash[tuple(sorted((0, 1)))] = -1
    
    def dfs(node, par):
        parents[node] = par
        par_edge_idx = edges_hash[tuple(sorted((node, par)))]
        for ch in g[node]:
            if ch != par:
                cur_edge_idx = edges_hash[tuple(sorted((node, ch)))]
                if cur_edge_idx > par_edge_idx:
                    edge_weight[tuple(sorted((node, ch)))] = edge_weight[tuple(sorted((node, par)))]
                    dfs(ch, node)
                else:
                    edge_weight[tuple(sorted((node, ch)))] = edge_weight[tuple(sorted((node, par)))] + 1
                    dfs(ch, node)
    
    dfs(1, 0)
    def dfs_path_max(node, par):
        cur_weight = edge_weight[tuple(sorted((node, par)))]    
        for ch in g[node]:
            if ch != par:
                ch_weight = dfs_path_max(ch, node)
                cur_weight = max(cur_weight, ch_weight)
        return cur_weight
    answer = dfs_path_max(1, 0)
    return answer
        


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n - 1):
            edge = list(map(int, input().split()))
            edges.append(edge)
        # print_adv("The answer is ", solve, n, edges)
        print(solve(n, edges))
main()