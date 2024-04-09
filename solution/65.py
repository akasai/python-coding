def solution(s):
    cnt, zero_cnt = 0, 0

    while s != "1":
        cnt += 1
        removed = s.count("0")
        zero_cnt += removed
        s = bin(s.count("1"))[2:]

    return [cnt, zero_cnt]


print(solution("01110"))  # [3, 3]
print(solution("110010101001"))  # [3, 8]
print(solution("1111111"))  # [3, 8]
