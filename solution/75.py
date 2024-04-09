def solution(triangle):
    N = len(triangle)
    dp = [triangle[-1]]

    for i in range(N - 2, -1, -1):
        M = len(triangle[i])
        dp.append([0] * M)
        for j in range(M):
            dp[(N - 1) - i][j] = triangle[i][j] + max(dp[(N - 2) - i][j:j + 2])
    return dp[-1][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
