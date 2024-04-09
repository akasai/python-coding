from collections import Counter


def solution(topping):
    topping_count = Counter(topping)
    half = set()
    ans = 0

    for t in topping:
        topping_count[t] -= 1
        half.add(t)

        if topping_count[t] == 0:
            topping_count.pop(t)

        if len(half) == len(topping_count):
            ans += 1

    return ans


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# print(solution([1, 2, 3, 1, 4]))
