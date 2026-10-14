from collections import deque
import math
import heapq as hq
import threading
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**7)



def print_adv(text, func, *args, **kwargs):
    print(text, end = ' ')
    result = func(*args, **kwargs)
    print(result)

def ainp():  
    return list(map(int, input().split()))

def iinp():
    return int(input())



def get_bits(num):
    ans = []
    for i in range(30):
        if (1<<i & num) == 0:
            ans.append(0)
        else:
            ans.append(1)
    return ans

def get_int(arr):
    ans = 0
    for i in range(len(arr)):
        ans += (2**i) * arr[i]
    return ans

def get_highest_2_power_less_than_k(k):
    num = None
    i = 0
    while (1 << i) <= k:
        num = 1 << i
        i += 1
    return num

def get_bit_count(num):
    cnt = 0
    while num > 0:
        num = num >> 1
        cnt += 1
    return cnt

def is_ith_bit_set(num, i):
    return ((1 << i) & num) != 0

def get_bit_freq(nums, k):
    bf = [0] * k
    for num in nums:
        i = 0
        while i < k:
            if ((num >> i) & 1) == 1:
                bf[i] += 1
            i += 1
    return bf

def xor_upto_n(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    if n % 4 == 3:
        return 0
    
def get_xor_of_arr(arr):
    ans = 0
    for num in arr:
        ans = ans ^ num
    return ans

def v2(num):
    i = 0
    while ((num >> i) & 1) == 0:
        i += 1
    return i



def solve(n, edges, pairs):
    g = {i:[] for i in range(n + 1)}
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)

    depth = [0]*n

    LOG = 20
    up = [[-1]*LOG for _ in range(n + 1)]

    def dfs(node, par, cur_depth):
        depth[node] = cur_depth
        for ch in g[node]:
            if ch == par:
                continue
            up[ch][0] = node
            dfs(ch, node, cur_depth + 1)

    dfs(1, -1, 0)

    for k in range(LOG - 1, -1, -1):
        for u in range(1, n + 1):
            ansc = up[u][k - 1]
            if ansc != -1:
                up[u][k] = up[ansc][k - 1]

    def get_kth_parent(u, k):
        if k == 0 or u == -1:
            return u 

        for jump in range(LOG - 1, -1, -1):
            if (k >= (1 << jump)) and (u != -1):
                u = up[u][jump]
                k -= (1 << jump)
        return u 

    def lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            u = get_kth_parent(u, du - dv)
        if dv > du:
            v = get_kth_parent(v, dv - du)
        if u == v:
            return u 

        for jump in range(LOG - 1, -1, -1):
            if up[u][jump] != up[v][jump]:
                u = up[u][jump]
                v = up[v][jump]
        return up[u][0]


    def get_dist(u, v):
        l = lca(u, v)
        du = depth[u]
        dv = depth[v]
        dl = depth[l]
        return (du + dv - 2*dl)

    

    


def main():
    n, k = ainp()
    pairs = ainp()
    edges = []
    for _ in range(n - 1):
        edge = ainp()
        edges.append(edge)

    ans = solve(n, edges, pairs)
    print(ans)
    
    
        
    
if __name__ == "__main__":
    main()