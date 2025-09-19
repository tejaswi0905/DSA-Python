#lets get the math first.
def eed(a, b): # This will return us the g, x and y for the equation ax + by = gcd(a, b)
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eed(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]


def phi_upto_n(n):
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] - phi[j] // i
    return phi

print(phi_upto_n(9))

def phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            res = res - res//i
        i += 1
    if n > 1:
        res = res - res // n
    return res


def mod_pow(a, b, mod):
    res = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b = b // 2
    return res

import math
def power_tower(base_list, m):
    if m == 1:
        return 0
    if len(base_list) == 1:
        return base_list[0] % m

    phi_m = phi(m)
    exp = power_tower(base_list[1:], phi_m)

    base = base_list[0]
    if math.gcd(base, m) == 1:
        return mod_pow(base, exp if exp < phi_m else exp + phi_m, m)
    else:
        # Safeguard: If the reduced exponent is too small, "lift" it manually
        return mod_pow(base, exp + phi_m, m)

def get_range(a, b):
    g = math.gcd(a,b)
    count = math.floor(b/g)
    res = []
    for i in range(count):
        res.append(g * i)
    return res

print(get_range(4, 8))

