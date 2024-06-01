#The logic of gcd is simple, the greatest factor of the 2 numbers.

def gcd(a, b):
    num1 = a    
    num2 = b    
    while num2 != 0:
        if num1 < num2:   
            num1, num2 = num2, num1
            continue
        num1 = num1 - num2
    return num1

result = gcd(47, 7)
print(result)

def gcd_modulo(a, b):
    num1 = a
    num2 = b
    while num2 != 0:
        hold = num2
        num2 = num1 % num2
        num1 = hold
    return num1
print(gcd_modulo(47, 7))

"""
the logic here follows:
12)30(2
   24
   6)12(2
     12
     0 => here when the reminder is 0, the current divisor is our greatest common divisor.
     And this process is repeated till we get the reminder as 0.
"""

