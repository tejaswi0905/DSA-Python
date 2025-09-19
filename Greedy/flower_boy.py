def solve(a, b):
    n = len(a)
    m = len(b)

    p = [float('inf')] * m
    s = [float('inf')] * m

    i = 0
    j = 0
    while i < n and j < m:
        cur = b[j]
        if a[i] >= b[j]:
            p[j] = i
            i += 1
            j += 1
        else:
            i += 1
    ii = n - 1
    jj = m - 1
    while ii >= 0 and jj >= 0:
        if a[ii] >= b[jj]:
            s[jj] = ii
            ii -= 1
            jj -= 1
        else:
            ii -= 1
    print(p, s)
    answer = float("inf")
    if p[-1] != float('inf'):
        return 0
    for i in range(1, m - 1):
        if p[i - 1] < s[i + 1]:
            answer = min(answer, b[i])
    
    if s[1] != float("inf"):
        answer = min(answer, b[0])
    if p[m - 2] != float("inf"):
        answer = min(answer, b[m - 1])
    
    if answer == float("inf"):
        return -1
    
    return answer


def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print("the answre is ---- ", solve(a, b))
main()