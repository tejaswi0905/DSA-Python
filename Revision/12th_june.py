# sieve algo
import math


def get_spf(n):
    nums = [i for i in range(n + 1)]
    for i in range(2, int(n**(0.5)) + 1):
        if nums[i] == i:
            for j in range(i*i, n + 1, i):
                nums[j] = i
    return nums


def facts_and_count(n):
    spf = get_spf(n)
    facts = {}
    while n > 1:
        count = 0
        p = spf[n]
        while n % p == 0:
            n = n // p
            count += 1
        facts[p] = count
    return facts


def get_primes(n):
    nums = [True for _ in range(n + 1)]
    primes = []
    for i in range(2, int(n**(0.5)) + 1):
        if nums[i] == True:
            for j in range(i * i, n + 1, i):
                nums[j] = False
    for i in range(2, n + 1):
        if nums[i]:
            primes.append(i)
    return primes


def count_of_p(n, p):
    count = 0
    prod = p
    while n >= prod:
        count += math.floor(n/prod)
        prod = prod * p
    return count


def primes_count_of_n_fact(n):
    primes = get_primes(n)
    primes_count = {}
    for p in primes:
        primes_count[p] = count_of_p(n, p)
    return primes_count


# The sieve style algo to find the number of factors of each number from 1 to n

def factors_count_upto(n):
    facts = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            facts[j] += 1
    return facts

# EEA, what does eea return, I don't know. But I am guessing, that for the equation ax + by = gcd(a, b), we are getting the solution using of x and y


def eea(a, b):  # gcd(a, b), x, y
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x - (a//b) * y1
    return [g, x, y]

# modular inverse of a and m, we need to find x such that (x * a)%m = 1, this only happens if gcd(a, m) == 1, finding mi using eea


def mi(a, m):
    def eea(a, b):
        if b == 0:
            return [a, 1, 0]
        g, x1, y1 = eea(b, a % b)
        x = y1
        y = x1 - (a//b)*y1
        return [g, x, y]
    g, x, _ = eea(a, m)
    if g != 1:
        return -1
    return x % m


def bin_pow(a, b, m):
    a = a % m
    if b == 0:
        return 1
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res % m * a % m) % m
        a = (a % m * a % m) % m
        b = b//2
    return res % m


def mi_flt(a, b):  # here b is prime, so mi will be a^b-2
    return bin_pow(a, b - 2, b)
