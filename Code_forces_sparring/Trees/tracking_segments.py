# non-weighted graphs

# For this problem I thought about segment-trees, but I need to work it out by using binary search, and the idea of binary serach is very strange here, we can't make one update at a time and then check if any one of the given ranges is beautiful or not, that will be o(n * m) No matter how efficient we make the updates, Here we have to do it by making k updates at a time, k something between 0 to len(q) - 1. So if k updates makes the array beautiful, then k can be a possible answer and we can search between 0 to k - 1 to find something better. Hence the binary search. The overal time complexity will be BigO(qlog(q + m + n)).

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

def solve(n, m, queires, q, updates):
    low = 0
    high = q - 1
    ans = -1
    while (low <= high):
        mid = (low + high) // 2
        b = [0] * n

        for i in range(mid + 1): #Now make the updates upto mid.
            b[updates[i]] = 1
        
        for i in range(1, n):# Prifix sum
            b[i] += b[i - 1]
        
        f = False
        for i in range(m): # Checking each range to find out if we have a beautiful range or not.
            l, r = queires[i]
            if l > 0:
                ones = b[r] - b[l - 1]
            else:
                ones = b[r]
            zeros = ((r - l) + 1) - ones
            if ones > zeros:
                f = True
                break
        if (f):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    if ans != -1:
        ans += 1
    return ans


def main():
    t = iinp()
    for _ in range(t):
        n, m = ainp()
        queries = []
        for _ in range(m):
            l, r = ainp()
            queries.append([l - 1, r - 1])
        
        q = iinp()
        updates = []
        for _ in range(q):
            u = iinp()
            updates.append(u - 1)
        # print_adv("The answer is ", solve, n, m, queries, q, updates)
        print(solve(n, m, queries, q, updates))

main()