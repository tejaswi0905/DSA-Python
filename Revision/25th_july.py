from collections import defaultdict

def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]

def p_in_n(n):
    spf = [i for i in range(n + 1)]
    spf[0], spf[1] = -1, -1
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                spf[j] = i
    def p_count(p, n):
        power = p
        count = 0
        while power <= n:
            count += n // power
            power = power * p
        return count
        
    primes = defaultdict(int)
    for p in range(2, n + 1):
        if spf[p] == p:
            c = p_count(p, n)
            primes[p] = c
    return primes

def num_of_factors(n):
    res = [1 for i in range(n + 1)]
    
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            res[j] += 1
    return res

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

def phi_upto_n(n):
    res = [i for i in range(n + 1)]
    