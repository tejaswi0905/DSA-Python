# Binary search, and greedy and sorting, the conclusion for the binary search is very intersting.
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


def solve(n, arr):
    arr = list(sorted(arr))
    low = 0
    high = 10**9
    ans = float("inf")

    def is_possible(x):
        i = 0
        for group in range(3):  # at most 3 groups
            if i >= n:
                break
            j = i
            while j < n and arr[j] - arr[i] <= 2 * x:
                j += 1
            i = j
        return i == n


    while (low <= high):
        mid = (low + high) // 2
        if is_possible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
        
    return ans


def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        arr = ainp()
        print(solve(n, arr))

main()