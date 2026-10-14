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

def oainp(nums):
    nums.extend(map(int, input().split()))
    return nums

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
def p0(n, nums):
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + nums[i]
    return p
def p1(n, nums):
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + nums[i]
    return p
    
# def solve(n, a):
#     pref = [0] * n
#     pref[0] = a[0]
#     for i in range(1, n):
#         pref[i] = math.gcd(pref[i - 1], a[i])
    
#     suff = [0] * n
#     suff[n - 1] = a[n - 1]
#     for i in range(n - 2, -1, -1):
#         suff[i] = math.gcd(suff[i + 1], a[i])

#     ans = 0
#     for i in range(n):
#         if i == 0:
#             curr = suff[1]
#         elif i == n - 1:
#             curr = pref[n - 2]
#         else:
#             curr = math.gcd(pref[i - 1], suff[i + 1])
#         ans = max(ans, curr)

#     return ans


# def solve(n, a):
#     p = p1(n, a)
#     mod = 1000000000 + 7
#     ans = 0
#     for i in range(1, n + 1):
#         ans += ((a[i] % mod) * (p[n]%mod - p[i]%mod))%mod
#     return ans % mod



# def solve(n,x,a):
#     p = p0(n, a)
#     ans = 0
#     hm = {}
#     for i in range(n + 1):
#         cur = p[i]
#         req = cur - x
#         ans += hm.get(req, 0)
#         if cur not in hm:
#             hm[cur] = 0
#         hm[cur] += 1
#     return ans



def solve(n, m, a):
    p = p1(n, a)
    print(a, p)
    cur = 0
    for i in range(1, m + 1):
        cur += i * a[i]

    ans = cur
    print("the initital ans is ", ans)

    for i in range(2, n - m + 1): 
        subtract = p[i + m - 1] - p[i - 1]
        add = m * a[i + m]
        cur -= subtract
        cur += add
        ans = max(ans, cur)

    return ans


def main():
    n, m = ainp()
    a = oainp([0])
    ans = solve(n, m, a)
    print("The answer is ", ans)
        
    
if __name__ == "__main__":
    main()