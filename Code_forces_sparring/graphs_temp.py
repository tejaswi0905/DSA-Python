from collections import deque
import math
import heapq as hq
import threading
import sys
Input = sys.stdin.readline

sys.setrecursionlimit(10**7)



def print_adv(text, func, *args, **kwargs):
    print(text, end = ' ')
    result = func(*args, **kwargs)
    print(result)

def ainp():  
    return list(map(int, Input().split()))

def oainp(nums):
    nums.extend(map(int, Input().split()))
    return nums

def iinp():
    return int(Input())



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

def bfs(n, g, start):
    dist = [-1]*(n + 1)
    q = deque()
    q.append((start, 0))

    while q:
        node, d = q.popleft()
        dist[node] = d
        for ch in g[node]:
            if dist[ch] == -1:
                q.append((ch, d + 1))
    return dist 
    

def mod_pow(a, b, m):
    if b == 0:
        return 1
    res = 1
    a = a%m
    while b > 0:
        if b%2 == 1:
            res = (res%m * a%m)%m
        a = (a%m * a%m)%m
        b = b//2
    return res%m


def solve(n, edges):
    g = {i:[] for i in range(1, n + 1)}
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    for i in range(1,n + 1):
        g[i].sort()
    visited = [-1] * (n + 1)
    ans = []
    def dfs(u):
        ans.append(u)
        visited[u] = 1
        for v in g[u]:
            if visited[v] == -1:
                dfs(v)
                ans.append(u)
    dfs(1)
    return ans

 
def main():
    n = iinp()
    edges = []
    for _ in range(n - 1):
        edge = ainp()
        edges.append(edge)
    ans = solve(n, edges)
    print(*ans[:])
    

    
if __name__ == "__main__":
    main()