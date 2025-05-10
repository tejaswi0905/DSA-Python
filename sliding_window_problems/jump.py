def canReach(s, minJump, maxJump):
        n = len(s)
        dp = [-1] * n
        dp[0] = True

        for idx in range(1, n):
            if s[idx] == "1":
                dp[idx] = False
                continue

            answer = False
            startIdx = idx - maxJump
            endIdx = idx - minJump

            if startIdx <= 0:
                 for j in range(idx):
                      answer = answer or dp[j]
            else:
                for j in range(startIdx, endIdx + 1):
                    answer = answer or dp[j]
            dp[idx] = answer
        print(dp)
        return dp[n - 1]

print(canReach("01101110", 2, 3))