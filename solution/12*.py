def solution(prices):
    stack = []
    for i in range(len(prices) - 1):
        term = -1
        for j in range(i, len(prices)):
            if prices[i] <= prices[j]:
                term += 1
        stack.append(term)

    stack.append(0)
    return stack


def other_solution(prices):
    n = len(prices)
    stack = [0]
    ret = [0] * n
    for i in range(1, n):
        while prices[stack[-1]] > prices[i]:  # 감소가 발견되면
            cur = stack.pop()
            ret[cur] = i - cur
        stack.append(i)

    while stack:
        i = stack.pop()
        ret[i] = (n - 1) - i

    return ret


# result = solution([1, 2, 3, 2, 3])
# result = other_solution([1, 2, 3, 2, 3])
result = other_solution([1, 6, 9, 5, 3, 2, 7])
print(result)
