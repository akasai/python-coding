def solution(m1, m2):
    tmp = [[0] * len(m1) for _ in range(len(m2[0]))]
    for i, row in enumerate(m1):
        for j in range(len(m1[0])):
            s = sum([m2[k][j] * row[k] for k in range(len(m1))])
            tmp[j][i] = s

    return tmp


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
print(solution([[2, 4, 6], [1, 3, 5], [7, 8, 9]], [[9, 1, 2], [4, 5, 6], [7, 3, 8]]))
