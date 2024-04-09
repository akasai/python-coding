from collections import deque


def solution(n, wires):
    graph = {node: [] for node in range(n + 1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)

    def dfs(node):
        cnt = 1
        visited[node] = True

        for child in graph[node]:
            if not visited[child]:
                cnt += dfs(child)

        return cnt

    ans = float('inf')

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        cnt_a = dfs(a)
        cnt_b = n - cnt_a
        ans = min(ans, abs(cnt_a - cnt_b))

        graph[a].append(b)
        graph[b].append(a)
        visited = [False] * (n + 1)

    return ans


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
