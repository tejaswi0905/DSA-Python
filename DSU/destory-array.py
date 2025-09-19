import sys 
sys.setrecursionlimit(10 ** 6)

def test_case(n, arr, permu):
    active = [False] * n
    par = [i for i in range(n)]
    segment_sum = [arr[i] for i in range(n)]
    cur_max = 0
    res = []

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        segment_sum[px] += segment_sum[py]
        par[py] = px
    
    for i in permu:
        i = i - 1
        res.append(cur_max)
        active[i] = True
        if i > 0 and active[i - 1] == True:
            union(i, i - 1)
        if i + 1 < n and active[i + 1] == True:
            union(i,  i + 1)       
        root = i
        pr = find(root)
        cur_sum = segment_sum[pr]
        if cur_sum > cur_max:
            cur_max = cur_sum
    return res[::-1]
        

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    permu = list(map(int, input().split()))
    reversed_permu = reversed(permu)
    ans = test_case(n, arr, reversed_permu)
    for val in ans:
        print(val)
main()