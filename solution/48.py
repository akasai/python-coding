def printArr(arr):
    for a in arr:
        print(a)
    print('')


def solution(board):
    def get_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid(num, row, col):
        return not (in_row(num, row) or in_col(num, col) or in_box(num, row, col))

    def in_row(num, row):
        return num in board[row]

    def in_col(num, col):
        return num in [row[col] for row in board]

    def in_box(num, row, col):
        nr = (row // 3) * 3
        nc = (col // 3) * 3
        for i in range(nr, nr + 3):
            for j in range(nc, nc + 3):
                if board[i][j] == num:
                    return True
        return False

    def sudoku():
        empty = get_empty()
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num
                if sudoku():
                    return True
                board[row][col] = 0
        return False

    sudoku()
    printArr(board)
    return


# print(solution([
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]))

print(solution([
    [8, 0, 5, 0, 0, 2, 4, 6, 0],
    [4, 6, 7, 9, 0, 0, 0, 0, 0],
    [0, 0, 9, 6, 0, 4, 0, 0, 8],
    [0, 0, 0, 2, 0, 0, 3, 0, 4],
    [0, 7, 2, 0, 0, 0, 9, 1, 0],
    [9, 0, 3, 0, 0, 5, 0, 0, 0],
    [5, 0, 0, 3, 0, 6, 2, 0, 0],
    [0, 0, 0, 0, 0, 1, 5, 8, 3],
    [0, 3, 4, 5, 0, 0, 6, 0, 1]
]))

# print(solution([
#     [0, 0, 0, 0, 5, 0, 3, 0, 0],
#     [2, 0, 0, 0, 0, 0, 0, 6, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 6, 4, 0, 0, 0, 2],
#     [0, 0, 5, 3, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [6, 0, 0, 2, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 7, 4, 0],
#     [0, 0, 0, 0, 0, 0, 5, 0, 0]
# ]))
