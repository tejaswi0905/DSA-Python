'''
1836C, it is just some math and implmentation.
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


def solve(A, B, C, k):
    # Precompute min/max for a, b, c (no leading zeros)
    min_a = 10 ** (A - 1)
    max_a = 10 ** A - 1
    min_b = 10 ** (B - 1)
    max_b = 10 ** B - 1
    min_c = 10 ** (C - 1)
    max_c = 10 ** C - 1

    # Track remaining k we need to satisfy
    current_k = k
    found = False  # Did we find the k-th?

    # Loop over possible a in order (smallest to largest)
    for a in range(min_a, max_a + 1):
        # Calculate range for b
        lb = max(min_b, min_c - a)  # b must be at least this to make c big enough
        ub = min(max_b, max_c - a)  # b must be at most this to make c small enough

        # If no possible b for this a
        if lb > ub:
            count = 0
        else:
            count = ub - lb + 1  # Number of possible b

        # If this a has enough b's to cover remaining k
        if current_k <= count:
            # The current_k-th b for this a
            b = lb + current_k - 1
            c = a + b  # c = a + b, and it will have exactly C digits
            # Output the string (spaces matter!)
            return [a, b, c]
        else:
            # Skip this a, reduce k by how many we "used"
            current_k -= count

    # If we looped through all a and still need more, not enough total sums
    return [-1]

def main():
    t = iinp()
    for _ in range(t):
        a, b, c, k = ainp()
        ans = solve(a, b, c, k)
        if len(ans) == 1:
            print("-1")
            continue
        a = ans[0]
        b = ans[1]
        c = ans[2]
        print(f"{a} + {b} = {c}")
main()