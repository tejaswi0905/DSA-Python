# non-weighted graphs
from collections import defaultdict, deque
import math
import heapq as hq
from bisect import bisect_right

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

def solve(n, p, queries):
    segs = []
    for i in range(n):
        l, r, a, b = p[i]
        # reduce portal to (l, b) as explained
        segs.append((l, b))

    if not segs:
        return queries

    # sort and merge
    segs.sort()  # by l then b
    merged = []
    curL, curR = segs[0]
    for l, b in segs[1:]:
        if l <= curR:          # overlap or touch
            if b > curR:
                curR = b
        else:
            merged.append((curL, curR))
            curL, curR = l, b
    merged.append((curL, curR))

    # prepare arrays for binary search
    starts = [seg[0] for seg in merged]
    ends   = [seg[1] for seg in merged]
    ans = []
    for x in queries:
        # find rightmost interval with start <= x
        idx = bisect_right(starts, x) - 1
        if idx >= 0 and x <= ends[idx]:
            ans.append(ends[idx])
        else:
            ans.append(x)
    return ans


def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        p = []
        for _ in range(n):
            portal = ainp()
            p.append(portal)
        q = iinp()
        queries = ainp()
        arr = solve(n, p, queries)
        print(*arr[:])

main()