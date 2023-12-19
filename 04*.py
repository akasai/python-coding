def solution(answer):
    l = len(answer)
    pattern = [
        [1, 2, 3, 4, 5],  # 1: 12345/12345/12345...
        [2, 1, 2, 3, 2, 4, 2, 5],  # 2: 21232425/21232425...
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],  # 3: 3311224455/3311224455....
    ]

    tmp = [0] * len(pattern)
    for n, p in enumerate(pattern):
        for i in range(l):
            idx = i % len(p)
            if answer[i] == p[idx]:
                tmp[n] += 1

    score = max(tmp)
    return list(filter(lambda x: x == score, tmp))


result = solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# result = solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(result)
