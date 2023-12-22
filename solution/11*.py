def solution(string):
    stack = []
    ret = 0
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    return int(not stack)


result = solution('baabaa')
# result = solution('cdcd')
print(result)
