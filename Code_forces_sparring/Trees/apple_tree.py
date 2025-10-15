#1843D
# non-weighted graphs
from collections import defaultdict, deque
import math
import heapq as hq

from sys import setrecursionlimit
setrecursionlimit(10**6)

def print_adv(text, func, *args, **kwargs):
    print(text, end = ' ')
    result = func(*args, **kwargs)
    print(result)

def ainp():
    return list(map(int, input().split()))

def iinp():
    return int(input())



def build_graph_non_weighted(n, edges, is_directed = False, need_degree = False, zero_to_n = False):
    g = defaultdict(list)
    degree = None
    in_degree = None
    out_degree = None

    if not is_directed:
        if need_degree:
            if zero_to_n:
                degree = [0] * n
            else:
                degree = [0] * (n + 1)
            for u, v in edges:
                g[u].append(v)
                degree[u] += 1
                g[v].append(u)
                degree[v] += 1
        else:
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
    
            
    
    else:
        if need_degree:
            if zero_to_n:
                in_degree = [0] * n
                out_degree = [0] * n
            
            else:
                in_degree = [0] * (n + 1)
                out_degree = [0] * (n + 1)
            
            for u, v in edges:
                g[u].append(v)
                in_degree[v] += 1
                out_degree[u] += 1
        else:
            for u, v in edges:
                g[u].append(v)
    return (g, degree, in_degree, out_degree)

def solve(n, edges, q, queries):
    g, _, _, _ = build_graph_non_weighted(n, edges, False, False, False)
    leaf = [0] * (n + 1)
    def dfs(node, par):
        leaf_count = 0
        is_leaf = True
        for ch in g[node]:
            if ch != par:
                is_leaf = False
                leaf_count += dfs(ch, node)
        if is_leaf:
            leaf[node] = 1
            return 1
        leaf[node] = leaf_count
        return leaf_count
    
    dfs(1, -1)
    answer = []
    for i in range(q):
        u, v = queries[i]
        answer.append(leaf[u] * leaf[v])
    return answer
    


def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        edges = []
        for _ in range(n - 1):
            edge = ainp()
            edges.append(edge)
        q = iinp()
        queries = []
        for _ in range(q):
            query = ainp()
            queries.append(query)
        answer = solve(n, edges, q, queries)
        for ele in answer:
            print(ele)
        
main()