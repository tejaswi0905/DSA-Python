def compute_phi(n):
    phi = [i for i in range(n+1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] - phi[j] // i
    return phi


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
        res = res - res//n
    return res



def modular_pow(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res

def power_tower(base_list, m):
    if m == 1:
        return 0
    if len(base_list) == 1:
        return base_list[0] % m
    phi_m = phi(m)
    reduced_exp = power_tower(base_list[1:], phi_m)
    return modular_pow(base_list[0], reduced_exp, m)

print("The answer for 2, 3, 2, mod 5 is ", power_tower([2, 3, 2], 5))


def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return [g, x, y]

print(eea(4, 10))

