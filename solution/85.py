def solution(N, stations, W):
    ans = 0
    location = 1
    idx = 0

    while location <= N:
        if idx < len(stations) and location >= stations[idx] - W:
            location = stations[idx] + W + 1
            idx += 1
        else:
            location += 2 * W + 1
            ans += 1

    return ans


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
