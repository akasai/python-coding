def solution(str):
    stack = []

    for s in str:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


# result = solution('(())()')
result = solution('((())()')
print(result)
