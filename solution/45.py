def solution(board):
    N = len(board)
    # move = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 0: 좌 / 1: 우 / 2: 위 / 3: 아래
    move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]

    q = [((0, 0), 0, -1)]  # 좌표, 코스트

    ans = float('inf')

    '''
    시작점, 구역 안, 벽
    '''

    def is_blocked(px, py):
        return (px, py) == (0, 0) or not (0 <= px < N and 0 <= py < N) or board[px][py] == 1

    def get_cost(d, pd):
        # 처음이거나,
        return 100 if pd == -1 or (pd - d) % 2 == 0 else 600

    while q:
        (x, y), cost, prev_direction = q.pop(0)

        for direction in range(4):
            (dx, dy) = move[direction]
            nx, ny = x + dx, y + dy

            if is_blocked(nx, ny):
                continue

            new_cost = cost + get_cost(direction, prev_direction)

            if (nx, ny) == (N - 1, N - 1):
                ans = min(ans, new_cost)
            elif visited[nx][ny][direction] == 0 or visited[nx][ny][direction] > new_cost:
                q.append(((nx, ny), new_cost, direction))
                visited[nx][ny][direction] = new_cost

    for v in visited:
        print(v)

    return ans


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0],
# ]))
