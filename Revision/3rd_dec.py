'''
Docstring for Revision.3rd_dec
1) We go through the graph and assign the least_time and discovered_time to each node, and add those nodes to the stack
2) When we are poping a node(or the dfs call for that node), we check if the lt[node] == dt[node] if so keep popping the stack until we get to the node, and those nodes that got popped does belong to one scc

stack = []
sccs = [[5], [4], [1, 2, 3]]

 1(1)1
   |  ^
   |   \
   v    \
 2(2)1->3(3)1-->4(4)4
             |
             |
             v
            5(5)5
'''

from collections import defaultdict

def compute_sieve(n):
    arr =[True] * (n + 1)
    primes = []
    for i in range(2, int(n**(0.5)) + 1):
        if arr[i] == True:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                arr[j] = False
    for i in range(int(n**(0.5)) + 1, n + 1):
        if arr[i] == True:
            primes.append(i)
    return primes

def prime_factors_of_n_factorial(n):
    primes = compute_sieve(n)
    facts = defaultdict(int)
    for p in primes:
        power = p
        count = 0
        while power <= n:
            count += (n//power)
            power *= p
        facts[p] = count
    return facts

def prime_factors_of_n(n):
    facts = defaultdict(int)
    i = 2
    while n > 1:
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count > 0:
            facts[i] = count
        i += 1
    return facts

def sum_of_factors(n):
    facts = prime_factors_of_n(n)
    print(facts)
    def formula(n, r):
        numerator = ((r**(n + 1)) - 1)
        denom = r - 1
        return numerator // denom
    answer = 1
    for p in facts:
        v = facts[p]
        contribution = formula(v, p)
        answer *= contribution
    return answer

        

def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a//b) * y1
    return [g, x, y]

def modulo_inverse_with_eea(a, m):
    g, x, y = eea(a, m)
    if g != 1:
        return -1
    return (x % m) # sometimes it can go negitive, so we have to mod it with m.


def mod_pow(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if (b % 2) == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res


def modulo_inverse_with_flt(a, m):
    #Here the assumption is that m is prime
    x = mod_pow(a, m - 2, m)
    return x

print(modulo_inverse_with_eea(3, 7), modulo_inverse_with_flt(3, 7))


def phi(n):
    res = n
    i = 2
    while i * i <= n:
        if (n  % i) == 0:
            while n % i == 0:
                n = n // i
            res = res - res // i
        i += 1
    if n > 1:
        res = res - res//n
    return res

def phi_upto_n(n):
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] - phi[j]//i
    return phi

print(phi(12), phi_upto_n(12))
