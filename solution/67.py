def solution(blue, white):
    half = blue // 2
    w, h = 0, 0
    for row in range(half // 2 + 1, half):
        col = half - row
        if row == col + 1:
            continue
        if (row - 2) * col == white:
            w, h = row, col + 2

    return [w, h]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
