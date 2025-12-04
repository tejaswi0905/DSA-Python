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



import sys
from math import inf
input = sys.stdin.readline

def baseline(d, x):
    # x is a list of positions with sentinels already included
    # computes: sum ((x[i] - x[i-1] - 1) // d) + (len(x) - 2)
    ans = 0
    for i in range(1, len(x)):
        ans += (x[i] - x[i-1] - 1) // d
    ans += len(x) - 2
    return ans

def solve_case():
    n, m, d = map(int, input().split())
    r = list(map(int, input().split()))

    # Insert editorial sentinels: 1-d at front, n+1 at end
    r.insert(0, 1 - d)
    r.append(n + 1)

    bestD = 10**18   # minimal D found (we want min)
    res_count = 0

    for i in range(1, m + 1):
        A = r[i] - r[i-1] - 1
        B = r[i+1] - r[i] - 1
        C = r[i+1] - r[i-1] - 1
        D = C // d - (A // d + B // d)

        if D < bestD:
            bestD = D
            res_count = 1
        elif D == bestD:
            res_count += 1

    total = bestD + baseline(d, r) - 1
    print(total, res_count)


def main():
    t = int(input().strip())
    for _ in range(t):
        solve_case()

if __name__ == "__main__":
    main()
