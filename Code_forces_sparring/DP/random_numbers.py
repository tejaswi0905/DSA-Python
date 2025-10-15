import sys
sys.setrecursionlimit(300000)

val = [1, 10, 100, 1000, 10000]

def solve(in_idx, mx, changed, s, dp):
    if in_idx == 0:  # base case: leftmost character done
        return 0

    if dp[in_idx][mx][changed] != -1:
        return dp[in_idx][mx][changed]

    cur_val = ord(s[in_idx]) - ord('A')

    # ✅ Option 1: Don't change this character
    sign = 1
    if cur_val < mx:
        sign = -1
    res = sign * val[cur_val] + solve(in_idx - 1, max(mx, cur_val), changed, s, dp)

    # ✅ Option 2: If not changed yet, try changing this character to any of the 4 others
    if changed == 0:
        for i in range(5):  # possible new character
            if i != cur_val:
                sign = 1
                if i < mx:
                    sign = -1
                res = max(res, sign * val[i] + solve(in_idx - 1, max(mx, i), 1, s, dp))

    dp[in_idx][mx][changed] = res
    return res


# Driver
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    n = len(s)
    # dp[index][max_seen][changed]
    dp = [[[-1 for _ in range(2)] for _ in range(7)] for _ in range(n + 1)]

    ans = solve(n - 1, 0, 0, s, dp)
    print(ans)
