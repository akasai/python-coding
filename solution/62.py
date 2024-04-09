def solution(arr, n):
    N = len(arr)
    for _ in range(n):
        arr = [[arr[N - 1 - j][i] for j in range(N)] for i in range(N)]
    return arr


print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2))
