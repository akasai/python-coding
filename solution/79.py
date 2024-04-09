def solution(strs, t):
    N = len(t)
    dp = [float('inf')] * (N + 1)
    sizes = set(len(s) for s in strs)

    dp[0] = 0
    for i in range(1, N + 1):
        for size in sizes:
            if i - size >= 0 and t[i - size:i] in strs:
                dp[i] = min(dp[i], dp[i - size] + 1)

    return dp[N] if dp[N] < float('inf') else -1

print(solution(['ba', 'na', 'n', 'a'], 'banana'))  # 3
# print(solution(['app', 'ap', 'p', 'l', 'e', 'ple', 'pp'], 'apple'))  # 2
# print(solution(['ba', 'an', 'nan', 'ban', 'n'], 'banana'))  # -1
