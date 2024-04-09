def printArr(m):
    for n in m:
        print(n)
    print()


def solution(str1, str2):
    N, M = len(str1), len(str2)
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[M][N]


print(solution("abcbdab", "bdcab"))
print(solution("aggtab", "gxtxayb"))
