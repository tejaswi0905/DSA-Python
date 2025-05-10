import math

def reverse(n):
    if n<10:
        return n
    answer = (n%10) * (10**(math.floor(math.log10(n)))) + reverse(n//10)
    # print(answer)
    return answer

print(reverse(1824))

