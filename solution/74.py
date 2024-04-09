def solution(n):
    dp = [0, 1, 2]

    for i in range(3, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % 1000000007)

    return dp[n]

print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(5))
print(solution(8))