def hitBricks(grid, hits):
    r, c = len(grid), len(grid[0])
    size = r * c
    TOP = size

    def get_id(i, j):
        return i * c + j
    
    par = [i for i in range(size + 1)]
    rank = [1] * (size + 1)
    sz = [1] * (size + 1)

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return 
        if rank[px] < rank[py]:
            px, py = py, px
        par[py] = px
        sz[px] += sz[py]
        if rank[px] == rank[py]:
            rank[px] += 1
    
    def top_size():
        return sz[find(TOP)]
        
    grid_copy = [row[:] for row in grid]
    for i, j in hits:
        if grid_copy[i][j] == 1:
            grid_copy[i][j] = 0
    for i in range(r):
        for j in range(c):
            if grid_copy[i][j] == 1:
                cur = get_id(i, j)
                if i == 0:
                    union(cur, TOP)
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ii = di + i
                    jj = dj + j
                    if ii >= 0 and ii < r and jj >= 0 and jj < c and grid_copy[ii][jj] == 1:
                        union(cur, get_id(ii, jj))
    ans = []
    for i, j in reversed(hits):
        if grid[i][j] == 0:
            ans.append(0)
            continue
        prev = top_size()
        grid_copy[i][j] = 1
        cur = get_id(i, j)
        if i == 0:
            union(cur, TOP)

        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ii = di + i
            jj = dj + j
            if ii >= 0 and ii < r and jj >= 0 and jj < c and grid_copy[ii][jj] == 1:
                union(cur, get_id(ii, jj))
        new = top_size()
        fallen = max(0, new - prev -1)
        ans.append(fallen)
    return ans[::-1]

grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
print(hitBricks(grid, hits))