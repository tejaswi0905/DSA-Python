# I am going to write the spf, 
# prime factorization of one number and then from 1 to n, 
# after that I am going to write code to find out the number of times a prime number comes in the prime factorization of n!, 
# Then how many times a number comes in the n(n - 2)(n - 4)...

from collections import defaultdict

n = 100
spf = [i for i in range(n + 1)]
for i in range(2, int(n ** (0.5)) + 1):
    if spf[i] == i:
        for j in range(i * i, n + 1, i):
            if spf[j] == j:
                spf[j] = i

# print([(i, spf[i]) for i in range(2, n + 1)])

def prime_factorization(n):
    num = n
    i = 2
    pf = defaultdict(int)
    while num > 1:
        while (num % i == 0):
            pf[i] += 1
            num = num // i
        i += 1
    return pf

# print(prime_factorization(36))

def number_of_p_in_n_factorial(n, p):
   count = 0
   power = p
   while n >= power:
       count += (n//power)
       power = power * p 
   return count
print(number_of_p_in_n_factorial(10, 2))

