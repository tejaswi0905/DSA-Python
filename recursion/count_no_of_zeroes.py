def zeroes(n):
    if n<10 and n!=0:
        return 0
    if n<10 and n==0:
        return 1
    last = n%10
    f = 0
    if last == 0:
        f = 1
    answer = f + zeroes(n//10)
    return answer

print(zeroes(3021409))