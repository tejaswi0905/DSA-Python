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

def printcol(arr):
    for num in arr:
        print(num)
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

def mod_pow(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = ((res%m)*(a%m))%m
        a = ((a%m)*(a%m))%m
        b = b//2
    return res

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

def next_permutation(n, a):
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i == -1:
        return a
    
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[j], a[i] = a[i], a[j]
    reversed_suffex = list(reversed (a[i+1:]))
    for idx in range(i + 1, n):
        a[idx] = reversed_suffex[idx - (i + 1)]
    return a

def facts(n,m):
    f = [0]*(n+1)
    f[0],f[1] = 1, 1
    for i in range(2, n + 1):
        f[i]=((i%m)*(f[i-1]%m))%m
    return f


def get_sum(s):
    m = {}
    for ch in s:
        if ch not in m:
            m[ch] = 0
        m[ch] += 1
    ans = 0
    for i in range(1, 10):
        if i not in m:
            ans += i
        else:
            ci = m[i]
            ans += i * (10**ci)
    return ans


def solve(k,ars,art):
    r = (9 * k) - 8
    total_ways = r * (r -1)

    cnt = [k] * 10
    for i in ars:
        cnt[i] -= 1
    for i in art:
        cnt[i] -= 1
    
    fav = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                ars.append(i)
                art.append(j)
                s_score = get_sum(ars)
                t_score = get_sum(art)
                if s_score > t_score:
                    fav += cnt[i] * cnt[j]
                ars.pop()
                art.pop()
            else:
                if cnt[i] >= 2:
                    ars.append(i)
                    art.append(i)
                    s_score = get_sum(ars)
                    t_score = get_sum(art)
                    if s_score > t_score:
                        fav += cnt[i] * (cnt[i] - 1)
                    ars.pop()
                    art.pop()
    return fav/total_ways
   
    

def main():
    k = iinp()
    s = list(input())
    t = list(input())
    ars = list(map(int, s[:-2]))
    art = list(map(int, t[:-2]))
    
    ans = solve(k, ars, art)
    print(ans)

if __name__ == "__main__":
    main()

