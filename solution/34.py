def solution(nums):
    n = len(nums)
    k = n // 2
    tree = set(nums)

    return min(k, len(tree))


print(solution([3, 1, 2, 3]))
