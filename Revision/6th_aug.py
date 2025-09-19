# starting with the primes and gcd
from math import gcd, floor
def num_of_factors_upto_n(n):
    facts = [1 for i in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            facts[j] += 1
    return facts

print(num_of_factors_upto_n(10))

def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]



def get_ten_soluton_pairs(a, b, c):
    g, xo, yo = eea(a, b)
    if c % g != 0:
        return [(-1, -1)]
    xp = xo * (c // g)
    yp = yo * (c // g)
    answer = []
    for i in range(1, 11):
        x = xp + (b // g) * i
        y = yp - (a // g) * i
        answer.append((x, y))
    return answer
print(get_ten_soluton_pairs(6, 15, 12))

def get_rem_range(a, b):
    g = gcd(a, b)
    total = floor(b/g)
    res = []
    for i in range(total):
        res.append(g * i)
    return res
print(get_rem_range(18, 4))

def mod_inv_with_eea(a, m):
    g, x, y = eea(a, m)
    if g != 1:
        return -1
    return x % m
print(mod_inv_with_eea(3, 7))

def mod_pow(a, b, m):
    if b == 0:
        return 1
    if b == 1:
        return a % m
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res
def mod_inv_with_flt(a, m):
    if gcd(a, m) != 1:
        return -1
    return mod_pow(a, m - 2, m)
print(mod_inv_with_flt(3, 7))

def phi_upto_n(n):
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] - phi[j] // i
    return phi
print(phi_upto_n(10))

def phi_of_n(n):
    i = 2
    res = n
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            res = res - res // i
        i += 1
    if n > 1:
        res = res - res // n
    return res
print(phi_of_n(9))

            