def solution(map, move):
    cnt = 0
    stack = []
    for m in move:
        x = m - 1
        for y in map:
            if y[x] != 0:
                if stack and stack[-1] == y[x]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(y[x])

                y[x] = 0
                break

    return cnt


result = solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                  [1, 5, 3, 5, 1, 2, 1, 4])
print(result)  # 4
