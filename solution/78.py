def solution(board):
    N, M = len(board), len(board[0])

    m = 0
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                u, l, ul = board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]
                board[i][j] = min(u, l, ul) + 1
                m = max(m, board[i][j])

    return m ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
# print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
