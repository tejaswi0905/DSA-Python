# def count_prime_in_n_factorial(num, p):
#     n = num
#     count = 0
#     power = p
#     while power <= n:
#         count += n // power
#         power = power * p
#     return count
# print(count_prime_in_n_factorial(10, 2))

# from collections import defaultdict

# MAX = 10 ** 5 + 1
# spf = [i for i in range(MAX)]
# for i in range(2, int(MAX ** (0.5)) + 1):
#     if spf[i] == i:
#         for j in range(i * i, MAX, i):
#             if spf[j] == j:
#                 spf[j] = i

# def prime_factorization_mod(num, k):
#     factorization = defaultdict(int)
#     n = num
#     while n > 1:
#         p = spf[n]
#         factorization[p] += 1
#         n = n // p
#     res = []
#     for prime in factorization:
#         mod = factorization[prime] % k
#         if mod != 0:
#             res.append((prime, mod))
#     return tuple(res)

# def get_complement(key, k):
#     res = []
#     for prime, mod in key:
#         complement_mod = (k - mod) % k
#         if complement_mod != 0:
#             res.append((prime, complement_mod))
#     return tuple(res)

# def count_kth_power_pairs(nums, k):
#     freq = defaultdict(int)
#     for num in nums:
#         key = prime_factorization_mod(num, k)
#         freq[key] += 1
#     total = 0
#     visited = set()
#     for key in freq:
#         complement = get_complement(key, k)
#         if key == complement:
#             count = freq[key]
#             total += count * (count - 1) // 2
#         elif key not in visited:
#             total += freq[key] * freq.get(complement, 0)
#         visited.add(key)
#     return total

import math

# def gcd(a,b):
#     while b > 0:
#         if b > a:
#             a, b = b, a
#         temp = a
#         a = b
#         b = temp % b
#     return a


# def get_pattern(a, b):
#     ans = []
#     g = gcd(a, b)
#     total = math.floor(b/g)
#     for i in range(total):
#         ans.append(g * i)
#     return ans



# def extended_euclide(a, b): # we return gcd(a, b), x, y
#     if b == 0:
#         return [a, 1, 0]
#     g, x1, y1 = extended_euclide(b, a % b)
#     x = y1
#     y = x1 - (a//b) * y1
#     return [g, x, y]
# def mod_inverse(a, m):
#     g, x, y = extended_euclide(a, m)
#     if g != 1:
#         return -1
#     return x % m
# print(mod_inverse(4, 5))

# def modular_exponentiation(a, b, m):
#     res = 1
#     a = a % m
#     while b > 0:
#         if b % 2 == 1:
#             res = (res * a) % m
#         a = (a * a) % m
#         b = b // 2
#     return res
# def mod_inverse_2(a, b):
#     ans = modular_exponentiation(a, b - 2, b)
#     return ans


# def compute_phi(n):
#     phi = [i for i in range(n + 1)]
#     for i in range(2, n + 1):
#         if phi[i] == i:
#             for j in range(i, n + 1, i):
#                 phi[j] = phi[j] - phi[j] // i
#     return phi


def phi2(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            res = res - res // i
        i += 1
    if n > 1:
        res = res - res // i
    return res

# def phi(n):
#     res = n
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             while n % i == 0:
#                 n = n // i
#             res = res - res // i
#         i += 1
#     if n > 1:
#         res = res - res // i
#     return res

def merge_sort(arr):
    def count_pairs(arr, l, y, r):
        count = 0
        i = l
        j = y
        while (i < y) and (j <= r):
            if arr[i] > arr[j]:
                count += y - i
                j += 1
            else:
                i += 1
        return count

    def merge_in_array(arr, l, y, r):
        i = l
        j = y
        c = []
        while (i < y) and (j <= r):
            if arr[i] <= arr[j]:
                c.append(arr[i])
                i += 1
            else:
                c.append(arr[j])
                j += 1
        while i < y:
            c.append(arr[i])
            i += 1
        while j <= r:
            c.append(arr[j])
            j += 1
        for i in range(l, r + 1):
            arr[i] = c[i - l]
        return arr
    
    def merge(arr, l, r):
        if l == r:
            return 0
        mid = (l + r) // 2
        left = merge(arr, l, mid)
        right = merge(arr, mid + 1, r)
        cur = count_pairs(arr, l, mid + 1, r)
        merge_in_array(arr, l, mid + 1, r)
        return left + right + cur
    l = 0
    r = len(arr) - 1
    ans = merge(arr, l, r)
    return ans

print(merge_sort([1, -2, 3, -4, 11, 1, 11]))

        