def solve(n, arr):
    i, j, k = None, None, None
    
    for ii in range(n):
        if arr[ii] == 1:
            i = ii
            continue
        if arr[ii] == 2:
            j = ii
            continue
        if arr[ii] == n:
            k = ii
    
    if i < k < j or j < k < i:
        return k, k - 1
    
    return i, k
            

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        answer = solve(n, arr)
        for ans in answer:
            print(ans, end = ' ')
        print()
main()