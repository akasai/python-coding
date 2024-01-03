from collections import deque


def solution(c1, c2, goal):
    c1 = deque(c1)
    c2 = deque(c2)
    goal = deque(goal)

    while goal:
        if c1 and c1[0] == goal[0]:
            c1.popleft()
            goal.popleft()
        elif c2 and c2[0] == goal[0]:
            c2.popleft()
            goal.popleft()
        else:
            break
    return "Yes" if not len(goal) else "No"


# print(solution(['i', 'drink', 'water'], ['want', 'to'], ['i', 'want', 'to', 'drink', 'water']))
print(solution(['i', 'water', 'drink'], ['want', 'to'], ['i', 'want', 'to', 'drink', 'water']))
