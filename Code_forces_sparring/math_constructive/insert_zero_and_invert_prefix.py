'''
1839C, This one is very good. The key idea behid solving this problem is think in opposite. Instead of truning an empty array into B, try to trun the array A into an empty array.
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

def solve(n, a):
    ans = []
    i = 0
    while i < n:
        j = i
        while (j < n and a[j] == 1):
            j += 1
        if j == n:
            return []
        ans.append(j)
        for _ in range(i, j):
            ans.append(0)
        i = j + 1
    return list(reversed(a))

def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        arr = ainp()
        ans = solve(n, arr)
        if not ans:
            print("NO")
            continue
        print("YES")
        print(*ans[:n])
        
main()
