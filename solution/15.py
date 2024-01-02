from collections import deque


def solution(n, k):
    q = deque(range(1, n + 1))

    while len(q) > 1:
        for _ in range(k - 1):
            q.append(q.popleft())
        q.popleft()

    return q.popleft()


r = solution(5, 2)
print(r)
