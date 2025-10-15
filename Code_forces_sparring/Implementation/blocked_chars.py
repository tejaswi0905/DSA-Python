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

def sinp():
    return list(input())



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


def solve(n, q, t, s1, s2, queries):
    blocked_until = [0] * n  # Time until which position is blocked
    current_time = 0

    def is_blocked(pos):
        return blocked_until[pos] > current_time

    diff_count = 0
    for i in range(n):
        if not is_blocked(i) and s1[i] != s2[i]:
            diff_count += 1

    def get_char(str_id, idx):
        return s1[idx] if str_id == 1 else s2[idx]

    def set_char(str_id, idx, c):
        if str_id == 1:
            s1[idx] = c
        else:
            s2[idx] = c

    for query in queries:
        current_time += 1
        parts = query
        if parts[0] == '1':
            pos = int(parts[1]) - 1
            # If pos currently unblocked and chars differ, remove from diff count
            if not is_blocked(pos) and s1[pos] != s2[pos]:
                diff_count -= 1
            blocked_until[pos] = current_time + t

        elif parts[0] == '2':
            s_id1, p1 = int(parts[1]), int(parts[2]) - 1
            s_id2, p2 = int(parts[3]), int(parts[4]) - 1

            # Check if both positions unblocked
            if is_blocked(p1) or is_blocked(p2):
                continue

            # Remove old differences at affected positions
            if not is_blocked(p1) and s1[p1] != s2[p1]:
                diff_count -= 1
            if not is_blocked(p2) and s1[p2] != s2[p2]:
                diff_count -= 1

            # Swap characters
            c1 = get_char(s_id1, p1)
            c2 = get_char(s_id2, p2)
            set_char(s_id1, p1, c2)
            set_char(s_id2, p2, c1)

            # Add new differences at affected positions
            if not is_blocked(p1) and s1[p1] != s2[p1]:
                diff_count += 1
            if not is_blocked(p2) and s1[p2] != s2[p2]:
                diff_count += 1

        else:  # Query type 3
            print("YES" if diff_count == 0 else "NO")



def main():
    t = iinp()
    for _ in range(t):
        s1 = sinp()
        s2 = sinp()
        time, q = ainp()
        queries = []
        for _ in range(q):
            query = ainp()
            queries.append(query)
        solve(len(s1), q, time, s1, s2, queries)

main()