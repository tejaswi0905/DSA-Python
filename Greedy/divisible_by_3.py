def solve(s):
    n = len(s)
    dp = [0] * (n + 1)  


    def is_valid_and_divisible(l, r):
        substr = s[l:r+1]
        if len(substr) > 1 and substr[0] == '0':
            return False

        return int(substr) % 3 == 0

    for i in range(1, n + 1):  
        dp[i] = dp[i-1]  
        for j in range(i):
            if is_valid_and_divisible(j, i-1):
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[n]

def main():
    s = input()
    print(solve(s))
main()