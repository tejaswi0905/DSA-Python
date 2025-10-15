def solve(n, a, b):
    c = [None] * (2 * n)
    j = 0
    for i in range(n):
        c[j] = a[i]
        j += 1
        c[j] = b[i]
        j += 1
    
    c.sort()
    answer = 0
    l = 0
    for r in range(1, len(c)):
        cur = c[r]
        while cur != c[l] and r > l:
            l += 1
        answer = max(answer, (r - l) + 1)
    return answer
            
        
            
    


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solve(n, a, b)
main()
