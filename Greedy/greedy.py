#coins scaler problem

def pow(a, b):
    ans = 1
    while b > 0:
        if (b & 1) == 1:
            ans = ans * a
        a = a * a
        b = b >> 1
    return ans

def largest_coin(amount):
    k = 0
    current = 1
    coin = 1
    while current <= amount:
        coin = current
        current = pow(5, k)
        k += 1
    return coin



def number_coins(A):
    count = 0
    while A > 0:
        print(A, end = ' ')
        lc = largest_coin(A)
        print(lc, end = ' ')
        A = A - lc
        print(A)
        count += 1
    return count

print(number_coins(3))

