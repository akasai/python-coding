def solution(k, ds):
    N = len(ds)
    v = [False] * N

    def dfs(ck, cnt):
        ans = cnt
        for i in range(N):
            n, u = ds[i]
            if ck >= n and not v[i]:
                v[i] = True
                ans = max(ans, dfs(ck - u, cnt + 1))
                v[i] = False
        return ans

    return dfs(k, 0)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3
