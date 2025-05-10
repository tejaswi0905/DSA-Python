def longest_palindrome(s):
    def is_palindrome(string):
        l = 0
        r = len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
    n = len(s)
    dp = [[-1] * n for i in range(n)]
    l = 0
    r = n - 1
    for i in range(n - 1, -1 , -1):
        for j in range(n):
            if i < j:
                dp[i][j] = ""
                continue
            if i == j:
                dp[i][j] = s[l]
                continue
            if i + 1 == j:
                if s[i] == s[j]:
                    dp[i][j] = s[i: j + 1]
            if is_palindrome(s[i: j + 1]) == True:
                dp[i][j] = s[i: j + 1]
                continue
            if i < n - 1:
                pal1 = dp[i + 1][j]
            else:
                pal1 = ""
            if j > 0:
                pal2 = dp[i][j - 1]
            else:
                pal2 = ""
            if len(pal1) > len(pal2):
                dp[i][j] = pal1
            else:
                dp[i][j] = pal2
            
    # def rec(l, r):
    #     if l == r:
    #         return s[l]
    #     if (l + 1 == r):
    #         if s[l] == s[r]:
    #             return s[l:r + 1]
    #         return s[l]
    #     if dp[l][r] != -1:
    #         return dp[l][r]
    #     if is_palindrome(s[l: r + 1]) == True:
    #         dp[l][r] = s[l: r + 1]
    #         return s[l: r + 1]
    #     else:
    #         palindrome1 =  rec(l + 1, r)
    #         palindrome2 = rec(l, r - 1)
    #         if len(palindrome1) > len(palindrome2):
    #             dp[l][r] = palindrome1
    #             return palindrome1
    #         dp[l][r] = palindrome2
    #         return palindrome2
    # return rec(l, r)
    print(dp)
longest_palindrome("babab")