def union(tree, a, b):
    r1 = find(tree, a)
    r2 = find(tree, b)

    tree[r2] = r1


"""
root를 찾는 함수
"""


def find(tree, a):
    # root면 아웃
    if tree[a] == a:
        return a
    tree[a] = find(tree, tree[a])
    return tree[a]


def solution(k, operations):
    tree = list(range(k))
    ans = k
    for op in operations:
        if op[0] == 'u':
            union(tree, op[1], op[2])
        if op[0] == 'f':
            find(tree, op[1])
    ans = len(set(find(tree, i) for i in range(k)))
    return ans


# print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))
