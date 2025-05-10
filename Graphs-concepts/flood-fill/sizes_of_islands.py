grid = [[1,1,0,0,1],
        [0,0,0,1,1],
        [0,1,0,0,0],
        [1,1,0,1,1],
        [1,1,0,0,1]]

def sizes_of_islands(grid):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    total_count = 0
    sizes = [0]

    def dfs(i, j, n, m, color_value):
        visited.add((i,j))
        grid[i][j] = color_value
        cur_size = 1

        for k in range(4):
            new_i = i + di[k]
            new_j = j + dj[k]

            if (new_i >= 0 and new_i < n) and (new_j >= 0 and new_j < m) and ((new_i, new_j) not in visited) and (grid[new_i][new_j] == 1):
                cur_size += dfs(new_i, new_j, n, m, color_value)
        return cur_size
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and grid[i][j] == 1:
                total_count += 1
                size = dfs(i, j, n, m, total_count)
                sizes.append(size)
    # for row in grid:
    #     print(row)
    return sizes

print(sizes_of_islands(grid))