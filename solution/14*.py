def solution(n, k, cmd):
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    d_stack = []

    cur_row = k + 1

    for c in cmd:
        if c.startswith('C'):
            d_stack.append(cur_row)
            up[down[cur_row]] = up[k]
            down[up[cur_row]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif c.startswith('Z'):
            re = d_stack.pop()
            down[up[re]] = re
            up[down[re]] = re
        else:
            [e, i] = c.split(' ')
            if e == 'D':
                for _ in range(int(i)):
                    cur_row = down[cur_row]
            elif e == 'U':
                for _ in range(int(i)):
                    cur_row = up[cur_row]

    ans = ['O'] * n
    for i in d_stack:
        ans[i] = 'X'

    return "".join(ans)


# ret = solution(8, 2, ['D 2', 'C'])  # , 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z'])  # OOOOXOOO
ret = solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z'])  # OOOOXOOO
# ret = solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z', 'U 1', 'C']) # OOXOXOOO
# ret = solution(5, 0, ['D 2', 'C', 'U 2', 'Z', 'C'])  # OXXOO
# ret = solution(5, 5, ['D 2', 'C', 'U 2', 'Z', 'C'])
# ret = solution(5, 0, ['C', 'D 2', 'C'])  # XOOXO
print(ret)
