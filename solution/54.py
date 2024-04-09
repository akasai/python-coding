def solution(str):
    count = [0] * 26

    for s in str:
        count[ord(s) - 97] += 1

    result = ""
    for i in range(26):
        result += chr(i + 97) * count[i]

    return result


print(solution("hello"))
print(solution("algorithm"))
