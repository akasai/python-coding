def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


print(solution(['119', '97674223', '1195524421']))  # False
print(solution(['123', '456', '789']))  # True
print(solution(['12', '123', '1235', '567', '88']))  # True
