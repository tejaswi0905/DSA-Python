from collections import defaultdict

def swimInWater(grid):
    n = len(grid)
    start = grid[0][0]
    end = grid[n - 1][n - 1]
    is_active = defaultdict(bool)
    val_to_idx = defaultdict(tuple)
    for i in range(n):
        for j in range(n):
            val_to_idx[grid[i][j]] = (i,j)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    par = [i for i in range(n**2)]


    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        par[py] = px
        return True
    

    for i in range(n**2):
        cur_level = i
        x, y = val_to_idx[i]
        is_active[(x, y)] = True
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if is_active[(xx, yy)]:
                neighbour_val = grid[xx][yy]
                union(neighbour_val, cur_level)
        if find(start) == find(end):
            return cur_level
    return -1
