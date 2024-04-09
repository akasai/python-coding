def solution(d, budget):
    d.sort()
    ans = 0
    for c in d:
        if c <= budget:
            budget -= c
            ans += 1
    return ans if budget >= 0 else ans - 1


print(solution([1, 3, 2, 5, 4], 9))  # 3
print(solution([2, 2, 3, 3], 10))  # 4
