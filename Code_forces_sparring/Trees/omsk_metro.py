"This is the simple version of 1843F, here the u is alwas 1"

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




def solve(n, queries):
    
    # Max possible stations: 1 initial + up to n additions
    MAXN = n + 2
    
    # Arrays to store per-station info (index 1 to ptr)
    mn = [0] * MAXN       # Min prefix sum on path (incl. 0)
    mx = [0] * MAXN       # Max prefix sum on path (incl. 0)
    sum_ = [0] * MAXN     # Prefix sum to this station
    dif_mn = [0] * MAXN   # Min subsegment sum on path
    dif_mx = [0] * MAXN   # Max subsegment sum on path
    
    # Initialize root station 1
    mn[1] = 0
    mx[1] = 1
    sum_[1] = 1
    dif_mn[1] = 0
    dif_mx[1] = 1
    
    # Current last station ID
    ptr = 1
    
    # Process each event
    for query in queries:
        type_ = query[0]
        
        if type_ == '+':
            # Add new station: read parent v and weight x (+1 or -1)
            v = int(query[1])
            x = int(query[2])

            
            # Increment station counter
            ptr += 1
            
            # Update prefix sum for new station
            sum_[ptr] = sum_[v] + x
            
            # Update min/max prefixes (extend from parent, include new sum)
            mn[ptr] = min(mn[v], sum_[ptr])
            mx[ptr] = max(mx[v], sum_[ptr])
            
            # Start with parent's max/min subseg
            dif_mx[ptr] = dif_mx[v]
            dif_mn[ptr] = dif_mn[v]
            
            # Update max subseg: consider new subsegs ending at ptr (new sum - min of prior prefixes)
            dif_mx[ptr] = max(dif_mx[ptr], sum_[ptr] - mn[v])
            
            # Update min subseg: consider new subsegs ending at ptr (new sum - max of prior prefixes)
            dif_mn[ptr] = min(dif_mn[ptr], sum_[ptr] - mx[v])
        
        else:
            # Query: read u (always 1, ignored), v, k
            u = int(query[1])
            v = int(query[2])
            k = int(query[3])
            
            # Check based on k's sign and the computed bounds
            if k == 0:
                print("YES")  # Always yes (empty subsegment)
            elif k > 0:
                if dif_mx[v] >= k:
                    print("YES")
                else:
                    print("NO")
            else:  # k < 0
                if dif_mn[v] <= k:
                    print("YES")
                else:
                    print("NO")

def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        queries = []
        for _ in range(n):
            query = input().split()
            queries.append(query)
        solve(n, queries)
main()