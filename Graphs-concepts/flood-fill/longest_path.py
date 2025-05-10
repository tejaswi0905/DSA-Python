matrix = [[7,8,9],[9,7,6],[7,2,3]]

def longestIncreasingPath(matrix):
    n = len(matrix)
    m = len(matrix[0])

    answer = 0
    dk = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(visited, i, j):
        cur_len = 0
        val = matrix[i][j]
        visited.add((i, j))

        for k in dk:
            di = k[0]
            dj = k[1]

            ii = i + di
            jj = j + dj

            if (ii >= 0 and ii < n) and (jj >= 0 and jj < m) and matrix[ii][jj] > val and (ii, jj) not in visited:
                cur_len = max(cur_len, dfs(visited, ii, jj))
                if (ii == 1 and jj == 1):
                    print("cur_len of 1, 1 is", cur_len)
                
        return 1 + cur_len
    # print(matrix[1][2])
    print("start 1, 2", dfs(set(), 1, 2))
    print("start 1, 1", dfs(set(), 1, 1))

    # for i in range(n):
    #     for j in range(m):
    #         val = dfs(set(), i, j)
    #         answer = max(answer, val)
    # return answer

longestIncreasingPath(matrix)