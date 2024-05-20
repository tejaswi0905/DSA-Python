#given any number n print its factorial. 1<= n <= 100
#since the value of the factorial can be very high, we need to modulo it to some number, here let us do with 47
#so every value will be less than or equal to 46
def main(n):
    answer = 1
    for i in range(2, n + 1):
        answer =( answer * i) % 47
        answer = answer % 47
    return answer

def binExpRecr(a, b, M):
    if b == 0:
        return 1
    res = binExpRecr(a, b // 2, M)
    if (b&1) == 1:
        return (a * res * res) % M
    else:
        return (res * res) % M

def binExpIter(a, b, M):
    answer = 1
    while b > 0:
        if (b&1) == 1:
            answer = (answer * a) % M
        a = (a * a) % M
        b = b >> 1
    return answer % M

M = 10 **9 + 7
print(binExpIter(4,5,M))
print(binExpRecr(4,5, M))
