from collections import deque
import math
import heapq as hq
import threading
import sys

sys.setrecursionlimit(10**6)


def ainp():
    return list(map(int, input().split()))


def iinp():
    return int(input())


def solve(n, edges):
    LIMIT = 10**6
    g = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    visited = [False]*(n + 1)
    count = 0

    def dfs(u):
        nonlocal count
        visited[u] = True
        count += 1

        if count >= LIMIT:
            return True

        for v in g[u]:
            if not visited[v]:
                completed = dfs(v)
                if completed:
                    return True
        visited[u] = False
        return False
    dfs(1)
    return min(count, LIMIT)


def main():
    n, m = ainp()
    edges = []
    for _ in range(m):
        edge = ainp()
        edges.append(edge)
    ans = solve(n, edges)
    print(ans)


main()
