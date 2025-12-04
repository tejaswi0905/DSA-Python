"This problem is 1845D, I did not solve this problem on my own"
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

def solve(n, a):
    # Step 1: Prefix sums
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + a[i]


    # Step 3: Traverse backwards to find suffix max gain
    mx = 0  # stores maximum suffix gain
    res = 0  # stores the corresponding k
    ans = float("-inf")
    for i in range(n, 0, -1):
        if p[i] > p[i - 1]:
            continue

        k = p[i - 1]
        mx = max(mx, p[n] - p[i])  # suffix gain
        if mx + k > ans:
            ans = mx + k
            res = k

    return res 


def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        a = ainp()
        print(solve(n, a))
main()