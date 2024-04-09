from collections import deque


def solution(info, edges):
    def build_tree(info, edges):
        tree = [[] for _ in info]
        for e in edges:
            tree[e[0]].append(e[1])
        return tree

    tree = build_tree(info, edges)
    max_sheep = 0
    q = deque([(0, 1, 0, set())])  # 현 위치, sheep, wolf, 방문 노드 집합

    while q:
        n, s, w, v = q.popleft()
        max_sheep = max(max_sheep, s)
        v.update(tree[n])

        for next in v:
            if info[next]:
                if s != w + 1:
                    q.append((next, s, w + 1, v - {next}))
            else:
                q.append((next, s + 1, w, v - {next}))

    return max_sheep


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
