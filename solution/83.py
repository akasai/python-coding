def solution(people, limit):
    people.sort(reverse=True)
    ans = 0
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        ans += 1

    return ans


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3
