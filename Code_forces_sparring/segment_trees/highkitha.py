'''
1847D
'''
class SegmentTree:
    def __init__(self, arr, merge_fn, neutral):
        self.n = len(arr)
        self.tree = [neutral] * (4 * self.n)  # Tree size is about 4*n for safety
        self.merge = merge_fn
        self.neutral = neutral
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]  # Leaf node: store the array value
            return
        mid = (start + end) // 2
        self.build(arr, 2*node + 1, start, mid)     # Left child
        self.build(arr, 2*node + 2, mid + 1, end)   # Right child
        # Merge children values into parent
        self.tree[node] = self.merge(self.tree[2*node + 1], self.tree[2*node + 2])
    
    def update(self, idx, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val  # Update leaf
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(idx, val, 2*node + 1, start, mid)  # Go left
        else:
            self.update(idx, val, 2*node + 2, mid + 1, end)  # Go right
        # Re-merge after update
        self.tree[node] = self.merge(self.tree[2*node + 1], self.tree[2*node + 2])
    
    def query(self, left, right, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if left > end or right < start:
            return self.neutral  # Out of range: return neutral (doesn't affect merge)
        if left <= start and end <= right:
            return self.tree[node]  # Fully covered: return node value
        mid = (start + end) // 2
        left_val = self.query(left, right, 2*node + 1, start, mid)
        right_val = self.query(left, right, 2*node + 2, mid + 1, end)
        return self.merge(left_val, right_val)  # Merge partial results


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



def solve(n, string, updates, queries):
    arr = list(map(int, list(string)))
    cur = 1
    priority = defaultdict(int)
    for l, r in updates:
        for i in range(l, r + 1):
            if i not in priority:
                priority[i] = cur
                cur += 1
                

    

def main():
    n, m, q = ainp()
    string = input()
    updates = []
    for _ in range(m):
        l, r = ainp()
        updates.append([l - 1, r - 1])
    queries = []
    for _ in range(q):
        cur = iinp()
        queries.append(cur - 1)
    print_adv("The answer is ", solve, n, string, updates, queries)

main()