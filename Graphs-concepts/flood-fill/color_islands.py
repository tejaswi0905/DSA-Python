grid = [[1,1,0,0,1],
        [0,0,0,1,1],
        [0,1,0,0,0],
        [1,1,0,1,1],
        [1,1,0,0,1]]


def color_islands(grid):
    n = len(grid)
    m = len(grid[0])
    total_count = 0
    di = [1, -1, 0, 1]
    dj = [0, 0, 1, -1]
    visited = set()

    def dfs(i, j, n, m, color_val):
        visited.add((i, j))
        grid[i][j] = color_val

        for k in range(4):
            new_i = di[k] + i
            new_j = dj[k] + j

            if (new_i >= 0 and new_i < n) and (new_j >=  0 and new_j < m) and (grid[new_i][new_j] == 1) and ((new_i, new_j) not in visited):
                dfs(new_i, new_j, n, m, color_val)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and ((i, j) not in visited):
                total_count += 1
                dfs(i, j, n, m, total_count)
    for row in grid:
        print(row)


color_islands(grid)



