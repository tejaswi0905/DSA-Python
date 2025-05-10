def min_steps(num):
    count = [0]
    # dp = [-1] * (num + 1)

    # dp[1] = 1
    # dp[2] = 1
    # dp[3] = 1

    def rec(i):
        count[0] += 1
        if i == 1:
            return 0
        
        # if dp[i] != -1:
        #     return dp[i]       

        steps = float("inf")

        if i > 1:
            steps = min(steps, 1 + rec(i - 1))
        if i % 2 == 0:
            steps = min(steps, 1 + rec(i // 2))
        if i % 3 == 0:
            steps = min(steps, 1 + rec(i // 3))
        # dp[i] = steps
        return steps
    answer = rec(num)
    print("number of calls--",count[0])
    return answer

print(min_steps(311))