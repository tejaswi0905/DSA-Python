import math

def k_factor(n, k):
    num = n
    MAXN = 100000 + 1
    spf = [i for i in range(MAXN + 1)]
    def pre_compute_spf():
        root = math.sqrt(MAXN)
        i = 2
        while (i <= int(root) + 1):
            if spf[i] == i:
                j = i * i
                while j < MAXN:
                    spf[j] = i
                    j += i
            i += 1
    pre_compute_spf()

    prod = 1
    answer_arr = []
    for _ in range(k - 1):
        n = n // spf[n]
        if n == 1:
            print(-1)
            return
        answer_arr.append(spf[n])
        prod *= spf[n]
    rem = num // prod
    answer_arr.append(rem)
    for num in answer_arr:
        print(num, end = ' ')

def main():
    n, k = map(int, input().split())
    k_factor(n, k)

main()
        