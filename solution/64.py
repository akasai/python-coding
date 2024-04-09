def printArr(m):
    for t in m:
        print(t)
    print()


def solution(n):
    ans = [[0] * n for _ in range(n)]
    num = 1
    s_r, e_r = 0, n - 1
    s_c, e_c = 0, n - 1

    while s_r <= e_r and s_c <= e_c:
        for c in range(s_c, e_c + 1):
            ans[s_r][c] = num
            num += 1
        s_r += 1

        for r in range(s_r, e_r + 1):
            ans[r][e_c] = num
            num += 1
        e_c -= 1

        if s_r <= e_r:
            for c in range(e_c, s_c - 1, -1):
                ans[e_r][c] = num
                num += 1
            e_r -= 1

        if s_c <= e_c:
            for r in range(e_r, s_r - 1, -1):
                ans[r][s_c] = num
                num += 1
            s_c += 1

    return ans


printArr(solution(3))
printArr(solution(4))
