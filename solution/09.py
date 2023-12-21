def solution(dec):
    stack = []
    while dec > 0:
        stack.append(str(dec % 2))
        dec //= 2
    stack.reverse()
    return "".join(stack)


# result = solution(10)
# result = solution(27)
result = solution(12345)
print(result)
