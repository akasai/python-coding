def solution(dirs):
    m = [[False] * 11 for _ in range(11)]
    x, y = 5, 5
    length = 0

    for d in dirs:
        if (x > 10 or x < 0) or (y > 10 or x < 0):
            break

        if not m[x][y]:
            m[x][y] = True
            length += 1
            if d == 'U':
                y -= 1
            elif d == 'D':
                y += 1
            elif d == 'R':
                x += 1
            elif d == 'L':
                x -= 1

    return length


def other_solution(dirs):
    x, y = 5, 5
    loc = set()

    for d in dirs:
        if (x > 10 or x < 0) or (y > 10 or x < 0):
            break

        loc.add((x, y))

        if d == 'U':
            y -= 1
        elif d == 'D':
            y += 1
        elif d == 'R':
            x += 1
        elif d == 'L':
            x -= 1

    return len(loc)


# result = solution('ULURRDLLU')
# result = other_solution('ULURRDLLU')
# result = solution('LULLLLLLU')
# result = other_solution('LULLLLLLU')

# print(result)
