#classic implementation of segment trees, we are doing the advanced implementation.
# The segment tree is a complete binary tree like Heaps, and we use the same trick to find the nodes and parent of each node
#We use an array, and for every node that is at i, it's parent is at (i - 1) // 2, and for a node at i, its left and right children are at (2 * i) + 1 and (2 * i) + 1.

import math  # For gcd, if needed

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


# The lazy propgation have One new funcitons, one is push_donw, before writing the general function lets write donw the easy version of merging array with new elements.

class SegmentTreeLazy:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Sum values
        self.lazy = [0] * (4 * self.n)  # Pending adds
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2*node + 1, start, mid)
        self.build(arr, 2*node + 2, mid + 1, end)
        self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]
    
    def push_down(self, node, start, end):
        if self.lazy[node] != 0:  # Pending update?
            # Apply to current node: add lazy * length
            self.tree[node] += self.lazy[node] * (end - start + 1)
            if start != end:  # Not leaf: pass to children
                self.lazy[2*node + 1] += self.lazy[node]
                self.lazy[2*node + 2] += self.lazy[node]
            self.lazy[node] = 0  # Clear
    
    def update(self, left, right, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        self.push_down(node, start, end)  # Apply pending first
        if left > end or right < start:
            return  # No overlap
        if left <= start and end <= right:
            # Full overlap: Apply lazy
            self.lazy[node] += val
            self.push_down(node, start, end)  # Immediately apply to tree (for consistency)
            return
        # Partial: Recurse
        mid = (start + end) // 2
        self.update(left, right, val, 2*node + 1, start, mid)
        self.update(left, right, val, 2*node + 2, mid + 1, end)
        # Re-merge
        self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]
    
    def query(self, left, right, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        self.push_down(node, start, end)  # Apply pending
        if left > end or right < start:
            return 0  # Neutral for sum
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(left, right, 2*node + 1, start, mid)
        right_sum = self.query(left, right, 2*node + 2, mid + 1, end)
        return left_sum + right_sum