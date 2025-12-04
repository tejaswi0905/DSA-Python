'''
This is problem 1846D, a very cool implementation problem, based on basic geomerty and I did not compe up with the solution. 
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


def solve(n, b, h, arr):
    def area(b, h):
        return (b * h) / 2

    answer = area(b, h)
    for i in range(1, len(arr)):
        y2 = arr[i]
        y1 = arr[i - 1]
        if y2 < arr[i - 1] + h:
            h1 = (y1 + h) - y2
            b1 = (h1) * ((b/2)/h)
            removed_area = area(2 * b1, h1)
            actual_area = area(b , h)
            answer += actual_area - removed_area
        else:
            answer += area(b , h)
    truncated = math.floor(answer * 10**6) / 10**6
    return truncated

def main():
    t = iinp()
    for _ in range(t):
        n, b, h = ainp()
        arr = ainp()
        # print_adv("the answer is ", solve, n, b, h, arr)
        print(solve(n, b, h, arr))
main()