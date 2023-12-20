def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    matrix = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                matrix[i][j] += arr1[i][k] * arr2[k][j]

    return matrix


# 2*3 3*2 = 2*2
# 3*2 2*3 = 3*3
# result = solution([[1, 2], [3, 4]], [[5, 6], [7, 8]])
result = solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
# result = solution([[1, 2, 1], [3, 4, 3]], [[5, 6], [7, 8], [9, 1]])
# result = solution([[5, 6], [7, 8], [9, 1]], [[1, 2, 1], [3, 4, 3]])
print(result)
