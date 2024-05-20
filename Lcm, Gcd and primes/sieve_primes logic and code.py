import math


def primes(n):
    primes_array = [True] * (n + 1)
    primes_array[0], primes_array[1] = False, False
    root = math.sqrt(n)

    i = 2
    while (i < int(root) + 1):
        if primes_array[i] == True:
            j = i * i
            while (j < n + 1):
                primes_array[j] = False
                j += i
        i += 1
    return primes_array

first_hundred_primes = primes(100)
# for i in range(len(first_hundred_primes)):
#     print(i, first_hundred_primes[i], end = ' ')

def spf(n):
    spf_array = [i for i in range(n + 1)]
    i = 2
    root = math.sqrt(n)
    while ( i <= int(root) + 1):
        if spf_array[i] == i:
            j = i * i
            while j < (n + 1):
                if spf_array[j] == j:
                    spf_array[j] = i
                j += i
        i += 1
    return spf_array

# spf_array = spf(100)
# for i in range(len(spf_array)):
#     print(f"({i}, {spf_array[i]})", end = ' ')


def hpf(n):
    hpf_array = [i for i in range(n + 1)]
    i = 2
    root = math.sqrt(n)

    while (i <= int(root) + 1):
        if hpf_array[i] == i:
            j = 2 * i
            while (j < n + 1):
                hpf_array[j] = i
                j += i
        i += 1
    return hpf_array

# hpf_array = hpf(100)
# for i in range(len(hpf_array)):
#     print(f"({i}, {hpf_array[i]})", end = ' ')


def prime_factors(n):
    spf_array = spf(n)
    prime_factor_map = {}
    while (n > 1):
        prime = spf_array[n]
        prime_factor_map[prime] = 0
        while n % prime == 0:
            prime_factor_map[prime] += 1
            n = n // prime
    return prime_factor_map
# print(prime_factors(36))

def sum_of_all_factors(n):
    prime_factors_map = prime_factors(n)
    total = 1
    for key in prime_factors_map.keys():
        a = 1
        r = key
        n = prime_factors_map[key] + 1
        numerator = a * ((r ** n) - 1)
        denominator = r - 1
        contribution = numerator // denominator
        total *= contribution
    return total
print(sum_of_all_factors(66))

def sum_of_all_factors_iter(n):
    root = math.sqrt(n)
    total = 0
    if root.is_integer():
        total = total - int(root)
    for i in range(1, int(root) + 1):
        if n % i == 0:
            total += i
            total += n // i
    return total

print(sum_of_all_factors_iter(66))

