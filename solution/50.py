def solution(N):
    w = [False] * N
    d1 = [False] * (N * 2)
    d2 = [False] * (N * 2)

    def dfs(cur_row):
        ans = 0
        if cur_row == N:
            ans += 1
        else:
            for col in range(N):  # 한줄씩 내려가면서
                if w[col] or d1[col + cur_row] or d2[col - cur_row + N]:
                    continue
                # 문제 없다면 한개 더 놓기
                w[col] = d1[col + cur_row] = d2[col - cur_row + N] = True
                ans += dfs(cur_row + 1)
                w[col] = d1[col + cur_row] = d2[col - cur_row + N] = False
        return ans

    return dfs(0)


print(solution(4))  # 2
