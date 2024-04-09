from collections import deque


def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])

    dist = [[-1] * m for _ in range(n)]

    def is_not_valid(p, t):
        return 0 > p or p >= t

    def dfs(x, y):
        q = deque([(x, y)])
        dist[x][y] = 1

        while q:
            nx, ny = q.popleft()
            for i in range(4):
                ox, oy = nx + dx[i], ny + dy[i]

                if is_not_valid(ox, n) or is_not_valid(oy, n):  # 좌표 벗어나면
                    continue
                if maps[ox][oy] == 0:  # 벽이면
                    continue

                if dist[ox][oy] == -1:
                    dist[ox][oy] = dist[nx][ny] + 1
                    q.append((ox, oy))

        return dist

    dfs(0, 0)
    return dist[n - 1][m - 1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
