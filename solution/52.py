from itertools import permutations


def solution(n, weak, dist):
    ans = len(dist)
    l = len(weak)
    for i in range(l):
        weak.append(weak[i] + n)

    for i in range(l):
        for case in permutations(dist, len(dist)):
            cnt = 1
            pos = weak[i] + case[cnt - 1]
            for j in range(i, i + l):
                if pos < weak[j]:
                    cnt += 1
                    if cnt >= len(dist):
                        break
                    pos = weak[j] + case[cnt - 1]
            ans = min(ans, cnt)

    return ans if ans <= len(dist) else -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))  # 2
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))  # 1
