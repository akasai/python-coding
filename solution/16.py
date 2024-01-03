from collections import deque
from math import ceil


def solution(p, s):
    q = deque([ceil((100 - p[i]) / s[i]) for i in range(len(p))])

    max_day = q.popleft()
    ans = [1]
    i = 0
    while len(q):
        next_task = q.popleft()
        if max_day >= next_task:
            ans[i] += 1
            max_day = next_task
        else:
            ans.append(1)
            i += 1
    return ans


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
