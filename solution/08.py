def solution(str):
    stack = []
    for s in str:
        if s == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)
    return True if not stack else False

print(solution('(())()'))
print(solution('((())()'))
