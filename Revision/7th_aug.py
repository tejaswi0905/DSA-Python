import math
def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]

print(eea(6, 15))

def solve_upto_n(a, b, c):
    g, xo, yo = eea(a, b)
    res = []
    if c % g != 0:
        return [(-1, -1)]
    xp = xo * (c // g)
    yp = yo * (c // g)

    for i in range(10):
        x = xp + (b // g) * i
        y = yp - (a // g) * i
        res.append((x, y))
    return res

print(solve_upto_n(6, 15, 12))

def mod_pow(a, b, m):
    if b == 0:
        return 1
    if b == 1:
        return a % m
    a = a % m
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res

print(mod_pow(2, 3, 100))

def phi_upto_n(n):
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] - phi[j] // i
    return phi
print(phi_upto_n(10))

def phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            res = res - res // i
        i += 1
    if n > 1:
        res = res - res // n
    return res
print(phi(10))

def power_tower(base_list, m):
    if m == 1:
        return base_list[0]
    if len(base_list) == 1:
        return base_list[0] % m
    
    phi_m = phi(m)
    exp = power_tower(base_list[1:], phi_m)

    base = base_list[0]
    if math.gcd(base, m) == 1:
        if exp < phi_m:
            return mod_pow(base, exp, m)
        else:
            return mod_pow(base, exp + phi_m, m)
    else:
        return mod_pow(base, exp, m)
print(power_tower([2, 3, 9], 100))