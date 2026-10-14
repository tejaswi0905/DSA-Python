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


# def solve(n, k, queries):
#     dp = [-1]*(n+1)
#     def rec(i):
#         if i == n:
#             return 1
#         if dp[i] != -1:
#             return dp[i]
#         cnt = 0
#         cnt += rec(i + 1)
#         if i + k <= n:
#             cnt += rec(i + k)
#         dp[i] = cnt
#         return cnt
    
#     ans = rec(0)
#     print("The ans in rec is ", ans)
    


def solve(n, k, quereis):
    dp = [0]*(n + 1)
    dp[n] = 1
    mod = 10**9 + 7

    for i in range(n-1, -1, -1):
        cnt = 0
        cnt = (cnt + dp[i + 1])%mod
        if i + k <= n:
            cnt = (cnt + dp[i + k])%mod
        dp[i] = cnt%mod
    a = dp[0:len(dp) - 1]
    a = a[::-1]
    pf = [0]*(len(a) + 1)
    for i in range(1, len(a) + 1):
        pf[i] = (pf[i - 1] + a[i - 1])%mod
    ans = []
    for ai, bi in quereis:
        if ai == bi:
            ans.append(a[ai - 1])
        else:
            ans.append((pf[bi] - pf[ai -1])%mod)
    return ans
          
 
def main():
    q, k = ainp()
    n = float("-inf")
    queries = []
    for _ in range(q):
        ai, bi = ainp()
        n = max(ai, n)
        n = max(bi, n)
        queries.append([ai, bi])
    ans = solve(n, k, queries)
    for val in ans:
        print(val)
    
  
if __name__ == "__main__":
    main()