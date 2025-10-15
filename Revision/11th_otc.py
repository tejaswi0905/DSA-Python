'''
if m and n are realitve prime then the largest number we can't make from mx + ny (where x and y are ints) is m * n - (m + n) and the count of numbers we are going to miss are (m - 1) * (n - 1) // 2. This is called chicken nugget theroem.

F stands for fib, and Fx + F(x1) + F(x2) + F(x3) + .... + F(xn) = F(xn2) - F(x1) 
example is F4 + F5 + F6 + F7 + .... + F10 is ?. Here n = 10 and xn2 = F12 and x1 = 5 so the answer is F12 - F5
If a number x is fib or not, the check is simple, if 5x^2 - 4 or 5x^2 + 4, if either of them is a perfect square then the number x is a fib number.

The number of prime factors in n! is very simple, the count of each prime is 
count_of_p = floor(n / p) + floor(n / p^2) + floor(n / p^3) + .... + 0

now (n * a) % b is going to return a pattern. The pattern have b//g number of elements in them, and the first one is 0 and last one (b//g - 1) * g, and the pattern looks like 0, g, 2g, 3g, ..., (b//g - 1) * g

so if a = 4 and b = 12 then we are looking for (n * 4) % 12, g = gcd(4, 12) == 3, so the number of elements in the pattern are 
b // g = 12 // 4 = 3, and the last element is (b // g - 1) * g == (3 - 1) * 4 = 8, so the pattern is going to be 0, 4, and 8.

'''

from collections import defaultdict
import math

def get_spf(n):
    spf = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                spf[j] = i
    return spf

def get_prime_factors_of_n(n):
    p = defaultdict(int)
    num = n
    i = 2
    while num > 1:
        while num % i == 0:
            p[i] += 1
            num = num // i
        i += 1
    return p

def get_num_of_factors_of_n(n):
    num = n
    i = 2
    res = 1
    while num > 1:
        count = 0
        while num % i == 0:
            count += 1
            num = num // i
        if count > 0:
            res = res * (count + 1)
        i += 1
        
    return res


def get_hpf(n):
    hpf = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if hpf[i] == i:
            for j in range(2 * i, n + 1, i):
                hpf[j] = i
    return hpf

# def get_both(n):
#     spf = [i for i in range(n + 1)]
#     hpf = [i for i in range(n + 1)]

#     for i in range(2, n + 1):
#         if 


# I need a way to find out the count of factors of all the numbers from 1 to n.
def get_factors(n):
    factors = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            factors[j] += 1
    return factors

def get_factors_of_n_factorial(n):
    primes = [True for _ in range(n + 1)]
    p = defaultdict(int)
    for i in range(2, int((n + 1) ** (0.5)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    for i, val in enumerate(primes):
        if i <= 1:
            continue
        if val:
            count = 0
            power = i
            while n >= power:
                count += math.floor(n/power)
                power = power * i
            p[i] = count
    return p


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]


def get_all(a, b):
    g = math.gcd(a, b)
    res = []
    count = math.floor(b/g)
    for i in range(count):
        res.append(i * g)

    return res


def modulo_inverse_eea(a, m):
    '''we are trying to find the modulo inverse of a and m. If gcd(a, m) == 1. Then we are going to find a number x such that 
    (a * x) % m == 1. We can do this with our eea, just take the equation  a * x + b * m = 1, now mod both sides with m
    then we get (a * x + b * y) % m = 1 % m and the lhs will be ((a * x) % m + (m * y) % m) = 1, since (m * y) % m = 0 so the equation will become (a * x) % m = 1.
    '''
    g, x, y = eea(a, m)
    if g != 1:
        return -1
    return x % m

def mod_pow(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res



def modulo_inverse_flt(a, m):
    '''This only works if m is prime, flt says that if p is prime, then a^(p - 1) % p == 1, Here "a" can be any number, and p must be a prime.
    a^(p - 1) = a^(p - 2) * a, now mod both sides with p, then we get (a^(p - 1)) % p = (a^(p - 2) * a) % p
    now if we write a^(p - 2) as x, then we get (x * a) % p = 1. (since according to flt a^(p - 1) % p == 1)
    Hence the modulo inverse of a % p is a^(p - 2)
    '''
    return mod_pow(a, m - 2, m)

print(modulo_inverse_eea(3, 7))
print(modulo_inverse_flt(3, 7))

'''
The toient function, this gives the count of co-prime of a number from 1 to n. The function represents as phi(n)
The foumula is let the prime factorization of a number n be n = p1**e1 * p2**e2...* pk^ek, then 
phi(n) = n*(1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)
'''

def phi_upto_n(n):
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] - phi[j]//i
    return phi



def phi_of_n(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            res = res - res // i 
        i += 1
    if n > 1: #This means n is a prime number, then we do this.
        res = res - res // n
    return res


# from now graphs and trees. First and foremost master segment trees.

'''
Rooting a tree is very simple, We have a tree class with node, and other infor like children array etc etc, and then we recursively go to each node and then call the rec fun on each child to build its sub-trees and then append that child to our current node. Each node can have a prent pointer

'''

edges = [[3, 2], [2, 0], [0, 1], [0, 5], [4, 5], [6, 5]]

def build_graph(n, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g

class Node:
    def __init__(self, id, par_id, children):
        self.id = id
        self.par_id = par_id
        self.children = []


def buildTree(g, node, parent):
    for ch_id in g[node.id]:
        if parent != None and ch_id == parent.id:
            continue
        ch_node = Node(ch_id, node.id, [])
        buildTree(g, ch_node, node)
        node.children.append(ch_node)
    return node

def rootTree(n, edges, rootId = 0):
    g = build_graph(n, edges)
    rootNode = Node(rootId, None, [])
    new_root = buildTree(g, rootNode, None)
    return new_root

def treversal_rooted_tree(rootNode):
    answer = []
    def dfs(node):
        if len(node.children) == 0:
            answer.append(node.id)
            return 
        answer.append(node.id)
        for ch_node in node.children:
            dfs(ch_node)
    dfs(rootNode)
    return answer

rootNode = rootTree(7, edges, 0)
print(treversal_rooted_tree(rootNode))

