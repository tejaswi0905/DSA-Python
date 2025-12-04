"The questin is 1847D, this problem is not so tough when we fully understand what is happening, So understanding the question is most important and this is a segment tree problem"

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


class SegmentTree:
    def __init__(self, arr, merge_fn, neutral):
        self.n = len(arr)
        self.tree = [neutral] * (self.n * 4)
        self.merge = merge_fn
        self.neutral = neutral
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end = None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = arr[start]
            return 
        mid = (start + end) // 2
        self.build(arr, 2*node + 1, start, mid)
        self.build(arr, 2*node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2*node + 1], self.tree[2*node + 2])
    
    def update(self, idx, val, node, start, end = None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(idx, val, 2*node + 1, start, mid)
        else:
            self.update(idx, val, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2*node + 1], self.tree[2*node + 2])
    
    def query(self, left, right, node, start, end = None):
        if end is None:
            end = self.n - 1
        if left > end or right < start:
            return self.neutral
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_val = self.query(left, right, 2*node + 1, start, mid)
        right_val = self.query(left, right, 2*node + 2, mid + 1, end)
        return self.merge(left_val, right_val)



def solve(n, s, ranges, queries):
    merge_fun = lambda a, b: a + b
    neutral = 0

    idx_to_priority_map = {}
    priorities = [False] * n
    arr = []
    next_priority = 0

    for l, r in ranges:
        for idx in range(l, r + 1):
            if not priorities[idx]:
                priorities[idx] = True
                idx_to_priority_map[idx] = next_priority
                arr.append(s[idx])
                next_priority += 1
    
    d = next_priority
    seg = SegmentTree(arr, merge_fun, neutral)
    total_ones = sum(s)

    results = []

    for q in queries:
        if s[q] == 0:
            s[q] = 1
            total_ones += 1
            if q in idx_to_priority_map:
                seg.update(idx_to_priority_map[q], 1, 0, 0, d - 1)
        elif s[q] == 1:
            s[q] = 0
            total_ones -= 1
            if q in idx_to_priority_map:
                seg.update(idx_to_priority_map[q], 0, 0, 0, d - 1)

        if d == 0:
            results.append(0)
            continue

        K = min(d, total_ones)
        ones_in_top_K = seg.query(0, K - 1, 0, 0, d - 1) if K > 0 else 0
        results.append(K - ones_in_top_K)

    return results


def main():
    n, m, q = map(int, input().split())
    s = list(map(int, list(input().strip())))
    ranges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    queries = [int(input()) - 1 for _ in range(q)]
    print(*solve(n, s, ranges, queries), sep='\n')    


main()
