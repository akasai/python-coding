def solution(arr):
    sorted = list(set(arr))
    sorted.sort(reverse=True)
    return sorted


result = solution([4, 2, 2, 1, 3, 4])
print(result)

# TEST Code
# print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
# print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]
