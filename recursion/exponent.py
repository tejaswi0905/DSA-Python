def exp_iter(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res


def exp_rec(a, n):
    memo = [-1] * (n + 1)
    memo[0] = 1

    def rec(a, n):
        if (n == 0):
            return 1
        if (n == 1):
            return a
        if memo[n] != -1:
            return memo[n]
        if (n % 2) == 0:
            res = rec(a, n//2) * rec(a, n//2)
        if (n % 2) == 1:
            res = rec(a, n//2) * rec(a, n//2) * a
        memo[n] = res
        return res
    rec(a, n)
    return memo[-1]

        