'''
1845C, I have something new to learn in this problem, which is the nxt 2D array to keep track of the positions, so a typical nxt[pos][ch] will tell us, what is the closest spot at or after pos that has the char ch in the given string.
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

def solve(S, m, l, r):    
    n = len(S)
    
    # Build the cheat map (nxt)
    nxt = [[n] * 10 for _ in range(n + 1)]  # Big table: rows=pos, cols=digit
    for d in range(10):  # For each sign type
        ptr = n  # Start off-road
        for pos in range(n - 1, -1, -1):  # Walk backward
            if int(S[pos]) == d:  # Found a sign!
                ptr = pos  # Update last seen
            nxt[pos][d] = ptr  # Fill for this pos
    # DP: Worst-spot tracker
    current_max = -1  # Haven't started
    
    for i in range(m):  # Each code position
        l_digit = int(l[i])
        r_digit = int(r[i])
        
        new_max = -1  # Temp worst for this step
        has_fail = False  # No block yet
        
        for digit in range(l_digit, r_digit + 1):  # Possible signs
            # Jump from after worst
            pos = nxt[current_max + 1][digit]
            if pos == n:  # Blocked!
                has_fail = True
            else:  # Ok, track new worst
                new_max = max(new_max, pos)
        
        if has_fail:
            return "YES"  # Found a strong code!

        
        current_max = new_max  # Update worst for next
    
    return "NO"  # All codes weak

def main():
    t = iinp()
    for _ in range(t):
        s = input().strip()
        m = iinp()
        l = input().strip()
        r = input().strip()
        print(solve(s, m, l, r))
main()