def solution(n, computers):
    ans = 0
    visited = [False] * n

    def dfs(nn, v, c):
        v[nn] = True
        for idx, connected in enumerate(c[nn]):
            if connected and not v[idx]:
                dfs(idx, v, c)

    for node in range(n):
        if not visited[node]:
            dfs(node, visited, computers)
            ans += 1

    return ans


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
