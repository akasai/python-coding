def solution(N):
    ans = []
    def bt(start, sum, selected):
        if sum == 10:
            ans.append(selected)
            return

        for i in range(start, N + 1):
            if sum + i <= 10:
                bt(i + 1, sum + i, selected + [i])

    bt(1, 0,[])
    return ans


print(solution(5))
print(solution(2))
print(solution(7))
