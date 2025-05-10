def grid_fall(grid):
    if len(grid) == 1:
        return min(grid[0])
    n = len(grid)
    dp = [[-100] * n for i in range(n)]

    def rec(i, j):
        if (i < 0):
            return 0
        if i == 0:
            return grid[i][j]
        
        answer = float("inf")
        for col_idx in range(n):
            if col_idx == j:
                continue
            answer = min(answer, rec(i - 1, col_idx))
        return answer + grid[i][j]
    answer = float("inf")
    for col_idx in range(n):
        answer = min(answer, rec(n - 1, col_idx))
    return answer
grid = [[1,2,3],[4,5,6],[7,8,9]]
print(grid_fall(grid)) 