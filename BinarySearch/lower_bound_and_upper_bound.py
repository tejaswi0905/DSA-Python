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

def find_position(nums, k):
    n = len(nums)
    l, r = 0, n - 1

    # FIRST TRUE: arr[i] >= k
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= k:
            r = mid
        else:
            l = mid + 1

    return l



def solve(n, nums, queries):
    nums.sort()
    ans = []
    for q in queries:
        idx = find_position(nums, q)
        if idx == n - 1:
            if q > nums[idx]:
                ans.append(0)
            else:
                ans.append(1)
            continue
        ans.append(n - idx)
    return ans

def main():
    n, q = ainp()
    nums = ainp()
    queries = []
    for _ in range(q):
        query = iinp()
        queries.append(query)
    ans = solve(n, nums, queries)
    for a in ans:
        print(a)

main()