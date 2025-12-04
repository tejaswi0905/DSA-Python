"1845A, I am making it way to complicated"
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


def solve(n, k, x):
    if x != 1:
        return [1] * n
    
    arr = []
    for i in range(1, k + 1):
        if i == x:
            continue
        arr.append(i)
    
    dp = {}

    def helper(target):
        if target == 0:
            return []
        if target < 0:
            return None
        if target in dp:
            return dp[target]

        for num in arr:
            res = helper(target - num)
            if res is not None:  # found a valid combination
                dp[target] = res + [num]
                return dp[target]

        dp[target] = None
        return None

    answer = helper(n)
    if answer is None:
        return []
    return answer  

def main():
    t = iinp()
    for _ in range(t):
        n, k, x = ainp()
        arr = solve(n, k, x)
        if len(arr) > 0:
            print("YES")
            print(len(arr))
            print(*arr[:n])
        else:
            print("NO")
main()