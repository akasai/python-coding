
def hashable(string):
    p = 31
    m = 1_000_000_007
    h = 0

    for i, s in enumerate(string):
        h = (h * p + ord(s)) % m

    return h


def solution(strings, queries):
    table = [None] * 1000000007

    for string in strings:
        table[hashable(string)] = string

    ans = []
    for query in queries:
        if not table[hashable(query)]:
            ans.append(False)
        else:
            ans.append(True)

    return ans


print(solution(['apple', 'banana', 'cherry'], ['banana', 'kiwi', 'melon', 'apple']))  # t, f, f, t
