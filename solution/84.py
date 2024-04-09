from collections import Counter


def solution(k, tangerine):
    count = Counter(tangerine)
    s = sorted(count.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    i = 0
    while k > 0:
        v, c = s[i]
        ans += 1
        if c > k:
            break
        k -= c
        i += 1

    return ans


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))  # 1
