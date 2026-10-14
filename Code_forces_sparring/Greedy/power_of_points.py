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

def ainp(nums):
    nums.extend(map(int, input().split()))
    return nums

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


def solve(n, nums):
    pairs = [(nums[i], i) for i in range(n + 1)]
    pairs.sort()
    p = [0] * (n + 1)
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + pairs[i][0]
    for i in range(1, n + 1):
        si = pairs[i][0]
        ans = (n) + si * (2 * i - n) + p[n] - 2 * p[i]
        res[pairs[i][1]] = ans
    return res


def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        nums = ainp([0])
        ans = solve(n, nums)
        print(*ans[1:])

main()

