def solution(keyinput, board):
    x, y = 0, 0
    move = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}

    width, height = board[0] // 2, board[1] // 2

    def is_valid(x, y, dx, dy):
        return abs(x + dx) <= width and abs(y + dy) <= height

    for key in keyinput:
        dx, dy = move[key]

        if is_valid(x, y, dx, dy):
            x += dx
            y += dy

    return [x, y]


print(solution(['left', 'right', 'up', 'right', 'right'], [11, 11]))  # 2,1
print(solution(['down', 'down', 'down', 'down', 'down'], [7, 9]))  # 0,-4
