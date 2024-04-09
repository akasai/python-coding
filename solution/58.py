def solution(array, commands):
    def get(i, j, k):
        tmp = sorted(array[i - 1:j])
        return tmp[k - 1]

    return [get(i, j, k) for i, j, k in commands]


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # 5,6,3
