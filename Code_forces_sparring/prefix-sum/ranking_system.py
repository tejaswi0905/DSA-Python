# 1845D I am not able to either understand the problem or solve it, 

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

def solve(a):
    n = len(a)
    if n == 0:
        return 0

    # compute prefix sums
    pa = [0] * n
    pa[0] = a[0]
    for i in range(1, n):
        pa[i] = pa[i-1] + a[i]

    suf_max = float('-inf')  # max of pa[j] for j >= current i
    ans = 0 
    k = None                  # initialize with 0 to handle all-negative arrays

    # traverse from right to left
    for i in range(n-1, 0, -1):
        suf_max = max(suf_max, pa[i])   # update suffix max
        if pa[i-1] > pa[i]:             # found a drop
            gain = max(0, suf_max - pa[i])  # only add positive gain
            new_ans = ans + gain
            if new_ans > ans:
                ans = new_ans
                k = pa[i - 1]

    return k if k else 0


def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        a = ainp()
        # print_adv("The answer is ", solve, a)
        print(solve(a))

main()