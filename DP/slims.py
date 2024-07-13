def slims(arr):
    n = len(arr)

    dp = [[-1] * n for i in range(n)]

    def rec(l, r):
        if (l>=r):
            return 0
        
        if (l + 1 == r):
            return arr[l] + arr[r]
        if dp[l][r] != -1:
            return dp[l][r]
        answer = float("inf")

        for mid in range(l + 1, r):
            answer = min(answer, rec(l, mid) + rec(mid + 1, r))
        dp[l][r] = answer
        return answer
    answer = rec(0, n - 1)
    for i in dp:
        print(i)
    return answer

arr = [7,6,8,6,1,1]
print(slims(arr))