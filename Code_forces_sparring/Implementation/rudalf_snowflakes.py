'''
1846E1, this problem is implementation and nothing more. For each k, the minimum number of nodes in the graph are, 1 + k + k^2, and we keep adding k powers to the graph, and k can be form 1 to inf, but the total number of nodes can't be more than 10^6.

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


const = 10**6 + 5
arr = [False] * const


def solve():
    global const
    k = 2
    while k < const:
        total = 1 + k + k * k
        x = k * k
        while total < const:
            arr[total] = True
            total += x * k
            x = x * k
        k += 1

solve()

    

def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        if arr[n]:
            print("YES")
        else:
            print("NO")
main()