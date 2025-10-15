'''
1838C
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

def solve(n, m):
    
    if n % 2 == 0:
        grid = [[None] * m for _ in range(n)]
        num = 1
        for col in range(m):
            for row in range(n):
                grid[row][col] = num
                num += 1
        return grid

        
    else:
        grid = []
        #odd rows 
        row = 1
        while row < n + 1:
            arr = []
            start = ((row - 1) * m) + 1
            for _ in range(m):
                arr.append(start)
                start += 1
            grid.append(arr)
            row += 2
        row = 2
        while row < n + 1:
            arr = []
            start = ((row - 1) * m) + 1
            for _ in range(m):
                arr.append(start)
                start += m
            grid.append(arr)
            row += 2
        return grid
            
            
        

def main():
    t = iinp()
    for _ in range(t):
        n, m = ainp()
        grid = solve(n, m)
        for row in grid:
            for ele in row:
                print(ele, end = ' ')
            print()
        print()

main()