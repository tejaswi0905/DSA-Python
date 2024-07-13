def solve_rec_form1(n, A, B, C):
    dp = [[-1] * 3 for i in range(n)]

    def rec(level, last):
        if level >= n:
            return 0
        
        if (last != -1 and dp[level][last] != -1):
            return dp[level][last]
        
        answer = 0
        for i in range(3):
            if i == last:
                continue
            if i == 0:
                answer = max(answer, rec(level + 1, 0) + A[level])
            if i == 1:
                answer = max(answer, rec(level + 1, 1) + B[level])
            if i == 2:
                answer = max(answer, rec(level + 1, 2) + C[level])
        if last == -1:
            return answer
        dp[level][last] = answer
        return answer
    answer = rec(0, -1)
    print(dp)
    return answer

def solve_iter_form1(n, A, B, C):
    dp = [[0] * 3 for i in range(n)]
    
    for i in range(3):
        if i == 0:
            dp[n - 1][i] = A[n - 1]
        if i == 1:
            dp[n - 1][i] = B[n - 1]
        if i == 2:
            dp[n - 1][i] = C[n - 1]
    
    for level in range(n-2, -1, -1):
        for task in range(3):
            answer = 0
            for j in range(3):
                if j == task:
                    continue
                if j == 0:
                    answer = max(answer, dp[level + 1][0] + A[level])
                if j == 1:
                    answer = max(answer, dp[level + 1][1] + B[level])
                if j == 2:
                    answer = max(answer, dp[level + 1][2] + C[level])
            dp[level][task] = answer
    print(dp[0])




def solve_rec_form2(n, A, B, C):
    dp = [[-1] * 3 for i in range(n)]
    def rec(level, task):
        
        if level < 0:
            return 0
        
        if level == 0:
            if task == 0:
                return A[0]
            if task == 1:
                return B[0]
            if task == 2:
                return C[0]
        if dp[level][task] != -1:
            return dp[level][task]
        
        answer = 0
        if task == 0:
            answer = max(answer, rec(level - 1, 1), rec(level - 1, 2)) + A[level]
        if task == 1:
            answer = max(answer, rec(level - 1, 0), rec(level - 1, 2)) + B[level]
        if task == 2:
            answer = max(answer, rec(level - 1, 0), rec(level - 1, 1)) + C[level]
        dp[level][task] = answer
        return answer
    
    return max(rec(n-1, 0), rec(n-1, 1), rec(n - 1, 2))

def solve_iter_form2(n, A, B, C):
    dp = [[0] * 3 for i in range(n)]

    for i in range(3):
        if i == 0:
            dp[0][i] = A[0]
        if i == 1:
            dp[0][i] = B[0]
        if i == 2:
            dp[0][i] = C[0]



    for level in range(1, n):
        for last in range(3):
            answer = 0
            if last == 0:
                answer = max(answer, dp[level - 1][1], dp[level - 1][2]) + A[level]
            if last == 1:
                answer = max(answer, dp[level - 1][0], dp[level - 1][2]) + B[level]
            if last == 2:
                answer = max(answer, dp[level - 1][0], dp[level - 1][1]) + C[level]
            
            dp[level][last] = answer
    return max(dp[n-1])

A = [6,8,2,7,4,2,7]
B = [7,8,5,8,6,3,5]
C = [8,3,2,6,8,4,1]

# print(solve_iter_form1(7, A, B, C))



print(solve_rec_form1(7, A, B, C))
# print(solve_iter_form2(7, A, B, C))
# print(solve_rec_form2(7, A, B, C))