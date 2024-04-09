from heapq import heappush, heappop


def solution(land, height):
    ans = 0
    N = len(land)

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * N for _ in range(N)]
    q = []

    heappush(q, (0, 0, 0))

    def is_valid(xx, yy):
        return 0 <= xx < N and 0 <= yy < N

    while q:
        cost, x, y = heappop(q)

        if visited[x][y]:
            continue

        visited[x][y] = True
        ans += cost

        for i in range(4):
            dx, dy = move[i]
            nx, ny = x + dx, y + dy

            if not is_valid(nx, ny):
                continue

            new_cost = abs(land[x][y] - land[nx][ny])
            heappush(q, (new_cost if new_cost > height else 0, nx, ny))

    return ans


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))  # 15
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))  # 18
