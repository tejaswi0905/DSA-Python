'''
Now the problems is same as rudalf_snowflake, 

'''


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


def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        found = False

        for p in range(2, 61):
            low, high = 2, int(1e18)
            while low <= high:
                mid = (low + high) // 2

                total, term = 1, 1
                overflow = False
                for _ in range(p):
                    term *= mid
                    total += term
                    if total > n:
                        overflow = True
                        break

                if total == n:
                    found = True
                    break
                elif total < n and not overflow:
                    low = mid + 1
                else:
                    high = mid - 1

            if found:
                break

        print("YES" if found else "NO")
solve()