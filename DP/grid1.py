def grid1(h, w, grid):
    dp = [[-1] * w for i in range(h)]

    def rec(i, j):
        if (i == 0 and j == 0):
            return 1
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        answer = 0
        if (i > 0):
            if grid[i - 1][j] != "#":
                answer += rec(i - 1, j)
        if (j > 0):
            if grid[i][j - 1] != "#":
                answer += rec(i, j - 1)
        dp[i][j] = answer
        return answer
    return rec(h-1, w-1)

# grid = [[".", ".", ".", "#"], [".", "#", ".", "."], [".", ".", ".", "."]]

grid = [[".", ".", "#", ".", "."], [".", ".", ".", ".", "."], ["#", ".", ".", ".", "#"], [".", ".", ".", ".", "."],[".", ".", "#", ".", "."]]

print(grid1(5, 5, grid))