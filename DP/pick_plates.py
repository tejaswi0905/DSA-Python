# This is my solution and this question is asked in google hacker earth competition. There can be an improvement that is 
# we can use a prefix sum array of each row instead of using the num_of_points function.


def pick_plates(plates, max_num):
    n = len(plates)
    m = len(plates[0])

    dp = [[-1 for i in range(max_num + 1)] for i in range(n)]

    def num_of_points(arr, k):
        answer = 0
        for i in range(k):
            answer += arr[i]
        return answer    

    def rec(level,left):
        if level < 0:
            return 0
        if dp[level][left] != -1:
            return dp[level][left]
        answer = float("-inf")
        for i in range(m + 1):
            if left - i >= 0:
                if i == 0:
                    answer = max(answer, rec(level - 1,left))
                else:
                    answer = max(answer, rec(level - 1,left - i) + num_of_points(plates[level], i))
        dp[level][left] = answer
        return answer
    return rec(n - 1,max_num)

plates = [[80,80],[15,50],[20,10]]
print(pick_plates(plates, 6))