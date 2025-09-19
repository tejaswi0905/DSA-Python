from collections import defaultdict
import math

# def cout_of_primes_in_factorial(n):
#     primes = {}
#     primes_upto_n = [i for i in range(n + 1)]
#     for i in range(2, n + 1):
#         if primes_upto_n[i] == i:
#             for j in range(i * i, n + 1, i):
#                 primes_upto_n[j] = i
    
#     for i in range(2, n + 1):
#         if primes_upto_n[i] == i:
#             power = i
#             count = 0
#             while power <= n:
#                 count += math.floor(n/power)
#                 power *= i
#             primes[i] = count
#     return primes

# # print(cout_of_primes_in_factorial(10))


# def eea(a, b): #returns gcd(a, b), x, and y where x and y are the solutions of the equation ax + by = g
#     if b == 0:
#         return [a, 1, 0]
#     g, xo, yo = eea(b, a % b)
#     x = yo
#     y = xo - (a//b)*yo
#     return [g, x, y]

# # print(eea(6, 9))


# def mod_pow(a, b, m):
#     res = 1
#     a = a % m
#     while b > 0:
#         if b % 2 == 1:
#             res = (res * a) % m
#         a = (a * a) % m
#         b = b // 2
#     return res

# def mod_inv(a, p):
#     return mod_pow(a, p - 2, p)

# def mod_inv_with_eea(a, m):
#     g, a, _ = eea(a, m)
#     if g != 1:
#         return -1
#     return a % m

# # print(mod_inv(3, 7))
# # print(mod_inv_with_eea(3, 7))

# '''
# if the prime factorizaion of num = p1^e1 * p2^e2 * p3^e3 ..... pk^ek
# phi(n) = n * (1 - 1/p1)(1-1/p2)...(1-1/pk)

# n * (1 - 1/p1) = n - n/p1 = newN
# n * (1 - 1/p1)(1-1/p2) = newN * (1 - 1/p2) = newN - newN/p2 = newNewN


# phi(12) = 2^2 * 3^1 ==> p1 = 2 and p2 = 3
#   ||    = 12 * (1 - 1/2) * (1 - 1/3)
#   ||    = 12 * 1/2 * 2/3
# phi(12) = 4
# '''

# # computing phi values for every number from 1 to n. Modified sieve algo
# def phi_upto_n(n):
#     phi = [i for i in range(n + 1)] # [2, 3, 4, 5, 6, 7, 8]
#     for i in range(2, n + 1):
#         if phi[i] == i:
#             for j in range(i, n + 1, i):
#                 phi[j] = phi[j] - phi[j] // i
#     return phi

# # print(phi_upto_n(12))

# #phi of only n

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
#         res = res - res // n
#     return res

# # print(phi(12))


# def find_lca(n, edges, queries):
#     g = defaultdict(list)
#     for u, v in edges:
#         g[u].append(v)
#         g[v].append(u)
    
#     LOG = 20
#     depth = [0] * (n + 1)
#     up = [[-1] * LOG for _ in range(n + 1)]

#     def dfs(node, p, d):
#         depth[node] = d
#         up[node][0] = p
#         for ng in g[node]:
#             if ng != p:
#                 dfs(ng, node, d + 1)
                
#     dfs(1, -1, 0)

#     for k in range(1, LOG):
#         for u in range(1, n + 1):
#             ancestor = up[u][k - 1]
#             if ancestor != -1:
#                 up[u][k] = up[ancestor][k - 1]
    
#     def get_kth_ancestor(node, k):
#         if node == -1 or k == 0:
#             return node
        
#         for i in range(LOG - 1, - 1, - 1):
#             if k >= (1 << i) and node != -1:
#                 node = up[node][i]
#                 k = k - (1 << i)
#         return node
    
#     def get_lca(u, v):
#         du = depth[u]
#         dv = depth[v]

#         if du > dv:
#             u = get_kth_ancestor(u, du - dv)
#         if dv > du:
#             v = get_kth_ancestor(v, dv - du)
#         if u == v:
#             return u
        
#         for k in range(LOG - 1, -1, -1):
#             if up[u][k] != up[v][k]:
#                 u = up[u][k]
#                 v = up[v][k]
#         return up[u][0]
    
#     answer = []
#     for u, v in queries:
#         l = get_lca(u, v)
#         answer.append(l)
#     return answer
    
# edges = [[1, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [5, 10], [6, 12], [8, 9], [10, 11]]

# print(find_lca(12, edges, [[10, 12], [10, 1], [5, 5]]))

'''MergeSort and its applications revision'''

arr = [1, 2, 5, 6, -2, 4, 9, 11, 3, 4]

def merge_sort(arr):
    def merge_step(arr, l, y, r):
        c = [None] * (r - l + 1)
        i = l
        j = y
        k = 0
        while (i < y) and (j <= r):
            if arr[i] < arr[j]:
                c[k] = arr[i]
                i += 1
            else:
                c[k] = arr[j]
                j += 1
            k += 1
        while i < y:
            c[k] = arr[i]
            i += 1
            k += 1
        while j <= r:
            c[k] = arr[j]
            j += 1
            k += 1
        for i in range(l, r + 1):
            arr[i] = c[i - l]
        return arr
    def merge(arr, l, r):
        if l == r:
            return 
        mid = (r + l) // 2
        merge(arr, l, mid)
        merge(arr, mid + 1, r)
        merge_step(arr, l, mid + 1, r)
    l = 0
    r = len(arr) - 1
    merge(arr, l, r)
    return arr
    
    

print(merge_sort(arr))
