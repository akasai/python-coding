def solution(str):
    ret = 0
    for i in range(len(str)):
        stack = []
        spined = str[i:len(str)] + str[0:i]

        if spined[0] == "]" or spined[0] == "}" or spined[0] == ")":
            continue

        for s in spined:
            if not stack:
                stack.append(s)
            else:
                if (stack[-1] == "(" and s == ")") or (stack[-1] == "{" and s == "}") or (
                        stack[-1] == "[" and s == "]"):
                    stack.pop()
                else:
                    stack.append(s)

        if not stack:
            ret += 1
    return ret


def other_solution(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i + j) % n]
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    break

                if (stack[-1] == "(" and c == ")") or (stack[-1] == "{" and c == "}") or (
                        stack[-1] == "[" and c == "]"):
                    stack.pop()
                else:
                    break
        else: # for-else문
            if not stack:
                cnt += 1

    return cnt


# result = solution("[](){}")
# result = other_solution("[](){}")
# result = solution("}]()[{")
# result = other_solution("}]()[{")
# result = solution("[)(]")
# result = other_solution("[)(]")
# result = solution("}}}")

print(result)
