from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

def print_adv(text, func, *args, **kwargs):
    print(text, end = ' ')
    result = func(*args, **kwargs)
    print(result)


def solve(n, a, b):
    h = defaultdict(list)
    for i in range(n):
        ai = a[i]
        bi = b[i]
        h[ai].append(bi)
    answer = 0
    for k in h:
        arr = h[k]
        if len(arr) < k:
            answer += sum(arr)
            continue
        arr.sort(reverse=True)
        for i in range(k):
            answer += arr[i]
    return answer
        

    


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            ai, bi = list(map(int, input().split()))
            a.append(ai)
            b.append(bi)
        # print_adv("The answer is ", solve, n, a, b)
        print(solve(n, a, b))


main()