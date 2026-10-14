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


    
def solve(n, k):
    if (k == n -1 and n < 8):
        return []
    ans = []
    if k == 0:
        i = 0
        while i < n//2:
            pair = [i, n - i - 1]
            ans.append(pair)
            i += 1
        return ans
    if k == n - 1:
        ans = []
        ans.append([n - 1, n - 2])
        ans.append([1, n - 3])
        ans.append([0, 2])
        i = 3
        while i < n//2:
            pair = [i, n - i - 1]
            ans.append(pair)
        return ans
    else:
        ans.append([0, n - k - 1])
        ans.append([k, n - 1])
        i = 1
        while i < n//2:
            if (i != k) and (i != n - k - 1):
                pair = [i, n - i - 1]
                ans.append(pair)
            i += 1
        return ans

def main():
    t = iinp()
    for _ in range(t):
        n, k = ainp()
        ans = solve(n, k)
        if not ans:
            print(-1)
        else:
            for u, v in ans:
                print(u, v)
        
    
if __name__ == "__main__":
    main()