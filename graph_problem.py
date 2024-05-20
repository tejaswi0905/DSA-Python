from collections import deque

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]



def number_of_regions(grid):
    regions = 0
    n = len(grid)
    m = len(grid[0])

    di = [0, 0, - 1, 1]
    dj = [1, -1, 0, 0]

    visited = set()

    def bfs(i, j, matrix, n, m, visited,di, dj):
        q = deque()
        q.append((i, j))
        while q:
            node = q.popleft()
            i = node[0]
            j = node[1]
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for k in range(4):
                ii = i + di[k]
                jj = j + dj[k]
                if (ii >= 0 and ii < n) and (jj >= 0 and jj < m) and matrix[ii][jj] == '1' and (ii, jj) not in visited:
                    q.append((ii, jj))
        
 
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and (i, j) not in visited:
                bfs(i, j, grid, n, m, visited,di, dj)
                regions += 1
    print(regions)
    
    

number_of_regions(grid)