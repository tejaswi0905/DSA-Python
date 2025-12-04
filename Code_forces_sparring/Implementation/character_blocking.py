"1840E This is a problem of implementation and I infact there is no logic for this code Just pure implementation. "

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


from collections import defaultdict

def solve(s1, s2, t, q, queries):
    n = len(s1)
    s1, s2 = list(s1), list(s2)

    is_blocked = [False] * n
    unblocks = defaultdict(list)

    # initial diff
    diff = sum(s1[i] != s2[i] for i in range(n))

    ans = []
    time = 0

    for query in queries:
        time += 1

        # ---- Unblock anything scheduled for this time ----
        for pos in unblocks[time]:
            if is_blocked[pos]:
                is_blocked[pos] = False
                if s1[pos] != s2[pos]:
                    diff += 1
        if time in unblocks:
            del unblocks[time]

        tp = query[0]

        # ---- Type 1 : block ----
        if tp == 1:
            pos = query[1] - 1
            if not is_blocked[pos]:
                if s1[pos] != s2[pos]:
                    diff -= 1
                is_blocked[pos] = True
                unblocks[time + t].append(pos)

        # ---- Type 2 : swap ----
        elif tp == 2:
            _, sA, iA, sB, iB = query
            iA -= 1
            iB -= 1

            # remove old contribution
            for p in (iA, iB):
                if not is_blocked[p] and s1[p] != s2[p]:
                    diff -= 1

            # perform swap
            if sA == 1 and sB == 1:
                s1[iA], s1[iB] = s1[iB], s1[iA]
            elif sA == 2 and sB == 2:
                s2[iA], s2[iB] = s2[iB], s2[iA]
            elif sA == 1 and sB == 2:
                s1[iA], s2[iB] = s2[iB], s1[iA]
            else:  # sA == 2 and sB == 1
                s2[iA], s1[iB] = s1[iB], s2[iA]

            # add new contribution
            for p in (iA, iB):
                if not is_blocked[p] and s1[p] != s2[p]:
                    diff += 1

        # ---- Type 3 : query ----
        else:
            ans.append("YES" if diff == 0 else "NO")

    return ans


def main():
    T = int(input())
    for _ in range(T):
        s1 = input().strip()
        s2 = input().strip()
        t, q = map(int, input().split())
        queries = [list(map(int, input().split())) for _ in range(q)]
        for out in solve(s1, s2, t, q, queries):
            print(out)
main()