# Tody I am writing some code and see if I remember how much.


def eea(a, b): # we are going to return the g, x and y
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b) # Now keep in mind that we need b, and a % b as the new arguments.
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]



def mod_pow(a, b, m):
    res = 1
    a = a % m
    while b > 0: # even if b == 1 we have to multiply "a" with "res", so we are using b > 0 in the while loop
        if b % 2 != 0:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res

